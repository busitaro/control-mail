from O365 import Account, FileSystemTokenBackend
from os import makedirs

from .config.config_api import Config
from .run_time import RunTime
from .monitoring import Monitoring
from .logger import Logger


def observe_mail(monitoring: Monitoring):
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
        mails = list(get_mail(monitoring))
        # ログ出力
        logger.info('check mails :count => {}'.format(len(mails)))
        # 添付ファイルの保存先作成
        makedirs(monitoring.file_out_dir, exist_ok=True)
        # 添付ファイルの保存
        for message in mails:
            store_attachment_file(message, monitoring.file_out_dir)
    except Exception as e:
        logger.critical(str(e))


def get_mail(monitoring: Monitoring):
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
    token_backend = FileSystemTokenBackend(token_path=config.token_path, 
                                            token_filename=config.token_file)
    account = Account(credentials, token_backend=token_backend)
    mailbox = account.mailbox()
    # 件名と時刻でメールを絞り込む
    query = mailbox.new_query() \
                .on_attribute('subject').contains(monitoring.search_word) \
                .on_attribute('receivedDateTime').greater_equal(run_time.read())

    messages = mailbox.get_messages(query=query, download_attachments=True)
    # 取得時刻を記録する
    run_time.record()

    return messages


def store_attachment_file(message, path: str):
    """
    メールから添付ファイルを取得し保存する

    Params
    ------
    message: メール
    path: 保存先
    """
    for attachment in message.attachments:
        attachment.save(path)
