# Import Dependencies
import cv2
import numpy as np
from skimage import io 
from skimage.transform import rotate, AffineTransform, warp
from skimage import img_as_ubyte
from skimage.util import random_noise
import matplotlib.pyplot as plt
import random
import os

# Defining functions for augmenting image
def anticlockwise_rotation(image):
    angle= random.randint(0,180)
    return rotate(image, angle)

def clockwise_rotation(image):
    angle= random.randint(0,180)
    return rotate(image, -angle)

def add_noise(image):
    return random_noise(image)

def blur_image(image):
    return cv2.GaussianBlur(image, (5,5), 0)

# Store transformations in dict
transformations = {'rotate anticlockwise': anticlockwise_rotation, 'rotate clockwise': clockwise_rotation,
                   'add noise': add_noise, 'blur image':blur_image}

# Generating path to images
curr_dir = os.getcwd()
images_to_aug_dir = os.path.dirname(curr_dir)

# Setting path for augmented images to go
images_dir = os.path.dirname(images_to_aug_dir)
augmented_dir = os.path.join(images_dir, 'augmented_images')

# Storing image files
images=[]
for im in os.listdir(curr_dir):
    if im.endswith('.png'):
        images.append(os.path.join(curr_dir,im))

# Setting number of generated images
images_to_generate = 100
i = 1

while i <= images_to_generate:    
    image = random.choice(images)
    original_image = io.imread(image)
    transformed_image=None

    # Choose random number of transformations to apply on image
    transformation_count = random.randint(1, len(transformations))
    n = 0
    
    while n <= transformation_count:
        key = random.choice(list(transformations))
        transformed_image = transformations[key](original_image)
        n = n + 1
    
    # Setting augmented image path
    new_image_path = "%s/augmented_yield%s.png" %(augmented_dir, i)
    
    # Processing transformed image to unsigned byte format
    transformed_image = img_as_ubyte(transformed_image)
    
    # Processing transformed image to RGB
    transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
    
    # Writing transformed image to file
    cv2.imwrite(new_image_path, transformed_image)
    i = i + 1
