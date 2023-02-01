import dataclasses


@dataclasses.dataclass
class Monitoring:
    """
    件名を検索するワード
    このワードが件名に含まれるメールが対象となる
    """
    search_word: str = ''
    """
    検索対象のディレクトリ
    階層をリストで表現する
    """
    search_directory: list = dataclasses.field(default_factory=list)
    """
    添付ファイル出力先ディレクトリ
    """
    file_out_dir: str = ''
    """
    メール検索間隔(秒)
    """
    period: int = -1
    """
    送信メール件名
    """
    send_subject: str = ''
    """
    送信メール内容
    """
    send_body: str = ''
