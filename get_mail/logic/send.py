from datetime import datetime
from datetime import timedelta

from O365 import Account
from O365 import FileSystemTokenBackend

from .interface import Logic
from .send_config import SendConfig
from ..config import Config
from ..data import Monitoring
from ..logger import Logger


class SendLogic(Logic):
    def __init__(self):
        self.__s_config = SendConfig()

    def exec(self, monitoring: Monitoring):
        logger = Logger(monitoring.search_word)
        logger.info('exec send')

        all_address = self.__s_config.get_all_address()
        mailbox = self.__get_mailbox()

        for address in all_address:
            message = mailbox.new_message()
            message.to.add(address)
            message.subject = monitoring.send_subject
            message.body = \
                monitoring.send_body.format(
                    self.__s_config.get_key_by_address(address)
                )
            logger.info('send mail to: {}'.format(address))
            message.send()

    def daemonize(self):
        return False

    def __get_mailbox(self):
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
        return mailbox
