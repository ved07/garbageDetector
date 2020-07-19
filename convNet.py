
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
from numpy import asarray
class model():
    def __init__(self):
        self.model = models.Sequential()

    def oneHotEncode(self):
        classes = (
            [d for d in os.listdir('Garbage classification') if
             os.path.isdir(os.path.join('Garbage classification', d))])
        self.classes = classes
        oneHotVector = []
        pos = 0
        for aclass in classes:
            array = np.zeros(6)
            array[pos] = 1
            pos += 1
            oneHotVector.append(array)
            print(oneHotVector)
        self.oneHot = oneHotVector

    def setupData(self):
        trainingImages = []
        trainingLabels = []
        for directory in os.walk('Garbage classification'):
            directory = list(directory)
            print(directory[1])
            for dir in directory[1]:
                posit = directory[1].index(dir)
                encodedValue = self.oneHot[posit]
                for file in os.listdir('Garbage classification/' + dir):
                    image = Image.open('Garbage classification/' + dir + '/' + file)
                    image = asarray(image)
                    trainingImages.append(image)
                    trainingLabels.append(encodedValue)
        trainingLabels = np.array(trainingLabels)
        trainingImages = np.array(trainingImages)
        print(trainingLabels.shape)
        print(trainingImages.shape)
        self.trainingImages = trainingImages
        print(trainingLabels)
        print(trainingImages)

        self.trainingLabels = trainingLabels

    def setupModel(self):
        model = self.model
        model.add(layers.Conv2D(32, (4, 4), activation='relu', input_shape=( 384,512, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (4, 4), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (4,4), activation='relu', input_shape=(384, 512, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(128, (4, 4), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(128, (4, 4), activation='relu'))

        model.add(layers.Flatten())

        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(6))
        self.model = model
    def compileAndTrain(self,  epochs):
        filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
        checkpoint = ModelCheckpoint(
            filepath,
            monitor='loss',
            verbose=0,
            save_best_only=True,
            mode='min'
        )
        callbacks_list = [checkpoint]
        model = self.model
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.MeanSquaredError(),
                      metrics=['mse'])

        history = model.fit(self.trainingImages, self.trainingLabels,epochs=epochs, callbacks=callbacks_list)

    def predict(self,testfile, test=False):
        self.model.load_weights('weights.hdf5')
        if test:
            inputData = Image.open('test/'+testfile)
        else:
            inputData = Image.open(testfile)
        inputData = inputData.resize((512, 384), Image.ANTIALIAS)
        inputData = asarray(inputData).reshape([1, 384, 512, 3])
        self.pred = self.model.predict(inputData)[0]
        return self.pred
    def decodeOneHot(self):
        pred = np.ndarray.tolist(self.pred)
        mp = max(pred)
        return self.classes[pred.index(mp)]


