import dataclasses


@dataclasses.dataclass
class Monitoring:
    """
    クライアントID
    """
    client_id: str = ''

    """
    クライアントシークレット
    """
    client_secret: str = ''

    """
    トークンファイルパス
    """
    token_path: str = '/'

    """
    トークンファイル名
    """
    token_file: str = 'token.json'

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
    送信メール宛先
    """
    send_to_list: list = dataclasses.field(default_factory=list)

    """
    送信メール件名
    """
    send_subject: str = ''

    """
    送信メール内容
    """
    send_body: str = ''

    """
    送信メール置き換え内容
    {
        'keyword1': [to1_value1, to2_value1, ...],
        'keyword2': [to1_value2, to2_value2, ...]
    }
    """
    send_values: dict = dataclasses.field(default_factory=dict)

    """
    転送設定
    """
    forward_address_words: list = dataclasses.field(default_factory=list)
