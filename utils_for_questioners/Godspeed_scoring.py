#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def Godspeed_scoring(Godspeed_data):
    score_dict={}

    #parametres:
    reverse_score_list=[21,23]

    Anthropomorphism =[1,2,3,4,5]
    Animacy= [6,7,8,9,10,11]
    Likeability= [12,13,14,15,16]
    perceived_Intelligence= [17,18,19,20,21]
    Safety_of_Robots= [22,23,24]


    #go over every subject:
    for index, row in Godspeed_data.iterrows():

        score_dict[index]={}
        total_score=[]
        Anthropomorphism_score=[]
        Animacy_score=[]
        Likeability_score=[]
        perceived_Intelligence_score=[]
        Safety_of_Robots_score=[]

        #go over every question:
        for question in range(1,25):
            #calculate the score:
            #reverse scores:
            if question in reverse_score_list:
                question_score=6-row[question]
            #Regular score:
            else:
                question_score = row[question]

            #Total score:
            total_score.append(question_score)


            #Sub scores:
            if question in Anthropomorphism:
                Anthropomorphism_score.append(question_score)

            elif question in Animacy:
                Animacy_score.append(question_score)

            elif question in Likeability:
                Likeability_score.append(question_score)

            elif question in perceived_Intelligence:
                perceived_Intelligence_score.append(question_score)

            elif question in Safety_of_Robots:
                Safety_of_Robots_score.append(question_score)

        score_dict[index]['Anthropomorphism'] = np.nanmean(Anthropomorphism_score)
        score_dict[index]['Animacy'] = np.nanmean(Animacy_score)
        score_dict[index]['Likeability'] = np.nanmean(Likeability_score)
        score_dict[index]['perceived_Intelligence'] = np.nanmean(perceived_Intelligence_score)
        score_dict[index]['Safety_of_Robots'] = np.nanmean(Safety_of_Robots_score)

    # crate df:
    Godspeed_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    Godspeed_score_df=Godspeed_score_df[['Anthropomorphism','Animacy','Likeability','perceived_Intelligence','Safety_of_Robots']]


    # ##export to excel
    # # Create a Pandas Excel writer using XlsxWriter as the engine.
    # writer = pd.ExcelWriter('data/BFI_scores.xlsx', engine='xlsxwriter')
    #
    # # Write each dataframe to a different worksheet.
    # BFI_score_df.to_excel(writer, sheet_name='BFI_scores')
    #
    #
    # # Close the Pandas Excel writer and output the Excel file.
    # writer.save()

    return Godspeed_score_df