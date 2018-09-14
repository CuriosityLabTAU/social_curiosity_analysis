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

# for each bag file
for f in files:
    info = f.split('_')
    subject_id = float(info[4])

    if subject_id > 0.0:
        print('processing ', subject_id)
        count+=1
        print "count= ",count
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



        try:

            for topic, msg, t in bag.read_messages():
                # get section_id
                if 'log' in topic:
                    if 'start:' in msg.data:
                        if len(msg.data)==7:
                            section_id=int(msg.data[-1])

                            data[subject_id][section_id] = {}

                #get turn
                if 'log' in topic:
                    if 'start:' in msg.data:
                        if 'turn:' in msg.data:
                            turn = int(msg.data[5])
                            data[subject_id][section_id][turn] = {'secondary_robots_data':{}}


                # #get tracker aggregation:
                # if 'log' in topic:
                #     if 'robot_counts:' in msg.data:
                #         tracker_aggregation= json.loads(msg.data.split(':')[1][:])
                #         data[subject_id][section_id][turn]['tracker_aggregation'] =tracker_aggregation
                #
                #         if sum(tracker_aggregation) < 10:
                #             print ('Problem with eye tracker-subject:'+str(subject_id)+'-section:'+str(section_id)+'turn:'+str(turn)+'-sum is:'+str(sum(tracker_aggregation)))


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


                #get looking at behaviour data:
                if 'log' in topic:
                    if 'secondary' in msg.data:
                        secondary_data= msg.data.split(":")
                        secondary_robot=int(secondary_data[1][0])
                        data[subject_id][section_id][turn]['secondary_robots_data'][secondary_robot]={'behavior': ":".join(secondary_data[2:-2]),'relationship':secondary_data[-1]}
                        collect_secondary_robots[secondary_robot]=True

                if 'log' in topic:
                    if 'all:back_to_sit' in msg.data:
                        #stop colecting
                        #update dict with the number of lookes

                #colect lookes


                #colect the total lookes

                #give number of robot that are secondery















        except:
            print('error - subject_id: ',subject_id)
            data.pop(subject_id)


print data

# sections = ['learn', 'task1', 'task2', 'task3']
# #
# subjects_with_no_angles_topic=[]


#
#
#         #is_nao_angles_topic
#         is_nao_angles_topic=False
#
#         is_working= False
#
#         current_skeleton_angle = None
#         current_nao_movements = None
#         current_nao_command = None
#
#         first_time = True
#
#         # try:
#
#         for topic, msg, t in bag.read_messages():
#             # get the first time, for reference
#             if first_time:
#                 t0 = t
#                 first_time = False
#
#             if 'log' in topic:
#                 if'current_state' in msg.data:
#                     step=int(msg.data.split(': ')[1])
#                     if step in data[subject_id]:
#                         continue
#
#                     data[subject_id][step]={}
#                     if step == 1:
#                         section_id = 1
#                         print 'here'
#                     else:
#                         section_id = 0
#
#                 if 'matrix' in msg.data:
#                     if step in data[subject_id]:
#                         matrix=msg.data.split(':')[1]
#                         data[subject_id][step]['matrix'] = np.array(np.matrix([[float(x)for x in row if x!=''] for row in [line[2:-1].split(' ') for line in  matrix[2:-1].split('\n ')]]))
#
#
#                 if'task' in msg.data:
#                     task_full_name=msg.data.split(',')[2]
#                     task=task_full_name.split('/')[-1]
#
#
#             if 'flow' in topic:
#                 #   get the transformation
#
#                 if msg.data.isdigit():
#                     if step in data[subject_id]:
#                         data[subject_id][step]['transformation'] = int(msg.data)
#
#                   # parse the time to sections (learning, task1, task2, task3)
#                 if 'start' in msg.data:
#                     if step in data[subject_id]:
#                         is_working=True
#                         data[subject_id][step][sections[section_id]] = {
#                             'start': t,
#                             'stop': None,
#                             'data': [],
#                             'task':task
#                         }
#
#                 if 'stop' in msg.data:
#                     if step in data[subject_id]:
#                         if sections[section_id] in data[subject_id][step]:
#                             is_working=False
#                             data[subject_id][step][sections[section_id]]['stop'] = t
#                             task = 0
#                             section_id += 1
#
#                             if step == 12:
#                                 bag.close()
#                                 break
#
#                 if section_id >= len(sections):
#                     section_id=0
#
#
#             if 'affdex' in topic:
#                 # print msg
#                 dict = {}
#                 for m in affdex_list:
#                     dict[m] = eval('msg.' + m)
#                     if m == 'face_points':
#                         n_list = []
#                         o_list = dict[m]
#                         for point in o_list:
#                             n_list.append({"x": point.x, "y": point.y})
#                         dict[m] = n_list
#                 affdex = dict
#
#
#               # for each section
#             # if 'nao_movements' in topic:
#             #    #          get command to robot
#             #     current_nao_movements = msg.data
#
#
#             # time between skeleton_angles is +- 0.04
#             # time between robot angles is +- 0.09
#
#
#             if 'nao_angles_topic' in topic:
#                 #       get command to robot
#
#                 is_nao_angles_topic = True
#
#                 list_of_movements_str = msg.data
#                 list_of_movements = list_of_movements_str[1:-1].split(', ')
#
#                 current_nao_movements = (list_of_movements[2:4]+[0.0,0.0]+list_of_movements[-6:-4]+[0.0,0.0])
#
#                 current_nao_movements= str([float(x) for x in current_nao_movements])
#                 current_nao_movements= current_nao_movements[1:-1]
#
#             if 'to_nao' in topic:
#                 #       get command to robot
#                 if'change_pose' in msg.data:
#                     current_nao_command = msg.data
#
#             if 'skeleton_angle' in topic:
#                 #       get raw skeleton markers
#                 current_skeleton_angle = msg.data
#                 # print current_skeleton_angle
#
#                     #dict[id] = dict[section] = array(dict{skeleton, robot, time})
#                 if is_working==True:
#                     if step in data[subject_id]:
#                         if sections[section_id] in data[subject_id][step]:
#                             if current_skeleton_angle is not None and current_nao_movements is not None and current_nao_command is not None:
#                                 new_data = {
#                                     'time': (t - t0).to_sec(),
#                                     'skeleton': current_skeleton_angle,
#                                     'robot_cimmand':current_nao_command,
#                                     'robot': current_nao_movements,
#                                     'affdex':affdex
#                                 }
#                                 data[subject_id][step][sections[section_id]]['data'].append(new_data)
#
#         if is_nao_angles_topic==False:
#             subjects_with_no_angles_topic.append(subject_id)
#
#         # except:
#         #     print('error')
#         #     data.pop(subject_id)
#
#
# print(data.keys())
# print 'subjects_with_no_angles_topic: ',subjects_with_no_angles_topic
#
# pickle.dump(obj=data, file=open('data/raw_data_28_6', 'wb'))
#
#
