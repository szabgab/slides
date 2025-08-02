import os
import sys
import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50

if len(sys.argv) < 2:
    exit(f"{sys.argv[0]} IMAGEs")


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
resnet50_weights = 'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
#rn50 = ResNet50(include_top=False, weights=None, pooling='avg')
#rn50 = ResNet50(include_top=False, weights=resnet50_weights, pooling='avg', input_shape=(512, 128, 1)) #(256, 256, 3))
rn50 = ResNet50(weights=resnet50_weights) #(256, 256, 3))
#rn50 = ResNet50(include_top=False, weights=None, input_shape=(640, 480, 3), pooling='avg')
#rn50 = ResNet50(include_top=False, weights=None)
#rn50 = ResNet50(include_top=False, weights="imagenet", pooling="avg")


#rn50.load_weights(resnet50_weights)
exit()
target_size = (640, 480)

for path in sys.argv[1:]:
    print(path)
    im = cv2.imread(path)
    print(im.shape)
    im = cv2.resize(im, target_size)
    print(im.shape)
    #old = im.copy()
    #im[0][0][0] = 0
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB) / 255.
    #print(np.array_equal(old, im))
    im = im[np.newaxis, ...]
    act = rn50.predict(im)
    print(act)
