import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
sns.set_style("darkgrid", {"axes.facecolor": "#DDE5EE"})
# sns.set()
import statsmodels.formula.api as sm
from scipy import stats
from matplotlib.ticker import MaxNLocator

# #Matan lab
external_filename = 'data/all_external_data.csv'
internal_filename = 'data/external_and_internal_data/all_internal_data.csv'

#Goren
# data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/'
# external_filename = data_path+'all_data/all_external_data.csv'
# internal_filename = data_path+'all_data/all_internal_data.csv'


all_internal = pd.read_csv(open(internal_filename))
all_internal.set_index('Subject_ID', inplace=True)
all_internal.dropna(inplace=True)

title_font = {'fontname':'Arial', 'size':'18', 'color':'black', 'weight':'bold',
              'verticalalignment':'bottom'}

def AMT_histogram():
    AMT_data = pd.read_csv('data/AMT_row.csv')
    # preprocessing:
    columns = ['Duration (in seconds)', 'Finished', 'RecordedDate', 'Q1.2', 'Q1.3', 'Q1.4', 'Q1.5', 'Q0_11', 'Q1_11',
               'Q2_11', 'Q3_11', 'Q4_11', 'Q5_11',
               'Q6_11', 'Q7_11', 'Q8_11', 'Q9_11', 'Q10_11', 'Q11_11', 'Q12_11', 'Q13_11', 'Q14_11', 'validation_11']

    columns_names = ['duration', 'finished', 'date', 'agree_to_participate', 'gender', 'age', 'degree', '0', '1', '2',
                     '3', '4', '5',
                     '6', '7', '8', '9', '10', '11', '12', '13', '14', 'validation']

    # remove_ferst_two_lines:#
    AMT_data = AMT_data.drop([0, 1])

    # columns_names
    AMT_data = AMT_data[columns]
    AMT_data.columns = columns_names

    # to numeric:
    final_list = list(
        set(columns_names).difference(set(['finished', 'date', 'agree_to_participate', 'gender', 'degree'])))
    for col in final_list:
        AMT_data[col] = AMT_data[col].astype(float)

    # Finished
    AMT_data = AMT_data[AMT_data.finished == 'True']

    # agree_to_participate
    AMT_data = AMT_data[AMT_data.agree_to_participate == 'Agree']

    # validation
    AMT_data = AMT_data[AMT_data.validation == 0]
    AMT_data = AMT_data[AMT_data.duration > 180]  # more then 3 min

    ######################################################################################
    # AMT data for analysis:
    AMT_data = AMT_data[[str(i) for i in range(15)]]
    AMT_data = AMT_data.reset_index(drop=True)

    # pandas.Index.astype
    AMT_data.columns = AMT_data.columns.astype(int)

    for col in list(AMT_data):
        AMT_data[col] = AMT_data[col].astype(int)
    # sacle:
    AMT_data = AMT_data.div(100)


    f, axes = plt.subplots(5, 3,constrained_layout=True)
    plt.subplots_adjust(top=.9, bottom=0.1)

    for i in range(0,15):

        a = sns.distplot(AMT_data[i],bins=9,kde=False,ax=axes[int(i/3),i%3] ,color='teal')

        if int(i%3)== 0:
            a.set_ylabel('Frequency' , fontsize = 23 )
        else:
            a.set(yticklabels=[])
            a.set_xlabel("", fontsize=0.1)


        if i/3==4:
            a.set_xlabel('Relationship Representation' ,fontsize=23 )

        else:
            a.set(xticklabels=[])
            a.set_xlabel("", fontsize=0.1)

        a.tick_params(axis='y', labelsize=15)
        a.tick_params(axis='x', labelsize=15)

        a.set(ylim=(0, 35),xlim=(0, 1))
        a.text(.97, .85, str(i), horizontalalignment='right', transform=a.transAxes, weight='bold' ,fontsize=22)


    plt.show()
# AMT_histogram()

