"""
Code Created by Aseem Gill May 15th 2021

Required Packages: csv, pandas, numpy
"""


import csv
import pandas as pd
import numpy as np
def data_in(file,kind):
    """Imports Data
    ==============================================================================================
    Imports the survey results for a mentee or mentor and stores the information as a dictionary
    
    :param file --> string containing the name of the csv file that has the survey results
    :param kind --> string indicating whether the results are for a "Mentor" or "Mentee"
    
    :type file --> string
    :type kind --> string
    
    :return_param names_dict --> nested dictionary containing survey results for a mentor or 
    mentee the keys of this dictionary will correspond to the mentee or mentors names while the 
    values will return a dictionary containing the survey questions as the keys and the 
    mentees/mentors results as the values 
    
    :return_type names_dict --> type
    
    Required packages: csv
    """
    
    names_dict = {}#Initialize empty dictionary
    
    #Collect information from Mentee pairing survey information from csv file as a series of lists
    if kind == "Mentees": #checks if the user has inputted the survey results for a mentee
        with open(file) as csvfile:
            #Reading in the csv file by comma delimeter
            Person = csv.reader(csvfile,delimiter=',')
            #Initializing empty lists to collect data
            name = list()
            email = list()
            desired = list()
            area = list()
            secondary_area = list()
            area_importance = list()
            career = list()
            career_import = list()
            frequency = list()
            leadership = list()
            hobby = list()
            year = list()
            for row in Person:
                #Filling empty lists with data from survey
                name.append(row[0])
                email.append(row[1])
                desired.append(row[2])
                area.append(row[3])
                secondary_area.append(row[4])
                area_importance.append(row[5])
                career.append(row[6])
                career_import.append(row[7])
                frequency.append(row[8])
                leadership.append(row[9])
                hobby.append(row[10])
                year.append(row[11])

        #Creates dictionary which will contain the names of the Mentees as keys and their survey
        #information stored in the dicitionary as the value
        for i in range(1,len(name)):
            names_dict[name[i]] = {"Email":email[i],"Mentor":desired[i],"Area":area[i],
                                   "Secondary Area":secondary_area[i],"Area Importance":int(area_importance[i]),"Career":career[i],"Career Importance":int(career_import[i]),"Frequency":frequency[i],"Leadership":int(leadership[i]),"Hobby":hobby[i],"Year":int(year[i])}
    
    #Collect information from Mentor pairing survey information from csv file as a series of lists
    elif kind == "Mentors": #checks if the user has inputted the survey results for a mentee
        with open(file) as csvfile:
            #Reading in the csv file by comma delimeter
            Person = csv.reader(csvfile,delimiter=',')
            #Initializing empty lists to collect data
            name = list()
            email = list()
            desired = list()
            area = list()
            career = list()
            frequency = list()
            leadership = list()
            hobby = list()
            age_pref = list()
            Num_mentees = list()
            for row in Person:
                #Filling empty lists with data from survey
                name.append(row[0])
                email.append(row[1])
                desired.append(row[2])
                area.append(row[3])
                career.append(row[4])
                frequency.append(row[5])
                leadership.append(row[6])
                hobby.append(row[7])
                age_pref.append(row[8])
                Num_mentees.append(row[9])
        
        #Creates dictionary which will contain the names of the Mentors as keys and their survey
        #information stored in the dicitionary as the value
        for i in range(1,len(name)):
            names_dict[name[i]] = {"Email":email[i],"Mentee":desired[i],"Area":area[i],
                                   "Career":career[i], "Frequency":frequency[i],"Leadership":bool(leadership[i]),"Hobby":hobby[i],"Age Preference":age_pref[i],"Number of Mentees":int(Num_mentees[i])}
    
    return(names_dict) #Returns a dictionary containing the Mentees or Mentors survey results


