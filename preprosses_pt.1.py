import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("utils_for_questioners")
from AQ_scoring import AQ_scoring
from BFI_scoring import BFI_scoring
from NARS_scoring import NARS_scoring


pt_1_data=pd.read_csv('data/qualtrics/pt.1/Pt.1_September+28%2C+2018_09.31.csv')

all_c=['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Duration (in seconds)',
       'Finished', 'RecordedDate', 'ResponseId', 'RecipientLastName', 'RecipientFirstName', 'RecipientEmail',
       'ExternalReference', 'LocationLatitude', 'LocationLongitude', 'DistributionChannel', 'UserLanguage', 'concent',
       'age', 'Q20', 'city', 'email', 'psychometric', 'grades avg.', 'Q24', 'BEAQ_1', 'BEAQ_2', 'BEAQ_3', 'BEAQ_4', 'BEAQ_5', 'BEAQ_6',
       'BEAQ_7', 'BEAQ_8', 'BEAQ_9', 'BEAQ_10', 'BEAQ_11', 'BEAQ_12', 'BEAQ_13', 'BEAQ_14', 'BEAQ_15', 'LSAS#1_1', 'LSAS#1_2', 'LSAS#1_3',
       'LSAS#1_4', 'LSAS#1_5', 'LSAS#1_6', 'LSAS#1_7', 'LSAS#1_8', 'LSAS#1_9', 'LSAS#1_10', 'LSAS#1_11', 'LSAS#1_12', 'LSAS#1_13', 'LSAS#1_14',
       'LSAS#1_15', 'LSAS#1_16', 'LSAS#1_17', 'LSAS#1_18', 'LSAS#1_19', 'LSAS#1_20', 'LSAS#1_21', 'LSAS#1_22', 'LSAS#1_23', 'LSAS#1_24', 'LSAS#2_1',
       'LSAS#2_2', 'LSAS#2_3', 'LSAS#2_4', 'LSAS#2_5', 'LSAS#2_6', 'LSAS#2_7', 'LSAS#2_8', 'LSAS#2_9', 'LSAS#2_10', 'LSAS#2_11', 'LSAS#2_12', 'LSAS#2_13',
       'LSAS#2_14', 'LSAS#2_15', 'LSAS#2_16', 'LSAS#2_17', 'LSAS#2_18', 'LSAS#2_19', 'LSAS#2_20', 'LSAS#2_21', 'LSAS#2_22', 'LSAS#2_23', 'LSAS#2_24', 'AAQ-2_1',
       'AAQ-2_2', 'AAQ-2_3', 'AAQ-2_4', 'AAQ-2_5', 'AAQ-2_6', 'AAQ-2_7', 'AAQ-2_8', 'AAQ-2_9', 'AAQ-2_10', 'GAD7_1', 'GAD7_2', 'GAD7_3', 'GAD7_4', 'GAD7_5', 'GAD7_6',
       'GAD7_7', 'GAD7_8', 'TCI-140_1', 'TCI-140_2', 'TCI-140_3', 'TCI-140_4', 'TCI-140_5', 'TCI-140_6', 'TCI-140_7', 'TCI-140_8', 'TCI-140_9', 'TCI-140_10',
       'TCI-140_11', 'TCI-140_12', 'TCI-140_13', 'TCI-140_14', 'TCI-140_15', 'TCI-140_16', 'TCI-140_17', 'TCI-140_18', 'TCI-140_19', 'TCI-140_20', 'TCI-140_21',
       'TCI-140_22', 'TCI-140_23', 'TCI-140_24', 'TCI-140_25', 'TCI-140_26', 'TCI-140_27', 'TCI-140_28', 'TCI-140_29', 'TCI-140_30', 'TCI-140_31', 'TCI-140_32',
       'TCI-140_33', 'TCI-140_34', 'TCI-140_35', 'TCI-140_36', 'TCI-140_37', 'TCI-140_38', 'TCI-140_39', 'TCI-140_40', 'TCI-140_41', 'TCI-140_42', 'TCI-140_43',
       'TCI-140_44', 'TCI-140_45', 'TCI-140_46', 'TCI-140_47', 'TCI-140_48', 'TCI-140_49', 'TCI-140_50', 'TCI-140_51', 'TCI-140_52', 'TCI-140_53', 'TCI-140_54',
       'TCI-140_55', 'TCI-140_56', 'TCI-140_57', 'TCI-140_58', 'TCI-140_59', 'TCI-140_60', 'TCI-140_61', 'TCI-140_62', 'TCI-140_63', 'TCI-140_64', 'TCI-140_65',
       'TCI-140_66', 'TCI-140_67', 'TCI-140_68', 'TCI-140_69', 'TCI-140_70', 'TCI-140_71', 'TCI-140_72', 'TCI-140_73', 'TCI-140_74', 'TCI-140_75', 'TCI-140_76',
       'TCI-140_77', 'TCI-140_78', 'TCI-140_79', 'TCI-140_80', 'AQ_1', 'AQ_2', 'AQ_3', 'AQ_4', 'AQ_5', 'AQ_6', 'AQ_7', 'AQ_8', 'AQ_9', 'AQ_10', 'AQ_11', 'AQ_12',
       'AQ_13', 'AQ_14', 'AQ_15', 'AQ_16', 'AQ_17', 'AQ_18', 'AQ_19', 'AQ_20', 'AQ_21', 'AQ_22', 'AQ_23', 'AQ_24', 'AQ_25', 'AQ_26', 'AQ_27', 'AQ_28', 'AQ_29',
       'AQ_30', 'AQ_31', 'AQ_32', 'AQ_33', 'AQ_34', 'AQ_35', 'AQ_36', 'AQ_37', 'AQ_38', 'AQ_39', 'AQ_40', 'AQ_41', 'AQ_42', 'AQ_43', 'AQ_44', 'AQ_45', 'AQ_46',
       'AQ_47', 'AQ_48', 'AQ_49', 'AQ_50', 'NARS_1', 'NARS_2', 'NARS_3', 'NARS_4', 'NARS_5', 'NARS_6', 'NARS_7', 'NARS_8', 'NARS_9', 'NARS_10', 'NARS_11',
       'NARS_12', 'NARS_13', 'NARS_14', 'BFI_1', 'BFI_2', 'BFI_3', 'BFI_4', 'BFI_5', 'BFI_6', 'BFI_7', 'BFI_8', 'BFI_9', 'BFI_10', 'BFI_11', 'BFI_12', 'BFI_13',
       'BFI_14', 'BFI_15', 'BFI_16', 'BFI_17', 'BFI_18', 'BFI_19', 'BFI_20', 'BFI_21', 'BFI_22', 'BFI_23', 'BFI_24', 'BFI_25', 'BFI_26', 'BFI_27', 'BFI_28', 'BFI_29',
       'BFI_30', 'BFI_31', 'BFI_32', 'BFI_33', 'BFI_34', 'BFI_35', 'BFI_36', 'BFI_37', 'BFI_38', 'BFI_39', 'BFI_40', 'BFI_41', 'BFI_42', 'BFI_43', 'BFI_44',
       'SC0', 'email.1', 'fname', 'pt1uniqueID', 'pt1uniqueID - Topics']




