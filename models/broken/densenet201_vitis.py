import tensorflow as tf

#batch norm + relu + conv
def bn_relu_conv(x,filters,kernel=1,strides=1):
        
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation(tf.nn.relu)(x)
    x = tf.keras.layers.Conv2D(filters, kernel, strides=strides, padding='same')(x)
    return x

def dense_block(x,filters,strides=1, bottleneck=True):
    if bottleneck is True:
        skip = tf.keras.layers.BatchNormalization()(x)
        skip = tf.keras.layers.Activation(tf.nn.relu)(skip)
        skip = tf.keras.layers.Conv2D(filters * 4, kernel_size=(1,1), strides=strides, padding='valid', use_bias=False)(skip)
    else:
        skip = x

    skip = tf.keras.layers.BatchNormalization()(skip)
    skip = tf.keras.layers.Activation(tf.nn.relu)(skip)
    skip = tf.keras.layers.Conv2D(filters, kernel_size=(3,3), strides=strides, padding='same', use_bias=False)(skip)

    out = tf.keras.layers.concatenate([skip,x])

    return out

def transition_layer(x, filters,strides=1, compression=0.5):
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation(tf.nn.relu)(x)
    x = tf.keras.layers.Conv2D((x.shape[-1])*compression, kernel_size=(1,1), strides=strides, padding='same', use_bias=False)(x) 

    x = tf.keras.layers.AvgPool2D(2, strides = 2, padding = 'same')(x)

    return x


def densenet201_vitis(input_tensor=None, include_top=True, weight_path=None, return_tensor=False, classes=1000, classifier_activation="softmax"):
    if input_tensor is None:
        input_tensor = tf.keras.layers.Input(shape=(224,224,3))

    grow_rate=32
    compression=0.5
    kernel_size_first_layer=(7,7)

    x = tf.keras.layers.ZeroPadding2D()(input_tensor)
    x = tf.keras.layers.Conv2D(grow_rate*2, kernel_size=kernel_size_first_layer, strides=2, padding='valid', use_bias=False)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation(tf.nn.relu)(x)
    x = tf.keras.layers.ZeroPadding2D()(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)

    no_blocks = [6,12,48,32]

    for idx, block_count in enumerate(no_blocks):
        for _ in range(block_count):
            x = dense_block(x, grow_rate)
        if idx != (len(no_blocks)-1):
            x = transition_layer(x, grow_rate, compression=compression)

    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation(tf.nn.relu)(x)
    
    if include_top is True:
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        #x = tf.keras.layers.Flatten()(x)
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
