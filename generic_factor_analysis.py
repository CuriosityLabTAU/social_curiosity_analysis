import pandas as pd
from factor_analyzer import FactorAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm


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


def get_stars_from_p(p):
    if p < 0.001:
        return '{}^{***}'
    if p < 0.01:
        return '{}^{**}'
    if p < 0.05:
        return '{}^{*}'
    return ''