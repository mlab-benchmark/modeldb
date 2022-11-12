import os
import importlib.util
import sys


def model_load(x):
    """Loads a convolutional neural network architecture by name.

    Args:
        x (string): the name of the CNN.

    Returns:
        The CNN architecture as generator function.
    """
    modulename=x.split(".")[0]

    spec = importlib.util.spec_from_file_location(modulename, "models/%s" % (x))
    mod = importlib.util.module_from_spec(spec)
    
    sys.modules[modulename] = mod
    spec.loader.exec_module(mod)
    return mod.__dict__[modulename] # this is the generator function
