# control_mail

Office365 の Exchange メールサーバ上のメールを操作します。

上のメールを監視し、  
添付ファイルを自動ダウンロードします。

# Installation

```bash
pip install -r requirement.txt
```

# Usage

事前に Azure ポータル上でアプリを登録する必要があります。

## 準備

設定ファイル  
conf/api.ini

```ini
client_id = your_client_id
client_secret = your_client_secret
token_path = where_to_save_token
token_file = token_file_name
```

auth トークンを取得する

```bash
python -m auth.auth client_id client_secret
```

## Usage

| mode       | function               |
| ---------- | ---------------------- |
| attachment | 添付ファイルを取得する |
| forward    | メールを転送する       |
| send       | 新規メールを送信する   |
| get_mail   | メール内容を取得する   |

### forward

指定文字列の含まれるメールを指定アドレスへ転送する

```python
from control_mail import Monitoring
from control_mail import start

monitoring = \
    Monitoring(
        client_id='your client id',
        client_secret='your client secret',
        token_path='path to m365 token file',
        token_file='file name of m365 token file',
        forward_address_words=[('forward_address1', 'search_word1'), ('forward_address2', 'search_word2'), ...],
        search_directory=['inbox', 'folder']
    )

start(monitoring, 'forward')
```

### send

メールを送信する

```python
from control_mail import Monitoring
from control_mail import start

monitoring = \
    Monitoring(
        client_id='your client id',
        client_secret='your client secret',
        token_path='path to m365 token file',
        token_file='file name of m365 token file',
        send_subject='subject of mail',
        send_to_list=['to1@hi-chubu.co.jp', 'to2@hi-chubu.co.jp'],
        send_body='mail body: {keyword1}: {keyword2}'
        send_values={
            'keyword1': ['to1_value1', 'to2_value1'],
            'keyword2': ['to1_value2', 'to2_value2'],
        }
    )

start(monitoring, 'send')
```

### get_mail

メール内容を取得する

```python
from datetime import datetime

from control_mail import Monitoring
from control_mail import start

monitoring = \
    Monitoring(
        client_id='your client id',
        client_secret='your client secret',
        token_path='path to m365 token file',
        token_file='file name of m365 token file',
        search_word='suject search word',
        search_datetime_from=datetime(2020, 1, 1),
    )

message = start(monitoring, 'get_mail')
```

# Author

- busitaro
- busitaro10@gmail.com
