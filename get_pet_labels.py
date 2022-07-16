#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: E. LeFort
# DATE CREATED: 07/04/2022                                 
# REVISED DATE: 07/06/2022
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
    filename_list = listdir(image_dir)
    results_dic = {}
    temp_dic = {}

    for filename in filename_list:
        print(filename)
        
        petLabel = "" #create blank variable. 
        pet_image_name = filename.lower().strip().split("_") #Remove unwanted txt from filename. 
        
        #Create petLabels from filename
        for idx in range(0, len(filename_list), 1):
            
            if filename_list[idx][0] != ".":
                
                pet_label = ""
            
                #Remove space at begining and end of petLabel (Value) 
                #and add back to dictionary
                #temp_dic[filename] = petLabel.strip() 
                    
                pet_name_list = filename_list[idx].lower().split("_")
            
                #Remove duplicate values from dictionary within temp_dic
                # with dictionary comprehension. 
                #temp = {val : key for key, val in temp_dic.items()}
                #results_dic = {val : key for key, val in temp.items()}
                
                for name in pet_name_list:
                    
                    if name.isalpha():
                        
                        pet_label += name + " "
                  
                pet_label = pet_label.strip()
                
                if filename_list[idx] not in results_dic:
                    
                    results_dic[filename_list[idx]] = [pet_label]
                    
                else:
                    
                    print("** Warning: Duplicate files exist in directory:", filename_list[idx])                   
    
    #Print temp_dic, contains all keys and values including duplicates
    #print("\n Tempory dictionary: " + str(temp_dic))
    
    #Print results_dic, contains all unique keys and values
    #print("\n Results Dictionary: " + str(results_dic))
    
    # Replace None with the results_dic dictionary 
    #that you created with this function
    return results_dic
