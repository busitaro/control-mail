from datetime import datetime
from datetime import timedelta

from O365 import Account
from O365 import FileSystemTokenBackend

from .interface import Logic
from .forward_config import ForwardConfig
from ..config import Config
from ..data import Monitoring
from ..logger import Logger


class ForwardLogic(Logic):
    def __init__(self, daemonize: bool):
        self.__daemonize = daemonize
        self.__f_config = ForwardConfig()

    def exec(self, monitoring: Monitoring):
        logger = Logger(monitoring.search_word)
        logger.info('exec forward')
        all_ids = self.__f_config.get_all_id()
        mailbox = self.__get_mailbox(monitoring)
        mails = self.__get_mail(mailbox, monitoring)

        for mail in mails:
            for id in all_ids:
                if id in mail.body:
                    address = self.__get_send_address(id)
                    send_mail = mail.forward()
                    send_mail.to.add(address)
                    print(id)
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
        config = Config()

        # メールボックスへの接続
        credentials = (config.client_id, config.client_secret)
        token_backend = \
            FileSystemTokenBackend(
                token_path=config.token_path,
                token_filename=config.token_file
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

    def __get_send_address(self, id: str):
        address = ''
        try:
            address = self.__f_config.get_address_by_id(id)
        except ValueError:
            pass
        return address
