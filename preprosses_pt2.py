import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("utils_for_questioners")
from CEI_2_scoring import CEI_2_scoring
from Five_Dimensional_Curiosity_scoring import Five_Dimensional_Curiosity_scoring
from SCS_scoring import SCS_scoring
from State_trait_scale_scoring import State_trait_scale_scoring
from Godspeed_scoring import Godspeed_scoring

pt_2_data=pd.read_csv('data/qualtrics/pt.2/Pt.2_September+28%2C+2018_09.51.csv')

all_c=['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Duration (in seconds)', 'Finished', 'RecordedDate', 'ResponseId',
       'RecipientLastName', 'RecipientFirstName', 'RecipientEmail', 'ExternalReference', 'LocationLatitude', 'LocationLongitude',
       'DistributionChannel', 'UserLanguage', 'unique ID', 'Godspeed_1', 'Godspeed_2', 'Godspeed_3', 'Godspeed_4', 'Godspeed_5',
       'Godspeed_6', 'Godspeed_7', 'Godspeed_8', 'Godspeed_10', 'Godspeed_11', 'Godspeed_12', 'Godspeed_13', 'Godspeed_14', 'Godspeed_15',
       'Godspeed_16', 'Godspeed_17', 'Godspeed_18', 'Godspeed_19', 'Godspeed_20', 'Godspeed_21', 'Godspeed_22', 'Godspeed_23', 'Godspeed_24',
       'Godspeed_26', 'State-trait scale 1_1', 'State-trait scale 1_2', 'State-trait scale 1_3', 'State-trait scale 1_4', 'State-trait scale 1_5',
       'State-trait scale 1_6', 'State-trait scale 1_7', 'State-trait scale 1_8', 'State-trait scale 1_9', 'State-trait scale 1_10',
       'State-trait scale 1_11', 'State-trait scale 1_12', 'State-trait scale 1_13', 'State-trait scale 1_14', 'State-trait scale 1_15',
       'State-trait scale 1_16', 'State-trait scale 1_17', 'State-trait scale 1_18', 'State-trait scale 1_19', 'State-trait scale 1_20',
       'State-trait scale 1_21', 'State-trait scale 1_22', 'State-trait scale 1_23', 'State-trait scale 1_24', 'State-trait scale 1_25',
       'State-trait scale 1_26', 'State-trait scale 1_27', 'State-trait scale 1_28', 'State-trait scale 1_29', 'State-trait scale 1_30',
       'State-trait scale 1_31', 'State-trait scale 1_32', 'State-trait scale 1_33', 'State-trait scale 1_34', 'State-trait scale 1_35',
       'State-trait scale 1_36', 'State-trait scale 1_37', 'State-trait scale 1_38', 'State-trait scale 1_39', 'State-trait scale 1_40',
       'State-trait scale 2_1', 'State-trait scale 2_2', 'State-trait scale 2_3', 'State-trait scale 2_4', 'State-trait scale 2_5',
       'State-trait scale 2_6', 'State-trait scale 2_7', 'State-trait scale 2_8', 'State-trait scale 2_9', 'State-trait scale 2_10',
       'State-trait scale 2_11', 'State-trait scale 2_12', 'State-trait scale 2_13', 'State-trait scale 2_14', 'State-trait scale 2_15',
       'State-trait scale 2_16', 'State-trait scale 2_17', 'State-trait scale 2_18', 'State-trait scale 2_19', 'State-trait scale 2_20',
       'State-trait scale 2_21', 'State-trait scale 2_22', 'State-trait scale 2_23', 'State-trait scale 2_24', 'State-trait scale 2_25',
       'State-trait scale 2_26', 'State-trait scale 2_27', 'State-trait scale 2_28', 'State-trait scale 2_29', 'State-trait scale 2_30',
       'State-trait scale 2_31', 'State-trait scale 2_41', 'State-trait scale 2_32', 'State-trait scale 2_33', 'State-trait scale 2_34',
       'State-trait scale 2_35', 'State-trait scale 2_36', 'State-trait scale 2_37', 'State-trait scale 2_38', 'State-trait scale 2_39',
       'State-trait scale 2_40', 'SCS_1', 'SCS_2', 'SCS_3', 'SCS_4', 'SCS_5', 'SCS_6', 'SCS_7', 'SCS_8', 'SCS_9', 'SCS_10', 'SCS_11',
       'SCS_12', 'SCS_13', 'SCS_14', '5DC_1', '5DC_2', '5DC_3', '5DC_4', '5DC_5', '5DC_6', '5DC_7', '5DC_8', '5DC_9', '5DC_10', '5DC_11',
       '5DC_12', '5DC_13', '5DC_14', '5DC_15', '5DC_16', '5DC_17', '5DC_18', '5DC_19', '5DC_20', '5DC_21', '5DC_22', '5DC_23', '5DC_24',
       '5DC_25', 'CEI-2_1', 'CEI-2_3', 'CEI-2_4', 'CEI-2_5', 'CEI-2_6', 'CEI-2_7', 'CEI-2_8', 'CEI-2_9', 'CEI-2_10', 'CEI-2_54']





