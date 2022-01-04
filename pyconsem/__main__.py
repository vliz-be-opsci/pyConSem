# -*- coding: utf-8 -*-
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
import os
from dotenv import load_dotenv
import logging
import logging.config
import yaml
from pyconsem import Convertor


log = logging.getLogger(__name__)
DEFAULT_CONFIG_FILE = 'pyconsem.yml'
load_dotenv()


def get_arg_parser():
    """ Defines the arguments to this script by using Python's [argparse](https://docs.python.org/3/library/argparse.html)
    """
    parser = ArgumentParser(description='Py Project to perform data conversion using semantics and knowledge-graphs',
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-l', '--logconf',
        type=str,
        metavar="LOGCONF.FILE",
        action='store',
        help='location of the logging config (yml) to use',
    )

    # TODO define your own command line arguments
    parser.add_argument(
        '-c', '--config',
        type=str,
        metavar="CONFIG.FILE",
        action='store',
        help='Config file for the conversion',
    )
    return parser


def yml_to_dict(fname):
    with open(fname, 'r') as ymlf:
        return yaml.load(ymlf, Loader=yaml.SafeLoader)


def enable_logging(args: Namespace):
    if args.logconf is None:
        return
    logging.config.dictConfig(yml_to_dict(args.logconf))
    log.info(f"Logging enabled according to config in {args.logconf}")


def load_config(args: Namespace):
    config_file = args.config if args.config else os.environ.get('CONSEM_CONFIG', DEFAULT_CONFIG_FILE)
    log.info(f"Using Convertor config from {config_file}")
    log.info(f"env == {os.environ}")
    return yml_to_dict(config_file)


def main():
    """ The main entry point to this module.
    """
    args = get_arg_parser().parse_args()
    enable_logging(args)
    config = load_config(args)

    Convertor(config).run()


if __name__ == '__main__':
    main()
