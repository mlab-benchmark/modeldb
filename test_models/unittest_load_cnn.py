import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf;
import numpy as np
from tensorflow.keras.preprocessing import image
import unittest
import importlib.util


def test_model_load(x):
    """Imports a neural network architecure by name.

    Args:
        x: the name of the CNN architecture.

    Returns:
        The CNN architecture as generator function.
    """
    modulename = x.split(".")[0]

    spec = importlib.util.spec_from_file_location(modulename, "models/%s" % (x))
    mod = importlib.util.module_from_spec(spec)

    sys.modules[modulename] = mod
    spec.loader.exec_module(mod)
    return mod.__dict__[modulename]  # this is the generator function


class TestAutoLoad(unittest.TestCase):
    """
    Tests to validate if all networks can be loaded automatically.
    """

    def test_auto_load(self):
        """
        TEST #1: check if all models can be loaded by name.
        """
        # let us check for models available
        modx = [x for x in os.listdir("models") if x.endswith(".py")]
        for x in modx:
            m = test_model_load(x)()


if __name__ == "__main__":
    pass
