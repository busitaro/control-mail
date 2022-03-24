import time
from typing import Callable

from data import Monitoring


def check(monitoring: Monitoring, exec: Callable[[Monitoring], None]):
    """
    監視プロセスループ

    Params
    ------
    monitoring: Monitoring
        監視設定オブジェクト
    """
    while True:
        exec(monitoring)
        # 指定時間待機する
        time.sleep(monitoring.period)
