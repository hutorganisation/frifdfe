import configparser
import os

config = configparser.ConfigParser()
config.read(os.getenv('CONFIG_PATH'))

db_path = config['DEFAULT']['db_path']