def b_over_time():
    a_color='#FFB38A'
    b_color='#1278A1'

    f, ax = plt.subplots(1, 1,figsize=(16,6))

    b_local_list=['b_local_0','b_local_1','b_local_2','b_local_3','b_local_4']
    b_global_list=['b_global_0','b_global_1','b_global_2','b_global_3','b_global_4']
    b_sequence_list=['b_sequence_0','b_sequence_1','b_sequence_2','b_sequence_3','b_sequence_4']


    b_local_data= all_internal[b_local_list]
    b_local_data.columns = [i for i in xrange(1,6)]
    b_local_data = pd.melt(b_local_data, var_name="Time", value_name="Score")

    a = sns.regplot(x="Time", y="Score", data=b_local_data, color=b_color ,  x_estimator=np.mean ,label=r"$b_{\rm local}$",line_kws={'linestyle':"-"})

    b_global_data= all_internal[b_global_list]
    b_global_data.columns = [i for i in xrange(1,6)]
    b_global_data = pd.melt(b_global_data, var_name="Time", value_name="Score")

    b = sns.regplot(x="Time", y="Score", data=b_global_data, color=a_color , x_estimator=np.mean,label=r"$b_{\rm global}$")
    # b.set(xlabel='Session Number', ylabel='Error' ,fontsize=23)

    b_sequence_data= all_internal[b_sequence_list]
    b_sequence_data.columns = [i for i in xrange(0,5)]
    b_sequence_data = pd.melt(b_sequence_data, var_name="Time", value_name="Score")

    # b = sns.regplot(x="Time", y="Score", data=b_sequence_data,  x_estimator=np.mean,label=r"$\beta_{\rm sequence}$")
    # ax.legend()

    a.set_xlabel('Session Number', fontsize=23)
    a.set_ylabel('Error', fontsize=23)


    # ax.axes.set_title(r'(a)', **title_font )
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.setp(ax.get_legend().get_texts(), fontsize='24') # for legend text
    a.text(.05, .93, '(a)', horizontalalignment='right', transform=a.transAxes, weight='bold', fontsize=22)

    # ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=3 , handlelength=3)
    plt.show()

    # print 'b_local vs time '
    # result = sm.ols(formula='Time ~ Score ', data=b_local_data).fit()
    # print result.summary()
    #
    # print 'b_global vs time '
    # result = sm.ols(formula='Time ~ Score ', data=b_global_data).fit()
    # print result.summary()
    #
    #
    # print 'b_sequence vs time '
    # result = sm.ols(formula='Time ~ Score ', data=b_sequence_data).fit()
    # print result.summary()
# b_over_time()

