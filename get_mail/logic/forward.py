from datetime import datetime
from datetime import timedelta

from O365 import Account
from O365 import FileSystemTokenBackend

from .interface import Logic
from .forward_config import ForwardConfig
from ..data import Monitoring
from ..logger import Logger


class ForwardLogic(Logic):
    def __init__(self, daemonize: bool):
        self.__daemonize = daemonize

    def exec(self, monitoring: Monitoring):
        logger = Logger(monitoring.search_word)
        logger.info('exec forward')

        # 検索対象のメール
        mails = \
            self.__get_mail(
                self.__get_mailbox(monitoring),
                monitoring
            )

        # 転送の実施
        for mail in mails:
            for (address, word) in monitoring.forward_address_words:
                # 検索対象文字列がメール内容に含まれていた場合
                if word in mail.body:
                    send_mail = mail.forward()
                    send_mail.to.add(address)
                    logger.info(
                        'address: {}, subject: {}'.format(
                            address,
                            send_mail.subject
                        )
                    )
                    send_mail.send()

    def daemonize(self):
        return self.__daemonize

    def __get_mailbox(self, monitoring: Monitoring):
        """
        メールボックスを取得する

        """
        # メールボックスへの接続
        credentials = (monitoring.client_id, monitoring.client_secret)
        token_backend = \
            FileSystemTokenBackend(
                token_path=monitoring.token_path,
                token_filename=monitoring.token_file
            )
        account = Account(credentials, token_backend=token_backend)
        mailbox = account.mailbox()
        for folder in monitoring.search_directory:
            mailbox = mailbox.get_folder(folder_name=folder)

        return mailbox

    def __get_mail(self, mailbox, monitoring: Monitoring):
        """
        メールを取得する

        Params
        -------
        monitoring: Monitoring
            監視設定オブジェクト
        """
        # 1週間前分のメールから、件名で絞込
        query = \
            mailbox.new_query() \
            .on_attribute('subject') \
            .contains(monitoring.search_word) \
            .on_attribute('receivedDateTime') \
            .greater_equal(datetime.now() - timedelta(days=7))

        messages = mailbox.get_messages(query=query, limit=100)

        return messages
