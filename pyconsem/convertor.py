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
        log.warning("TODO - create the run method")
