from concurrent.futures import ThreadPoolExecutor

from .monitoring import Monitoring
from .daemon import check


executor = ThreadPoolExecutor(thread_name_prefix='thread')

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
