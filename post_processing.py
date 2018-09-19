import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy

# load data
data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/'
filename = 'raw_data_18-09-2018_03_33/raw_data_18-09-2018_03_33'
x = pickle.load(open(data_path+filename, 'rb'))

# load behavior_relationship probability
beh_rel_prob = pd.read_csv(data_path + 'probs_from_AMT.csv').values
num_discrete = beh_rel_prob.shape[1]
num_behaviors = beh_rel_prob.shape[0]

# real_matrix
real_matrix = [np.ones([3, 4]) for _ in range(5)]


def task_performance(tasks_, which_matrix):
    correct = 0
    for t in tasks_:
        correct += int(t['subject_answer'] == t[which_matrix])
    return correct


def update_bayes(prob_i_j_, i_robot_, j_robot_, behavior_):
    prob_i_j_[i_robot_, j_robot_, :] = np.multiply(prob_i_j_[i_robot_, j_robot_, :], beh_rel_prob[behavior_, :])
    norm = np.sum(prob_i_j_[i_robot_, j_robot_, :])
    prob_i_j_[i_robot_, j_robot_, :] /= norm
    return prob_i_j_


def matrix_from_prob(prob_i_j_):
    attitude_matrix_ = np.zeros(prob_i_j_.shape[:2])

    for i in range(attitude_matrix_.shape[0]):
        for j in range(attitude_matrix_.shape[1]):
            attitude_matrix_[i, j] = np.sum(np.multiply(np.arange(1, num_discrete + 1) / (num_discrete+1.0), prob_i_j_[i,j,:]))
    return attitude_matrix_


def task_from_matrix(attitude_matrix_):
    answers = np.zeros([4])
    answers[0] = np.argmax(np.sum(attitude_matrix_[:,:-1], axis=0))
    answers[1] = np.argmin(np.sum(attitude_matrix_[:, :-1], axis=0))
    answers[2] = np.argmax(attitude_matrix_[:, -1])
    answers[3] = np.argmin(attitude_matrix_[:, -1])
    return answers



# subject_id --> {section_id[1-5]} --> turn [4, 8, 8, 8 , 8] -->

