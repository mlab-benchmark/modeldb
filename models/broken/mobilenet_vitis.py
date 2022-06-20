import tensorflow as tf


def conv_layer(x, filters, stride=1):
    x = tf.keras.layers.Conv2D(filters, kernel_size=(3,3), strides=(stride,stride), padding='same', use_bias=False)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)
    
    return x


def depthwise_conv_layer(x, filters, stride=1, depth_multiplier=1):
    x = tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), strides=(stride,stride), padding='same', depth_multiplier=depth_multiplier, use_bias=False)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)


    x = tf.keras.layers.Conv2D(filters, kernel_size=(1,1), strides=(1,1), padding='same', use_bias=False)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)

    return x


def mobilenet_vitis(input_tensor=None, alpha = 1.0,depth_multiplier=1, include_top=True, weight_path=None, return_tensor=False, classes=1000, classifier_activation="softmax"):
    """_summary_
    Args:
        alpha (float, optional): controls the width of the network.
            - If `alpha` < 1.0, proportionally decreases the number
                of filters in each layer.
            - If `alpha` > 1.0, proportionally increases the number
                of filters in each layer.
            - If `alpha` = 1, default number of filters from the paper
                 are used at each layer.
        depth_multiplier (int, optional): The number of depthwise convolution output channels
            for each input channel. Defaults to 1.
    """
    if input_tensor is None:
        input_tensor = tf.keras.layers.Input(shape=(224,224,3))

    x = tf.keras.layers.ZeroPadding2D()(input_tensor)
    x = conv_layer(x, int(32 * alpha), 2)
    x = depthwise_conv_layer(x, int(64 * alpha), depth_multiplier=depth_multiplier)
    x = tf.keras.layers.ZeroPadding2D()(x)
    x = depthwise_conv_layer(x, int(128 * alpha), 2, depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(128 * alpha), depth_multiplier=depth_multiplier)
    x = tf.keras.layers.ZeroPadding2D()(x)
    x = depthwise_conv_layer(x, int(256 * alpha), 2, depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(256 * alpha), depth_multiplier=depth_multiplier)
    x = tf.keras.layers.ZeroPadding2D()(x)
    x = depthwise_conv_layer(x, int(512 * alpha), 2, depth_multiplier=depth_multiplier)

    x = depthwise_conv_layer(x, int(512 * alpha), depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(512 * alpha), depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(512 * alpha), depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(512 * alpha), depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(512 * alpha), depth_multiplier=depth_multiplier)

    x = tf.keras.layers.ZeroPadding2D()(x)
    x = depthwise_conv_layer(x, int(1024 * alpha), 2, depth_multiplier=depth_multiplier)
    x = depthwise_conv_layer(x, int(1024 * alpha), 2, depth_multiplier=depth_multiplier)

    if include_top is True:
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = tf.keras.layers.Reshape((None, 1000))
        x = tf.keras.layers.Flatten()(x)
        #new_outputs = tf.keras.layers.Dense(number_of_classes, activation='softmax')(x)
        #return tf.keras.Model(input_tensor, new_outputs)

    if return_tensor:
        return x
    else:
        model = tf.keras.Model(input_tensor, x)
        if weight_path is not None:
            model.load_weights(weight_path)
            if return_tensor is True:
                print('loading of pretrained weights only supported through the model API. Set return_tensor to False, load the weights, and extract the required layer manually from the returned model')


        return model 
    
