# get_mail

Office365 の Exchange メールサーバ上のメールを操作します。

上のメールを監視し、  
添付ファイルを自動ダウンロードします。

# Requirement

requirement.txt 参照

- beautifulsoup4 4.9.3
- certifi 2020.12.5
- chardet 4.0.0
- idna 2.10
- O365 2.0.14
- oauthlib 3.1.0
- python-dateutil 2.8.1
- pytz 2021.1
- requests 2.25.1
- requests-oauthlib 1.3.0
- six 1.15.0
- soupsieve 2.2
- stringcase 1.2.0
- tzlocal 2.1
- urllib3 1.26.3

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
python -m auth.auth
```

## Usage

| mode       | function               |
| ---------- | ---------------------- |
| attachment | 添付ファイルを取得する |
| forward    | メールを転送する       |
| send       | 新規メールを送信する   |

```python
from get_mail import Monitoring
from get_mail import start

monitoring = Monitoring('search_word_for_subject', 'file_save_destination', 60) # 60 is check interval(sec.)
mode = 'attachment'     # function mode
damonize = False        # set True if damonize
start(monitoring, mode, daemonize)
```

# Author

- busitaro
- busitaro10@gmail.com