for subject_id, a in x.items():
    for section_id, b in a.items():
        # for each section, a new matrix

        # initialize the probabilities
        prob_i_j = np.ones([3, 4, num_discrete]) / float(num_discrete)
        attitude_matrix = np.zeros(prob_i_j.shape[:2])
        optimal_prob_i_j = np.ones([3, 4, num_discrete]) / float(num_discrete)
        sequence_prob_i_j = np.ones([3, 4, num_discrete]) / float(num_discrete)

        tasks = []
        error = []
        local_error = []
        global_error = []
        sequence_error = []
        the_sequence = []
        for turn, c in b.items():
            if 'q' not in str(turn):
                j_robot = c['main']  # robot acting on
                if j_robot == 'h':
                    j_robot = 3

                # go over all the tracking data, which robot was looked at
                for i_track, track_data in enumerate(c['tracking_data']['informative']):
                    if track_data:  # only if it was informative
                        i_robot = c['tracking_data']['direction'][i_track]
                        if i_robot != j_robot:
                            the_sequence.append(i_robot)

        print(subject_id, section_id, len(the_sequence))

        for turn, c in b.items():
            # for each turn, a different agent does something

            # at the end of each turn, 4 questions
            if 'q' in str(turn):
                answers = task_from_matrix(attitude_matrix)
                c['learned_matrix'] = str(int(answers[int(turn[-1])]))
                tasks.append(c)

            else: # analyze behavior and resulting matrix / learning
                j_robot = c['main'] # robot acting on
                if j_robot == 'h':
                    j_robot = 3

                # go over all the tracking data, which robot was looked at
                for i_track, track_data in enumerate(c['tracking_data']['informative']):
                    if track_data: # only if it was informative

                        what_if_local_prob = [copy.deepcopy(prob_i_j) for _ in range(3)]

                        # this is the looked at robot
                        i_robot = c['tracking_data']['direction'][i_track]
                        if i_robot != j_robot:
                            # update bayes
                            behavior = c['secondary_robots_data'][i_robot]['behavior']
                            prob_i_j = update_bayes(prob_i_j, i_robot, j_robot, behavior)
                            attitude_matrix = matrix_from_prob(prob_i_j)

                            error_t = np.mean(np.power(attitude_matrix[:] - real_matrix[:], 2.0))
                            error.append(error_t)

                            # for local optimal behavior
                            # look at all the robots
                            what_if_local_error = np.ones([3])
                            for k_robot in range(3):
                                if k_robot != j_robot:
                                    # update bayes
                                    behavior = c['secondary_robots_data'][k_robot]['behavior']
                                    what_if_local_prob[k_robot] = update_bayes(what_if_local_prob[k_robot], k_robot, j_robot, behavior)
                                    what_if_local_attitude_matrix = matrix_from_prob(what_if_local_prob[k_robot])

                                    what_if_local_error[k_robot] = np.mean(np.power(
                                        what_if_local_attitude_matrix[:] - real_matrix[:], 2.0))
                            what_if_local_min_error = np.min(what_if_local_error)
                            local_error.append(what_if_local_min_error)

                            # for global optimal behavior
                            # look at all the robots
                            what_if_global_error = np.ones([3])

                            what_if_global_prob = [copy.deepcopy(optimal_prob_i_j) for _ in range(3)]

                            for k_robot in range(3):
                                if k_robot != j_robot:
                                    # update bayes
                                    behavior = c['secondary_robots_data'][k_robot]['behavior']
                                    what_if_global_prob[k_robot] = update_bayes(what_if_global_prob[k_robot], k_robot,
                                                                               j_robot, behavior)
                                    what_if_global_attitude_matrix = matrix_from_prob(what_if_global_prob[k_robot])

                                    what_if_global_error[k_robot] = np.mean(np.power(
                                        what_if_global_attitude_matrix[:] - real_matrix[:], 2.0))
                            optimal_behavior = np.argmin(what_if_global_error)
                            what_if_global_min_error = np.min(what_if_global_error)
                            global_error.append(what_if_global_min_error)

                            optimal_prob_i_j = copy.deepcopy(what_if_global_prob[optimal_behavior])

                            # for sequence optimal behavior
                            # look at all the robots
                            what_if_sequence_error = np.ones([len(the_sequence)])
                            what_if_sequence_prob = [copy.deepcopy(sequence_prob_i_j) for _ in range(len(the_sequence))]

                            for k_sequence, k_robot in enumerate(the_sequence):
                                if k_robot != j_robot:
                                    # update bayes
                                    behavior = c['secondary_robots_data'][k_robot]['behavior']
                                    what_if_sequence_prob[k_sequence] = update_bayes(what_if_sequence_prob[k_sequence],
                                                                                     k_robot, j_robot, behavior)
                                    what_if_sequence_attitude_matrix = matrix_from_prob(what_if_sequence_prob[k_sequence])

                                    what_if_sequence_error[k_sequence] = np.mean(np.power(
                                        what_if_sequence_attitude_matrix[:] - real_matrix[:], 2.0))
                            sequence_behavior = np.argmin(what_if_sequence_error)
                            what_if_sequence_min_error = np.min(what_if_sequence_error)
                            sequence_error.append(what_if_sequence_min_error)

                            sequence_prob_i_j = copy.deepcopy(what_if_sequence_prob[sequence_behavior])
                            del the_sequence[sequence_behavior]

        error = np.array(error)
        global_error = np.array(global_error)
        local_error = np.array(local_error)
        sequence_error = np.array(sequence_error)

        # MEASURES:
        b['measures'] = {}
        b['measures']['delta'] = task_performance(tasks, 'right_answer')
        b['measures']['delta_tilde'] = task_performance(tasks, 'learned_matrix')

        b['measures']['b_global'] = np.mean(error - global_error)
        b['measures']['b_local'] = np.mean(error - local_error)
        b['measures']['b_sequence'] = np.mean(error - sequence_error)
        # plt.plot(error, 'b')
        # plt.plot(local_error, 'k')
        # plt.plot(global_error, 'r')
        # plt.plot(sequence_error, 'c')
        # plt.show()


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

# - given behavior (?) in each section (over turns) --> what does the matrix look like? [DONE]

# MEASURES: (for each section)
# optimal learner + behavior: error in tasks [DONE]
# learned matrix (optimal learner): error in tasks [DONE]

# global behavior: error in matrix [DONE]
# local behavior: error in matrix [DONE]
# sequence behavior: error in matrix [DONE]


for subject_id, a in x.items():
    for section_id, b in a.items():
        print(subject_id, section_id, b['measures'])