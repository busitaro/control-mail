import configparser
import os
import errno

file_path = 'conf'
config_file = 'api.ini'


class Config():
    def __init__(self):
        path_to_config_file = '{}/{}'.format(file_path, config_file)
        if not os.path.exists(path_to_config_file):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                path_to_config_file
            )
        self.__parser = configparser.ConfigParser()
        self.__parser.read(path_to_config_file, encoding='utf_8')

    @property
    def client_id(self):
        section = 'DEFAULT'
        key = 'client_id'
        return self.__parser.get(section, key)

    @property
    def client_secret(self):
        section = 'DEFAULT'
        key = 'client_secret'
        return self.__parser.get(section, key)

    @property
    def token_path(self):
        section = 'DEFAULT'
        key = 'token_path'
        return self.__parser.get(section, key)

    @property
    def token_file(self):
        section = 'DEFAULT'
        key = 'token_file'
        return self.__parser.get(section, key)