# remove_ferst_two_lines:
pt_2_data=pt_2_data.drop([0,1])

#change two subfects ID:
pt_2_data['unique ID'] = pt_2_data['unique ID'].replace(['5237101'], '1000')
pt_2_data['unique ID'] = pt_2_data['unique ID'].replace(['2768968'], '1001')

print list(pt_2_data)

##Godspeed data
Godspeed_data=pt_2_data[['unique ID','Godspeed_1', 'Godspeed_2', 'Godspeed_3', 'Godspeed_4', 'Godspeed_5',
       'Godspeed_6', 'Godspeed_7', 'Godspeed_8', 'Godspeed_10', 'Godspeed_11', 'Godspeed_12', 'Godspeed_13', 'Godspeed_14', 'Godspeed_15',
       'Godspeed_16', 'Godspeed_17', 'Godspeed_18', 'Godspeed_19', 'Godspeed_20', 'Godspeed_21', 'Godspeed_22', 'Godspeed_23', 'Godspeed_24',
       'Godspeed_26']]

Godspeed_data.columns = ['unique_ID']+[i for i in xrange(1,25)]

for col in list(Godspeed_data):
    Godspeed_data[col] = Godspeed_data[col].astype(float)

Godspeed_data.set_index('unique_ID',inplace=True)

# scoring:
Godspeed_score=Godspeed_scoring(Godspeed_data)

##State_trait_scale_1 data
State_trait_scale_data=pt_2_data[['unique ID','State-trait scale 1_1', 'State-trait scale 1_2', 'State-trait scale 1_3', 'State-trait scale 1_4',
                                    'State-trait scale 1_5',
       'State-trait scale 1_6', 'State-trait scale 1_7', 'State-trait scale 1_8', 'State-trait scale 1_9', 'State-trait scale 1_10',
       'State-trait scale 1_11', 'State-trait scale 1_12', 'State-trait scale 1_13', 'State-trait scale 1_14', 'State-trait scale 1_15',
       'State-trait scale 1_16', 'State-trait scale 1_17', 'State-trait scale 1_18', 'State-trait scale 1_19', 'State-trait scale 1_20',
       'State-trait scale 1_21', 'State-trait scale 1_22', 'State-trait scale 1_23', 'State-trait scale 1_24', 'State-trait scale 1_25',
       'State-trait scale 1_26', 'State-trait scale 1_27', 'State-trait scale 1_28', 'State-trait scale 1_29', 'State-trait scale 1_30',
       'State-trait scale 1_31', 'State-trait scale 1_32', 'State-trait scale 1_33', 'State-trait scale 1_34', 'State-trait scale 1_35',
       'State-trait scale 1_36', 'State-trait scale 1_37', 'State-trait scale 1_38', 'State-trait scale 1_39', 'State-trait scale 1_40',
        'State-trait scale 2_1', 'State-trait scale 2_2', 'State-trait scale 2_3', 'State-trait scale 2_4','State-trait scale 2_5',
       'State-trait scale 2_6', 'State-trait scale 2_7', 'State-trait scale 2_8', 'State-trait scale 2_9', 'State-trait scale 2_10',
       'State-trait scale 2_11', 'State-trait scale 2_12', 'State-trait scale 2_13', 'State-trait scale 2_14', 'State-trait scale 2_15',
       'State-trait scale 2_16', 'State-trait scale 2_17', 'State-trait scale 2_18', 'State-trait scale 2_19', 'State-trait scale 2_20',
       'State-trait scale 2_21', 'State-trait scale 2_22', 'State-trait scale 2_23', 'State-trait scale 2_24', 'State-trait scale 2_25',
       'State-trait scale 2_26', 'State-trait scale 2_27', 'State-trait scale 2_28', 'State-trait scale 2_29', 'State-trait scale 2_30',
       'State-trait scale 2_41', 'State-trait scale 2_32', 'State-trait scale 2_33', 'State-trait scale 2_34','State-trait scale 2_35',
       'State-trait scale 2_36', 'State-trait scale 2_37', 'State-trait scale 2_38', 'State-trait scale 2_39','State-trait scale 2_40']]

