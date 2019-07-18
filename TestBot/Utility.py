import configparser
from pathlib import Path
import os


class Util:

    @staticmethod
    def get_config_parser(config_file_path):
        config = configparser.RawConfigParser()
        config.read(config_file_path)
        return config

    @staticmethod
    def get_js_str(file_path):
        with open(file_path,'r') as file1:
            str_val=file1.read()
            return str_val


if __name__ == "__main__":
    cls1=Util()
    path=os.path.join(Path(__file__).parents[1],'js_file')
    print(cls1.get_js_str(path))
