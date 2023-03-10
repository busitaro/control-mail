import os
from datetime import datetime
from pathlib import Path


class RunTime:
    output_path = 'run_time'
    time_format = '%Y/%m/%d %H:%M:%S'

    def __init__(self, name: str):
        """
        コンストラクタ

        Params
        ------
        name: str
            時刻保存ファイル名称
        """
        self.__name = name
        self.__file = '{}/{}'.format(self.output_path, self.__name)

    def record(self):
        """
        時刻を記録する

        """
        if not os.path.exists(self.__file):
            # ファイルが存在しない場合、作成する
            os.makedirs(self.output_path, exist_ok=True)
            Path(self.__file).touch()
        with open(self.__file, 'w', encoding='utf-8') as f:
            f.write(datetime.now().strftime(self.time_format))

    def read(self):
        """
        時刻を読みだす

        """
        if os.path.exists(self.__file):
            # ファイルが存在する場合、ファイル内の時刻を返す
            with open(self.__file, 'r', encoding='utf-8') as f:
                return datetime.strptime(f.read(), self.time_format)
        else:
            # ファイルが存在しない場合、1970/01/01を返す
            return datetime.strptime('1970/01/01 00:00:00', self.time_format)
