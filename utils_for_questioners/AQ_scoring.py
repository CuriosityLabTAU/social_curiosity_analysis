#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

def AQ_scoring(aq_data):

    score_dict={}

    #parametres:
    questions_high=[1, 2, 4, 5, 6, 7,9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41,42, 43, 45, 46]
    questions_low=[3, 8, 10, 11, 14, 15, 17, 24, 25, 27, 28, 29, 30, 31, 32,34, 36, 37, 38, 40, 44, 47, 48, 49, 50]

    social_skill=[1,11,13,15,22,36,44,45,47,48]
    attention_switching=[2,4,10,16,25,32,34,37,43,46]
    attention_to_detail=[5,6,9,12,19,23,28,29,30,49]
    communication=[7,17,18,26,27,31,33,35,38,39]
    imagination=[3,8,14,20,21,24,40,41,42,50]

    #go over every subject:
    for index, row in aq_data.iterrows():
        score_dict[index]={}
        total_score=0
        social_skill_score=0
        attention_switching_score=0
        attention_to_detail_score=0
        communication_score=0
        imagination_score=0

        #go over every question:
        for question in range(1,51):
            #calculate the score:

            if question in questions_high:
                if row[question]>2:
                    total_score+=1

                    if question in social_skill:
                        social_skill_score+=1

                    elif question in attention_switching:
                        attention_switching_score+=1

                    elif question in attention_to_detail:
                        attention_to_detail_score += 1

                    elif question in communication:
                        communication_score += 1

                    elif question in imagination:
                        imagination_score += 1

            elif question in questions_low:
                if row[question] <3:
                    total_score+=1

                    if question in social_skill:
                        social_skill_score += 1

                    elif question in attention_switching:
                        attention_switching_score += 1

                    elif question in attention_to_detail:
                        attention_to_detail_score += 1

                    elif question in communication:
                        communication_score += 1

                    elif question in imagination:
                        imagination_score += 1



        score_dict[index]['AQ_total_score']=total_score
        score_dict[index]['social_skill'] = social_skill_score
        score_dict[index]['attention_switching'] = attention_switching_score
        score_dict[index]['attention_to_detail'] = attention_to_detail_score
        score_dict[index]['communication'] = communication_score
        score_dict[index]['imagination'] = imagination_score


    # crate df:
    aq_score_df= pd.DataFrame.from_dict(score_dict, orient='index')

    aq_score_df=aq_score_df[['social_skill','attention_switching','attention_to_detail','communication','imagination','AQ_total_score']]


    # ##export to excel
    # # Create a Pandas Excel writer using XlsxWriter as the engine.
    # writer = pd.ExcelWriter('data/AQ_scores.xlsx', engine='xlsxwriter')
    #
    # # Write each dataframe to a different worksheet.
    # aq_score_df.to_excel(writer, sheet_name='AQ_scores')
    #
    #
    # # Close the Pandas Excel writer and output the Excel file.
    # writer.save()

    return aq_score_df
