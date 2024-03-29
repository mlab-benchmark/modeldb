import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import unittest
import importlib
import subprocess
import numpy as np
import urllib.request
import tensorflow as tf
from pathlib import Path
from yaml import safe_load, YAMLError
from utils import model_load


class cfg:
    """
    Configuration for the test.
    """
    weight_store="./tmp"
    ds_store="./tmp"
    model_name="densenet121_vitis"


def train_model(model):
    """
    Inferance of a given model using a image from ImageNet.
    :param model: The Keras model.
    :return: a list containing the prediction results (format depends on the type and activation of the last layer).
    """
    img = tf.keras.preprocessing.image.load_img("testdata/Walking_tiger_female.jpg", target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    return model.predict(img_batch)[0]


class TestCNN(unittest.TestCase):
    """
    Tests to validate a single convolutional neural network.
    """
    @classmethod
    def setUpClass(cls):
        """Gets all needed data and information for the tests."""
        try:
            with open("credentials.yaml", 'r') as stream:
                cred = safe_load(stream)
        except FileNotFoundError as e:
            print(e)
            print("Filed loading credentials for webpage", )
            exit()

        cfg.httpauth = (cred["User"], cred["Pwd"])
        cfg.baseurl = cred["Url"]

        Path(cfg.weight_store).mkdir(parents=True, exist_ok=True)
        Path(cfg.weight_store).mkdir(parents=True, exist_ok=True)

        print("Downloading Weights...")
        cls.w_top = "%s/imagenet_%s.h5" % (cfg.weight_store, cfg.model_name.split("_")[0])
        cls.w_notop = "%s/imagenet_%s_notop.h5" % (cfg.weight_store, cfg.model_name.split("_")[0])

        def mlab_getweight(outfile):
            """
            Downloads and saves the weights for a model.
            :param outfile: The location where the file will be saved.
            """
            if os.path.exists(outfile):
                print("Using cached file %s" % outfile)
            url = '%s/weights/%s' % (cfg.baseurl, outfile.split('/')[-1])
            try:

                passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
                passman.add_password(None, cfg.baseurl, cfg.httpauth[0], cfg.httpauth[1])
                authhandler = urllib.request.HTTPBasicAuthHandler(passman)
                opener = urllib.request.build_opener(authhandler)
                urllib.request.install_opener(opener)

                urllib.request.urlretrieve(url, outfile)

            except urllib.error.HTTPError as e:
                # do something
                print('Error code: ', e.code, ", ", url)
                exit()
            except urllib.error.URLError as e:
                # do something
                print('Reason: ', e.reason, ", ", url)
                exit()

        mlab_getweight(cls.w_top)
        mlab_getweight(cls.w_notop)

    def test_no_w_no_top_tensor(self):
        """Test #1 to test the functionality of the neural network

        Config:
        -------
        Weights: False
        Top Layers: False
        Network as Tensor: True
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            x = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=False, return_tensor=True, weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        self.assertNotEqual(x._name, "predictions", "Model has top layers!")
        self.assertFalse("dense" in x._name.lower(), "Model has top layers!")

        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)

        model = tf.keras.Model(new_inputs, x, name="TestModel")

        prediction = train_model(model)

        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_no_w_with_top_tensor(self):
        """Test #2 to test the functionality of the neural network

        Config:
        -------
        Weights: False
        Top Layers: True
        Network as Tensor: True
        """

        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            x = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=True, return_tensor=True, weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        self.assertTrue("predictions"  in x._name or "dense" in x._name.lower(), "Model has no top layers!")

        model = tf.keras.Model(new_inputs, x, name="TestModel")
        prediction = train_model(model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_no_w_no_top_sequential(self):
        """Test #3 to test the functionality of the neural network

        Config:
        -------
        Weights: False
        Top Layers: False
        Network as Tensor: False
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            base_model = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=False, return_tensor=False, weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        self.assertNotEqual(base_model.layers[-1].name.lower(), "predictions", "Model has top layers!")
        self.assertFalse("dense" in base_model.layers[-1].name.lower(), "Model has top layers!")
        self.assertTrue(isinstance(base_model, tf.keras.Model))

        x = base_model(new_inputs)
        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)

        model = tf.keras.Model(new_inputs, x, name="TestModel")
        prediction = train_model(model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_no_w_with_top_sequential(self):
        """Test #4 to test the functionality of the neural network

        Config:
        -------
        Weights: False
        Top Layers: True
        Network as Tensor: True
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            base_model = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=True, return_tensor=False, weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        self.assertTrue("predictions"  in base_model.layers[-1].name.lower() or "dense" in base_model.layers[-1].name.lower(), "Model has no top layers!")
        self.assertTrue(isinstance(base_model, tf.keras.Model))

        prediction = train_model(base_model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_with_w_no_top_tensor(self):
        """Test #5 to test the functionality of the neural network

        Config:
        -------
        Weights: True
        Top Layers: False
        Network as Tensor: True
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            x = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=False, return_tensor=True, weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        conv = tf.keras.Model(new_inputs, x)
        old_w = conv.get_weights()
        conv.load_weights(self.w_notop)
        new_w = conv.get_weights()

        self.assertFalse((np.array_equal(old_w, new_w)), "Weights not loaded!")

        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)

        model = tf.keras.Model(new_inputs, x, name="TestModel")
        prediction = train_model(model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_with_w_with_top_tensor(self):
        """Test #6 to test the functionality of the neural network

        Config:
        -------
        Weights: True
        Top Layers: True
        Network as Tensor: True
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            x = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=True, return_tensor=True,weight_path=None)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        conv = tf.keras.Model(new_inputs, x)
        old_w = conv.get_weights()
        conv.load_weights(self.w_top)
        new_w = conv.get_weights()

        self.assertFalse((np.array_equal(old_w, new_w)), "Weights not loaded!")

        model = tf.keras.Model(new_inputs, x, name="TestModel")
        prediction = train_model(model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_with_w_no_top_sequential(self):
        """Test #7 to test the functionality of the neural network

        Config:
        -------
        Weights: True
        Top Layers: False
        Network as Tensor: False
        """
        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            base_model = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=False, return_tensor=False,weight_path=self.w_notop)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        x = base_model(new_inputs)
        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)

        model = tf.keras.Model(new_inputs, x, name="TestModel")
        prediction = train_model(model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")

    def test_with_w_with_top_sequential(self):
        """Test #8 to test the functionality of the neural network

        Config:
        -------
        Weights: True
        Top Layers: True
        Network as Tensor: False
        """

        new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
        try:
            base_model = model_load("%s.py" % cfg.model_name)(new_inputs, include_top=True, return_tensor=False,weight_path=self.w_top)
        except ValueError:
            self.fail("[test_cnn_no_w_no_top] model_load() raised ValueError unexpectedly!")

        prediction = train_model(base_model)
        self.assertEqual(len(prediction), 1000, "Test expected length of the output tensor!")


if __name__=="__main__":
    pass