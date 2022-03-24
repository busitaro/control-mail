from datetime import datetime
from datetime import timedelta

from O365 import Account
from O365 import FileSystemTokenBackend

from .interface import Logic
from ..config import Config
from ..data import Monitoring


class ForwardLogic(Logic):
    def __init__(self, daemonize: bool):
        self.__daemonize = daemonize

    def exec(self, monitoring: Monitoring):
        return self.__get_mail(monitoring)

    def daemonize(self):
        return self.__daemonize

    def __get_mail(self, monitoring: Monitoring):
        """
        メールを取得する

        Params
        -------
        monitoring: Monitoring
            監視設定オブジェクト
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

        # 1週間前分のメールから、件名で絞込
        query = \
            mailbox.new_query() \
            .on_attribute('subject') \
            .contains(monitoring.search_word) \
            .on_attribute('receivedDateTime') \
            .greater_equal(datetime.now() - timedelta(days=7))

        messages = mailbox.get_messages(query=query)

        return messages
