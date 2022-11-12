# CNN Tests

Here are some scripts provided to test the models for their functionality.

### Model Loading
The script `unittest_load_cnn.py` tests if all implemented neural networks can be automatically loaded. 

**Usage:**<br/>
```console
user@hostnmame:~$ python -m unittest  test_models/unittest_load_cnn.py
```
*Run the script from the project root directory.*

### Functionality Test
The script `unittest_cnn.py` validates the basic functionality of a specific model. This includes the following test 
configurations, and tested by predicting the class of a sample image from the dataset ImageNet:

1. **Test#1**: Load network without weights, without top, as tensor.
2. **Test#2**: Load network without weights, with top, as tensor.
3. **Test#3**: Load network without weights, without top, as `tf.keras.model.
4. **Test#4**: Load network with weights, with top, as `tf.keras.model.
5. **Test#5**: Load network with weights, without top, as tensor.
6. **Test#6**: Load network with weights, with top, as tensor.
7. **Test#7**: Load network with weights, without top, as `tf.keras.model.
8. **Test#8**: Load network with weights, with top, as `tf.keras.model.

**Usage:**<br/>
```console
user@hostnmame:~$ python -m unittest  test_models/unittest_cnn.py
```
*Run the script from the project root directory.*

### Model Loading (without testcases)
We alco provide a python script with tests if all models can be loaded.

**Usage:**<br/>
```console
user@hostnmame:~$ python test_models/unittest_load_cnn.py
```
*Run the script from the project root directory.*

### Functionality Test (without testcases)
We alco provide a python script with tests the inference of a model by first loading the model including ImageNet 
weights, followed by predicting the class of a selected image from the dataset ImageNet. 

**Usage:**<br/>
```console
user@hostnmame:~$ python test_models/legacy_test_inferance.py
```