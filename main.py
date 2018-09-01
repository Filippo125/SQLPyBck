from optparse import OptionParser
import json
import yaml     
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from const import HI_DEBUG,MD_DEBUG,LOW_DEBUG

DEBUG = 0


class Initializer:

    def __init__(self):
        self.readCli()
        self.readConf()

    def readCli(self):
        usageInfo = "usage: %prog [option]"
        parser = OptionParser(usage=usageInfo, version="%prog 0.1")
        parser.add_option("-v", dest="low_vrb", action="store_true", help="low level of verbosity", default=False)
        parser.add_option("-vv", dest="md_vrb", action="store_true", help="medium level of verbosity", default=False)
        parser.add_option("-vvv", dest="hi_vrb", action="store_true", help="high level of verbosity", default=False)
        parser.add_option("-V", "--version", dest="version", action="store_true", help="show version info", default=False)
        parser.add_option("-c", "--config", dest="config_path", action="store_true", default="./config.yaml",)
        (options, args) = parser.parse_args()
        if options.hi_vrb:
            DEBUG = HI_DEBUG
        elif options.md_vrb:
            DEBUG = MD_DEBUG
        elif options.low_vrb:
            DEBUG = LOW_DEBUG
        self.config_path = options.config_path

    def readConf(self):
        """
        Read yaml config file 
        """
        with open(self.config_path,"r") as f:
            config = yaml.load(f.read())
            if DEBUG >= HI_DEBUG:
                print("Read configuration from yaml:")
                print(json.dumps(config,indent=2))
                print("\n")
            self.database = config['database']
            self.exclude  = config['exclude_databases']



if __name__ == '__main__':
    Initializer()