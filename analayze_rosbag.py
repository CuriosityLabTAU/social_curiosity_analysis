import rosbag
import pickle
from os import listdir
from os.path import isfile, join
import numpy as np
import json

# get a list of all the relevant bag files
mypath = '/home/matan/Desktop/social_curiosity_data/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and '.bag' in f]

#for each subject
#   for each section
#       dict[id] = dict[section] = dict[turn] = dict{}

#initialize data an count:
count =0
data = {}

position_inv = {'left': 0, 'center': 1, 'right': 2}

# for each bag file
for f in files:
    info = f.split('_')
    subject_id = float(info[4])

    if subject_id > 0.0:
        print('processing ', subject_id,"count= ",count)
        count+=1
        data[subject_id] = {}
        data[subject_id][0] = {}



        # open the bag file
        bag = rosbag.Bag(mypath + f)

        # the sections:
        section_id = 0

        #the turn:
        turn=0

        # the question:
        current_question  = str


        looking_at_dict={0:0, 1:0, 2:0}
        collect_secondary_robots={0:False, 1:False, 2:False}

        tracker_dict={0:0, 1:0, 2:0}
        collect_tracker={0:False, 1:False, 2:False}



        try:

            for topic, msg, t in bag.read_messages():
                # get section_id
                if 'log' in topic:
                    if 'start:' in msg.data:
                        if len(msg.data)==7:
                            section_id=int(msg.data[-1])

                            data[subject_id][section_id] = {}




                #get turn info
                if 'log' in topic:
                    if 'start:' in msg.data:
                        if 'turn:' in msg.data:
                            turn_data= msg.data.split(':')
                            turn = int(turn_data[1])
                            main=turn_data[-1]
                            if main=='h':
                                number_of_secondary=3
                            else:
                                main=int(main)
                                number_of_secondary=2

                            data[subject_id][section_id][turn] = {'secondary_robots_data':{}, 'main':main, 'number_of_secondary':number_of_secondary}

                            # collect eye tracker data on the turn
                            collect_tracker = {0: True, 1: True, 2: True}


                #get question data:
                if 'log' in topic:
                    if 'question:start:' in msg.data:
                        current_question='q'+msg.data[-1]


                if 'log' in topic:
                    if "question:answer" in msg.data:
                        question_data=msg.data.split(':')

                        subject_answer=question_data[2]
                        right_answer  =question_data[4]

                        data[subject_id][section_id][current_question] = {'right_answer':right_answer,'subject_answer':subject_answer,'was_correct':right_answer==subject_answer}


                ##get looking at behaviour data:
                if 'log' in topic:
                    if 'secondary' in msg.data:
                        secondary_data= msg.data.split(":")
                        secondary_robot=int(secondary_data[1][0])
                        data[subject_id][section_id][turn]['secondary_robots_data'][secondary_robot]={'behavior': ":".join(secondary_data[2:-2]),'relationship':secondary_data[-1]}
                        collect_secondary_robots[secondary_robot]=True

                #tracker info:
                if 'log' in topic:
                    if 'all:back_to_sit' in msg.data:
                        for i in xrange(3):
                            if collect_secondary_robots[i]:
                                data[subject_id][section_id][turn]['secondary_robots_data'][i]['look_data']=looking_at_dict[i]

                        data[subject_id][section_id][turn]['tracker_aggregation'] = tracker_dict

                        sum_tracking=tracker_dict[0]+tracker_dict[1]+tracker_dict[2]
                        if sum_tracking < 10:
                            print ('Problem with eye tracker-subject:'+str(subject_id)+'-section:'+str(section_id)+'turn:'+str(turn)+'-sum is:'+str(sum_tracking))


                        #restart counters
                        collect_secondary_robots = {0: False, 1: False, 2: False}
                        looking_at_dict = {0: 0, 1: 0, 2: 0}

                        tracker_dict = {0: 0, 1: 0, 2: 0}
                        collect_tracker = {0: False, 1: False, 2: False}


                if 'eye_tracking' in topic:
                    direction=msg.data
                    position=position_inv[direction]
                    if collect_secondary_robots[position]:
                        looking_at_dict[position]+=1

                    if collect_tracker[position]:
                        tracker_dict[position]+=1

                #give number of robot that are secondery

        except:
            print('error - subject_id: ',subject_id)
            data.pop(subject_id)


print data

# print(data.keys())

# pickle.dump(obj=data, file=open('data/raw_data_28_6', 'wb'))#
