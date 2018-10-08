import pandas as pd
from factor_analyzer import FactorAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import seaborn as sns
sns.set()


# load data
# MATAN:
data_path = 'data/external_and_internal_data'
external_filename = '/all_external_data.csv'
internal_filename = '/all_internal_data.csv'

# GOREN:
# data_path = 'C:/Goren/CuriosityLab/Data/social_curiosity/'
# external_filename = 'all_data/all_external_data.csv'
# internal_filename = 'all_data/all_internal_data.csv'
# filename = 'raw_data_18-09-2018_03_33/raw_data_18-09-2018_03_33'

all_external = pd.read_csv(open(data_path + external_filename))
all_external = all_external[all_external.Subject_ID.notnull()]
all_external.set_index('Subject_ID', inplace=True)

all_internal = pd.read_csv(open(data_path + internal_filename)).dropna()
all_internal.set_index('Subject_ID', inplace=True)
internal_columns = [a for a in all_internal.columns if 'ground' not in a and 'sequence' not in a and '_2' not in a and '_3' not in a and 'error' not in a] # and '_4' not in a]


all_data = pd.concat([all_external, all_internal], axis=1)
all_data = all_data[all_data.b_local_0.notnull()]
print(all_data.shape)

interesting_measures = [
    'S_Curiosity', 'T_Curiosity',
    'SCS_total_score', 'General_Social_Curiosity', '_5DC_Social_Curiosity',
    'Covert_Social_Curiosity',
    '_5DC_Joyous_Exploration', '_5DC_Deprivation_Sensitivity',
    '_5DC_Stress_Tolerance', '_5DC_Thrill_Seeking',
    'CEI_2_total_score', 'AQ_total_score',
    'pet', 'avg_grades',
    'Openness', 'Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness'
]

# Factor analysis
# step 0.
# do the factor analysis
def the_fa(all_measures_, n_factors=-1):
    fa_ = FactorAnalyzer()
    if n_factors < 0:
        fa_.analyze(all_measures_, len(all_measures_.columns), rotation='promax')
    else:
        fa_.analyze(all_measures_, n_factors, rotation='promax')
    return fa_


# step 1. SCREE PLOT
# select number of factors
def scree_plot(fa_):
    ev, v = fa_.get_eigenvalues()
    plt.xlabel('Factor Number')
    plt.ylabel('Eigenvalue')
    plt.plot(ev)
    plt.show()


# step 2. Print factors
def print_factors(fa_, n_factors):
    for i in range(n_factors):
        factor_name = 'Factor%d' % (i + 1)
        print('----- %s ------' % factor_name)
        print(fa.loadings[factor_name][abs(fa.loadings[factor_name]) > 0.4])


# step 3. Get factor scores
def factor_scores(all_measures_, fa_, n_factors=4):
    x = np.zeros([all_measures_.shape[0], n_factors])
    for i in range(n_factors):
        factor_name = 'Factor%d' % (i+1)
        # print(np.expand_dims(fa_.loadings[factor_name], 1).shape)
        # print(all_measures_.values.shape)
        relevant_factors = abs(fa_.loadings[factor_name]) > 0.4
        weighted_measures = fa_.loadings[factor_name][relevant_factors] / np.sum(abs(fa_.loadings[factor_name][relevant_factors]))
        relevant_measures = all_measures_.values[:, relevant_factors.values]
        x[:, i - 1] = np.squeeze(np.dot(relevant_measures, np.expand_dims(weighted_measures, 1)))
        # x[:, i-1] = np.squeeze(np.dot(all_measures_.values,  np.expand_dims(fa.loadings[factor_name], 1)))


    # convert x into data_frame, columns = factor_1, factor_2
    factor_names = ['Factor%d' % (s+1) for s in range(n_factors)]
    factor_df_ = pd.DataFrame(x, columns=factor_names,index=all_measures_.index)
    return factor_df_