def calculate_score(Mentee,Mentor,Mentee_name,Mentor_name):
    """ Calculate the Pairing Score between a single mentee-mentor pairing
    ==============================================================================================
    
    This function calcualtes the score of a single mentee-mentor pairing based on the survey 
    results. The weightings for each category may be modified easily by changing the numbers 
    within this function.
    
    :param Mentee -->  dictionary containing the survery results of a single Mentee, the keys
    contain the questions while the values contain their survey responses
    :param Mentor -->  dictionary containing the survery results of a single Mentor, the keys
    contain the questions while the values contain their survey responses
    :param Mentee_name --> string containing the name of the current Mentee
    :param Mentor_name --> string containing the name of the current Mentor
    
    :type Mentee --> dictionary
    :type Mentor --> dictionary
    :type Mentee_name --> dictionary
    :type Mentor_name --> dictionary
    
    :returned
    
    Required packages: None
    """
    score = 0 #initialize score to 0
    
    #if the Mentor's Area of expertise is the same as the Mentee's Primary Desired Area we will
    #take the value of the Area Importance that the Mentee inputted multply it by 2 and add it 
    #to the score.
    if Mentee["Area"] == Mentor["Area"]:
        score += (Mentee['Area Importance'])*2
    
    #if the Mentor's Area of expertise is the same as the Mentee's Secondary Desired Area we will
    #take the value of the Area Importance that the Mentee inputted multply subtract it from 6
    #then divide the result by 2. Add this number to the score.    
    if Mentee["Secondary Area"] == Mentor["Area"]:
        score += (6-(Mentee['Area Importance']))/2
    
    #if the Mentor has had a leadership position add the Mentee's leadership importance divide by
    #2 to the score. (Mentee["Leadership"] is a bool)
    score += Mentee["Leadership"]*Mentor["Leadership"]/2
    
    #if the Mentee's desired career path (role in organization) matches the Mentor's desired 
    #career path add the value of Career Importance that the mentee inputted to the score
    if Mentor["Career"] == Mentee["Career"]:
        score += Mentee["Career Importance"] 
        
    #if the Mentor prefers a Mentee who is in their upper years of study (3rd or 4th) and the 
    #Mentee is in 3rd or 4th year a 1 is added to the score otherwise 10 is subtracted
    if Mentor["Age Preference"] == "3rd/4th year":
        if Mentee["Year"] == 3 or 4:
            score += 1
        elif Mentee["Year"] == 1 or 2:
            score -= 10
    #if the Mentor prefers a Mentee who is in their lower years of study (1st or 2nd) and the 
    #Mentee is in 1st or 2nd year a 1 is added to the score otherwise 4 is subtracted
    if Mentor["Age Preference"] == "1st/2nd year":
        if Mentee["Year"] == 1 or 2:
            score += 1
        elif Mentee["Year"] == 3 or 4:
            score -= 4
    #if the Mentee and Mentor have a common Hobby 2.5 is added to the score
    if Mentor["Hobby"] == Mentee["Hobby"]:
        score += 2.5
    #if the Mentee's preferred Mentor is the current mentor a score of 30 is added
    if Mentee["Mentor"] != "No Preference":
        if Mentor_name == Mentee["Mentor"]:
            score += 30
    #if the Mentors's preferred Mentee is the current mentor a score of 30 is added
    if Mentor["Mentee"] != "No Preference":
        if Mentee_name == Mentor["Mentee"]:
            score += 30
    #if the Mentee and Mentor have the same desired meeting frequency 2 is added to the score
    if Mentee["Frequency"] == Mentor["Frequency"]:
        score += 2
    return(score)

