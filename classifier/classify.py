__author__ = 'Naleen'


__author__ = 'Naleen'

import pickle

import numpy as np

import cv2
import Orange
import os
from src.mapper import feature_mapper
from src.scripts import normalize, fileIO, locate_character, prob_match


package_directory = os.path.dirname(os.path.abspath(__file__))

np.set_printoptions(threshold='nan')

classifier_lower = pickle.load(open(os.path.join(package_directory,'learner/ANN_lower')))
classifier_middle = pickle.load(open(os.path.join(package_directory,'learner/ANN_middle')))
classifier_upper = pickle.load(open(os.path.join(package_directory,'learner/ANN_upper')))
# lowerZoneLabels = fileIO.read_label_file('learner/lowerZoneLabels')
# middleZoneLabels = fileIO.read_label_file('learner/middleZoneLabels')
# upperZoneLabels = fileIO.read_label_file('learner/upperZoneLabels')


def classify(img):
    lowerZoneLabels = fileIO.read_label_file('learner/lowerZoneLabels')
    middleZoneLabels = fileIO.read_label_file('learner/middleZoneLabels')
    upperZoneLabels = fileIO.read_label_file('learner/upperZoneLabels')

    index = 0
    #print img
    # for i in range(1, 3)
    if img is None:
        # print "None"
        return ""

    if img.any() == np.array([0]).all():
        # print "space"
        return " "

    else:        
        #im = np.array(img * 255, dtype = np.uint8)
        #gray = np.array(img * 255, dtype = np.uint8)

        dataString_middle=""
        dataString_lower=""
        dataString_upper=""

        character = img
        # print character

        character = normalize.get_mask(character, 5)
        xMin, xMax, yMin, yMax= locate_character.char_location(character)
        # print xMin, xMax, yMin, yMax

        dataArray_middle = feature_mapper.middle(character, 21, 43, xMin, xMax)
        dataArray_middle.append('m1')
        # print dataArray_middle

        dataArray_lower = feature_mapper.lower(character, 42, 64, xMin, xMax)
        dataArray_lower.append('l0')
        # print dataArray_lower

        dataArray_upper = feature_mapper.upper(character, 0, 22, xMin, xMax)
        dataArray_upper.append('u0')

        # for i in range(1, 3):
        # char1=""
        # char2=""
        # char3=""
        MiddleZoneProb = classifier_middle(dataArray_middle, Orange.classification.Classifier.GetProbabilities)
        UpperZoneProb = classifier_upper(dataArray_upper, Orange.classification.Classifier.GetProbabilities)
        LowerZoneProb = classifier_lower(dataArray_lower, Orange.classification.Classifier.GetProbabilities)

        # MiddleZoneClass=(classifier_middle(dataArray_middle, Orange.classification.Classifier.GetBoth))
        # UpperZoneClass=(classifier_upper(dataArray_upper, Orange.classification.Classifier.GetBoth))
        # LowerZoneClass=(classifier_lower(dataArray_lower, Orange.classification.Classifier.GetBoth))

        ###############################################
        if classifier_lower(dataArray_lower, Orange.classification.Classifier.GetValue) == 'l0':
        
            for i in range(0, len(lowerZoneLabels)):
               lowerZoneLabels[i] = 'l0'
        
            for i in xrange(0, len(LowerZoneProb)):
               LowerZoneProb[i] = 1
        
        
        if classifier_upper(dataArray_upper, Orange.classification.Classifier.GetValue) == 'u0':
        
            for i in range(0, len(upperZoneLabels)):
               upperZoneLabels[i] = 'u0'
        
            for i in xrange(0, len(UpperZoneProb)):
               UpperZoneProb[i] = 1

        predicted_char, lower, middle, upper = prob_match.probability_match(lower=[LowerZoneProb,lowerZoneLabels],
                                                middle=[MiddleZoneProb, middleZoneLabels],
                                                upper=[UpperZoneProb,upperZoneLabels])
        # char_mapper.char_map()

        # print char+"   "+lower+"  "+middle+"  "+upper
        return predicted_char

def classify_image(url):
    img = cv2.imread(url)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    char = classify(img)
    print char

#classify_image("/home/viduranga/Desktop/project/segmenter/single_characters/2_1_r.jpg")
# classify_image("C:/Users/Naleen/PycharmProjects/sinhala_ocr/segmenter/final_characters/14.jpg")
