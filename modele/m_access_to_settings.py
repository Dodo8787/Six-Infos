import configparser
from pathlib import Path


class accessToSettings():

    def __init__(self, file_name):
        self.path = Path(__file__).parent.parent
        if file_name != 'theme.ini':
            parser_theme = configparser.ConfigParser()
            parser_theme.read(str(self.path) + '/theme.ini')
            theme_actuel = parser_theme.get('theme', 'theme_actuel')
            complement_path = '/Themes/' + theme_actuel
        else:
            complement_path = ''
        self.parser = configparser.ConfigParser()
        self.parser.read(str(self.path) + complement_path + '/' + file_name)
        self.file_name = file_name

    def get(self, section, option):
        try:
            return str(self.parser.get(section, option))
        except configparser.NoSectionError:
            pass

    def set(self, section, option, value):
        if self.file_name != 'theme.ini':
            parser_theme = configparser.ConfigParser()
            parser_theme.read(str(self.path) + '/theme.ini')
            theme_actuel = parser_theme.get('theme', 'theme_actuel')
            complement_path = '/Themes/' + theme_actuel
        else:
            complement_path = ''
        try:
            self.parser.set(section, option, str(value))
        except configparser.NoSectionError:
            self.parser.add_section(section)
            self.parser.set(section, option, str(value))
        with open(str(self.path) + complement_path + '/' + self.file_name, 'w') as f:
            self.parser.write(f)
        return value

    def set_section(self, section):
        if self.file_name != 'theme.ini':
            parser_theme = configparser.ConfigParser()
            parser_theme.read(str(self.path) + '/theme.ini')
            theme_actuel = parser_theme.get('theme', 'theme_actuel')
            complement_path = '/Themes/' + theme_actuel
        else:
            complement_path = ''
        self.parser.add_section(section)
        with open(str(self.path) + complement_path + '/' + self.file_name, 'w') as f:
            self.parser.write(f)
