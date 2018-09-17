import pickle
import numpy as np
import matplotlib.pyplot as plt

data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/raw_data_17-09-2018_10_57/'
filename = 'raw_data_17-09-2018_10_57'

x = pickle.load(open(data_path+filename, 'rb'))


def task_performance(tasks):
    correct = 0
    for t in tasks:
        correct += int(t['was_correct'])
    return correct

# subject_id --> {section_id[1-5]} --> turn [4, 8, 8, 8 , 8] -->

for subject_id, a in x.items():
    for section_id, b in a.items():
        # for each section, a new matrix
        for turn, c in b.items():
            # for each turn, a different agent does something
            # at the end of each turn, 4 questions
            tasks = []
            if 'q' in str(turn):
                tasks.append(c)
        b['task_performance'] = task_performance(tasks)

# research questions:

# - did they improve in learning (tasks/questions)?
# (optimal learner & behavior: use the real matrix for error calculation)
# figure: error vs section
data_for_improving = [] # list for each section
for section_id in range(5):
    s = []
    for _, a in x.items():
        s.append(a[section_id]['task_performance'])
    data_for_improving.append(s)
data_for_improving = np.array(data_for_improving)
print(data_for_improving)
plt.plot(np.arange(5), np.mean(data_for_improving, axis=1))
plt.show()

# statistical test: binomial between first and last (?)

# - given behavior (?) in each section (over turns) --> what does the matrix look like?

# MEASURES: (for each section)
# optimal learner + behavior: error in tasks
# learned matrix (optimal learner): error in tasks

#