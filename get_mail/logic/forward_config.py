import csv


filename = './conf/forward.conf'


class ForwardConfig:
    def __init__(self):
        with open(filename, encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            content = [row for row in reader]
        self.__header = header
        self.__contents = [dict(zip(header, row)) for row in content]

    def get_all_id(self):
        id_key = self.__header[0]
        return [content[id_key] for content in self.__contents]

    def get_address_by_id(self, id):
        id_key = self.__header[0]
        address_key = self.__header[1]

        for content in self.__contents:
            if id == content[id_key]:
                return content[address_key]
        raise ValueError('キーが存在しません')
