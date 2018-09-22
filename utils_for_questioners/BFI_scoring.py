#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def BFI_scoring(BFI_data):
    score_dict={}

    #parametres:
    reverse_score_list=[6, 21, 31,2, 12, 27, 37,8, 18, 23, 43,9, 24, 34,35, 41]

    Extraversion =[1, 6, 11, 16, 21, 26, 31, 36]
    Agreeableness= [2, 7, 12, 17, 22, 27, 32, 37, 42]
    Conscientiousness= [3, 8, 13, 18, 23, 28, 33, 38, 43]
    Neuroticism= [4, 9, 14, 19, 24, 29, 34, 39]
    Openness= [5, 10, 15, 20, 25, 30, 35, 40, 41, 44]


    #go over every subject:
    for index, row in BFI_data.iterrows():

        score_dict[index]={}
        total_score=[]
        Extraversion_score = []
        Agreeableness_score = []
        Conscientiousness_score = []
        Neuroticism_score = []
        Openness_score = []


        #go over every question:
        for question in range(1,45):
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
            if question in Extraversion:
                Extraversion_score.append(question_score)

            elif question in Agreeableness:
                Agreeableness_score.append(question_score)

            elif question in Conscientiousness:
                Conscientiousness_score.append(question_score)

            elif question in Neuroticism:
                Neuroticism_score.append(question_score)

            elif question in Openness:
                Openness_score.append(question_score)

        score_dict[index]['BFI_total_score']=np.nanmean(total_score)
        score_dict[index]['Extraversion'] = np.nanmean(Extraversion_score)
        score_dict[index]['Agreeableness'] = np.nanmean(Agreeableness_score)
        score_dict[index]['Conscientiousness'] = np.nanmean(Conscientiousness_score)
        score_dict[index]['Neuroticism'] = np.nanmean(Neuroticism_score)
        score_dict[index]['Openness'] = np.nanmean(Openness_score)

    # crate df:
    BFI_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    BFI_score_df=BFI_score_df[['Extraversion','Agreeableness','Conscientiousness','Neuroticism','Openness','BFI_total_score']]


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

    return BFI_score_df