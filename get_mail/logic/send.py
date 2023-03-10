from O365 import Account
from O365 import FileSystemTokenBackend

from .interface import Logic
from ..data import Monitoring
from ..logger import Logger


class SendLogic(Logic):
    def exec(self, monitoring: Monitoring):
        logger = Logger(monitoring.search_word)
        logger.info('exec send')

        mailbox = self.__get_mailbox(monitoring)

        for index, address in enumerate(monitoring.send_to_list):
            message = mailbox.new_message()
            # 宛先
            message.to.add(address)
            # 件名
            message.subject = monitoring.send_subject
            # テンプレート文字列を置き換え
            replace_dict = dict()
            for key, value in monitoring.send_values.items():
                replace_dict[key] = value[index]
            message.body = \
                monitoring.send_body.format(
                    **replace_dict
                )
            # 送信の実行
            logger.info('send mail to: {}'.format(address))
            message.send()

    def daemonize(self):
        return False

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
        return mailbox
