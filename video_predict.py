import numpy as np
from keras import optimizers
from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers import InputLayer , Conv2D ,MaxPooling2D ,Dense , UpSampling2D
from keras.preprocessing.image import img_to_array, load_img, ImageDataGenerator
from IPython.display import display, Image
from skimage.color import rgb2lab , lab2rgb ,rgb2gray
import cv2
from skimage.io import imsave
#import progressbar
from keras.models import model_from_json
json_file = open('model/model.json','r')
loaded_model = json_file.read()
model = model_from_json(loaded_model)
model.load_weights('model/model.h5')

videoCap = cv2.VideoCapture('video_input/trimed_video3.mp4')
ret, image = videoCap.read()
count = 0
frames = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
#frame_size = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(frame_size)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out_file = cv2.VideoWriter('coloured_video.avi',-1,20.0, frame_size)

#bar = progressbar.ProgressBar(redirect_stdout=True)

for i in range(frames):
    try:
        X = rgb2lab(1.0/255*image)[:,:,0]
        #Y = rgb2lab(1.0/255*image)[:,:,1:]
        X = X.reshape(1, len(image), len(image[0]), 1)
        #Y = Y.reshape(1, len(image), len(image[0]), 2)
        output = model.predict(X)
        output *= 128
        cur = np.zeros((len(image), len(image[0]), 3))
        cur[:,:,0] = X[0][:,:,0]
        cur[:,:,1:] = output[0] 
        imsave("video_output/img_"+str(count)+".png", lab2rgb(cur) )
        count += 1
        #for j in range(30):
        ret,image = videoCap.read()
        #bar.update(i/frames*100)
        #output_image = lab2rgb(cur)
        #out_file.write(output_image)
    except:
        pass
#out_file.release()
