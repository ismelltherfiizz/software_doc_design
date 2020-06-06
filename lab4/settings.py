import configparser
class settings:
    conf = configparser.ConfigParser()
    conf.read("settings.ini")
    CONFIG = conf['LAB']