# remove_ferst_two_lines:
pt_1_data=pt_1_data.drop([0,1])

#remove subject with no pt1uniqueID (did not finish):
pt_1_data=pt_1_data[pd.notnull(pt_1_data['pt1uniqueID'])]


##BFI data
BFI_data=pt_1_data[['pt1uniqueID','BFI_1', 'BFI_2', 'BFI_3', 'BFI_4', 'BFI_5', 'BFI_6', 'BFI_7', 'BFI_8', 'BFI_9', 'BFI_10', 'BFI_11', 'BFI_12', 'BFI_13',
       'BFI_14', 'BFI_15', 'BFI_16', 'BFI_17', 'BFI_18', 'BFI_19', 'BFI_20', 'BFI_21', 'BFI_22', 'BFI_23', 'BFI_24', 'BFI_25', 'BFI_26', 'BFI_27', 'BFI_28', 'BFI_29',
       'BFI_30', 'BFI_31', 'BFI_32', 'BFI_33', 'BFI_34', 'BFI_35', 'BFI_36', 'BFI_37', 'BFI_38', 'BFI_39', 'BFI_40', 'BFI_41', 'BFI_42', 'BFI_43', 'BFI_44']]

BFI_data.columns = ['pt1uniqueID']+[i for i in xrange(1,45)]

for col in list(BFI_data):
       BFI_data[col] = BFI_data[col].astype(float)

BFI_data.set_index('pt1uniqueID',inplace=True)


# scoring:
BFI_score=BFI_scoring(BFI_data)


##AQ data:
AQ_data=pt_1_data[['pt1uniqueID','AQ_1', 'AQ_2', 'AQ_3', 'AQ_4', 'AQ_5', 'AQ_6', 'AQ_7', 'AQ_8', 'AQ_9', 'AQ_10', 'AQ_11', 'AQ_12',
       'AQ_13', 'AQ_14', 'AQ_15', 'AQ_16', 'AQ_17', 'AQ_18', 'AQ_19', 'AQ_20', 'AQ_21', 'AQ_22', 'AQ_23', 'AQ_24', 'AQ_25', 'AQ_26',
       'AQ_27', 'AQ_28', 'AQ_29','AQ_30', 'AQ_31', 'AQ_32', 'AQ_33', 'AQ_34', 'AQ_35', 'AQ_36', 'AQ_37', 'AQ_38', 'AQ_39', 'AQ_40',
       'AQ_41', 'AQ_42', 'AQ_43', 'AQ_44', 'AQ_45', 'AQ_46','AQ_47', 'AQ_48', 'AQ_49', 'AQ_50']]

