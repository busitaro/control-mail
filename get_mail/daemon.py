import time

from .monitoring import Monitoring
from .mail import observe_mail


def check(monitoring: Monitoring):
    """
    監視プロセスループ

    Params
    ------
    monitoring: Monitoring
        監視設定オブジェクト
    """
    while True:
        observe_mail(monitoring)
        # 指定時間待機する
        time.sleep(monitoring.period)
