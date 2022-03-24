import dataclasses


@dataclasses.dataclass
class Monitoring:
    """
    件名を検索するワード
    このワードが件名に含まれるメールが対象となる
    """
    search_word: str
    """
    添付ファイル出力先ディレクトリ
    """
    file_out_dir: str
    """
    メール検索間隔(秒)
    """
    period: int