AQ_data.columns = ['pt1uniqueID']+[i for i in xrange(1,51)]

for col in list(AQ_data):
       AQ_data[col] = AQ_data[col].astype(float)

AQ_data.set_index('pt1uniqueID',inplace=True)

#scoring:
AQ_score=AQ_scoring(AQ_data)

## NARS data:
NARS_data=pt_1_data[['pt1uniqueID','NARS_1', 'NARS_2', 'NARS_3', 'NARS_4', 'NARS_5', 'NARS_6', 'NARS_7', 'NARS_8', 'NARS_9', 'NARS_10', 'NARS_11',
       'NARS_12', 'NARS_13', 'NARS_14']]

NARS_data.columns = ['pt1uniqueID']+[i for i in xrange(1,15)]

for col in list(NARS_data):
       NARS_data[col] = NARS_data[col].astype(float)

NARS_data.set_index('pt1uniqueID',inplace=True)

#scoring:
NARS_score=NARS_scoring(NARS_data)

##personal_info:
personal_info_data=pt_1_data[['pt1uniqueID','concent','age', 'Q20', 'city', 'email', 'psychometric', 'grades avg.','Q24']]

#validation
personal_info_data=personal_info_data[personal_info_data.concent=='1']

personal_info_data.columns = ['pt1uniqueID']+['concent','age', 'gender', 'city', 'email', 'pet', 'avg_grades','faculty']


for col in  ['pt1uniqueID','concent','age', 'gender','pet', 'avg_grades']:
       personal_info_data[col] = personal_info_data[col].astype(float,errors='ignore')
       personal_info_data[col]=personal_info_data[col].replace('[^0-9\/]+', np.nan, regex=True)

personal_info_data.set_index('pt1uniqueID',inplace=True)

# print personal_info_data



#all pt1 concat
all_pt1_matan = pd.concat([BFI_score,AQ_score,NARS_score,personal_info_data], axis=1)
all_pt1_matan.to_csv('data/qualtrics/pt.1/processed_pt1.csv')


# save all pt_1 scored data:

