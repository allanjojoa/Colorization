from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

img = x_train[0]

from skimage.io import imsave

imsave("new.jpeg",img)
