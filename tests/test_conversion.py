import pytest
from util4tests import run_single_test, log
from pyconsem import Convertor


def test_convertor():
    log. info("testing the conversion")
    with pytest.raises(AssertionError, match="Convertor needs input to work on"):
        Convertor(dict()).run()


""" The kind of config we should be able to handle:
env:
  SOME_KEY: some_value

in:
  - wget: https://www.marineregions.org/ns/placetypes.ttl
  - wget: https://www.marineregions.org/ns/ontology.ttl
  - pysubyt:
      sets:
        _: "{BASE}/input/file.csv"
      template:
        foler: "{BASE}/pysubyt/"
        name: huppeldepup.ttl

out:
  - dump: "{BASE}/dump/full-graph.ttl"
  - pykm2tbl:
      result: "{BASE}/output/whatever.csv"
      query:
        folder: "{BASE}/pykm2tbl/"
        name: zomaar.sparql
        args:
          x: 1
"""


if __name__ == "__main__":
    run_single_test(__file__)
