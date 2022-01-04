""" pyconsem

.. module:: pyconsem
    :synopsis: Py Project to perform data conversion using semantics and knowledge-graphs

.. moduleauthor:: Marc Portier <marc.portier@gmail.com>

"""

from .convertor import MyModel
import logging

__all__ = ['MyModel']

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
