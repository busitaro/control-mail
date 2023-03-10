from sys import argv

from O365 import Account
from O365 import FileSystemTokenBackend


def main(client_id: str, client_secret: str):
    """
    認証を行う

    """
    credentials = (client_id, client_secret)
    token_backend = \
        FileSystemTokenBackend(
            token_path='.',
            token_filename='token.json'
        )
    account = Account(credentials, token_backend=token_backend)
    if account.authenticate(scopes=['basic', 'message_all']):
        print('Authenticated!')


if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError('insufficent params')

    client_id = argv[1]
    client_secret = argv[2]

    main(client_id, client_secret)
