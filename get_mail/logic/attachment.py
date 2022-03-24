from O365 import Account, FileSystemTokenBackend
from os import makedirs
from os.path import isfile

from config import Config
from data import Monitoring
from .run_time import RunTime
from .interface import Logic
from .logger import Logger


class AttachmentLogic(Logic):
    def __init__(self, daemonize: bool):
        self.__daemonize = daemonize

    def exec(self, monitoring: Monitoring):
        """
        メール監視を行い、
        取得したメールから添付ファイルを取得する

        メールはrun_timeの時刻以降のメッセージを対象に取得する

        Params
        ------
        monitoring: Monitoring
            監視設定オブジェクト
        """
        # loggerの初期化
        logger = Logger(monitoring.search_word)
        try:
            # mailの取得
            mails = list(self.__get_mail(monitoring))
            # ログ出力
            logger.info('check mails :count => {}'.format(len(mails)))
            # 添付ファイルの保存先作成
            makedirs(monitoring.file_out_dir, exist_ok=True)
            # 添付ファイルの保存
            for message in mails:
                self.__store_attachment_file(message, monitoring.file_out_dir)
            # 取得時刻を記録する
            run_time = RunTime(monitoring.search_word)
            run_time.record()
        except Exception as e:
            logger.critical(str(e))

    def daemonize(self):
        return self.__daemonize

    def __get_mail(self, monitoring: Monitoring):
        """
        メールを取得する

        Params
        ------
        monitoring: Monitoring
            監視設定オブジェクト
        """
        config = Config()
        run_time = RunTime(monitoring.search_word)

        # メールボックスへの接続
        credentials = (config.client_id, config.client_secret)
        token_backend = \
            FileSystemTokenBackend(
                token_path=config.token_path,
                token_filename=config.token_file
            )
        account = Account(credentials, token_backend=token_backend)
        mailbox = account.mailbox()
        # 件名と時刻でメールを絞り込む
        query = mailbox.new_query() \
            .on_attribute('subject') \
            .contains(monitoring.search_word) \
            .on_attribute('receivedDateTime') \
            .greater_equal(run_time.read())

        messages = mailbox.get_messages(query=query, download_attachments=True)

        return messages

    def __store_attachment_file(self, message, path: str):
        """
        メールから添付ファイルを取得し保存する

        Params
        ------
        message: メール
        path: 保存先
        """
        for attachment in message.attachments:
            attachment.save(
                path,
                custom_name=self.__make_store_name(attachment.name, path)
            )

    def __make_store_name(self, attachment_name: str, path: str):
        """
        添付ファイルの保存名を作成する

        Params
        ------
        attachment_name: str
            添付ファイル名
        path: str
            保存先パス

        Returns
        -------
        0: 保存ファイル名
        """
        if isfile('{}/{}'.format(path, attachment_name)):
            # 同名ファイルが存在した場合

            # ファイル名の後ろに "_連番" を付与する
            underbar_split = attachment_name.split('_')
            base_name, suffix_num = \
                '_'.join(underbar_split[:-1]), underbar_split[-1]

            # _連番を付けた上で、再度同名ファイルの存在チェック
            if suffix_num.isdecimal():
                suffix_num = str(int(suffix_num) + 1)
            else:
                suffix_num = '1'
            store_name = \
                self.__make_store_name(
                    '{}_{}'.format(base_name, suffix_num),
                    path
                )
        else:
            store_name = attachment_name
        return store_name