def construct_matrix(Mentors,Mentees,Mentors_names,Mentees_names):
    """ Construct a dataframe of the scores of every Mentee-Mentor pairing
    ==============================================================================================
    
    Construct a dataframe of the scores of every Mentee-Mentor pairing as pandas dataframe. The 
    columns are the names of the Mentors while the indices are the names of the Mentees
    
    :param Mentors --> nested dictionary containing the survey results of all Mentors, the outer
    dictionary's keys are the names of the Mentors, while the values are a dictionary containing
    the questions and results of the survey questions
    :param Mentees --> nested dictionary containing the survey results of all Mentees, the outer
    dictionary's keys are the names of the Mentees, while the values are a dictionary containing
    the questions and results of the survey questions
    :param Mentors_names --> list containing the names of all Mentors
    :param Mentees_names --> list containing the names of all Mentees
    
    :types Mentors --> dictionary
    :types Mentors --> dictionary
    :types Mentors_names --> string
    :types Mentors_names --> string
    
    :returned_param Matrix --> dataframe containing the scores between the Mentees and Mentors
    
    :returned_types Matrix --> pandas.dataframe
    
    Required packages: pandas (import pandas as pd)
    """
    Matrix = pd.DataFrame() #initialize empty dataframe
    count = 1
    #iterate through Mentors
    for j in Mentors_names:
        Mentor_name = j #Name of the current Mentor
        current_col = list() #initialize empty list to fill scores in
        col_name = list() #initialize empty list to fill Mentee names in
        for i in Mentees_names: #Iterate through names of Mentees
            Mentee = Mentees[i]  #Select Current Mentee information
            Mentor = Mentors[Mentor_name] #Select Current Mentee information
            #Calculate score between current Mentee and Mentor
            score = calculate_score(Mentee,Mentor,i,Mentor_name) 
            col_name.append(i) #Append Current Mentee name to list
            current_col.append(score) #Append score of Current Mentee and Mentor to list
        #Create single column dataframe with indices as Mentees names (col_names), and column 
        #name as current mentor and fill it with scores (current_col)
        Column = pd.DataFrame({Mentor_name:current_col},index = col_name)
        frame = [Matrix,Column] #Add column to data frame
        Matrix[Mentor_name] = pd.Series(current_col,index = Mentees_names)
        count += 1
    return(Matrix)

def pairing(Score_matrix,Mentors_names):
    """ Creates a dictionary of Mentee and Mentor pairs
    ==============================================================================================
    
    Creates a dictionary of Mentee and Mentor pairs by pairing Mentees and Mentors one by one then
    removing them from the dataframe. Mentees and Mentors are paired starting from the highest 
    score to lowest.
    
    :param Score_matrix --> dataframe containing scores of all the Mentor-Mentee pairings
    :param Mentors_names --> list containing the names of all Mentors
    
    :type Score_matrix --> pandas dataframe
    :type Mentors_names --> list
    
    :return_param pair --> dictionary containing the Mentor-Mentee Pairs, keys are Mentees, values
    are Mentors
    :return_param Matrix --> dataframe containing unpaired Mentees and Mentors after pairing
    
    :return_type pair --> dictionary
    :return_type Matrix --> dataframe
    
    Required packages: pandas
    """
    pair = dict()
    Matrix = Score_matrix
    (rows,cols) = Score_matrix.shape
    count = 1
    # Create a Mentee-Mentor pair based on highest score then remove the both individuals
    for i in range(0,len(Mentors_names)):
        Col_max = Matrix.max() #Returns max score for each Mentor
        
        #Find the Mentor with the Max score
        Max_index = list(Col_max).index(max(list(Col_max))) 
        Max_mentors = list(Matrix.columns)[Max_index]
        
        #Find the Mentee that corresponds to the max score of the Mentor
        Max_mentor_col = Matrix[Max_mentors]
        Max_mentee_no = (list(Max_mentor_col).index(max(list(Max_mentor_col))))
        Max_mentee = list(Max_mentor_col.index)[Max_mentee_no]
        
        #Pair the Mentee and Mentor together and remove the Mentee and Mentor from the dataframe
        pair[Max_mentee] = Max_mentors
        Matrix = Matrix.drop(Max_mentee)
        Matrix = Matrix.drop(Max_mentors,axis=1)
        count += 1
        #if the number of available Mentees is less than the available Mentors this will stop the code
        if count > rows:
            break
    return(pair,Matrix)

def dup_mentors(Mentors_names,Mentors):
    """ Finds Mentors who volunteered to Mentor Multiple Mentees
    ==============================================================================================
    Finds Mentors who volunteered to Mentor Multiple Mentees using the pairing survey results
    
    :param Mentors_names --> string of Mentors names
    
    :types Mentors_names --> string
    
    :return_param Num_2mentees --> list of Mentors who volunteered to mentor 2 Mentees
    :return_param Num_3mentees --> list of Mentors who volunteered to mentor 3 Mentees
    
    :return_type Num_2mentees --> list 
    :return_type Num_3mentees --> list 
    
    Required packages: None
    """
    Num_2mentees = dict()
    Num_3mentees = dict()

    for i in Mentors_names:
        if Mentors[i]["Number of Mentees"] > 1:
            Num_2mentees[i] = Mentors[i]["Number of Mentees"]
        if Mentors[i]["Number of Mentees"] > 2:
            Num_3mentees[i] = Mentors[i]["Number of Mentees"]
    return(Num_2mentees,Num_3mentees)

