import configparser
from pathlib import Path


class MColumnSetter:

    def __init__(self):
        self.path = Path(__file__).parent.parent
        self.parser = configparser.ConfigParser()
        self.parser.read(str(self.path) + '/Themes/Defaut/settings.ini')
        self.monitor = self.parser.get('app_settings', 'monitor')
