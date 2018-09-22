#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def NARS_scoring(NARS_data):
    score_dict={}

    #parametres:
    reverse_score_list=[3,5,6]

    Negative_Attitude_toward_Situations_of_Interaction_with_Robots =[4,7,8,9,10,12]
    Negative_Attitude_toward_Social_Influence_of_Robots= [1,2,11,13,14]
    Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots= [3,5,6]

    #go over every subject:
    for index, row in NARS_data.iterrows():

        score_dict[index]={}
        total_score=[]
        Negative_Attitude_toward_Situations_of_Interaction_with_Robots_score = []
        Negative_Attitude_toward_Social_Influence_of_Robots_score = []
        Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots_score = []



        #go over every question:
        for question in range(1,15):
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
            if question in Negative_Attitude_toward_Situations_of_Interaction_with_Robots:
                Negative_Attitude_toward_Situations_of_Interaction_with_Robots_score.append(question_score)

            elif question in Negative_Attitude_toward_Social_Influence_of_Robots:
                Negative_Attitude_toward_Social_Influence_of_Robots_score.append(question_score)

            elif question in Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots:
                Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots_score.append(question_score)

        score_dict[index]['NARS_total_score']=np.nanmean(total_score)
        score_dict[index]['Negative_Attitude_toward_Situations_of_Interaction_with_Robots'] = np.nanmean(Negative_Attitude_toward_Situations_of_Interaction_with_Robots_score)
        score_dict[index]['Negative_Attitude_toward_Social_Influence_of_Robots'] = np.nanmean(Negative_Attitude_toward_Social_Influence_of_Robots_score)
        score_dict[index]['Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots'] = np.nanmean(Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots_score)

    # crate df:
    NARS_score_df= pd.DataFrame.from_dict(score_dict, orient='index')
    NARS_score_df=NARS_score_df[['Negative_Attitude_toward_Situations_of_Interaction_with_Robots','Negative_Attitude_toward_Social_Influence_of_Robots','Negative_Attitude_toward_Elmotions_in_Interaction_with_Robots','NARS_total_score']]


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

    return NARS_score_df