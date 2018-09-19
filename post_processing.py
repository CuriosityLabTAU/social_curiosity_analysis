import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load data
data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/'
filename = 'raw_data_18-09-2018_03_33/raw_data_18-09-2018_03_33'
x = pickle.load(open(data_path+filename, 'rb'))

# load behavior_relationship probability
beh_rel_prob = pd.read_csv(data_path + 'probs_from_AMT.csv').values
num_discrete = beh_rel_prob.shape[1]
num_behaviors = beh_rel_prob.shape[0]


def task_performance(tasks_):
    correct = 0
    for t in tasks_:
        correct += int(t['was_correct'])
    return correct


def update_bayes(prob_i_j_, i_robot_, j_robot_, behavior_):
    norm = np.sum(prob_i_j_[i_robot_, j_robot_, :])

    prob_i_j_[i_robot_, j_robot_, :] = np.multiply(prob_i_j_[i_robot_, j_robot_, :], beh_rel_prob[behavior_, :])
    norm = np.sum(prob_i_j_[i_robot_, j_robot_, :])
    prob_i_j_[i_robot_, j_robot_, :] /= norm

    norm = np.sum(prob_i_j_[i_robot_, j_robot_, :])
    return prob_i_j_


def task_from_prob(prob_i_j_):
    # create matrix
    attitude_matrix = np.zeros(prob_i_j_.shape[:2])

    for i in range(attitude_matrix.shape[0]):
        for j in range(attitude_matrix.shape[1]):
            attitude_matrix[i, j] = np.sum(np.multiply(np.arange(1, num_discrete + 1) / (num_discrete+1.0), prob_i_j_[i,j,:]))

    answers = np.zeros([4])
    answers[0] = np.argmax(np.sum(attitude_matrix[:,:-1], axis=0))
    answers[1] = np.argmin(np.sum(attitude_matrix[:, :-1], axis=0))
    answers[2] = np.argmax(attitude_matrix[:, -1])
    answers[3] = np.argmin(attitude_matrix[:, -1])

    return answers



# subject_id --> {section_id[1-5]} --> turn [4, 8, 8, 8 , 8] -->

for subject_id, a in x.items():
    for section_id, b in a.items():
        # for each section, a new matrix

        # initialize the probabilities
        prob_i_j = np.ones([3, 4, num_discrete]) / float(num_discrete)

        for turn, c in b.items():
            # for each turn, a different agent does something

            # at the end of each turn, 4 questions
            tasks = []
            if 'q' in str(turn):
                tasks.append(c)
            else: # analyze behavior and resulting matrix / learning
                j_robot = c['main'] # robot acting on
                if j_robot == 'h':
                    j_robot = 3

                # go over all the tracking data, which robot was looked at
                for i_track, track_data in enumerate(c['tracking_data']['informative']):
                    if track_data: # only if it was informative
                        i_robot = c['tracking_data']['direction'][i_track]
                        if i_robot != j_robot:
                            # update bayes
                            behavior = c['secondary_robots_data'][i_robot]['behavior']
                            prob_i_j = update_bayes(prob_i_j, i_robot, j_robot, behavior)
                            task_from_prob(prob_i_j)

        # MEASURES:
        b['task_performance'] = task_performance(tasks)
        b['measures'] = {}



        for turn, c in b.items():
            print(c)
            break
        break
    break


# research questions:

# - did they improve in learning (tasks/questions)?
# (optimal learner & behavior: use the real matrix for error calculation)
# figure: error vs section
def figure_1():
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