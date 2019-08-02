## referencia : https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten , Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.regularizers import l2
from keras.layers.normalization import BatchNormalization

def model(tamanho,profundidade,numero_classes):
    modelo = Sequential()

    # fully-connected layer
    modelo.add(Flatten(),input_shape = (tamanho,tamanho,profundidade))
    modelo.add(Dense(512))
    modelo.add(Activation("relu"))
    modelo.add(BatchNormalization())
    modelo.add(Dropout(0.5))

    # softmax classifier
    modelo.add(Dense(numero_classes))
    modelo.add(Activation("softmax"))
    return modelo