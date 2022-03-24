from O365 import Account, FileSystemTokenBackend

from ..config import Config


def main():
    """
    認証を行う

    """
    config = Config()
    credentials = (config.client_id, config.client_secret)
    token_backend = \
        FileSystemTokenBackend(
            token_path=config.token_path,
            token_filename=config.token_file
        )
    account = Account(credentials, token_backend=token_backend)
    if account.authenticate(scopes=['basic', 'message_all']):
        print('Authenticated!')


if __name__ == '__main__':
    main()
