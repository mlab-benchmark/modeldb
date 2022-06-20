import tensorflow as tf

def vgg19_vitis(input_tensor=None,include_top=True, weight_path=None,return_tensor=False, classes=1000, classifier_activation="softmax"):
    
    if input_tensor is None:
        input_tensor = tf.keras.layers.Input(shape=(224,224,3))
    
    
    
    x = tf.keras.layers.Conv2D(filters =64, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(input_tensor)
    x = tf.keras.layers.Conv2D(filters =64, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(x)

    x = tf.keras.layers.Conv2D(filters =128, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =128, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(x)

    x = tf.keras.layers.Conv2D(filters =256, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =256, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =256, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =256, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(x)

    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(x)

    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters =512, kernel_size=3, strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(x)

    if include_top is True:
        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(4096, activation='relu')(x)
        x = tf.keras.layers.Dense(4096, activation='relu')(x)
        x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)
        #return tf.keras.Model(input_tensor, new_outputs)

    if return_tensor:
        return x
    else:
        model = tf.keras.Model(input_tensor, x)
        if weight_path is not None:
            model.load_weights(weight_path)

        return model
