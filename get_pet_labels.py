#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nour Mallak
# DATE CREATED:  27/5/2024                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #create empty ditionary named results_dic
    results_dic = dict()
    # Retrieve file names from the image_dir folder
    in_files = listdir(image_dir) 
    files_list=listdir(image_dir) 
    for n in range(0,len(in_files),1) :
      #The pet image labels the following way:should be Lower case letters
        in_files[n]=in_files[n].lower()
    #create empty string named pet_label at started
    pet_label_list=[]
    for file in in_files:
      split_file=file.split("_")
      pet_label=""
      for word in split_file:
        # check if word in pet image name is only alphabetic characters  if true append word to pet_label separated by trailing space 
        if word.isalpha(): 
          #Single space separating each word
          pet_label +=word+" " 
          # strip off starting/trailing whitespace characters 
      pet_label=pet_label.strip()
      pet_label_list.append(pet_label)
    for key in range(0,len(files_list),1):
      list_for_labels = []
      #add new key-value pairs to results_dic when key does not already exis
      if files_list[key] not in results_dic :
          list_for_labels.append(pet_label_list[key])
          results_dic[files_list[key]]=list_for_labels
      else:
          print("Warning! This key is already exists in result_dec with value :", results_dic[files_list[key]])
    return results_dic