def save_data_to_csv_for_matan_and_noga(pt_1_data):
       # save data as csv for matan and noga:
       # BEAQ data
       BEAQ_data=pt_1_data[['pt1uniqueID', 'BEAQ_1', 'BEAQ_2', 'BEAQ_3', 'BEAQ_4', 'BEAQ_5', 'BEAQ_6',
              'BEAQ_7', 'BEAQ_8', 'BEAQ_9', 'BEAQ_10', 'BEAQ_11', 'BEAQ_12', 'BEAQ_13', 'BEAQ_14', 'BEAQ_15']]

       BEAQ_data.columns = ['pt1uniqueID']+[i for i in xrange(1,16)]

       for col in list(NARS_data):
              NARS_data[col] = BEAQ_data[col].astype(float)

       BEAQ_data.set_index('pt1uniqueID',inplace=True)

       BEAQ_data.to_csv('data/data_for_matan_and_noga/BEAQ_data.csv')

       # LSAS_1 data
       LSAS_1_data=pt_1_data[['pt1uniqueID', 'LSAS#1_1', 'LSAS#1_2', 'LSAS#1_3',
              'LSAS#1_4', 'LSAS#1_5', 'LSAS#1_6', 'LSAS#1_7', 'LSAS#1_8', 'LSAS#1_9', 'LSAS#1_10', 'LSAS#1_11', 'LSAS#1_12', 'LSAS#1_13', 'LSAS#1_14',
              'LSAS#1_15', 'LSAS#1_16', 'LSAS#1_17', 'LSAS#1_18', 'LSAS#1_19', 'LSAS#1_20', 'LSAS#1_21', 'LSAS#1_22','LSAS#1_23', 'LSAS#1_24']]

       LSAS_1_data.columns = ['pt1uniqueID']+[i for i in xrange(1,25)]

       for col in list(LSAS_1_data):
              LSAS_1_data[col] = LSAS_1_data[col].astype(float)

       LSAS_1_data.set_index('pt1uniqueID',inplace=True)

       LSAS_1_data.to_csv('data/data_for_matan_and_noga/LSAS_1_data.csv')


       # LSAS_2 data
       LSAS_2_data=pt_1_data[['pt1uniqueID', 'LSAS#2_1',
              'LSAS#2_2', 'LSAS#2_3', 'LSAS#2_4', 'LSAS#2_5', 'LSAS#2_6', 'LSAS#2_7', 'LSAS#2_8', 'LSAS#2_9', 'LSAS#2_10', 'LSAS#2_11', 'LSAS#2_12', 'LSAS#2_13',
              'LSAS#2_14', 'LSAS#2_15', 'LSAS#2_16', 'LSAS#2_17', 'LSAS#2_18', 'LSAS#2_19', 'LSAS#2_20', 'LSAS#2_21', 'LSAS#2_22', 'LSAS#2_23', 'LSAS#2_24']]

       LSAS_2_data.columns = ['pt1uniqueID']+[i for i in xrange(1,25)]

       for col in list(LSAS_2_data):
              LSAS_2_data[col] = LSAS_2_data[col].astype(float)

       LSAS_2_data.set_index('pt1uniqueID',inplace=True)

       LSAS_2_data.to_csv('data/data_for_matan_and_noga/LSAS_2_data.csv')


       # AAQ-2 data
       AAQ_2_data=pt_1_data[['pt1uniqueID', 'AAQ-2_1','AAQ-2_2', 'AAQ-2_3', 'AAQ-2_4', 'AAQ-2_5', 'AAQ-2_6', 'AAQ-2_7', 'AAQ-2_8', 'AAQ-2_9', 'AAQ-2_10']]

       AAQ_2_data.columns = ['pt1uniqueID']+[i for i in xrange(1,11)]

       for col in list(AAQ_2_data):
              AAQ_2_data[col] = AAQ_2_data[col].astype(float)

       AAQ_2_data.set_index('pt1uniqueID',inplace=True)

       AAQ_2_data.to_csv('data/data_for_matan_and_noga/AAQ_2_data.csv')


       # GAD7 data
       GAD7_data=pt_1_data[['pt1uniqueID', 'GAD7_1', 'GAD7_2', 'GAD7_3', 'GAD7_4', 'GAD7_5', 'GAD7_6',
              'GAD7_7', 'GAD7_8']]

       GAD7_data.columns = ['pt1uniqueID']+[i for i in xrange(1,9)]

       for col in list(GAD7_data):
              GAD7_data[col] = GAD7_data[col].astype(float)

       GAD7_data.set_index('pt1uniqueID',inplace=True)

       GAD7_data.to_csv('data/data_for_matan_and_noga/GAD7_data.csv')


       # TCI-140 data
       TCI_140_data=pt_1_data[['pt1uniqueID', 'TCI-140_1', 'TCI-140_2', 'TCI-140_3', 'TCI-140_4', 'TCI-140_5', 'TCI-140_6', 'TCI-140_7', 'TCI-140_8', 'TCI-140_9', 'TCI-140_10',
              'TCI-140_11', 'TCI-140_12', 'TCI-140_13', 'TCI-140_14', 'TCI-140_15', 'TCI-140_16', 'TCI-140_17', 'TCI-140_18', 'TCI-140_19', 'TCI-140_20', 'TCI-140_21',
              'TCI-140_22', 'TCI-140_23', 'TCI-140_24', 'TCI-140_25', 'TCI-140_26', 'TCI-140_27', 'TCI-140_28', 'TCI-140_29', 'TCI-140_30', 'TCI-140_31', 'TCI-140_32',
              'TCI-140_33', 'TCI-140_34', 'TCI-140_35', 'TCI-140_36', 'TCI-140_37', 'TCI-140_38', 'TCI-140_39', 'TCI-140_40', 'TCI-140_41', 'TCI-140_42', 'TCI-140_43',
              'TCI-140_44', 'TCI-140_45', 'TCI-140_46', 'TCI-140_47', 'TCI-140_48', 'TCI-140_49', 'TCI-140_50', 'TCI-140_51', 'TCI-140_52', 'TCI-140_53', 'TCI-140_54',
              'TCI-140_55', 'TCI-140_56', 'TCI-140_57', 'TCI-140_58', 'TCI-140_59', 'TCI-140_60', 'TCI-140_61', 'TCI-140_62', 'TCI-140_63', 'TCI-140_64', 'TCI-140_65',
              'TCI-140_66', 'TCI-140_67', 'TCI-140_68', 'TCI-140_69', 'TCI-140_70', 'TCI-140_71', 'TCI-140_72', 'TCI-140_73', 'TCI-140_74', 'TCI-140_75', 'TCI-140_76',
              'TCI-140_77', 'TCI-140_78', 'TCI-140_79', 'TCI-140_80']]

       TCI_140_data.columns = ['pt1uniqueID']+[i for i in xrange(1,81)]

       for col in list(TCI_140_data):
              TCI_140_data[col] = TCI_140_data[col].astype(float)

       TCI_140_data.set_index('pt1uniqueID',inplace=True)


       TCI_140_data.to_csv('data/data_for_matan_and_noga/TCI_140_data.csv')

# save_data_to_csv_for_matan_and_noga(pt_1_data)