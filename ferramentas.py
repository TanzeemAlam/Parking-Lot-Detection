import cv2  
import imutils
from imutils import perspective 

import numpy as np
from matplotlib import pyplot as plt 
import glob


class image_utils():

    def __init__(self):
        pass
    
    #extracting the features
    def extract_features(self, img_resize):

        lista_globals = []

        for image in img_resize:
            
            #Calculating the histogram for arrays.
            hist = cv2.calcHist([image], [0], None, [256], [0,256])
            #Flattening the images/ histogram or we can say reshapping
            hist = hist.flatten()
            
            #detecting the edges in an image
            edged = cv2.Canny(image, 200, 250)
            #reshaping the edges
            edged = edged.flatten()

            flat = image.flatten()
            
            #stacking the arrays into a single array
            global_feature = np.hstack([hist, edged, flat])
            
            #print(global_feature.shape)
            lista_globals.append(global_feature)

        #print(lista_globals.shape)
        lista_globals = np.asarray(lista_globals)
        #print(lista_globals.shape)
    return lista_globals

            
            

    def getSpotsCoordiantesFromImage(img, num_space) :
        #coordinate_lists has this format[ [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], [], [] ]
        coordinate_lists = []
        spots_index_list = []
        
        for i in range(num_space):
            plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
            #setting the current tick location
            plt.xticks([]), plt.yticks([])
            #we need 4 points to get rectangle
            #calculating the click locations of user and storing it
            coordinate = plt.ginput(4)
            print("The clicked coordinates are", coordinate)
            coordinate_lists.append(coordinate)
            spots_index_list.append(i)
        #closing the figure
        plt.close()
        
        return coordinate_lists


    ''' rotating image '''
    def getRotateRect(img, cooridnate_lists, WIDTH = 100, HEIGHT = 100):
        
        #Incomplete


    def load_image_from_path(self, path):

        lista_imagens = []

        img_list = []
        for files in glob.glob(path + "/*.jpg"):
            img = cv2.imread(files)

            img = self.transform_image(img)            
            img_list.append(img)

        return img_list


    def load_imagens_keras_with_labels(path):
        #Incomplete

    def transform_image(self, image, WIDTH = 100, HEIGHT = 100):

        img = image
        #converting the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #blur or smoothen the image
        img = cv2.GaussianBlur(img, (7, 7), 0)   
        #resizing the image
        img = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_CUBIC)

        return img