def next_pairing(Matrix,Mentors_names,Num_nmentees,Mentors,Mentees,leftover_Mentees):
    """ Pairs Leftover Mentees with Mentors who are open to having multiple Mentees
    ==============================================================================================
    
    :param Matrix --> dataframe containing unpaired Mentees and Mentors after pairing
    :param Num_nmentees --> list of Mentors who volunteered for 'n' mentees
    :param Mentors_names --> list containing the names of all Mentors
    :param Mentors --> nested dictionary containing the survey results of all Mentors, the outer
    dictionary's keys are the names of the Mentors, while the values are a dictionary containing
    the questions and results of the survey questions
    :param Mentees --> nested dictionary containing the survey results of all Mentees, the outer
    dictionary's keys are the names of the Mentees, while the values are a dictionary containing
    the questions and results of the survey questions
    
    :type Matrix --> dataframe
    :type Num_nmentees --> list
    :type Mentors_names --> list
    :type Mentors --> dicitionary
    :type Mentees --> dicitionary
    
    :return_param pairn --> dictionary containing the Mentor-Mentee Pairs for Mentors with n Mentees
    keys are Mentees, valuesare Mentors
    :return_param Matrix --> dataframe containing unpaired Mentees and Mentors after pairing
    
    :type pairn --> dicitionary
    :type Matrix --> dataframe
    
    Required Packages: pandas
    """
    (rows,cols) = Matrix.shape #gets the shape of the matrix
    n_mentors_dict = dict() #initialize dictionary
    
    # Collects survey results as dictionary of Mentors who volunteered for n Mentees
    for i in Mentors_names:
        if i in Num_nmentees:
            n_mentors_dict[i] = Mentors[i]

    leftover_Mentees_dict = dict()
    
    # Collects survey results as dictionary of Mentees who are unpaired
    for i in leftover_Mentees:
        leftover_Mentees_dict[i] = Mentees[i]
        
    # Score Matrix 
    n_Matrix = construct_matrix(n_mentors_dict,leftover_Mentees_dict,list(n_mentors_dict.keys()),list(leftover_Mentees_dict.keys()))
    
    # Pair Remaining Mentees
    (pairn,leftover_Menteesn) = pairing(n_Matrix,list(n_mentors_dict.keys()))
    return(pairn,leftover_Menteesn)

def reformat_csv(pair,Mentees,Mentors):
    """ Formats the pairing results in the correct fasion also included emails 
    ==============================================================================================
    
    :param pair --> dictionary containing the Mentor-Mentee Pairs, keys are Mentees, values
    are Mentors
    :param Mentors --> nested dictionary containing the survey results of all Mentors, the outer
    dictionary's keys are the names of the Mentors, while the values are a dictionary containing
    the questions and results of the survey questions
    :param Mentees --> nested dictionary containing the survey results of all Mentees, the outer
    dictionary's keys are the names of the Mentees, while the values are a dictionary containing
    the questions and results of the survey questions
    
    :param pair --> dictionary
    :types Mentors --> dictionary
    :types Mentors --> dictionary
    
    :return_param Final_list --> numpy array containing formatted results
    
    :return_types Final_list --> numpy array
    
    Required Packages: Numpy
    """
    #initialize array with header
    Final_list = np.array(['Mentee','Mentee Email','Mentor','Mentor Email'])

    for i in list(pair.keys()):
        row = list() #initialize list of empty row
        Mentee = i.replace(",","")
        row.append(Mentee) #add Mentee name to current row
        row.append(Mentees[i]["Email"]) #add Mentee email to current row
        Mentor = pair[i].replace(",","")
        M = pair[i]
        row.append(Mentor) #add Mentor name to current row
        row.append(Mentors[M]["Email"]) #add Mentor email to current row
        Final_list = np.vstack((Final_list,row)) # add pair to array
    return(Final_list)


