#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def CEI_2_scoring(CEI_2_data):
    score_dict={}

    #parametres:
    reverse_score_list=[]

    stretching =[1,3,5,7,9]
    embracing= [2,4,6,8,10]

    #go over every subject:
    for index, row in CEI_2_data.iterrows():

        score_dict[index]={}
        total_score=[]
        stretching_score = []
        embracing_score = []


        #go over every question:
        for question in range(1,11):
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
            if question in stretching:
                stretching_score.append(question_score)

            elif question in embracing:
                embracing_score.append(question_score)

        score_dict[index]['CEI_2_total_score']=np.nanmean(total_score)
        score_dict[index]['stretching'] = np.nanmean(stretching_score)
        score_dict[index]['embracing'] = np.nanmean(embracing_score)

    # crate df:
    CEI_2_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    CEI_2_score_df=CEI_2_score_df[['stretching','embracing','CEI_2_total_score']]


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

    return CEI_2_score_df