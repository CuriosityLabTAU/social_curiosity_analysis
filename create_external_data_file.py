import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("utils_for_questioners")


processed_pt1_df=pd.read_csv('data/qualtrics/pt.1/processed_pt1.csv')
processed_pt2_df=pd.read_csv('data/qualtrics/pt.2/processed_pt2.csv')
participants_id_df=pd.read_csv('data/participants_ids/participants_id_form.csv')

# preprosses_pt1 and pt2 file:
processed_pt1_df=processed_pt1_df.rename(columns = {'Unnamed: 0':'Qualtrics_unique_ID'})
processed_pt2_df=processed_pt2_df.rename(columns = {'Unnamed: 0':'Subject_ID'})

# preprosses_id_file
participants_id_df=participants_id_df[['Subject ID', 'Qualtrics unique ID']]
participants_id_df.columns = ['Subject_ID', 'Qualtrics_unique_ID']
participants_id_df.dropna(inplace=True)


#pt2 concat to participants_id_df
processed_pt2_df.set_index('Subject_ID',inplace=True)
participants_id_df.set_index('Subject_ID',inplace=True)
pt2_to_id_df = pd.concat([processed_pt2_df,participants_id_df], axis=1)


#pt1 concat to pt2_to_id_df:
pt2_to_id_df.reset_index(inplace=True)

pt2_to_id_df.set_index('Qualtrics_unique_ID',inplace=True)
processed_pt1_df.set_index('Qualtrics_unique_ID',inplace=True)



all_external_data_df = pd.concat([pt2_to_id_df,processed_pt1_df], axis=1)

all_external_data_df.to_csv('data/external_and_internal_data/all_external_data.csv')
