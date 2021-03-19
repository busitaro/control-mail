class Monitoring:
    def __init__(self, search_word: str, file_out_dir: str, period: int):
        """
        コンストラクタ

        Params
        ------
        search_word: str
            件名を検索するワード
            このワードが件名に含まれるメールが対象となる

        file_out_dir: str
            添付ファイル出力先ディレクトリ

        period: int
            メール検索間隔(秒)
        """
        self.__search_word = search_word
        self.__file_out_dir = file_out_dir
        self.__period = period

    @property
    def search_word(self):
        """
        件名検索ワード

        """
        return self.__search_word

    @property
    def file_out_dir(self):
        """
        添付ファイル保存先パス

        """
        return self.__file_out_dir

    @property
    def period(self):
        """
        メール確認間隔(秒)

        """
        return self.__period
