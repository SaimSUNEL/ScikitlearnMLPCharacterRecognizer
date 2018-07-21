from sklearn import neural_network
import cv2
from cv2 import *
import random
import pickle

resim_klasoru = "Characters/"

#We are loding trained nn from the disk....
network = pickle.load ( open ( 'CharacterRecognizer.ns' , 'rb'))
#The characters being tested...
characters = ["A", "B", "C"]

correct_count = 0
wrong_count = 0

#We are testing all training images....
for character in characters:
    for image_index in range(0, 50):

        test_image = cv2.imread(resim_klasoru+character+str(image_index)+".jpg")
        #We are obtaining its vector form
        test = []
        for b in range(0, 28):
            for a in range(0, 28):
                if test_image[b, a].all() > 0:
                    test.append(1.0)
                else:
                    test.append(0.0)

        #We are feeding it to our trained neural network and displayin the result...
        result = network.predict([test])
        print "Result : ", result
        #We are keeping the accuracy statistics...
        if result[0] == character:
            correct_count +=1
        else:
            wrong_count +=1
        print "score : " , network.score( [ test ]  , [ 'iki'])
        print "Result : ", network.predict_proba([test])
        
print("Total accuracy : %f" % (correct_count/(correct_count+wrong_count)*100.0))