#import numpy array as training data

import numpy as np


### importing data


training_data_images =[]

training_data_images = np.load('training_data_images.npy')

print (training_data_images)

print ("foo")

training_data_labels = []

training_data_labels = np.load('training_data_labels.npy')

file_name = "compiled_training_data.npy"

#import complete 
compiled_foo = []



def compile():
    training_data_images = np.load('training_data_images.npy')
    training_data_labels = np.load('training_data_labels.npy')
    i = 0
    for i in range (0,6087):
        comp_image = training_data_images[i]
        comp_label = training_data_labels[i]
        compiled_foo.append([comp_image, comp_label])


compile()       

np.save(file_name, compiled_foo)

print ("import complete")