def delta_over_time():
    a_color='teal'
    b_color='#E47A2E'
    c_color='#79C753'




    f, ax = plt.subplots(1, 1,figsize=(16,6))

    delta_list=['delta_0','delta_1','delta_2','delta_3','delta_4']
    delta_tilde_list = ['delta_tilde_0', 'delta_tilde_1','delta_tilde_2' ,'delta_tilde_3', 'delta_tilde_4']
    delta_tag_list = ['delta_tag_0', 'delta_tag_1','delta_tag_2' ,'delta_tag_3', 'delta_tag_4']

    delta_tag_data= all_internal[delta_tag_list]
    delta_tag_data.columns = [i for i in xrange(1,6)]
    delta_tag_data = pd.melt(delta_tag_data, var_name="Time", value_name="Score")

    c = sns.regplot(x="Time", y="Score", data=delta_tag_data,color=b_color , x_estimator=np.mean, label=r"$\hat{l}$", line_kws={'linestyle':"-."})


    delta_data= all_internal[delta_list]
    delta_data.columns = [i for i in xrange(1,6)]
    delta_data = pd.melt(delta_data, var_name="Time", value_name="Score")

    a = sns.regplot(x="Time", y="Score", data=delta_data,color=a_color , x_estimator=np.mean, label=r"$l$", line_kws={'linestyle':"--"})

    delta_tilde_data= all_internal[delta_tilde_list]
    delta_tilde_data.columns = [i for i in xrange(1,6)]
    delta_tilde_data = pd.melt(delta_tilde_data, var_name="Time", value_name="Score")


    b = sns.regplot(x="Time", y="Score", data=delta_tilde_data, color=c_color , x_estimator=np.mean,label=r"$\tilde{l}$",line_kws={'linestyle':'-'})
    # b.set(xlabel='Session Number', ylabel='Performance')

    # ax.axes.set_title(r'(b)', **title_font )

    random = (1.0 / 3 + 1.0 / 2) * 2
    # random = (1.5 / 3 + 1.5 / 2 ) * 2


    ax.axhline(linewidth=1.3, color='r', y=random, linestyle=":")
    a.text(1.5, random +0.02, 'Random', horizontalalignment='right', color='r',
           # transform=a.transAxes,
           weight='bold', fontsize=19)

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))


    ax.set_xlabel('Session Number', fontsize=23)
    ax.set_ylabel('Performance', fontsize=23)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.setp(ax.get_legend().get_texts(), fontsize='24') # for legend text
    # plt.setp(ax.get_legend().get_title(), fontsize='32') # for legend title
    a.text(.05, .93, '(b)', horizontalalignment='right', transform=a.transAxes, weight='bold', fontsize=22)

    plt.show()


    print 'delta vs time '
    result = sm.ols(formula='Time ~ Score ', data=delta_data).fit()
    print result.summary()

    print 'tilde_tilde vs time '
    result = sm.ols(formula='Time ~ Score ', data=delta_tilde_data).fit()
    print result.summary()

    delta_list=['delta_0','delta_1','delta_2','delta_3','delta_4']
    delta_tilde_list = ['delta_tilde_0', 'delta_tilde_1','delta_tilde_2' ,'delta_tilde_3', 'delta_tilde_4']

    tt_dict={}
    for i in range(5):
        B=all_internal[delta_list[i]].values.tolist()
        C=all_internal[delta_tilde_list[i]].values.tolist()

        ttb=stats.ttest_ind(B, [random]*len(B))
        ttc=stats.ttest_ind(C, [random]*len(C))

        tt_dict[i]={'delta -t':ttb[0],'delta -p':ttb[1]/2,'delta~ -t':ttc[0],'delta~ -p':ttc[1]/2}

    tt_df = pd.DataFrame.from_dict(tt_dict, orient='index')
    print tt_df
# delta_over_time()

def delta_tilde_vs_b():
    # b_error_list=['b_error_0','b_error_1','b_error_2','b_error_3','b_error_4']
    b_local_list = ['b_local_0', 'b_local_1', 'b_local_2', 'b_local_3', 'b_local_4']
    delta_tilde_list = ['delta_tilde_0', 'delta_tilde_1', 'delta_tilde_2', 'delta_tilde_3', 'delta_tilde_4']

    f, axes = plt.subplots(3, 2)

    for i in range(5):
        data= all_internal[[b_local_list[i],delta_tilde_list[i]]]

        a = sns.regplot(x=b_local_list[i], y=delta_tilde_list[i], data=data, x_estimator=np.mean ,ax=axes[int(i / 2), i % 2],)
        title=r"$\delta$~_"+str(i)+" vs "+r"$\beta_{\rm error}$_"+str(i)
        a.set(xlabel='Relationship Representation ', ylabel='Frequency',)
        a.axes.set_title(title)

        print title
        result = sm.ols(formula=b_local_list[i]+'~'+delta_tilde_list[i], data=data).fit()
        print result.summary()

    plt.show()

# delta_tilde_vs_b()

def delta_tag_vs_error():
    data = {
        'x': [],
        'y': []
    }
    for i in range(3, 4):
        data['x'].extend([j[0] for j in all_internal[['b_global_%d' % i]].values.tolist()])
        data['y'].extend([j[0] for j in all_internal[['delta_tilde_%d' % i]].values.tolist()])
    df = pd.DataFrame.from_dict(data=data)
    print(df.head())
    a = sns.regplot(x='x', y='y', x_estimator=np.mean, data=df)

    result = sm.ols(formula='y ~ x', data=df).fit()
    print result.summary()
    plt.show()

# delta_tag_vs_error()
