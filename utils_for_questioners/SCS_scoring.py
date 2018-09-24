#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def SCS_scoring(SCS_data):
    score_dict={}

    #parametres:
    reverse_score_list=[]

    General_Social_Curiosity = [1,2,3,4,5]
    Covert_Social_Curiosity  = [8,9,10,11,12]
    total=[1,2,3,4,5,8,9,10,11,12]


    #go over every subject:
    for index, row in SCS_data.iterrows():

        score_dict[index]={}
        total_score=[]
        General_Social_Curiosity_score = []
        Covert_Social_Curiosity_score = []


        #go over every question:
        for question in range(1,15):
            #calculate the score:
            #reverse scores:
            if question in reverse_score_list:
                question_score=5-row[question]
            #Regular score:
            else:
                question_score = row[question]

            #Total score:
            if question in total:
                total_score.append(question_score)


            #Sub scores:
            if question in General_Social_Curiosity:
                General_Social_Curiosity_score.append(question_score)

            elif question in Covert_Social_Curiosity:
                Covert_Social_Curiosity_score.append(question_score)

        score_dict[index]['SCS_total_score']=np.nanmean(total_score)
        score_dict[index]['General_Social_Curiosity'] = np.nanmean(General_Social_Curiosity_score)
        score_dict[index]['Covert_Social_Curiosity'] = np.nanmean(Covert_Social_Curiosity_score)

    # crate df:
    SCS_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    SCS_score_df=SCS_score_df[['General_Social_Curiosity','Covert_Social_Curiosity','SCS_total_score']]


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

    return SCS_score_df