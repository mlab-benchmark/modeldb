# CNN Architecture DenseNet121

This is a re-implementation of DenseNet121 as [1] changed to fulfill hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as follows:

- **imagenet_densenet121.h5:** /weights/imagenet_densenet121.h5 
- **imagenet_densenet121_notop.h5:** /weights/imagenet_densenet121_notop.h5 

**Source file**: `/models/densenet121_vitis.py`

## Usage:

```python
models.densenet121_vitis.densenet121_vitis(
    input_tensor=None, 
    include_top=True, 
    weight_path=None, 
    return_tensor=False, 
    classes=1000, 
    classifier_activation="softmax",
    grow_rate=32, 
    compression=0.5, 
    kernel_size_first_layer=(7,7)
)
```

#### Arguments:
* **input_tensor**: optional keras layer, like an input tensor. 
* **include_top**: whether to include the top layers or top. 
* **weight_path**: If not none, these weights will be loaded. 
* **return_tensor**: Whether to return the network as tensor or as `tf.keras.model` (if true, weights will not be loaded). 
* **classes**: By default the number of classes are 1000 (ImageNet). Only important `include_top=True`. 
* **classifier_activation**: By default softmax (ImageNet). Only important if `include_top=True`.
* **grow_rate**: Graw rate of the network, by default 32. 
* **compression**: Compression factor of the transition layer blocks, by default 0.5 
* **kernel_size_first_layer**: Kernel size of the first layer, by default (7,7)

#### Returns:
The CNN architecture as `tf.keras.model` if `return_tensor=False`, otherwise as `tf.keras.layers`.

## References:
[1] G. Huang, Z. Liu, L. Van Der Maaten and K. Q. Weinberger, "[Densely Connected Convolutional Networks](https://doi.org/10.1109/CVPR.2017.243)," 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 2261-2269, doi: 10.1109/CVPR.2017.243.
[2]	O. Russakovsky et al., “[ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575),” International Journal of Computer Vision (IJCV), vol. 115, no. 3, pp. 211–252, 2015, doi: 10.1007/s11263-015-0816-y.
