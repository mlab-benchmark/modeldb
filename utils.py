import os
import importlib.util
import sys


def model_load(x):
    modulename=x.split(".")[0]

    spec = importlib.util.spec_from_file_location(modulename, "models/%s" % (x))
    mod = importlib.util.module_from_spec(spec)
    
    sys.modules[modulename] = mod
    spec.loader.exec_module(mod)
    return mod.__dict__[modulename] # this is the generator function
