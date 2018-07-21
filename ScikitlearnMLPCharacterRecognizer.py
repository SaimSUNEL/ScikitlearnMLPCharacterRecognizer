import cv2
from sklearn import neural_network
import pickle

#For this sample program we will recognize just three characters....
resimler = ["A", "B", "C"]
#The train images are in this directory...
resim_klasoru = "Characters/"
#We will hold the samples in these lists...
#Input vectors will be hold in this list...
X = []
#The corresponding ground thruths for the samples will be hold in this list...
Y = []

#We are loading our images in to the train set...
for harf in resimler:
    #We will load 50 images per character....
    for i in range(0, 50):
        #We are reading the image file from the directory...
        image = cv2.imread(resim_klasoru+harf+str(i)+".jpg")

        #for each image we need to create a vector size of which is 28x28=784
        sample = []
        #We are looking at each pixel of the image, the images consists of r,g,b channels...
        #but our images are just blank and white
        #If the current pixel's rgb values are bigger than 0, we will put a 1.0 value into the vector of sample
        #otherwise we will add 0.0
        for b in range(0, 28):
            for a in range(0, 28):
                if image[b, a].all() >0:
                    sample.append(1.0)
                else:
                    sample.append(0.0)

        #After we have we have vectorized our image, we are putting it to our train set...
        #We are also putting the corresponding ground truth of the sample...
        X.append(sample)
        Y.append(harf)
        cv2.waitKey(0)

#After loading the train data we are constructing our MLP
#Our MLP has only 1 hidden layer with 500 neurons
#learning rate of the nn is 0.01
#We are using stochastic gradien descent for learning...
#While the nn is being trained, we are displaying the current loss information..
#If our loss function improves less that 1e-7 than we are terminating the learning
#We are using sigmoid for the activation of the hidden layer...
#Max 1500 times, the train set will be passed over for training if no improvement less than 1e-7 occurs in the loss function...
network = neural_network.MLPClassifier( tol=1e-7 , verbose=1000,learning_rate_init=.01,solver="sgd" , activation="logistic", max_iter = 1500 , hidden_layer_sizes= (500 ,  )   )
#We are training our neural network....
network.fit(X, Y)

#after training we are saving our nn to disk to load it from the other programs...
pickle.dump ( network , open ( "CharacterRecognizer.ns" , "wb"))

#After training we are testing our nn
#We are getting an image which has not been included in the train set
test_image = cv2.imread(resim_klasoru+"A51.jpg")
#We are obtaining its vector form in the same form as train samples...
test = []
for b in range(0, 28):
    for a in range(0, 28):
        if test_image[b, a].all() > 0:
            test.append(1.0)
        else:
            test.append(0.0)

#We are feeding it to our trained neural network and displayin the final result...
print "Result : ", network.predict([test])
print "score : " , network.score( [ test ]  , [ 'iki'])
print "Result : ", network.predict_proba([test])