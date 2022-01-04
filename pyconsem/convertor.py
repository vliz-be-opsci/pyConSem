# Use this file to describe the datamodel handled by this module
# we recommend using abstract classes to achieve proper service and interface insulation
from abc import ABC  # , abstractmethod
import logging


log = logging.getLogger(__name__)


class Convertor(ABC):
    """ Main class performing the conversion
    """

    def __init__(self, config: dict):
        """ constructor

        :param config: The configuration describing the conversion to be ran
        """
        self._config = config

    def run(self):
        """ Runs the steps described in the config
        """
        self.prepare()
        self.input()
        log.warning("TODO -- load and output")
        # self.load()
        # self.output()
        log.info("conversion complete")

    def prepare(self):
        """ analyzes the config and creates internal worker-objects to actually handle the conversion
        """
        #  TODO - make some work-space-temp-folder

        assert 'in' in self._config, "Convertor needs input to work on"
        self._input_producers = list()
        for num, input_config in enumerate(self._config['in']):
            # out_file = num
            log.warning(f"have to make InputProducer {num}, {input_config}")
            # append producer

    def input(self):
        """ produces the inputs to load
        """
        for i in self._input_producers:
            i.produce(self)
