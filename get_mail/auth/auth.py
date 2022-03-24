from O365 import Account, FileSystemTokenBackend

from ..config import Config


def main():
    """
    認証を行う

    """
    config = Config()
    credentials = (config.get_client_id(), config.get_client_secret())
    token_backend = \
        FileSystemTokenBackend(
            token_path=config.get_token_path(),
            token_filename=config.get_token_file()
        )
    account = Account(credentials, token_backend=token_backend)
    if account.authenticate(scopes=['basic', 'message_all']):
        print('Authenticated!')


if __name__ == '__main__':
    main()
