import csv


filename = './conf/send.conf'


class SendConfig:
    def __init__(self):
        with open(filename, encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            content = [row for row in reader]
        self.__header = header
        self.__contents = [dict(zip(header, row)) for row in content]

    def get_all_address(self):
        address_key = self.__header[0]
        return [content[address_key] for content in self.__contents]

    def get_key_by_address(self, address):
        address_key = self.__header[0]
        key_key = self.__header[1]

        for content in self.__contents:
            if address == content[address_key]:
                return content[key_key]
        raise ValueError('キーが存在しません')
