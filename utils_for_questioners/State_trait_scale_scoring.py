#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def State_trait_scale_scoring(State_trait_data):
    score_dict={}

    #parametres:
    reverse_score_list=[1,4,9,20,25,28,30,33,36,38,40,
                        41,45,48,65,68,70,72,76,78,80]

    S_Anxiety =[1,5,9,13,17,21,25,29,33,37]
    S_Curiosity= [2,6,10,14,18,22,26,30,34,38]
    S_Anger =[3,7,11,15,19,23,27,31,35,39]
    S_Depression= [4,8,12,16,20,24,28,32,36,40]

    T_Anxiety =[41,45,49,53,57,61,65,69,73,77]
    T_Curiosity= [42,46,50,54,58,62,66,70,74,78]
    T_Anger =[43,47,51,55,59,63,67,71,75,79]
    T_Depression= [44,48,52,56,60,64,68,72,76,80]

    #go over every subject:
    for index, row in State_trait_data.iterrows():

        score_dict[index]={}
        total_score=[]
        S_Anxiety_score=[]
        S_Curiosity_score=[]
        S_Anger_score=[]
        S_Depression_score=[]

        T_Anxiety_score=[]
        T_Curiosity_score=[]
        T_Anger_score=[]
        T_Depression_score=[]


        #go over every question:
        for question in range(1,81):
            #calculate the score:
            #reverse scores:
            if question in reverse_score_list:
                question_score=5-row[question]
            #Regular score:
            else:
                question_score = row[question]

            #Total score:
            total_score.append(question_score)


            #Sub scores:
            if question in S_Anxiety:
                S_Anxiety_score.append(question_score)

            elif question in S_Curiosity:
                S_Curiosity_score.append(question_score)

            elif question in S_Anger:
                S_Anger_score.append(question_score)

            elif question in S_Depression:
                S_Depression_score.append(question_score)


            elif question in T_Anxiety:
                T_Anxiety_score.append(question_score)

            elif question in T_Curiosity:
                T_Curiosity_score.append(question_score)

            elif question in T_Anger:
                T_Anger_score.append(question_score)

            elif question in T_Depression:
                T_Depression_score.append(question_score)



        score_dict[index]['S_Anxiety'] = np.nanmean(S_Anxiety_score)
        score_dict[index]['S_Curiosity'] = np.nanmean(S_Curiosity_score)
        score_dict[index]['S_Anger'] = np.nanmean(S_Anger_score)
        score_dict[index]['S_Depression'] = np.nanmean(S_Depression_score)

        score_dict[index]['T_Anxiety'] = np.nanmean(T_Anxiety_score)
        score_dict[index]['T_Curiosity'] = np.nanmean(T_Curiosity_score)
        score_dict[index]['T_Anger'] = np.nanmean(T_Anger_score)
        score_dict[index]['T_Depression'] = np.nanmean(T_Depression_score)

    # crate df:
    State_trait_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    State_trait_score_df=State_trait_score_df[['S_Anxiety','S_Curiosity','S_Anger','S_Depression','T_Anxiety','T_Curiosity','T_Anger','T_Depression']]


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

    return State_trait_score_df