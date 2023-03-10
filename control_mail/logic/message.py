from bs4 import BeautifulSoup

from ..data import Monitoring
from ..logger import Logger
from .interface import Logic
from .control import get_mail


class MessageLogic(Logic):
    def exec(self, monitoring: Monitoring) -> list:
        """
        メールの内容を取得する

        Params
        -------
        monitoring: Monitoring
            監視設定オブジェクト

        Returns
        -------
        0: list
            メール内容
            検索条件に合致するメールがない場合にはNone
        """
        # loggerの初期化
        logger = Logger(f'get_{monitoring.search_word}')
        try:
            # mailの取得
            mails = get_mail(monitoring, monitoring.search_datetime_from)

            # mailのメッセージを取得
            if len(mails) == 0:
                messages = None
            else:
                messages = []
                for mail in mails:
                    if mail.body_type == 'html':
                        messages.append(
                            BeautifulSoup(mail.body, 'lxml').text
                        )
                    else:
                        messages.append(mail.body)
            return messages
        except Exception as e:
            logger.critical(str(e))

    def daemonize(self):
        return False
