from logging import getLogger, FileHandler, StreamHandler, Formatter, DEBUG
import os


output_dir = 'log'
file_name = 'get_mail_{}.log'

# 出力先ディレクトリの準備
os.makedirs(output_dir, exist_ok=True)

# loggerの設定
logger = getLogger(__name__)
logger.setLevel(DEBUG)
formatter = Formatter('%(asctime)s %(levelname)s %(name)s :%(message)s')

# 標準出力へのハンドラ
stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 子loggerを保持する辞書
logger_dict = dict()

class Logger:
    def __init__(self, name: str):
        """
        コンストラクタ

        Params
        ------
        name: str
            ログファイルに出力する名称
        """
        self.__name = name

        if name not in logger_dict:
            child_logger = logger.getChild(name)
            log_file_name = file_name.format(name)
            handler = FileHandler('{}/{}'.format(output_dir, log_file_name))
            handler.setFormatter(formatter)
            child_logger.addHandler(handler)
            # 辞書に保持
            logger_dict[name] = child_logger

    def info(self, message):
        """
        infoログを出力する

        Params
        ------
        message: str
            ログ出力メッセージ
        """
        logger_dict[self.__name].info(message)

    def critical(self, message):
        """
        criticalログを出力する
        直近のstack_traceも出力される

        Params
        ------
        message: str
            ログ出力メッセージ
        """
        logger_dict[self.__name].critical(message, exc_info=True)
