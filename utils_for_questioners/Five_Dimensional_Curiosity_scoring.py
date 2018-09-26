#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def Five_Dimensional_Curiosity_scoring(Five_Dimensional_Curiosity_data):
    score_dict={}

    #parametres:

    Joyous_Exploration =[1,5,11,16,21]
    Deprivation_Sensitivity= [2,7,12,17,22]
    Stress_Tolerance =[3,8,13,18,23]
    Social_Curiosity= [4,9,14,19,24]
    Thrill_Seeking =[5,10,15,20,25]

    reverse_score_list= Stress_Tolerance

    #go over every subject:
    for index, row in Five_Dimensional_Curiosity_data.iterrows():

        score_dict[index]={}
        Joyous_Exploration_score = []
        Deprivation_Sensitivity_score = []
        Stress_Tolerance_score = []
        Social_Curiosity_score = []
        Thrill_Seeking_score = []

        #go over every question:
        for question in range(1,26):
            #calculate the score:
            #reverse scores:
            if question in reverse_score_list:
                question_score=8-row[question]
            #Regular score:
            else:
                question_score = row[question]

            #Sub scores:
            if question in Joyous_Exploration:
                Joyous_Exploration_score.append(question_score)

            elif question in Deprivation_Sensitivity:
                Deprivation_Sensitivity_score.append(question_score)

            elif question in Stress_Tolerance:
                Stress_Tolerance_score.append(question_score)

            elif question in Social_Curiosity:
                Social_Curiosity_score.append(question_score)

            elif question in Thrill_Seeking:
                Thrill_Seeking_score.append(question_score)

        score_dict[index]['_5DC_Joyous_Exploration'] = np.nanmean(Joyous_Exploration_score)
        score_dict[index]['_5DC_Deprivation_Sensitivity'] = np.nanmean(Deprivation_Sensitivity_score)
        score_dict[index]['_5DC_Stress_Tolerance'] = np.nanmean(Stress_Tolerance_score)
        score_dict[index]['_5DC_Social_Curiosity'] = np.nanmean(Social_Curiosity_score)
        score_dict[index]['_5DC_Thrill_Seeking'] = np.nanmean(Thrill_Seeking_score)

    # crate df:
    Five_Dimensional_Curiosity_scoring_scoring_df= pd.DataFrame.from_dict(score_dict, orient='index')
    Five_Dimensional_Curiosity_scoring_scoring_df=Five_Dimensional_Curiosity_scoring_scoring_df[['_5DC_Joyous_Exploration',
                                                                                                 '_5DC_Deprivation_Sensitivity',
                                                                                                 '_5DC_Stress_Tolerance',
                                                                                                 '_5DC_Social_Curiosity',
                                                                                                 '_5DC_Thrill_Seeking']]


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

    return Five_Dimensional_Curiosity_scoring_scoring_df