def calc_correlation(all_measures_, factor_names):
    ylabel_map = {
        'psychometric_grade': 'PET',
        'AQ_total_score': 'AQ score',
        'CEI_II_Total': 'CEI II score'
    }

    for i_m in interesting_measures:
        print(' ***************************************************** ')
        print(' ***************************************************** ')
        print(' ***************************************************** ')
        the_formula = i_m + ' ~ '
        for fn in factor_names:
            the_formula += fn + ' +'
        the_formula = the_formula[:-2]
        print(the_formula)
        result = sm.ols(formula=the_formula, data=all_measures_).fit()
        print result.summary()

        most_significant_factor = np.argmin(result.pvalues[1:].values)

        result = sm.ols(formula='%s ~ %s' % (i_m, factor_names[most_significant_factor]), data=all_measures_).fit()
        print result.summary()

        two_factor = {}
        for fn in factor_names:
            if fn != factor_names[most_significant_factor]:
                the_formula = i_m + ' ~ %s + %s' % (factor_names[most_significant_factor], fn)
                print(the_formula)
                result = sm.ols(formula=the_formula, data=all_measures_).fit()
                # print result.summary()
                two_factor[result.f_pvalue] = (factor_names[most_significant_factor], fn)

        best_p_value = np.min(two_factor.keys())
        best_two_factors = two_factor[best_p_value]

        the_formula = i_m + ' ~ %s + %s' % (best_two_factors[0], best_two_factors[1])
        print(the_formula)
        result = sm.ols(formula=the_formula, data=all_measures_).fit()
        print result.summary()

        the_formula = i_m + ' ~ %s * %s' % (best_two_factors[0], best_two_factors[1])
        print(the_formula)
        result = sm.ols(formula=the_formula, data=all_measures_).fit()
        print result.summary()

        if 'Factor' in best_two_factors[0]:
            best_measure = np.argmax(abs(fa.loadings[best_two_factors[0]]))
            the_formula = i_m + ' ~ %s + %s' % (best_measure, best_two_factors[1])
            print(the_formula)
            result = sm.ols(formula=the_formula, data=all_measures_).fit()
            print result.summary()

        if 'Factor' in best_two_factors[1]:
            best_measure = np.argmax(abs(fa.loadings[best_two_factors[1]]))
            the_formula = i_m + ' ~ %s + %s' % (best_measure, best_two_factors[0])
            print(the_formula)
            result = sm.ols(formula=the_formula, data=all_measures_).fit()
            print result.summary()





                #
    #     best_factor = np.argmin(result.pvalues.values[1:])
    #     the_formula = i_m + ' ~ ' + factor_names[best_factor]
    #     result = sm.ols(formula=the_formula, data=factors_and_external_df).fit()
    #     print result.summary()
    #     print_result(result)
    #
    #     df_plot = factors_and_external_df[[factor_names[best_factor], i_m]].dropna()
    #     # plt.scatter(df_plot[[factor_names[best_factor]]], df_plot[i_m], marker='x')
    #     font = {'family': 'normal',
    #             'weight': 'bold',
    #             'size': 76}
    #     matplotlib.rc('font', **font)
    #     sns.regplot(x=df_plot[factor_names[best_factor]], y=df_plot[i_m])
    #     plt.tick_params(axis='both', which='major', labelsize=48)
    #     plt.xlabel('Factor %d' % (best_factor+1), fontsize=48)
    #     try:
    #         plt.ylabel(ylabel_map[i_m], fontsize=48)
    #     except:
    #         pass
    #     plt.show()

n_factors = 5
all_measures = all_data[internal_columns]
fa = the_fa(all_measures, n_factors)
# scree_plot(fa)

fa = the_fa(all_measures, n_factors)
print_factors(fa, n_factors)
factor_df = factor_scores(all_measures, fa, n_factors)
factor_names = list(factor_df.columns)
# factor_names.append('age')
# factor_names.append('gender')
# factor_names.append('NARS_total_score')
# factor_names.append('Anthropomorphism')
# factor_names.append('Animacy')


all_data = pd.concat([all_data, factor_df], axis=1)
print(all_data.shape)

calc_correlation(all_data, factor_names)

# the_formula = 'SCS_total_score ~ Factor1 * Factor5 + gender'
# print(the_formula)
# result = sm.ols(formula=the_formula, data=all_data).fit()
# print result.summary()
