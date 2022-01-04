from util4tests import run_single_test, log
from pyconsem import Convertor


def test_convertor():
    log. info("testing the conversion")
    Convertor(dict()).run()


if __name__ == "__main__":
    run_single_test(__file__)
