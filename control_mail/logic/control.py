from datetime import datetime

from O365 import Account
from O365 import FileSystemTokenBackend

from ..data import Monitoring


def get_mail(
    monitoring: Monitoring,
    from_time: datetime,
):
    """
    メールを取得

    Params
    -------
    monitoring: Monitoring,
        監視設定オブジェクト
    """
    # メールボックスへの接続
    credentials = (monitoring.client_id, monitoring.client_secret)
    token_backend = \
        FileSystemTokenBackend(
            token_path=monitoring.token_path,
            token_filename=monitoring.token_file,
        )
    account = Account(credentials, token_backend=token_backend)
    mailbox = account.mailbox()
    # 件名と時刻でメールを絞り込む
    query = \
        mailbox.new_query() \
        .on_attribute('subject') \
        .contains(monitoring.search_word) \
        .on_attribute('receivedDateTime') \
        .greater_equal(from_time)

    messages = mailbox.get_messages(query=query, download_attachments=True)
    return list(messages)
