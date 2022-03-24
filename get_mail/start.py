from concurrent.futures import ThreadPoolExecutor

from data import Monitoring
from .daemon import check
from logic import observe_mail


executor = ThreadPoolExecutor(thread_name_prefix='thread')


def start(monitoring: Monitoring, daemonize=False):
    """
    処理を開始する

    Params
    -------
    monitoring: Monitoring
        監視設定オブジェクト
    daemonize: bool = False
        デーモンかするかどうかのフラグ
    """
    if daemonize:
        start_daemon(monitoring)
    else:
        observe_mail(monitoring)


def start_daemon(monitoring: Monitoring):
    """
    デーモンプロセスを別スレッドで起動する

    Params
    ------
    monitoring: Monitoring
        監視設定オブジェクト
    """
    # チェックスレッドの開始
    executor.submit(check, monitoring=monitoring)
