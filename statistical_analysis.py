import pandas as pd

# load data
# MATAN:
# data_path = 'data/'
# filename = 'robot_interaction_data/raw_data_25-09-2018_09:30'
# beh_rel_prob = pd.read_csv(data_path + 'amt_probs/probs_from_AMT.csv').values
# GOREN:
data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/'
external_filename = 'all_data/all_external_data.csv'
internal_filename = 'all_data/all_internal_data.csv'
# filename = 'raw_data_18-09-2018_03_33/raw_data_18-09-2018_03_33'

all_external = pd.read_csv(open(data_path + external_filename))
all_external = all_external[all_external.Subject_ID.notnull()]
all_external.set_index('Subject_ID', inplace=True)
all_internal = pd.read_csv(open(data_path + internal_filename))
all_internal.set_index('Subject_ID', inplace=True)

all_data = pd.concat([all_external, all_internal], axis=1)



print(all_data.shape)