State_trait_scale_data.columns = ['unique_ID']+[i for i in xrange(1,81)]

for col in list(State_trait_scale_data):
       State_trait_scale_data[col] = State_trait_scale_data[col].astype(float)

State_trait_scale_data.set_index('unique_ID',inplace=True)

# scoring:
State_trait_scale_score=State_trait_scale_scoring(State_trait_scale_data)


##scs data
scs_data=pt_2_data[['unique ID','SCS_1', 'SCS_2', 'SCS_3', 'SCS_4', 'SCS_5', 'SCS_6', 'SCS_7', 'SCS_8', 'SCS_9', 'SCS_10', 'SCS_11',
       'SCS_12', 'SCS_13', 'SCS_14']]

scs_data.columns = ['unique_ID']+[i for i in xrange(1,15)]

for col in list(scs_data):
       scs_data[col] = scs_data[col].astype(float)

scs_data.set_index('unique_ID',inplace=True)

# scoring:
scs_score=SCS_scoring(scs_data)



##Five_Dimensional_Curiosity data
Five_Dimensional_Curiosity_data=pt_2_data[['unique ID','5DC_1', '5DC_2', '5DC_3', '5DC_4', '5DC_5', '5DC_6', '5DC_7', '5DC_8', '5DC_9', '5DC_10', '5DC_11',
       '5DC_12', '5DC_13', '5DC_14', '5DC_15', '5DC_16', '5DC_17', '5DC_18', '5DC_19', '5DC_20', '5DC_21', '5DC_22', '5DC_23', '5DC_24','5DC_25']]

Five_Dimensional_Curiosity_data.columns = ['unique_ID']+[i for i in xrange(1,26)]

for col in list(Five_Dimensional_Curiosity_data):
       Five_Dimensional_Curiosity_data[col] = Five_Dimensional_Curiosity_data[col].astype(float)

Five_Dimensional_Curiosity_data.set_index('unique_ID',inplace=True)


# scoring:
Five_Dimensional_Curiosity_score=Five_Dimensional_Curiosity_scoring(Five_Dimensional_Curiosity_data)


##CEI-2 data
CEI_2_data=pt_2_data[['unique ID','CEI-2_1', 'CEI-2_3', 'CEI-2_4', 'CEI-2_5', 'CEI-2_6', 'CEI-2_7', 'CEI-2_8', 'CEI-2_9', 'CEI-2_10', 'CEI-2_54']]

CEI_2_data.columns = ['unique_ID']+[i for i in xrange(1,11)]

for col in list(CEI_2_data):
       CEI_2_data[col] = CEI_2_data[col].astype(float)

CEI_2_data.set_index('unique_ID',inplace=True)

# scoring:
CEI_2_score=CEI_2_scoring(CEI_2_data)

#all pt1 concat
all_pt2_matan = pd.concat([Godspeed_score ,State_trait_scale_score,scs_score, Five_Dimensional_Curiosity_score ,CEI_2_score], axis=1)
all_pt2_matan.to_csv('data/qualtrics/pt.2/processed_pt2.csv')
