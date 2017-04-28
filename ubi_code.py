
# coding: utf-8

# # Universal Basic Income Reform

# In[1]:

# import packages
from taxcalc import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

from bokeh.plotting import show, output_file, figure
from bokeh.charts import Scatter, Bar
from bokeh.io import output_notebook
output_notebook()


# In[3]:

# define utilities


# In[4]:

in_millions = 1.0e-6
in_billions = 1.0e-9
in_trillions = 1.0e-12


# In[5]:

# define parameters for macro dictionary
labels = []
values = []
macros = []
macro_dict = pd.DataFrame()


# In[6]:

# define agi bins
agi_bins = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']


# In[7]:

# text_file = open(tab_name, "w")
# text_file.write(df2.to_latex())
# text_file.close()


# # ADDED PROGRAMS

# In[8]:

millnames = ['',' thousand',' million',' billion',' trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


# In[9]:

# replace value if it is blank
def units(n):
    millnames = ['',' thousand',' million',' billion',' trillion']
    n = float(n)
    if n < 1000000:
        macro_val_string = '\${:,.0f}'.format(n)
        return(macro_val_string)
    if n >= 1000000:
        millidx = max(0, min(len(millnames)-1,
                            int(math.floor(o if n == 0 else math.log10(abs(n))/3))))                  
        macro_val_string = '\${:,.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
        return(macro_val_string)


# In[10]:

def dist_macro_old(dataframe, section):
          
    brackets = ['0-10%', '90-100%']
    for bracket in brackets:
        total = dataframe['Total (dollars)'][bracket]
        average = dataframe['Average (dollars)'][bracket]
        increase = dataframe['Increase (percent)'][bracket]
        share = dataframe['Share (percent)'][bracket]
        
        if bracket == '0-10%':
            rankcode = 'zz'
        if bracket == '90-100%':
            rankcode = 'aa'

        total_name = section + 't' + rankcode
        average_name = section + 'a' + rankcode
        increase_name = section + 'i' + rankcode
        share_name = section + 's' + rankcode

        def_macro('Total Tax Liability Change (' + bracket + ') ', '${:,.2f}'.format(total * in_billions) + ' billion', total_name)
        def_macro('Average Tax Liability Change (' + bracket + ') ', '${:,.0f}'.format(average), average_name)
        def_macro('Increase in Tax Liability (' + bracket + ') ', increase.strip('%') + ' percent', increase_name)
        def_macro('Share of Tax Liability (' + bracket + ') ', share.strip('%') + ' percent', share_name)


# In[11]:

def dist_macro(dataframe, section):
             
    brackets = ['0-10%', '90-100%', 'Sum']
    for bracket in brackets:
        for column in dataframe:             
                macro_val = dataframe[column][bracket]
                
                # set rankcode according to distributional characteristic
                if bracket == '0-10%':
                    rankcode = 'n'
                if bracket == '90-100%':
                    rankcode = 'x'
                if bracket == 'Sum':
                    rankcode = 'g'
                
                # extract first letter from column for column code
                letter = column[0:1]
                letter = letter.lower()
                
                # define and print macro
                macro_name = section + 'd' + letter + rankcode
                
                # determine unit type (symbol or string)
                unit_key = column[-3:]
                if unit_key[0:1] == '(' and unit_key[2:3] == ')':
                    unit_type = 'symbol'
                if unit_key[0:1] != '(' and unit_key[2:3] == ')':
                    unit_type = 'string'
                    unit_key2 = column[-9:]
                
                # if units are in symbols...
                if unit_type == 'symbol':
                    # if column is in dollars
                    if unit_key == '($)':
                        # convert to human readable units
                        millnames = ['',' thousand',' million',' billion',' trillion']
                        
                        # replace value if it is blank
                        if macro_val == '':
                            macro_val = '0'                        
                        
                        n = float(macro_val)
                        if n < 1000000:
                            macro_val_string = '\${:,.0f}'.format(n)
                            display = macro_name + ' ' + macro_val_string
                            print(display)
                        if n >= 1000000:
                            millidx = max(0, min(len(millnames)-1,
                                                int(math.floor(o if n == 0 else math.log10(abs(n))/3))))                  
                            macro_val_string = '\${:,.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
                            display = macro_name + ' ' + macro_val_string
                            print(display)
                        
                    # if column is in percentages
                    if unit_key == '(%)':
                        macro_val_string = macro_val.strip('%') + ' percent'
                        display = macro_name + ' ' + macro_val_string
                        print(display)
                        
                # test if units are in strings...
                if unit_type == 'string':
                    # if column is in dollars
                    if unit_key2 == '(dollars)':
                        # convert to human readable units
                        millnames = ['',' thousand',' million',' billion',' trillion']

                        # replace value if it is blank
                        if macro_val == '':
                            macro_val = '0'
                        
                        n = float(macro_val)
                        if n < 1000000:
                            macro_val_string = '\${:,.0f}'.format(n)
                            display = macro_name + ' ' + macro_val_string
                            print(display)
                        if n >= 1000000:
                            millidx = max(0, min(len(millnames)-1,
                                                int(math.floor(o if n == 0 else math.log10(abs(n))/3))))                  
                            macro_val_string = '\${:,.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
                            display = macro_name + ' ' + macro_val_string
                            print(display)

                    # if column is in percent
                    if unit_key2 == '(percent)':
                        macro_val_string = macro_val.strip('%') + ' percent'
                        display = macro_name + ' ' + macro_val_string
                        print(display)

                
                # describe macro
                macro_desc = column + ' (' + bracket + ') (part ' + section + ') '

                def_macro(macro_desc, macro_val_string, macro_name)     


# In[12]:

# this program allows defining latex macros for use in document generation

# "it" should be a single number or a string

# any characters other than letters in the "macro_name" will nuke the latex doc

def def_macro(label, value, macro):
    
    # generate macro string
    
    value = str(value)
    string = '\\newcommand{\\'
    string = string + macro
    string = string + '}{'
    string = string + value
    string = string + '}'
    
    labels.append(label)
    values.append(value)
    macros.append(macro)
    
    # write latex string to macro document
    f = open('macros.txt','a') #opens file with name of "test.txt"
    f.write(string + '\n')
    f.close()    
    
    # write definition to macro dictionary
    f = open('macro_dict.txt','a') #opens file with name of "test.txt"
    f.write(macro + ', ' + value + ', ' + label + '\n')
    f.close()    
    
    return(macro)


# In[13]:

# clear macros
def clear_macros():
    labels = []
    values = []
    macros = []
    open('macros.txt', 'w').close()
    


# In[14]:

def restricted_table(df, varlist, lablist, tab_name, reindex = True, na=True):

    """
    Creates a restricted distribution table
    including the variables in varlist
    
    Parameters
    ----------
    df : Pandas dataframe object
                
    varlist : list of variables to include in the table
    
    lablist : list of variable labels for that table 
    
    tab_name : name the table will be saved as
        
    Returns
    -------
    Pandas DataFrame object
    """
    
    # build table
    df2 = df
    
    if na == True:
        df2['mean']['sums'] = ''
        df2['perc_inc']['sums'] = ''
    
    df2 = df2[varlist]
    df2.columns = lablist

    # create file name 
    tab_name = tab_name + ".txt"
    
    if reindex == True:
        df2['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%', 'Sum']
        df2 = df2.set_index(df2['Income Bins'])
        df2 = df2.drop('Income Bins', 1)
        del df2.index.name

    if reindex == False:
        df2['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']
        df2 = df2.set_index(df2['Income Bins'])
        df2 = df2.drop('Income Bins', 1)
        del df2.index.name        
    
    text_file = open(tab_name, "w")
    text_file.write(df2.to_latex())
    text_file.close()
    
    return(df2)


# In[15]:

def makebar(inputdf, plotname = 'xx', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Benefit Loss'):
    
    # transform data frame 
    df = pd.DataFrame()
    df['Benefit Loss'] = inputdf['Benefit Loss']
    df['Income Percentile'] = inputdf['Income Percentile']
    df['Average AGI'] = inputdf['Average AGI'].apply(np.round)

    # replace index in dataframe
    df['index'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    df.set_index('index', inplace=True)
    del df.index.name

    # set data parameters
    x2scale = df['Average AGI']
    bardata = df['Benefit Loss']

    # generate plot
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.set_xlabel(x1label)
    ax2.set_xlabel(x2label)
    ax1.set_ylabel(ylabel)

    ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax2.set_xticks([0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9, 10.9])

    ax1.set_xticklabels(['0', '0 - 10', '10 - 20', '20 - 30', '30 - 40', '40 - 50', 
                         '50 - 60', '60 - 70', '70 - 80', '80 - 90', '90 - 100'])
    ax2.set_xticklabels(x2scale)

    ax1.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], bardata, color='red')
    
    plotname = plotname + '.png'
    plt.savefig(plotname, dpi=1000)
    plt.show()


# In[16]:

def makeline(calc1, 
             calc2, 
             mars='ALL', 
             mtr_measure='combined', 
             mtr_variable='e00200p', 
             alt_e00200p_text='', 
             mtr_wrt_full_compen=False, 
             income_measure='agi', 
             dollar_weighting=False, 
             x1label = 'AGI Percentile', 
             x2label = 'Average AGI by Percentile', 
             ylabel = 'Combined Marginal Tax Rate', 
             plotname = 'plotname'):
    
    # pylint: disable=too-many-arguments,too-many-statements,
    # pylint: disable=too-many-locals,too-many-branches
    # check that two calculator objects have the same current_year
    if calc1.current_year == calc2.current_year:
        year = calc1.current_year
    else:
        msg = 'calc1.current_year={} != calc2.current_year={}'
        raise ValueError(msg.format(calc1.current_year, calc2.current_year))
    # check validity of function arguments
    # . . check income_measure value
    weighting_function = weighted_mean
    if income_measure == 'wages':
        income_var = 'e00200'
        income_str = 'Wage'
        if dollar_weighting:
            weighting_function = wage_weighted
    elif income_measure == 'agi':
        income_var = 'c00100'
        income_str = 'AGI'
        if dollar_weighting:
            weighting_function = agi_weighted
    elif income_measure == 'expanded_income':
        income_var = 'expanded_income'
        income_str = 'Expanded Income'
        if dollar_weighting:
            weighting_function = expanded_income_weighted
    else:
        msg = ('income_measure="{}" is neither '
               '"wages", "agi", nor "expanded_income"')
        raise ValueError(msg.format(income_measure))
    # . . check mars value
    if isinstance(mars, six.string_types):
        if mars != 'ALL':
            msg = 'string value of mars="{}" is not "ALL"'
            raise ValueError(msg.format(mars))
    elif isinstance(mars, int):
        if mars < 1 or mars > 4:
            msg = 'integer mars="{}" is not in [1,4] range'
            raise ValueError(msg.format(mars))
    else:
        msg = 'mars="{}" is neither a string nor an integer'
        raise ValueError(msg.format(mars))
    # . . check mars value if mtr_variable is e00200s
    if mtr_variable == 'e00200s' and mars != 2:
        msg = 'mtr_variable == "e00200s" but mars != 2'
        raise ValueError(msg)
    # . . check mtr_measure value
    if mtr_measure == 'itax':
        mtr_str = 'Income-Tax'
    elif mtr_measure == 'ptax':
        mtr_str = 'Payroll-Tax'
    elif mtr_measure == 'combined':
        mtr_str = 'Income+Payroll-Tax'
    else:
        msg = ('mtr_measure="{}" is neither '
               '"itax" nor "ptax" nor "combined"')
        raise ValueError(msg.format(mtr_measure))
    # calculate marginal tax rates
    (mtr1_ptax, mtr1_itax,
     mtr1_combined) = calc1.mtr(variable_str=mtr_variable,
                                wrt_full_compensation=mtr_wrt_full_compen)
    (mtr2_ptax, mtr2_itax,
     mtr2_combined) = calc2.mtr(variable_str=mtr_variable,
                                wrt_full_compensation=mtr_wrt_full_compen)
    # extract needed output that is assumed unchanged by reform from calc1
    record_columns = ['s006']
    if mars != 'ALL':
        record_columns.append('MARS')
    record_columns.append(income_var)
    output = [getattr(calc1.records, col) for col in record_columns]
    dfx = pd.DataFrame(data=np.column_stack(output), columns=record_columns)
    # set mtr given specified mtr_measure
    if mtr_measure == 'itax':
        dfx['mtr1'] = mtr1_itax
        dfx['mtr2'] = mtr2_itax
    elif mtr_measure == 'ptax':
        dfx['mtr1'] = mtr1_ptax
        dfx['mtr2'] = mtr2_ptax
    elif mtr_measure == 'combined':
        dfx['mtr1'] = mtr1_combined
        dfx['mtr2'] = mtr2_combined
    # select filing-status subgroup, if any
    if mars != 'ALL':
        dfx = dfx[dfx['MARS'] == mars]

    # bin data for graphing
    dfx = add_weighted_income_bins(dfx, num_bins = 100,
                                   income_measure = income_var,
                                   weight_by_income_measure = dollar_weighting)
    # split dfx into groups specified by 'bins' column
    gdfx = dfx.groupby('bins', as_index = False)
    # apply the weighting_function to percentile-grouped mtr values
    mtr1_series = gdfx.apply(weighting_function, 'mtr1')
    mtr2_series = gdfx.apply(weighting_function, 'mtr2')
    agi_series = gdfx.apply(weighting_function, 'c00100')
    decile_series = gdfx.apply(weighting_function, 'bins')

    # construct DataFrame containing the two mtr_series
    lines = pd.DataFrame()
    lines['base'] = mtr1_series
    lines['reform'] = mtr2_series
    lines['agi'] = agi_series.round()
    lines['percentiles'] = decile_series

    # generate labels for secondary x-axis

    # create 'bins' column given specified income_var and dollar_weighting
    dfx = add_weighted_income_bins(dfx, num_bins = 10,
                                   income_measure = income_var,
                                   weight_by_income_measure = dollar_weighting)
    # split dfx into groups specified by 'bins' column
    gdfx = dfx.groupby('bins', as_index=False)

    # apply the weighting_function to percentile-grouped mtr values
    agi_series = gdfx.apply(weighting_function, 'c00100')
    agi_series[agi_series < 0] = 0

    # add a zero to the beginning of 'agi_series'
    zero = pd.Series(0)
    agi_series = zero.append(agi_series)

    # begin plot
    fig = plt.figure(figsize=(10, 5))
    # legend = ax1.legend(loc='lower right', shadow=False)

    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.set_xlabel(x1label)
    ax2.set_xlabel(x2label)
    ax1.set_ylabel(ylabel)

    ax1.set_xticks(np.arange(0, 110, 10))
    ax2.set_xticks(np.arange(0, 110, 10))

    ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax2.set_xticklabels(agi_series.round())

    ax1.plot(lines['reform'], color='red', label='Reform')
    ax2.plot(lines['base'], color='blue', label='Baseline')
    
    ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
    ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)
    
    # save plot
    plotname = plotname + '.png'
    fig.savefig(plotname, dpi=800)
    fig.show()


# In[17]:

def create_difference_table(recs1, recs2, groupby,
                            income_measure='expanded_income',
                            income_to_present='iitax'):
    """
    Get results from two different Records objects for the same year, compare
    the two results, and return the differences as a Pandas DataFrame that is
    sorted according to the variable specified by the groupby argument.
    Parameters
    ----------
    recs1 : a Tax-Calculator Records object that refers to the baseline
    recs2 : a Tax-Calculator Records object that refers to the reform
    groupby : String object
        options for input: 'weighted_deciles', 'small_income_bins',
        'large_income_bins', 'webapp_income_bins'
        determines how the columns in the resulting Pandas DataFrame are sorted
    income_measure : String object
        options for input: '_expanded_income', '_iitax'
        classifier of income bins/deciles
    income_to_present : String object
        options for input: '_iitax', '_payrolltax', '_combined'
    Returns
    -------
    Pandas DataFrame object
    """
    # pylint: disable=too-many-locals
    if recs1.current_year != recs2.current_year:
        msg = 'recs1.current_year not equal to recs2.current_year'
        raise ValueError(msg)
    res1 = results(recs1)
    res2 = results(recs2)
    baseline_income_measure = income_measure + 'baseline'
    res2[baseline_income_measure] = res1[income_measure]
    income_measure = baseline_income_measure
    if groupby == 'weighted_deciles':
        pdf = add_weighted_income_bins(res2, num_bins=10,
                                       income_measure=income_measure)
    elif groupby == 'small_income_bins':
        pdf = add_income_bins(res2, compare_with='soi',
                              income_measure=income_measure)
    elif groupby == 'large_income_bins':
        pdf = add_income_bins(res2, compare_with='tpc',
                              income_measure=income_measure)
    elif groupby == 'webapp_income_bins':
        pdf = add_income_bins(res2, compare_with='webapp',
                              income_measure=income_measure)
    else:
        msg = ("groupby must be either "
               "'weighted_deciles' or 'small_income_bins' "
               "or 'large_income_bins' or 'webapp_income_bins'")
        raise ValueError(msg)
    # compute difference in results
    # Positive values are the magnitude of the tax increase
    # Negative values are the magnitude of the tax decrease
    res2['avg-agi'] = res2['c00100']
    diffs = means_and_comparisons('avg-agi',
                                  pdf.groupby('bins', as_index=False),
                                  (res2['avg-agi'] * res2['s006']).sum())
    output = pd.DataFrame()
    output['avg-agi'] = diffs['mean']
    res2['tax_diff'] = res2[income_to_present] - res1[income_to_present]    
    diffs = means_and_comparisons('tax_diff',
                                  pdf.groupby('bins', as_index=False),
                                  (res2['tax_diff'] * res2['s006']).sum())

    sum_row = get_sums(diffs)[diffs.columns.values.tolist()]
    diffs = diffs.append(sum_row)  # pylint: disable=redefined-variable-type
    pd.options.display.float_format = '{:8,.0f}'.format
    srs_inc = ['{0:.2f}%'.format(val * 100) for val in diffs['perc_inc']]
    diffs['perc_inc'] = pd.Series(srs_inc, index=diffs.index)

    srs_cut = ['{0:.2f}%'.format(val * 100) for val in diffs['perc_cut']]
    diffs['perc_cut'] = pd.Series(srs_cut, index=diffs.index)
    srs_change = ['{0:.2f}%'.format(val * 100)
                  for val in diffs['share_of_change']]
    diffs['share_of_change'] = pd.Series(srs_change, index=diffs.index)
       
    # columns containing weighted values relative to the binning mechanism
    non_sum_cols = [col for col in diffs.columns
                    if 'mean' in col or 'perc' in col]
    for col in non_sum_cols:
        diffs.loc['sums', col] = 'n/a'
        
    diffs['avg-agi'] = output['avg-agi']
    
    return diffs


# In[18]:

# define MTR macros
def mtr_macro(calc1, 
              calc2, 
              section = 'z',
              mars='ALL', 
              mtr_measure='combined', 
              mtr_variable='e00200p', 
              alt_e00200p_text='', 
              mtr_wrt_full_compen=False, 
              income_measure='agi', 
              dollar_weighting=False):
    
    # pylint: disable=too-many-arguments,too-many-statements,
    # pylint: disable=too-many-locals,too-many-branches
    # check that two calculator objects have the same current_year
    if calc1.current_year == calc2.current_year:
        year = calc1.current_year
    else:
        msg = 'calc1.current_year={} != calc2.current_year={}'
        raise ValueError(msg.format(calc1.current_year, calc2.current_year))
    # check validity of function arguments
    # . . check income_measure value
    weighting_function = weighted_mean
    if income_measure == 'wages':
        income_var = 'e00200'
        income_str = 'Wage'
        if dollar_weighting:
            weighting_function = wage_weighted
    elif income_measure == 'agi':
        income_var = 'c00100'
        income_str = 'AGI'
        if dollar_weighting:
            weighting_function = agi_weighted
    elif income_measure == 'expanded_income':
        income_var = 'expanded_income'
        income_str = 'Expanded Income'
        if dollar_weighting:
            weighting_function = expanded_income_weighted
    else:
        msg = ('income_measure="{}" is neither '
               '"wages", "agi", nor "expanded_income"')
        raise ValueError(msg.format(income_measure))
    # . . check mars value
    if isinstance(mars, six.string_types):
        if mars != 'ALL':
            msg = 'string value of mars="{}" is not "ALL"'
            raise ValueError(msg.format(mars))
    elif isinstance(mars, int):
        if mars < 1 or mars > 4:
            msg = 'integer mars="{}" is not in [1,4] range'
            raise ValueError(msg.format(mars))
    else:
        msg = 'mars="{}" is neither a string nor an integer'
        raise ValueError(msg.format(mars))
    # . . check mars value if mtr_variable is e00200s
    if mtr_variable == 'e00200s' and mars != 2:
        msg = 'mtr_variable == "e00200s" but mars != 2'
        raise ValueError(msg)
    # . . check mtr_measure value
    if mtr_measure == 'itax':
        mtr_str = 'Income-Tax'
    elif mtr_measure == 'ptax':
        mtr_str = 'Payroll-Tax'
    elif mtr_measure == 'combined':
        mtr_str = 'Income+Payroll-Tax'
    else:
        msg = ('mtr_measure="{}" is neither '
               '"itax" nor "ptax" nor "combined"')
        raise ValueError(msg.format(mtr_measure))
    # calculate marginal tax rates
    (mtr1_ptax, mtr1_itax,
     mtr1_combined) = calc1.mtr(variable_str=mtr_variable,
                                wrt_full_compensation=mtr_wrt_full_compen)
    (mtr2_ptax, mtr2_itax,
     mtr2_combined) = calc2.mtr(variable_str=mtr_variable,
                                wrt_full_compensation=mtr_wrt_full_compen)
    # extract needed output that is assumed unchanged by reform from calc1
    record_columns = ['s006']
    if mars != 'ALL':
        record_columns.append('MARS')
    record_columns.append(income_var)
    output = [getattr(calc1.records, col) for col in record_columns]
    dfx = pd.DataFrame(data=np.column_stack(output), columns=record_columns)
    # set mtr given specified mtr_measure
    if mtr_measure == 'itax':
        dfx['mtr1'] = mtr1_itax
        dfx['mtr2'] = mtr2_itax
    elif mtr_measure == 'ptax':
        dfx['mtr1'] = mtr1_ptax
        dfx['mtr2'] = mtr2_ptax
    elif mtr_measure == 'combined':
        dfx['mtr1'] = mtr1_combined
        dfx['mtr2'] = mtr2_combined
    # select filing-status subgroup, if any
    if mars != 'ALL':
        dfx = dfx[dfx['MARS'] == mars]

    # bin data for graphing
    dfx = add_weighted_income_bins(dfx, num_bins=100,
                                   income_measure=income_var,
                                   weight_by_income_measure=dollar_weighting)
    # split dfx into groups specified by 'bins' column
    gdfx = dfx.groupby('bins', as_index=False)
    # apply the weighting_function to percentile-grouped mtr values
    mtr1_series = gdfx.apply(weighting_function, 'mtr1')
    mtr2_series = gdfx.apply(weighting_function, 'mtr2')
    agi_series = gdfx.apply(weighting_function, 'c00100')
    decile_series = gdfx.apply(weighting_function, 'bins')

    # construct DataFrame containing the two mtr_series
    lines = pd.DataFrame()
    lines['base'] = mtr1_series
    lines['reform'] = mtr2_series
    lines['agi'] = agi_series.round()
    lines['percentiles'] = decile_series
    
    # calculate ten year averages
    
    # average MTR, bottom ten percent, baseline case
    var1 = (lines['base'][0] + lines['base'][1] + lines['base'][2] + lines['base'][3] 
    + lines['base'][4] + lines['base'][5] + lines['base'][6] + lines['base'][7] 
    + lines['base'][8] + lines['base'][9])/10

    # average MTR, bottom ten percent, reform case
    var2 = (lines['reform'][0] + lines['reform'][1] + lines['reform'][2] + lines['reform'][3] 
    + lines['reform'][4] + lines['reform'][5] + lines['reform'][6] + lines['reform'][7] 
    + lines['reform'][8] + lines['reform'][9])/10
 
    # spread for bottom ten percent between reform and baseline
    var3 = ((lines['reform'][0] - lines['base'][0]) 
    + (lines['reform'][1] - lines['base'][1])
    + (lines['reform'][2] - lines['base'][2])
    + (lines['reform'][3] - lines['base'][3])
    + (lines['reform'][4] - lines['base'][4])
    + (lines['reform'][5] - lines['base'][5])
    + (lines['reform'][6] - lines['base'][6])
    + (lines['reform'][7] - lines['base'][7])
    + (lines['reform'][8] - lines['base'][8])
    + (lines['reform'][9] - lines['base'][9]))/10
       
    # average MTR, top ten percent, baseline case
    var4 = (lines['base'][90] + lines['base'][91] + lines['base'][92] + lines['base'][93] 
    + lines['base'][94] + lines['base'][95] + lines['base'][96] + lines['base'][97] 
    + lines['base'][98] + lines['base'][99])/10

    # average MTR, top ten percent, reform case
    var5 = (lines['reform'][90] + lines['reform'][91] + lines['reform'][92] + lines['reform'][93] 
    + lines['reform'][94] + lines['reform'][95] + lines['reform'][96] + lines['reform'][97] 
    + lines['reform'][98] + lines['reform'][99])/10
    
    # spread for top ten percent between reform and baseline
    var6 = ((lines['reform'][90] - lines['base'][90]) 
    + (lines['reform'][91] - lines['base'][91])
    + (lines['reform'][92] - lines['base'][92])
    + (lines['reform'][93] - lines['base'][93])
    + (lines['reform'][94] - lines['base'][94])
    + (lines['reform'][95] - lines['base'][95])
    + (lines['reform'][96] - lines['base'][96])
    + (lines['reform'][97] - lines['base'][97])
    + (lines['reform'][98] - lines['base'][98])
    + (lines['reform'][99] - lines['base'][99]))/10
    
    # multiply by 100 for formatting
    var1 = var1 * 100
    var2 = var2 * 100
    var3 = var3 * 100
    var4 = var4 * 100
    var5 = var5 * 100
    var6 = var6 * 100
    
    # basleine min
    name1 = section + 'bn'
    # reform min
    name2 = section + 'rn'
    # spread min
    name3 = section + 'vn'
    # baseline max
    name4 = section + 'bx'
    # reform max
    name5 = section + 'rx'
    # spread max
    name6 = section + 'vx'
    
    # set macro descriptions 
    desc1 = 'Section ' + section + ' baseline MTR (0-10%)'
    desc2 = 'Section ' + section + ' reform MTR (0-10%)'
    desc3 = 'Section ' + section + ' spread MTR (0-10%)'
    desc4 = 'Section ' + section + ' baseline MTR (90-100%)'
    desc5 = 'Section ' + section + ' reform MTR (90-100%)'
    desc6 = 'Section ' + section + ' spread MTR (90-100%)'
    
    # define macros
    def_macro(desc1, '{:.2f} percent'.format(var1), name1)
    def_macro(desc2, '{:.2f} percent'.format(var2), name2)
    def_macro(desc3, '{:.2f} percentage points'.format(var3), name3)
    def_macro(desc4, '{:.2f} percent'.format(var4), name4)
    def_macro(desc5, '{:.2f} percent'.format(var5), name5)
    def_macro(desc6, '{:.2f} percentage points'.format(var6), name6)


# In[19]:

def mtr_macros(c2, sec = 'a'):
    
    # perform calculation for primary income earner
    mtr_macro(calc1 = calc_base, 
              calc2 = c2,
              section = sec + 'p',
              mars='ALL', 
              mtr_measure='combined', 
              mtr_variable='e00200p', 
              alt_e00200p_text='', 
              mtr_wrt_full_compen=False, 
              income_measure='agi', 
              dollar_weighting=False)

    # perform calculation for secondary income earner
    mtr_macro(calc1 = calc_base, 
              calc2 = c2,
              section = sec + 's',
              mars=2, 
              mtr_measure='combined', 
              mtr_variable='e00200p', 
              alt_e00200p_text='', 
              mtr_wrt_full_compen=False, 
              income_measure='agi', 
              dollar_weighting=False)


# ## Baseline Calculations

# In[65]:

# perform baseline calculations
recs_base = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_base = Policy()
calc_base = Calculator(records=recs_base, policy=pol_base, verbose=False)
calc_base.advance_to_year(2014)
calc_base.calc_all()


# In[66]:

# define baseline marginal tax rates (MTRs) for primary and secondary earners

# baseline MTR for primary earners
mtrp_base = pd.DataFrame()
mtrp_base['c00100'] = calc_base.records.c00100
mtrp_base['s006'] = calc_base.records.s006
mtrp_base['mtr'] = calc_base.mtr()[2]
mtrp_base['1 - mtr'] = 1.00 - mtrp_base['mtr']

# baseline MTR for secondary earners
mtrs_base = pd.DataFrame()
mtrs_base['c00100'] = calc_base.records.c00100
mtrs_base['s006'] = calc_base.records.s006
mtrs_base['MARS'] = calc_base.records.MARS
mtrs_base['mtr'] = calc_base.mtr('e00200s')[2]
mtrs_base = mtrs_base[mtrs_base['MARS'] == 2]
mtrs_base['1 - mtr'] = 1.00 - mtrs_base['mtr']


# ## Section 2, Part A: Welfare and Transfer Program Repeal

# Repeal all welfare and transfer programs

# In[67]:

# import data

# import snap and ssi MTR data
snap_ssi = pd.read_csv('snap_ssi_mtr.csv')

# import social security MTR data
ss_mtr = pd.read_csv('SS_MTR_futurereg_RETS.csv')

# import cps benefits data
cps_benefits = pd.read_csv('cps_benefit.csv', index_col=None)

# read in CSV of non-modeled welfare programs
otherbenefits = pd.read_csv('benefitprograms.csv')
otherbenefits['Cost'] *= 1000000


# In[68]:

# augment cps benefits data with snap, ssi, and ss data

# calculate total income to approximate average gross income (AGI)
cps_benefits['tot_inc'] = (cps_benefits['WAS'] + cps_benefits['INTST'] + cps_benefits['DBE'] +
                           cps_benefits['ALIMONY'] + cps_benefits['BIL'] + cps_benefits['PENSIONS'] +
                           cps_benefits['RENTS'] + cps_benefits['FIL'] + cps_benefits['UCOMP'])

# sum all benefits programs 
cps_benefits['tot_benefits'] = (cps_benefits['MedicareX'] + cps_benefits['MEDICAID'] + cps_benefits['SSI'] +
                                cps_benefits['SNAP'] + cps_benefits['SS'] + cps_benefits['VB'])

# sum all benefits excluding social security
cps_benefits['ex_ss'] = (cps_benefits['MedicareX'] + cps_benefits['MEDICAID'] + cps_benefits['SSI'] +
                                cps_benefits['SNAP'] + cps_benefits['VB'])

# sum all benefits excluding social security, medicare
cps_benefits['ex_ss_mc'] = (cps_benefits['SSI'] + cps_benefits['MEDICAID'] + 
                                cps_benefits['SNAP'])

# sum all benefits excluding social security and medicare
cps_benefits['dist_benefits'] = (cps_benefits['MEDICAID'] + cps_benefits['SSI'] + cps_benefits['SNAP'] +
                                 cps_benefits['VB'])

# add ssi MTR data for primary and secondary earners
cps_benefits['ssi_p_mtr'] = snap_ssi['ssi_p_mtr']
cps_benefits['ssi_s_mtr'] = snap_ssi['ssi_s_mtr']

# add snap MTR data for primary and secondary earners
cps_benefits['snap_p_mtr'] = snap_ssi['snap_p_mtr']
cps_benefits['snap_s_mtr'] = snap_ssi['snap_s_mtr']

# merge social security MTR data
cps_benefits = cps_benefits.merge(ss_mtr, on='CPSSEQ')

# sum all benefits excluding social security and medicare
dist_benefits_total = (cps_benefits['dist_benefits'] * cps_benefits['s006']).sum()

# cps_benefits


# In[69]:

# sort data and find decile
cps_benefits.sort_values(by='tot_inc', inplace=True)
cps_benefits['cumsum'] = np.cumsum(cps_benefits['s006'].values)
cps_benefits['pct'] = cps_benefits['cumsum'] / cps_benefits['cumsum'].values[-1]
pcts = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
avgs = {}
sums = {}
dist = {}
ex_ss = {}
ex_ss_mc = {}
ppl = {}
agi = {}
distben = {}
for i in range(1,len(pcts)):
    
    avgs['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['tot_benefits'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])] *
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])]).sum() /
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])].sum())
    ex_ss['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['ex_ss'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])] *
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])]).sum() /
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])].sum())
    ex_ss_mc['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['ex_ss_mc'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])] *
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])]).sum() /
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])].sum())  
    sums['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['tot_benefits'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])]) *
                                                                (cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                      (cps_benefits['pct'] < pcts[i])])).sum()
    dist['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['dist_benefits'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                               (cps_benefits['pct'] < pcts[i])] *
                                                                 cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                      (cps_benefits['pct'] < pcts[i])]).sum() /
                                                    dist_benefits_total)
    ppl['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = (cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                    (cps_benefits['pct'] < pcts[i])]).sum()    
    agi['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['tot_inc'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])] *
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])]).sum() /
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])].sum())
    distben['{}%-{}%'.format(pcts[i - 1] * 100, pcts[i] * 100)] = ((cps_benefits['dist_benefits'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                              (cps_benefits['pct'] < pcts[i])] *
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])]).sum() /
                                                                cps_benefits['s006'][(cps_benefits['pct'] >= pcts[i - 1]) &
                                                                                     (cps_benefits['pct'] < pcts[i])].sum())
    
    
ben_df = pd.DataFrame([avgs, sums, dist, ppl, agi, distben, ex_ss, ex_ss_mc])
ben_df = ben_df.transpose()
ben_df.columns = ['avg-modeled', 
                  'sum-modeled', 
                  'distribution', 
                  'num units', 
                  'avg-agi', 
                  'distro_benefits', 
                  'excluding ss', 'excluding ss, medicare']
# ben_df


# In[70]:

# combine distribution of non-modeled and modeled reforms
ben_df['sum-non-modeled'] = ben_df['distribution'] * otherbenefits['Cost'].sum()
ben_df['modeled + non-modeled'] = ben_df['sum-non-modeled'] + ben_df['sum-modeled']
ben_df['total avg'] = ben_df['modeled + non-modeled'] / ben_df['num units']

# ben_df = ben_df.append(ben_df.sum(numeric_only=True), ignore_index=True)
ben_df.index = agi_bins
ben_df.loc['sums'] = ben_df.sum()
ben_df['pct of loss'] = ((ben_df['modeled + non-modeled'] /
                          float(ben_df['modeled + non-modeled'].sum() - ben_df['modeled + non-modeled']['sums'])) * 100)
    
ben_df


# In[73]:

a1_df = restricted_table(ben_df, 
                         ['modeled + non-modeled', 'total avg', 'excluding ss'], 
                         ['Total Benefits ($)', 'Average Benefits ($)', 'Benefits Excluding Social Security ($)'],
                         'a1_df',
                          reindex = True, 
                          na = False)


# In[74]:

# define macros

# bottom 10 percent of income earners lose this amount of their benefits
def_macro('Benefit Loss (0-10%) (part A)', 
          '{:.2f} percent'.format(100*(a1_df['Total Benefits ($)']['0-10%'])/(a1_df['Total Benefits ($)']['Sum'])), 
          'adsn')

# top 10 percent of income earners lose this amount of their benefits
def_macro('Benefit Loss (90-100%) (part A)', 
          '{:.2f} percent'.format(100*(a1_df['Total Benefits ($)']['90-100%'])/(a1_df['Total Benefits ($)']['Sum'])), 
          'adsx')

# general macro function
dist_macro(a1_df, 'a')


# In[75]:

a1_df_edit = a1_df
clist = ['Total Benefits ($)', 'Average Benefits ($)', 'Benefits Excluding Social Security ($)']
rlist = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%', 'Sum']

for citem in clist:
    for ritem in rlist:
        a1_df_edit[citem][ritem] = '{:,.0f}'.format(a1_df[citem][ritem])
    

a1_df_edit = restricted_table(a1_df, 
                         ['Total Benefits ($)', 'Average Benefits ($)', 'Benefits Excluding Social Security ($)'], 
                         ['Total Benefits ($)', 'Average Benefits ($)', 'Benefits Excluding Social Security ($)'],
                         'a1_df',
                          reindex = True, 
                          na = False)

a1_df_edit


# In[28]:

# create data frames for average and total change in benefits
avg_ben_loss = pd.DataFrame()
avg_ben_loss['Benefit Loss'] = ben_df['total avg'].drop('sums')
avg_ben_loss['Income Percentile'] = agi_bins
avg_ben_loss['Average AGI'] = ben_df['avg-agi']

tot_ben_loss = pd.DataFrame()
tot_ben_loss['Benefit Loss'] = ben_df['modeled + non-modeled'].drop('sums') * in_billions
tot_ben_loss['Income Percentile'] = agi_bins
tot_ben_loss['Average AGI'] = ben_df['avg-agi']


# In[29]:

# generate bar charts
makebar(avg_ben_loss, 'a1', x1label = 'AGI Decile', x2label = 'Average AGI by Decile', ylabel = 'Average Benefit Loss')
makebar(tot_ben_loss, 'a2', x1label = 'AGI Decile', x2label = 'Average AGI by Decile', ylabel = 'Total Benefit Loss (billions)')


# In[30]:

# create decile bins
ben_mtr = utils.add_weighted_income_bins(cps_benefits, num_bins=100, income_measure='tot_inc')
ben_mtr_group = ben_mtr.groupby('bins', as_index=False)

# create dictionary for all the lines
mtr_dta = pd.DataFrame()
mtr_dta['ssi_p'] = ben_mtr_group.apply(utils.weighted_mean, 'ssi_p_mtr').values
mtr_dta['ssi_s'] = ben_mtr_group.apply(utils.weighted_mean, 'ssi_s_mtr').values
mtr_dta['snap_p'] = ben_mtr_group.apply(utils.weighted_mean, 'snap_p_mtr').values
mtr_dta['snap_s'] = ben_mtr_group.apply(utils.weighted_mean, 'snap_s_mtr').values
mtr_dta['ss_p'] = ben_mtr_group.apply(utils.weighted_mean, 'SS_MTR_head').values
mtr_dta['ss_s'] = ben_mtr_group.apply(utils.weighted_mean, 'SS_MTR_spouse').values
mtr_dta['pos'] = [i for i in range(1, 101)]


# In[31]:

# generate chart showing mtr change by income percentile

fig = figure(title='Benefit Program MTR Change by Income Percentile')
fig.line(mtr_dta['pos'], mtr_dta['ssi_p'], legend='SSI-Primary Tax Payer')
fig.line(mtr_dta['pos'], mtr_dta['ssi_s'], color='red', legend='SSI-Secondary Tax Payer')
fig.line(mtr_dta['pos'], mtr_dta['snap_p'], color='green', legend='SNAP-Primary Tax Payer')
fig.line(mtr_dta['pos'], mtr_dta['snap_s'], color='purple', legend='SNAP-Secondary Tax Payer')
fig.line(mtr_dta['pos'], mtr_dta['ss_p'], color='coral', legend='Social Security-Primary Tax Payer')
fig.line(mtr_dta['pos'], mtr_dta['ss_s'], color='mediumspringgreen', legend='Social Security-Secondary Tax Payer')

show(fig)


# In[32]:

# tax calculations with zeroed out social security benefits
recs_ss = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ss = Policy()
calc_ss = Calculator(records=recs_ss, policy=pol_ss, verbose=False)
calc_ss.records.e02400 = np.zeros(len(calc_ss.records.e02400))
calc_ss.advance_to_year(2014)
calc_ss.calc_all()
ss_diffs = utils.create_difference_table(calc_base.records, calc_ss.records, 'weighted_deciles',
                                         income_to_present='combined')
ss_tax_revloss = ((calc_ss.records.combined - calc_base.records.combined) * calc_ss.records.s006).sum()
# print (ss_tax_revloss)
ss_diffs


# In[33]:

a2_df = restricted_table(ss_diffs, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total (dollars)', 'Average (dollars)', 'Increase (percent)', 'Share (percent)'],
                 'a2_df',
                  reindex = True
                )

a2_df


# In[34]:

# holds the total cost of benefit program repeal
welfare_repeal = ben_df['modeled + non-modeled'].drop('sums').sum() + ss_tax_revloss
welfare_repeal * in_billions


# In[35]:

def_macro('Welfare/Transfer Porgram Repeal (trillions)', '\${:,.2f}'.format(welfare_repeal * in_trillions), 'aoog')


# In[36]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc1 = calc_base, 
         calc2 = calc_ss, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'a3')


# In[37]:

# average secondary earner MTR change by percentile of AGI
makeline(calc1 = calc_base, 
         calc2 = calc_ss, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'a4')


# In[38]:

mtr_macros(calc_ss, sec = 'a')


# ## Section 3, Part B: Tax Reform

# Repeal all tax preferences, standard deduction, personal exemption, above the line deduction, itemized deductions, tax credits, etc.

# In[39]:

recs_tax = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_tax = Policy()

# fix this to allow for charitable deductions, just adjust haircut amounts
tax_reform = {
    2014: {
        '_ALD_StudentLoan_hc': [1.0],
        '_ALD_SelfEmploymentTax_hc': [1.0],
        '_ALD_SelfEmp_HealthIns_hc': [1.0],
        '_ALD_KEOGH_SEP_hc': [1.0],
        '_ALD_EarlyWithdraw_hc': [1.0],
        '_ALD_Alimony_hc': [1.0],
        '_ALD_Dependents_hc': [1.0],
        '_ALD_EducatorExpenses_hc': [1.0],
        '_ALD_HSADeduction_hc': [1.0],
        '_ALD_IRAContributions_hc': [1.0],
        '_ALD_DomesticProduction_hc': [1.0],
        '_ALD_Tuition_hc': [1.0],
        '_CR_RetirementSavings_hc': [1.0],
        '_CR_ForeignTax_hc': [1.0],
        '_CR_ResidentialEnergy_hc': [1.0],
        '_CR_GeneralBusiness_hc': [1.0],
        '_CR_MinimumTax_hc': [1.0],
        '_CR_AmOppRefundable_hc': [1.0],
        '_CR_AmOppNonRefundable_hc': [1.0],
        '_CR_SchR_hc': [1.0],
        '_CR_OtherCredits_hc': [1.0],
        '_CR_Education_hc': [1.0],
        '_II_em': [0.0],
        '_STD': [[0.0, 0.0, 0.0, 0.0, 0.0]],
        '_STD_Aged': [[0.0, 0.0, 0.0, 0.0, 0.0]],
        '_ID_Medical_hc': [1.0],
        '_ID_StateLocalTax_hc': [1.0],
        '_ID_RealEstate_hc': [1.0],
        '_ID_InterestPaid_hc': [1.0],
        '_ID_Casualty_hc': [1.0],
        '_ID_Miscellaneous_hc': [1.0],
        '_CDCC_c': [0.0],
        '_CTC_c': [0.0],
        '_EITC_c': [[0.0, 0.0, 0.0, 0.0]],
        '_LLC_Expense_c': [0.0],
        '_ETC_pe_Single': [0.0],
        '_ETC_pe_Married': [0.0],
    }
}
pol_tax.implement_reform(tax_reform)
calc_tax = Calculator(records=recs_tax, policy=pol_tax, verbose=False)


# In[40]:

calc_tax.advance_to_year(2014)
calc_tax.calc_all()


# In[41]:

# diag_tax = utils.create_diagnostic_table(calc_tax)
# diag_tax


# In[42]:

# generate difference table 
diff_table = utils.create_difference_table(calc_base.records, 
                                           calc_tax.records, 
                                           'weighted_deciles', 
                                           income_to_present='combined')
diff_table


# In[43]:

# generate difference table 
diff_table = create_difference_table(calc_base.records, 
                                     calc_tax.records, 
                                     'weighted_deciles', 
                                     income_to_present='combined')
diff_table


# In[44]:

# percent of tax units facing a tax increase
pct_inc = (diff_table['tax_inc']['sums'] / diff_table['count']['sums'])*100

def_macro('Percent of tax units facing a tax increase (section B)', '{:,.2f} percent'.format(pct_inc), 'bdpp')


# In[45]:

b1_df = restricted_table(diff_table, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total (dollars)', 'Average (dollars)', 'Increase (percent)', 'Share (percent)'],
                 'b1_df', 
                reindex = True
                )

b1_df


# In[46]:

# make macros for top and bottom ten percent
dist_macro(b1_df, 'b')


# ### Part B Plots

# In[47]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = list(diff_table['mean'].drop('sums'))
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diff_table['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name

makebar(avg_change_data, 'b1', x1label = 'AGI Decile', x2label = 'Average Tax Liability Increase', ylabel = 'Average Benefit Loss')
# avg_change_data


# In[48]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = list(diff_table['tot_change'].drop('sums') * in_billions)
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diff_table['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name

makebar(tot_change_data, 'b2', x1label = 'AGI Decile', x2label = 'Total Tax Liability Increase', ylabel = 'Total Benefit Loss (billions)')

# tot_change_data


# In[49]:

results_pdf = utils.results(calc_base.records)
results_pdf['c02900'] = calc_base.records.c02900
results_pdf = utils.add_weighted_income_bins(results_pdf, num_bins=100)


# In[50]:

# mtr_tax_primary = utils.mtr_graph_data(calc_base, calc_tax, income_measure='agi')


# In[51]:

# mtr_primary_plot = utils.xtr_graph_plot(mtr_tax_primary,
#                                        title='Mean Primary Earner Marginal Tax Rate by Income Percentile')
# show(mtr_primary_plot)


# In[52]:

# mtr_tax_secondary = utils.mtr_graph_data(calc_base, calc_tax, mtr_variable='e00200s', mars=2, income_measure='agi')


# In[53]:

# mtr_secondary_plot = utils.xtr_graph_plot(mtr_tax_secondary,
#                                           title='Mean Secondary Earner Marginal Tax Rate',
#                                           xlabel='AGI Percentile')
# show(mtr_secondary_plot)


# In[54]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc1 = calc_base, 
         calc2 = calc_tax, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'b3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_tax, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'b4')


# In[55]:

mtr_macros(calc_tax, sec = 'b')


# In[56]:

# primary earner's MTR Change
mtrp_df = pd.DataFrame()
mtrp_df['c00100'] = calc_tax.records.c00100
mtrp_df['s006'] = calc_tax.records.s006
mtrp_df['mtr'] = calc_tax.mtr()[2]
mtrp_df['1 - mtr'] = 1. - mtrp_df['mtr']
mtrp_df['pct change'] = ((mtrp_df['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# create graph of 1 - MTR
mtrp_df = utils.add_weighted_income_bins(mtrp_df, num_bins=100, income_measure='c00100')
mtrp_ = mtrp_df.groupby('bins')
mtr1 = mtrp_.apply(utils.weighted_mean, 'pct change')
agi = mtrp_.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_.apply(utils.weighted_mean, 's006')

lines = pd.DataFrame()
lines['primary'] = mtr1
lines['avg-agi'] = agi
lines['s006'] = s006


# In[57]:

# secondary earner
mtrs_df = pd.DataFrame()
mtrs_df['c00100'] = calc_tax.records.c00100
mtrs_df['s006'] = calc_tax.records.s006
mtrs_df['MARS'] = calc_tax.records.MARS
mtrs_df['mtr'] = calc_tax.mtr('e00200s')[2]
mtrs_df = mtrs_df[mtrs_df['MARS'] == 2]
mtrs_df['1 - mtr'] = 1. - mtrs_df['mtr']
mtrs_df['pct change'] = ((mtrs_df['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# create graph of 1 - MTR
mtrs_df = add_weighted_income_bins(mtrs_df, num_bins=100, income_measure='c00100')
mtrs_ = mtrs_df.groupby('bins')
mtr2 = mtrs_.apply(utils.weighted_mean, 'pct change')
lines['secondary'] = mtr2


# In[58]:

# generate dataframe for graph
lines['bins'] = lines.index
del lines.index.name

plines = lines['primary'].values
slines = lines['secondary'].values
agi = lines['avg-agi'].values
s006 = lines['s006'].values
idlines = lines.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[59]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[60]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'b5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)    

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[61]:

fig = figure(title='Mean Percent Change in 1 - MTR After Tax Reform')
fig.line(idlines, plines, legend='Primary Earner')
fig.line(idlines, slines, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# ## Section 4, Part C: Tax and Welfare/Transfer

# Combine parts A and B

# In[62]:

# Revenue from tax and welfare program repeal
tax_rev = ((calc_tax.records.combined - calc_base.records.combined) * calc_tax.records.s006).sum()
revenue = tax_rev + welfare_repeal
revenue * in_billions

revenue_in_trillions = revenue * in_trillions


# In[63]:

def_macro('Money freed from Section C for UBI', '\${:,.2f} billions'.format(revenue_in_trillions), 'cuog')


# In[64]:

pt_c = pd.DataFrame()
pt_c['Total Revenue Change'] = (ben_df['modeled + non-modeled'].values + diff_table['tot_change'].values -
                                ss_diffs['tot_change'].values)
pt_c['Count'] = ss_diffs['count']
pt_c['Average Revenue Change'] = pt_c['Total Revenue Change'] / pt_c['Count']

pt_c['Average AGI'] = diff_table['avg-agi']
#pt_c

pt_c.index = agi_bins + ['sums']
pt_c_plot_data = pt_c.drop('sums')
pt_c_plot_data['Income Bin'] = pt_c_plot_data.index.values
# pt_c_plot_data['Total Revenue Change'] *= in_billions 
pt_c_plot_data['Average AGI'] = pt_c['Average AGI'] 
pt_c_plot_data


# In[65]:

avg_change_data = pd.DataFrame()

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name

avg_change_data['Benefit Loss'] = pt_c['Average Revenue Change']
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = pt_c_plot_data['Average AGI']

avg_change_data


# In[66]:

tot_change_data = pd.DataFrame()

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name

tot_change_data['Benefit Loss'] = pt_c['Total Revenue Change']
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = pt_c_plot_data['Average AGI']

tot_change_data


# In[67]:

pt_c_plot_data['mean'] = 1
pt_c_plot_data['perc_inc'] = 1

c1_df = restricted_table(pt_c_plot_data, 
                 ['Total Revenue Change', 'Average Revenue Change'], 
                 ['Total Revenue Change ($)', 'Average Revenue Change ($)'],
                 'c1_df',
                 reindex = False
                )

# add sum row
sum1 = (c1_df['Total Revenue Change ($)']['0-10%'] 
     + c1_df['Total Revenue Change ($)']['10-20%'] 
     + c1_df['Total Revenue Change ($)']['20-30%'] 
     + c1_df['Total Revenue Change ($)']['30-40%'] 
     + c1_df['Total Revenue Change ($)']['40-50%'] 
     + c1_df['Total Revenue Change ($)']['50-60%'] 
     + c1_df['Total Revenue Change ($)']['60-70%'] 
     + c1_df['Total Revenue Change ($)']['70-80%'] 
     + c1_df['Total Revenue Change ($)']['80-90%'] 
     + c1_df['Total Revenue Change ($)']['90-100%'])

sum2 = (c1_df['Average Revenue Change ($)']['0-10%'] 
     + c1_df['Average Revenue Change ($)']['10-20%'] 
     + c1_df['Average Revenue Change ($)']['20-30%'] 
     + c1_df['Average Revenue Change ($)']['30-40%'] 
     + c1_df['Average Revenue Change ($)']['40-50%'] 
     + c1_df['Average Revenue Change ($)']['50-60%'] 
     + c1_df['Average Revenue Change ($)']['60-70%'] 
     + c1_df['Average Revenue Change ($)']['70-80%'] 
     + c1_df['Average Revenue Change ($)']['80-90%'] 
     + c1_df['Average Revenue Change ($)']['90-100%'])

c1_sum = pd.DataFrame({'Total Revenue Change ($)':[sum1],
                    'Average Revenue Change ($)':[sum2]},
                   index = ['Sum'])

c1_df = pd.concat([c1_df, c1_sum])


c1_df


# In[68]:

# make macros for top and bottom ten percent
dist_macro(c1_df, 'c')


# In[69]:

# generate bar charts
makebar(avg_change_data, 'c1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Loss from Welfare/Transfer and Tax Reforms')
makebar(tot_change_data, 'c2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Loss from Welfare/Transfer and Tax Reforms (billions)')


# ## Section 5, Part D: Tax and Welfare/Transfer Plus UBI for All

# Tax and welfare reform plus a UBI for the entire population. UBI is X for those above 18 and .5X for those under 18

# In[70]:

# Total Population for a UBI
u18 = (calc_tax.records.nu18 * calc_tax.records.s006).sum()
abv18 = ((calc_tax.records.n1821 + calc_tax.records.n21) * calc_tax.records.s006).sum()
abv21 = (calc_tax.records.n21 * calc_tax.records.s006).sum()


# In[71]:

# Function to determine UBI levels
def ubi_amt(revenue):
    ubi_18 = revenue / ((u18 * 0.5) + abv18)
    ubi_u18 = ubi_18 * 0.5
    total_ubi = (ubi_18 * abv18) + (ubi_u18 * u18)
    return ubi_18, ubi_u18


# In[72]:

initial_ubi = ubi_amt(revenue)
ubi_u18 = initial_ubi[1]
ubi_18 = initial_ubi[0]
print ('UBI for those above 18: {:.2f}'.format(ubi_18))
print ('UBI for those bellow 18: {:.2f}'.format(ubi_u18))


# In[73]:

# define macros
def_macro('UBI for those above 18 (part D)', '\${:,.2f}'.format(ubi_18), 'duag')
def_macro('UBI for those bellow 18 (part D)', '\${:,.2f}'.format(ubi_u18), 'dubg')


# In[74]:

# UBI all Calculator - Initial UBI tax revenue
recs_ubi_all = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_all = Policy()
pol_ubi_all.implement_reform(tax_reform)
ubi_reform_all = {
    2014: {
        '_UBI1': [ubi_u18],
        '_UBI2': [ubi_18],
        '_UBI3': [ubi_18]
    }
}
pol_ubi_all.implement_reform(ubi_reform_all)
calc_ubi_all = Calculator(records=recs_ubi_all, policy=pol_ubi_all, verbose=False)
calc_ubi_all.records.e02400 = np.zeros(len(calc_ubi_all.records.e02400))
calc_ubi_all.advance_to_year(2014)
calc_ubi_all.calc_all()

# Initial UBI tax revenue
ubi_tax_rev = ((calc_ubi_all.records.combined - calc_tax.records.combined) * calc_ubi_all.records.s006).sum()
ubi_tax_rev


# In[75]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finder(ubi_18, ubi_u18):
    # Build a calculator with the specified UBI levels
    recs_finder = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finder = Policy()
    pol_finder.implement_reform(tax_reform)
    ubi_finder_reform = {
        2014: {
            '_UBI1': [ubi_u18],
            '_UBI2': [ubi_18],
            '_UBI3': [ubi_18]
        }
    }
    pol_finder.implement_reform(ubi_finder_reform)
    calc_finder = Calculator(records=recs_finder, policy=pol_finder, verbose=False)
    calc_finder.records.e02400 = np.zeros(len(calc_finder.records.e02400))
    calc_finder.advance_to_year(2014)
    calc_finder.calc_all()
    
    # Check if UBI is greater or less than the additional revenue
    # Revenue from tax reform
    ubi_tax_rev = ((calc_finder.records.combined - calc_tax.records.combined) * calc_finder.records.s006).sum()
    total_rev = ubi_tax_rev + revenue
    ubi = (calc_finder.records.ubi * calc_finder.records.s006).sum()
    diff = ubi - total_rev
    return diff, ubi_tax_rev


# In[76]:

# While loop to call ubi_finder function until optimal UBI is found
diff = 9e99
prev_ubi_tax_rev = ubi_tax_rev
while abs(diff) >= 0.01:
    ubi_18, ubi_u18 = ubi_amt(revenue + ubi_tax_rev)
    diff, ubi_tax_rev = ubi_finder(ubi_18, ubi_u18)
    if diff > 0:
        ubi_tax_rev = prev_ubi_tax_rev * 0.5
    prev_ubi_tax_rev = ubi_tax_rev
print (ubi_18, ubi_u18)


# In[77]:

calc_ubi_all.records.e00200.sum()


# In[78]:

# Create actual UBI Calculator
recs_ubiall = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubiall = Policy()
ubi_all = {
    2014: {
        '_UBI1': [ubi_u18],
        '_UBI2': [ubi_18],
        '_UBI3': [ubi_18]
    }
}
pol_ubiall.implement_reform(tax_reform)
pol_ubiall.implement_reform(ubi_all)
calc_ubiall = Calculator(records=recs_ubiall, policy=pol_ubiall, verbose=False)
calc_ubiall.records.e02400 = np.zeros(len(calc_ubiall.records.e02400))
calc_ubiall.advance_to_year(2014)
calc_ubiall.calc_all()


# In[79]:

# Check that comparison to be post-tax reform, not the base
diffs_ubi_all = create_difference_table(calc_base.records, calc_ubiall.records, 'weighted_deciles',
                                              income_to_present='combined')
diffs_ubi_all


# In[80]:

d1_df = restricted_table(diffs_ubi_all, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'd1_df',
                 reindex = True
                )

d1_df


# In[81]:

# make macros for top and bottom ten percent
dist_macro(d1_df, 'd')


# In[82]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubiall.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubiall.records.s006[neg_combined < 0]).sum() /
calc_ubiall.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubiall.records.ubi[neg_combined < 0] * calc_ubiall.records.s006[neg_combined < 0]).sum() /
calc_ubiall.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part D)', units(stat1), 'datd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part D)', units(stat2), 'dasd')
def_macro('Average UBI to those who see tax decrease with UBI (part D)', units(stat3), 'daud')


# In[83]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diffs_ubi_all['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diffs_ubi_all['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[84]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diffs_ubi_all['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diffs_ubi_all['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[85]:

# generate bar charts
makebar(avg_change_data, 'd1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'd2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[86]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubiall, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'd3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubiall, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'd4')


# In[87]:

mtr_macros(calc_ubiall, sec = 'd')


# In[88]:

# Primary earner's MTR Change
mtrp_ubidf = pd.DataFrame()
mtrp_ubidf['c00100'] = calc_ubiall.records.c00100
mtrp_ubidf['s006'] = calc_ubiall.records.s006
mtrp_ubidf['mtr'] = calc_ubiall.mtr()[2]
mtrp_ubidf['1 - mtr'] = 1. - mtrp_ubidf['mtr']
mtrp_ubidf['pct change'] = ((mtrp_ubidf['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_ubidf = utils.add_weighted_income_bins(mtrp_ubidf, num_bins=100, income_measure='c00100')
mtrp_ubiall = mtrp_ubidf.groupby('bins')
mtr1ubiall = mtrp_ubiall.apply(utils.weighted_mean, 'pct change')
agi = mtrp_ubiall.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_ubiall.apply(utils.weighted_mean, 's006')

lines_ubiall = pd.DataFrame()
lines_ubiall['primary'] = mtr1ubiall
lines_ubiall['avg-agi'] = agi
lines_ubiall['s006'] = s006


# In[89]:

# Secondary earner
mtrs_ubiall_df = pd.DataFrame()
mtrs_ubiall_df['c00100'] = calc_ubiall.records.c00100
mtrs_ubiall_df['s006'] = calc_ubiall.records.s006
mtrs_ubiall_df['MARS'] = calc_ubiall.records.MARS
mtrs_ubiall_df['mtr'] = calc_ubiall.mtr('e00200s')[2]
mtrs_ubiall_df = mtrs_ubiall_df[mtrs_ubiall_df['MARS'] == 2]
mtrs_ubiall_df['1 - mtr'] = 1. - mtrs_ubiall_df['mtr']
mtrs_ubiall_df['pct change'] = ((mtrs_ubiall_df['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_ubiall_df = utils.add_weighted_income_bins(mtrs_ubiall_df, num_bins=100, income_measure='c00100')
mtrs_ubiall = mtrs_ubiall_df.groupby('bins')
mtr2ubiall = mtrs_ubiall.apply(utils.weighted_mean, 'pct change')
lines_ubiall['secondary'] = mtr2ubiall


# In[90]:

plines_ubiall = lines_ubiall['primary'].values
slines_ubiall = lines_ubiall['secondary'].values
idlines_ubiall = lines_ubiall.index.values

# generate dataframe for graph
lines_ubiall['bins'] = lines_ubiall.index
del lines_ubiall.index.name

plines = lines_ubiall['primary'].values
slines = lines_ubiall['secondary'].values
agi = lines_ubiall['avg-agi'].values
s006 = lines_ubiall['s006'].values
idlines = lines_ubiall.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[91]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[92]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'd5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)    

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[93]:

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_ubiall, plines_ubiall, legend='Primary Earner')
fig.line(idlines_ubiall, slines_ubiall, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# In[94]:

# Show, by total amount, the difference between additional taxes and UBI income
(calc_ubi_all.records.ubi * calc_ubi_all.records.s006).sum() - diffs_ubi_all['tot_change']['sums']


# ## Section 6, Part E: Tax, Welfare/Transfew, and UBI 18+

# Tax and welfare reform, plus a UBI for all those 18 and over

# In[95]:

# Function to determine UBI levels
def ubi_amt18(revenue):
    ubi_a18 = revenue / abv18
    return ubi_a18


# In[96]:

ubi_a18 = ubi_amt18(revenue)
print ('UBI for those above 18: {:.2f}'.format(ubi_a18))


# In[97]:

# define macros
def_macro('UBI for those above 18 (part E)', '\${:,.2f}'.format(ubi_a18), 'euog')


# In[98]:

# UBI above 18 Calculator - Initial UBI tax revenue
recs_ubi_18 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_18 = Policy()
pol_ubi_18.implement_reform(tax_reform)
ubi_reform_18 = {
    2014: {
        '_UBI2': [ubi_a18],
        '_UBI3': [ubi_a18]
    }
}
pol_ubi_18.implement_reform(ubi_reform_all)
calc_ubi_18 = Calculator(records=recs_ubi_18, policy=pol_ubi_18, verbose=False)
calc_ubi_18.records.e02400 = np.zeros(len(calc_ubi_18.records.e02400))
calc_ubi_18.advance_to_year(2014)
calc_ubi_18.calc_all()

# Initial UBI tax revenue
ubi_tax_rev18 = ((calc_ubi_18.records.combined - calc_tax.records.combined) * calc_ubi_18.records.s006).sum()
ubi_tax_rev18


# In[99]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finder18(ubi_a18):
    # Build a calculator with the specified UBI levels
    recs_finder18 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finder18 = Policy()
    pol_finder18.implement_reform(tax_reform)
    ubi_finder_reform18 = {
        2014: {
            '_UBI2': [ubi_a18],
            '_UBI3': [ubi_a18]
        }
    }
    pol_finder18.implement_reform(ubi_finder_reform18)
    calc_finder18 = Calculator(records=recs_finder18, policy=pol_finder18, verbose=False)
    calc_finder18.records.e02400 = np.zeros(len(calc_finder18.records.e02400))
    calc_finder18.advance_to_year(2014)
    calc_finder18.calc_all()
    # Revenue from tax reform
    ubi_tax_rev18 = ((calc_finder18.records.combined - calc_tax.records.combined) * calc_finder18.records.s006).sum()
    total_rev18 = ubi_tax_rev18 + revenue
    ubi18 = (calc_finder18.records.ubi * calc_finder18.records.s006).sum()
    diff18 = ubi18 - total_rev18
    return diff18, ubi_tax_rev18


# In[100]:

# While loop to call ubi_finder function until optimal UBI is found
diff18 = 9e99
prev_ubi_tax_rev18 = ubi_tax_rev18
while abs(diff18) >= 0.01:
    ubi_a18 = ubi_amt18(revenue + ubi_tax_rev18)
    diff18, ubi_tax_rev18 = ubi_finder18(ubi_a18)
    if diff18 > 0:
        ubi_tax_rev18 = prev_ubi_tax_rev18 * 0.5
    prev_ubi_tax_rev18 = ubi_tax_rev18
print (ubi_a18)


# In[101]:

# Run calculator with UBI
recs_ubi18 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi18 = Policy()
pol_ubi18.implement_reform(tax_reform)
ubi18_reform = {
    2014: {
        '_UBI2': [ubi_a18],
        '_UBI3': [ubi_a18]
    }
}
pol_ubi18.implement_reform(ubi18_reform)
calc_ubi18 = Calculator(records=recs_ubi18, policy=pol_ubi18, verbose=False)
calc_ubi18.records.e02400 = np.zeros(len(calc_ubi18.records.e02400))
calc_ubi18.advance_to_year(2014)
calc_ubi18.calc_all()


# In[102]:

# Create differences table
diffs_ubi18 = create_difference_table(calc_base.records, calc_ubi18.records, 'weighted_deciles',
                                      income_to_present='combined')
diffs_ubi18


# In[103]:

e1_df = restricted_table(diffs_ubi18, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'e1_df', 
                 reindex = True
                )
e1_df


# In[104]:

# make macros for top and bottom ten percent
dist_macro(e1_df, 'e')


# In[105]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubi18.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubi18.records.s006[neg_combined < 0]).sum() /
calc_ubi18.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubi18.records.ubi[neg_combined < 0] * calc_ubi18.records.s006[neg_combined < 0]).sum() /
calc_ubi18.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part J)', units(stat1), 'eatd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part J)', units(stat2), 'easd')
def_macro('Average UBI to those who see tax decrease with UBI (part J)', units(stat3), 'eaud')


# In[106]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diffs_ubi18['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diffs_ubi18['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[107]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diffs_ubi18['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diffs_ubi18['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[108]:

# generate bar charts
makebar(avg_change_data, 'e1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'e2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[109]:

# Anderson
neg_combined = (calc_ubiall.records.combined - calc_base.records.combined)
((neg_combined[neg_combined < 0] * calc_ubiall.records.s006[neg_combined < 0]).sum() /
 calc_ubi18.records.s006[neg_combined < 0].sum())


# In[110]:

# MTR Plots
# mtr_ubi18 = utils.mtr_graph_data(calc_base, calc_ubi18)
# mtr_ubi18_plot = utils.xtr_graph_plot(mtr_ubi18)
# show(mtr_ubi18_plot)


# In[111]:

# mtrs_ubi18 = utils.mtr_graph_data(calc_base, calc_ubi18, mars=2, mtr_variable='e00200s')
# mtrs_ubi18_plot = utils.xtr_graph_plot(mtrs_ubi18)
# show(mtrs_ubi18_plot)


# In[112]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi18, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'e3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi18, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'e4')


# In[113]:

mtr_macros(calc_ubi18, sec = 'e')


# In[114]:

# Primary earner's MTR Change
mtrp_ubidf18 = pd.DataFrame()
mtrp_ubidf18['c00100'] = calc_ubi18.records.c00100
mtrp_ubidf18['s006'] = calc_ubi18.records.s006
mtrp_ubidf18['mtr'] = calc_ubi18.mtr()[2]
mtrp_ubidf18['1 - mtr'] = 1. - mtrp_ubidf18['mtr']
mtrp_ubidf18['pct change'] = ((mtrp_ubidf18['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_ubidf18 = utils.add_weighted_income_bins(mtrp_ubidf18, num_bins=100, income_measure='c00100')
mtrp_ubi18 = mtrp_ubidf18.groupby('bins')
mtr1ubi18 = mtrp_ubi18.apply(utils.weighted_mean, 'pct change')
agi = mtrp_ubi18.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_ubi18.apply(utils.weighted_mean, 's006')

lines_ubi18 = pd.DataFrame()
lines_ubi18['primary'] = mtr1ubi18
lines_ubi18['avg-agi'] = agi
lines_ubi18['s006'] = s006


# In[115]:

# Secondary earner
mtrs_ubi18_df = pd.DataFrame()
mtrs_ubi18_df['c00100'] = calc_ubi18.records.c00100
mtrs_ubi18_df['s006'] = calc_ubi18.records.s006
mtrs_ubi18_df['MARS'] = calc_ubi18.records.MARS
mtrs_ubi18_df['mtr'] = calc_ubi18.mtr('e00200s')[2]
mtrs_ubi18_df = mtrs_ubi18_df[mtrs_ubi18_df['MARS'] == 2]
mtrs_ubi18_df['1 - mtr'] = 1. - mtrs_ubi18_df['mtr']
mtrs_ubi18_df['pct change'] = ((mtrs_ubi18_df['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_ubi18_df = utils.add_weighted_income_bins(mtrs_ubi18_df, num_bins=100, income_measure='c00100')
mtrs_ubi18 = mtrs_ubi18_df.groupby('bins')
mtr2ubi18 = mtrs_ubi18.apply(utils.weighted_mean, 'pct change')
lines_ubi18['secondary'] = mtr2ubi18


# In[116]:

# generate dataframe for graph
lines_ubi18['bins'] = lines_ubi18.index
del lines_ubi18.index.name

plines = lines_ubi18['primary'].values
slines = lines_ubi18['secondary'].values
agi = lines_ubi18['avg-agi'].values
s006 = lines_ubi18['s006'].values
idlines = lines_ubi18.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[117]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[118]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'e5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)  

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[119]:

plines_ubi18 = lines_ubi18['primary'].values
slines_ubi18 = lines_ubi18['secondary'].values
idlines_ubi18 = lines_ubi18.index.values


# In[120]:

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_ubi18, plines_ubi18, legend='Primary Earner')
fig.line(idlines_ubi18, slines_ubi18, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# ## Section 7, Part F: Tax, Welfare/Transfer, and UBI for 21+

# Tax and welfare/transfer reform, plus a UBI for all over 21

# In[121]:

# Function to determine UBI levels
def ubi_amt21(revenue):
    ubi_a21 = revenue / abv21
    return ubi_a21


# In[122]:

ubi_a21 = ubi_amt21(revenue)
print ('UBI for those above 21: {:.2f}'.format(ubi_a21))


# In[123]:

# define macros
def_macro('UBI for those above 21 (part F)', '\${:,.2f}'.format(ubi_18), 'fuog')


# In[124]:

# UBI above 21 Calculator - Initial UBI tax revenue
recs_ubi_21 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_21 = Policy()
pol_ubi_21.implement_reform(tax_reform)
ubi_reform_21 = {
    2014: {
        '_UBI2': [ubi_a21],
        '_UBI3': [ubi_a21]
    }
}
pol_ubi_21.implement_reform(ubi_reform_all)
calc_ubi_21 = Calculator(records=recs_ubi_21, policy=pol_ubi_21, verbose=False)
calc_ubi_21.records.e02400 = np.zeros(len(calc_ubi_21.records.e02400))
calc_ubi_21.advance_to_year(2014)
calc_ubi_21.calc_all()

# Initial UBI tax revenue
ubi_tax_rev21 = ((calc_ubi_21.records.combined - calc_tax.records.combined) * calc_ubi_21.records.s006).sum()
ubi_tax_rev21


# In[125]:

def_macro('Tax revenue from UBI for those above 21 (part F)', '\${:,.2f}'.format(ubi_tax_rev21), 'futg')


# In[126]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finder21(ubi_a21):
    # Build a calculator with the specified UBI levels
    recs_finder21 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finder21 = Policy()
    pol_finder21.implement_reform(tax_reform)
    ubi_finder_reform21 = {
        2014: {
            '_UBI3': [ubi_a21]
        }
    }
    pol_finder21.implement_reform(ubi_finder_reform21)
    calc_finder21 = Calculator(records=recs_finder21, policy=pol_finder21, verbose=False)
    calc_finder21.records.e02400 = np.zeros(len(calc_finder21.records.e02400))
    calc_finder21.advance_to_year(2014)
    calc_finder21.calc_all()
    # Revenue from tax reform
    ubi_tax_rev21 = ((calc_finder21.records.combined - calc_tax.records.combined) * calc_finder21.records.s006).sum()
    total_rev21 = ubi_tax_rev21 + revenue
    ubi21 = (calc_finder21.records.ubi * calc_finder21.records.s006).sum()
    diff21 = ubi21 - total_rev21
    return diff21, ubi_tax_rev21


# In[127]:

# While loop to call ubi_finder function until optimal UBI is found
diff21 = 9e99
prev_ubi_tax_rev21 = ubi_tax_rev21
while abs(diff21) >= 0.01:
    ubi_a21 = ubi_amt21(revenue + ubi_tax_rev21)
    diff21, ubi_tax_rev21 = ubi_finder21(ubi_a21)
    if diff21 > 0:
        ubi_tax_rev21 = prev_ubi_tax_rev21 * 0.5
    prev_ubi_tax_rev21 = ubi_tax_rev21
print (ubi_a21)


# In[128]:

# Create calc for UBI simulations
recs_ubi21 = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi21 = Policy()
pol_ubi21.implement_reform(tax_reform)
ubi21_reform = {
    2013: {
        '_UBI3': [ubi_a21]
    }
}
pol_ubi21.implement_reform(ubi21_reform)
calc_ubi21 = Calculator(records=recs_ubi21, policy=pol_ubi21, verbose=False)
calc_ubi21.records.e02400 = np.zeros(len(calc_ubi21.records.e02400))
calc_ubi21.advance_to_year(2014)
calc_ubi21.calc_all()


# In[129]:

diff_ubi21 = create_difference_table(calc_base.records, calc_ubi21.records, 'weighted_deciles',
                                           income_to_present='combined')
diff_ubi21


# In[130]:

f1_df = restricted_table(diff_ubi21, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'f1_df',
                  reindex = True
                )
f1_df


# In[131]:

# make macros for top and bottom ten percent
dist_macro(f1_df, 'f')


# In[132]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubi21.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubi21.records.s006[neg_combined < 0]).sum() /
calc_ubi21.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubi21.records.ubi[neg_combined < 0] * calc_ubi21.records.s006[neg_combined < 0]).sum() /
calc_ubi21.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part F)', units(stat1), 'fatd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part F)', units(stat2), 'fasd')
def_macro('Average UBI to those who see tax decrease with UBI (part F)', units(stat3), 'faud')


# In[133]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diff_ubi21['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diff_ubi21['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[134]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diff_ubi21['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diff_ubi21['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[135]:

# generate bar charts
makebar(avg_change_data, 'f1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'f2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[136]:

# MTR Plots
# mtr_ubi21 = utils.mtr_graph_data(calc_base, calc_ubi21)
# mtr_ubi21_plot = utils.xtr_graph_plot(mtr_ubi21)
# show(mtr_ubi21_plot)


# In[137]:

# mtrs_ubi21 = utils.mtr_graph_data(calc_base, calc_ubi21, mars=2, mtr_variable='e00200s')
# mtrs_ubi21_plot = utils.xtr_graph_plot(mtrs_ubi21)
# show(mtrs_ubi21_plot)


# In[138]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi21, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'f3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi21, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'f4')


# In[139]:

mtr_macros(calc_ubi21, sec = 'f')


# In[140]:

# Primary earner's MTR Change
mtrp_ubidf21 = pd.DataFrame()
mtrp_ubidf21['c00100'] = calc_ubi21.records.c00100
mtrp_ubidf21['s006'] = calc_ubi21.records.s006
mtrp_ubidf21['mtr'] = calc_ubi21.mtr()[2]
mtrp_ubidf21['1 - mtr'] = 1. - mtrp_ubidf21['mtr']
mtrp_ubidf21['pct change'] = ((mtrp_ubidf21['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_ubidf21 = utils.add_weighted_income_bins(mtrp_ubidf21, num_bins=100, income_measure='c00100')
mtrp_ubi21 = mtrp_ubidf21.groupby('bins')
mtr1ubi21 = mtrp_ubi21.apply(utils.weighted_mean, 'pct change')
agi = mtrp_ubi21.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_ubi21.apply(utils.weighted_mean, 's006')

lines_ubi21 = pd.DataFrame()
lines_ubi21['primary'] = mtr1ubi21
lines_ubi21['avg-agi'] = agi
lines_ubi21['s006'] = s006


# In[141]:

# Secondary earner
mtrs_ubi21_df = pd.DataFrame()
mtrs_ubi21_df['c00100'] = calc_ubi21.records.c00100
mtrs_ubi21_df['s006'] = calc_ubi21.records.s006
mtrs_ubi21_df['MARS'] = calc_ubi21.records.MARS
mtrs_ubi21_df['mtr'] = calc_ubi21.mtr('e00200s')[2]
mtrs_ubi21_df = mtrs_ubi21_df[mtrs_ubi21_df['MARS'] == 2]
mtrs_ubi21_df['1 - mtr'] = 1. - mtrs_ubi21_df['mtr']
mtrs_ubi21_df['pct change'] = ((mtrs_ubi21_df['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_ubi21_df = utils.add_weighted_income_bins(mtrs_ubi21_df, num_bins=100, income_measure='c00100')
mtrs_ubi21 = mtrs_ubi21_df.groupby('bins')
mtr2ubi21 = mtrs_ubi21.apply(utils.weighted_mean, 'pct change')
lines_ubi21['secondary'] = mtr2ubi21


# In[142]:

# generate dataframe for graph
lines_ubi21['bins'] = lines_ubi21.index
del lines_ubi21.index.name

plines = lines_ubi21['primary'].values
slines = lines_ubi21['secondary'].values
agi = lines_ubi21['avg-agi'].values
s006 = lines_ubi21['s006'].values
idlines = lines_ubi21.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[143]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[144]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'f5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Avg. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)   

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[145]:

plines_ubi21 = lines_ubi21['primary'].values
slines_ubi21 = lines_ubi21['secondary'].values
idlines_ubi21 = lines_ubi21.index.values


# In[146]:

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_ubi21, plines_ubi21, legend='Primary Earner')
fig.line(idlines_ubi21, slines_ubi21, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# In[147]:

# Find UBI benefit, net tax increase
combined_change = calc_ubi21.records.combined - calc_base.records.combined
net_benefit = calc_ubi21.records.ubi - combined_change

# DataFrame that will be sorted and holds net benefit, weight, and AGI
net_ben_df = pd.DataFrame()
net_ben_df['net benefit'] = net_benefit
net_ben_df['c00100'] = calc_ubi21.records.c00100
net_ben_df['s006'] = calc_ubi21.records.s006
net_ben_df = utils.add_weighted_income_bins(net_ben_df, num_bins=10, income_measure='c00100')


# # Dynamic Simulations

# In[148]:

# Behavioral reform to be used for all calculators
behavioral_reform = {
    2014: {
        '_BE_inc': [-0.05],
        '_BE_sub': [0.24]
    }
}


# In[149]:

# Tax reform dynamic calculator
recs_tax_d = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_tax_d = Policy()
pol_tax_d.implement_reform(tax_reform)
behavior_tax_d = Behavior()
behavior_tax_d.update_behavior(behavioral_reform)
calc_tax_d = Calculator(records=recs_tax_d, policy=pol_tax_d, behavior=behavior_tax_d, verbose=False)
calc_tax_d.advance_to_year(2014)
calc_tax_d.calc_all()


# In[150]:

# Get change in tax revenue for dynamic reform
calc_dynamic = Behavior.response(calc_base, calc_tax_d)


# In[151]:

# Find dynamic tax revenue
dynamic_tax_rev = ((calc_dynamic.records.combined - calc_base.records.combined) * calc_dynamic.records.s006).sum()
dynamic_tax_rev


# In[152]:

dynamic_rev = dynamic_tax_rev + welfare_repeal


# ## Section 8, Part G: Tax, Welfare/Transfer, and UBI for All - Dynamic

# Tax and welfare reform plus a dynamic simulation of UBI for all

# In[153]:

# Function to determine UBI levels
def ubi_amtd(revenue):
    ubi_18b = revenue / ((u18 * 0.5) + abv18)
    ubi_u18b = ubi_18b * 0.5
    return ubi_18b, ubi_u18b


# In[154]:

initial_ubid = ubi_amtd(dynamic_rev)
ubi_u18d = initial_ubid[1]
ubi_18d = initial_ubid[0]
print ('UBI for those above 18: {:.2f}'.format(ubi_18d))
print ('UBI for those bellow 18: {:.2f}'.format(ubi_u18d))


# In[155]:

# define macros
def_macro('UBI for those above 18 (part G)', '\${:,.2f}'.format(ubi_18d), 'guag')
def_macro('UBI for those bellow 18 (part G)', '\${:,.2f}'.format(ubi_u18d), 'gubg')


# In[156]:

# UBI all Calculator - Initial UBI tax revenue - behavioral reform
recs_ubi_allb = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_allb = Policy()
pol_ubi_allb.implement_reform(tax_reform)
ubi_reform_allb = {
    2014: {
        '_UBI1': [ubi_u18d],
        '_UBI2': [ubi_18d],
        '_UBI3': [ubi_18d]
    }
}
pol_ubi_allb.implement_reform(ubi_reform_all)
# Behavioral reform
behavior_all = Behavior()
behavior_all.update_behavior(behavioral_reform)

calc_ubi_allb = Calculator(records=recs_ubi_allb, policy=pol_ubi_allb, behavior=behavior_all,
                           verbose=False)
calc_ubi_allb.records.e02400 = np.zeros(len(calc_ubi_allb.records.e02400))
calc_ubi_allb.advance_to_year(2014)
calc_ubi_allb.calc_all()

calc_dynamic_all = Behavior.response(calc_dynamic, calc_ubi_allb)

# Initial UBI tax revenue
ubi_tax_revb = ((calc_dynamic_all.records.combined - calc_dynamic.records.combined) * calc_dynamic_all.records.s006).sum()
ubi_tax_revb


# In[157]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finderb(ubi_18b, ubi_u18b):
    # Build a calculator with the specified UBI levels
    recs_finderb = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finderb = Policy()
    pol_finderb.implement_reform(tax_reform)
    ubi_finder_reformb = {
        2014: {
            '_UBI1': [ubi_u18b],
            '_UBI2': [ubi_18b],
            '_UBI3': [ubi_18b]
        }
    }
    pol_finderb.implement_reform(ubi_finder_reformb)
    # Behavioral reform
    behavior_finder = Behavior()
    behavior_finder.update_behavior(behavioral_reform)
    
    calc_finderb = Calculator(records=recs_finderb, policy=pol_finderb, behavior=behavior_finder,
                              verbose=False)
    calc_finderb.records.e02400 = np.zeros(len(calc_finderb.records.e02400))
    calc_finderb.advance_to_year(2014)
    calc_finderb.calc_all()
    
    calc_dynamic_finder = Behavior.response(calc_base, calc_finderb)

    # Revenue from tax reform
    ubi_tax_revb = ((calc_dynamic_finder.records.combined - calc_dynamic.records.combined) *
                     calc_dynamic_finder.records.s006).sum()
    total_revb = ubi_tax_revb + dynamic_rev
    ubib = (calc_dynamic_finder.records.ubi * calc_dynamic_finder.records.s006).sum()
    diffb = ubib - total_revb
    return diffb, ubi_tax_revb


# In[158]:

# While loop to call ubi_finder function until optimal UBI is found
diffb = 9e99
prev_ubi_tax_revb = ubi_tax_revb
while abs(diffb) >= 100:
    ubi_18b, ubi_u18b = ubi_amtd(dynamic_rev + ubi_tax_revb)
    diffb, ubi_tax_revb = ubi_finderb(ubi_18b, ubi_u18b)
    if diffb > 0:
        ubi_tax_revb = prev_ubi_tax_revb * .97
    prev_ubi_tax_revb = ubi_tax_revb
print (ubi_18b, ubi_u18b)
print ('Remaining Revenue: {:.2f}'.format(diffb))


# In[159]:

# Dynamic UBI calculator - UBI for all
recs_ubi18d = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi18d = Policy()
pol_ubi18d.implement_reform(tax_reform)
ubi_reform_18d = {
    2014: {
        '_UBI1': [ubi_u18b],
        '_UBI2': [ubi_18b],
        '_UBI3': [ubi_18b]
    }
}
pol_ubi18d.implement_reform(ubi_reform_18d)
behavior_ubi18d = Behavior()
behavior_ubi18d.update_behavior(behavioral_reform)
calc_ubi18d = Calculator(records=recs_ubi18d, policy=pol_ubi18d, behavior=behavior_ubi18d, verbose=False)
calc_ubi18d.records.e02400 = np.zeros(len(calc_ubi18d.records.e02400))
calc_ubi18d.advance_to_year(2014)
calc_ubi18d.calc_all()

dynamic_all = Behavior.response(calc_base, calc_ubi18d)


# In[160]:

diff_dynamic_all = create_difference_table(calc_base.records, dynamic_all.records, groupby='weighted_deciles',
                                                 income_to_present='combined')
diff_dynamic_all


# In[161]:

g1_df = restricted_table(diff_dynamic_all, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'g1_df', 
                  reindex = True
                )
g1_df


# In[162]:

# make macros for top and bottom ten percent
dist_macro(g1_df, 'g')


# In[163]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubi18d.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubi18d.records.s006[neg_combined < 0]).sum() /
calc_ubi18d.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubi18d.records.ubi[neg_combined < 0] * calc_ubi18d.records.s006[neg_combined < 0]).sum() /
calc_ubi18d.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part G)', units(stat1), 'gatd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part G)', units(stat2), 'gasd')
def_macro('Average UBI to those who see tax decrease with UBI (part G)', units(stat3), 'gaud')


# In[164]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diff_dynamic_all['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diff_dynamic_all['avg-agi']


avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[165]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diff_dynamic_all['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diff_dynamic_all['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[166]:

# generate bar charts
makebar(avg_change_data, 'g1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'g2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[167]:

# Primary earner MTR
# dynamic_mtrp_all = utils.mtr_graph_data(calc_base, dynamic_all)
# dynamic_plot_all = utils.xtr_graph_plot(dynamic_mtrp_all)
# show(dynamic_plot_all)

# Secondary earner MTR
# dynamic_mtrs_all = utils.mtr_graph_data(calc_base, dynamic_all, mars=2, mtr_variable='e00200s')
# dynamic_plot_alls = utils.xtr_graph_plot(dynamic_mtrs_all)
# show(dynamic_plot_alls)


# In[168]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi_allb, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'g3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi_allb, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'g4')


# In[169]:

mtr_macros(calc_ubi_allb, sec = 'g')


# In[170]:

# Primary earner's MTR Change
mtrp_dynamic_all = pd.DataFrame()
mtrp_dynamic_all['c00100'] = dynamic_all.records.c00100
mtrp_dynamic_all['s006'] = dynamic_all.records.s006
mtrp_dynamic_all['mtr'] = dynamic_all.mtr()[2]
mtrp_dynamic_all['1 - mtr'] = 1. - mtrp_dynamic_all['mtr']
mtrp_dynamic_all['pct change'] = ((mtrp_dynamic_all['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_dynamic_all = utils.add_weighted_income_bins(mtrp_dynamic_all, num_bins=100, income_measure='c00100')
mtrp_dynamic_allg = mtrp_dynamic_all.groupby('bins')
mtr1dynamicall = mtrp_dynamic_allg.apply(utils.weighted_mean, 'pct change')
agi = mtrp_.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_.apply(utils.weighted_mean, 's006')

lines_dynamic_all = pd.DataFrame()
lines_dynamic_all['primary'] = mtr1dynamicall
lines_dynamic_all['avg-agi'] = agi
lines_dynamic_all['s006'] = s006


# In[171]:

# Secondary earner
mtrs_dynamic_all = pd.DataFrame()
mtrs_dynamic_all['c00100'] = dynamic_all.records.c00100
mtrs_dynamic_all['s006'] = dynamic_all.records.s006
mtrs_dynamic_all['MARS'] = dynamic_all.records.MARS
mtrs_dynamic_all['mtr'] = dynamic_all.mtr('e00200s')[2]
mtrs_dynamic_all = mtrs_dynamic_all[mtrs_dynamic_all['MARS'] == 2]
mtrs_dynamic_all['1 - mtr'] = 1. - mtrs_dynamic_all['mtr']
mtrs_dynamic_all['pct change'] = ((mtrs_dynamic_all['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_dynamic_all = utils.add_weighted_income_bins(mtrs_dynamic_all, num_bins=100, income_measure='c00100')
mtrs_dynamicall = mtrs_dynamic_all.groupby('bins')
mtr2dynamicall = mtrs_dynamicall.apply(utils.weighted_mean, 'pct change')
lines_dynamic_all['secondary'] = mtr2dynamicall


# In[172]:

# generate dataframe for graph
lines_dynamic_all['bins'] = lines_dynamic_all.index
del lines_dynamic_all.index.name

plines = lines_dynamic_all['primary'].values
slines = lines_dynamic_all['secondary'].values
agi = lines_dynamic_all['avg-agi'].values
s006 = lines_dynamic_all['s006'].values
idlines = lines_dynamic_all.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[173]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[174]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'g5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)       

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[175]:

plines_dynamic_all = lines_dynamic_all['primary'].values
slines_dynamic_all = lines_dynamic_all['secondary'].values
idlines_dynamic_all = lines_dynamic_all.index.values

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_dynamic_all, plines_dynamic_all, legend='Primary Earner')
fig.line(idlines_dynamic_all, slines_dynamic_all, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# ## Section 9, Part H: Tax, Welfare/Transfer, and UBI 18+ - Dynamic

# Tax and welfare reform plus a UBI for all those above 18 - dynamic

# In[176]:

# Function to determine UBI levels
def ubi_amt18d(revenue):
    ubi_18d = revenue / abv18
    return ubi_18d


# In[177]:

# Initial UBI
ubi_18d = ubi_amt18d(dynamic_rev)
print ('UBI for those above 18: {:.2f}'.format(ubi_18d))


# In[178]:

# define macros
def_macro('UBI for those above 18 (part H)', '\${:,.2f}'.format(ubi_18d), 'huog')


# In[179]:

# UBI all Calculator - Initial UBI tax revenue - behavioral reform
recs_ubi_18b = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_18b = Policy()
pol_ubi_18b.implement_reform(tax_reform)
ubi_reform_18b = {
    2014: {
        '_UBI2': [ubi_18b],
        '_UBI3': [ubi_18b]
    }
}
pol_ubi_18b.implement_reform(ubi_reform_all)
# Behavioral reform
behavior18 = Behavior()
behavior18.update_behavior(behavioral_reform)

calc_ubi_18b = Calculator(records=recs_ubi_18b, policy=pol_ubi_18b, behavior=behavior18,
                           verbose=False)
calc_ubi_18b.records.e02400 = np.zeros(len(calc_ubi_18b.records.e02400))
calc_ubi_18b.advance_to_year(2014)
calc_ubi_18b.calc_all()

calc_dynamic_18 = Behavior.response(calc_base, calc_ubi_18b)

# Initial UBI tax revenue
ubi_tax_revb = ((calc_dynamic_18.records.combined - calc_dynamic.records.combined) * calc_dynamic_18.records.s006).sum()
ubi_tax_revb


# In[180]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finderb(ubi_18b):
    # Build a calculator with the specified UBI levels
    recs_finderb = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finderb = Policy()
    pol_finderb.implement_reform(tax_reform)
    ubi_finder_reformb = {
        2014: {
            '_UBI2': [ubi_18b],
            '_UBI3': [ubi_18b]
        }
    }
    pol_finderb.implement_reform(ubi_finder_reformb)
    # Behavioral reform
    behavior_finder = Behavior()
    behavior_finder.update_behavior(behavioral_reform)
    
    calc_finderb = Calculator(records=recs_finderb, policy=pol_finderb, behavior=behavior_finder,
                              verbose=False)
    calc_finderb.records.e02400 = np.zeros(len(calc_finderb.records.e02400))
    calc_finderb.advance_to_year(2014)
    calc_finderb.calc_all()
    
    calc_dynamic_finder = Behavior.response(calc_base, calc_finderb)

    # Revenue from tax reform
    ubi_tax_revb = ((calc_dynamic_finder.records.combined - calc_dynamic.records.combined) *
                     calc_dynamic_finder.records.s006).sum()
    total_revb = ubi_tax_revb + dynamic_rev
    ubib = (calc_dynamic_finder.records.ubi * calc_dynamic_finder.records.s006).sum()
    diffb = ubib - total_revb
    return diffb, ubi_tax_revb


# In[181]:

# While loop to call ubi_finder function until optimal UBI is found
diffb = 9e99
prev_ubi_tax_revb = ubi_tax_revb
while abs(diffb) >= 100:
    ubi_18b = ubi_amt18d(dynamic_rev + ubi_tax_revb)
    diffb, ubi_tax_revb = ubi_finderb(ubi_18b)
    if diffb > 0:
        ubi_tax_revb = prev_ubi_tax_revb * .97
    prev_ubi_tax_revb = ubi_tax_revb
print (ubi_18b)


# In[182]:

# Dynamic UBI calculator - UBI for 18+
recs_ubi18d = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi18d = Policy()
pol_ubi18d.implement_reform(tax_reform)
ubi_reform_18d = {
    2014: {
        '_UBI2': [ubi_18b],
        '_UBI3': [ubi_18b]
    }
}
pol_ubi18d.implement_reform(ubi_reform_18d)
behavior_ubi18d = Behavior()
behavior_ubi18d.update_behavior(behavioral_reform)
calc_ubi18d = Calculator(records=recs_ubi18d, policy=pol_ubi18d, behavior=behavior_ubi18d, verbose=False)
calc_ubi18d.records.e02400 = np.zeros(len(calc_ubi18d.records.e02400))
calc_ubi18d.advance_to_year(2014)
calc_ubi18d.calc_all()

dynamic_18 = Behavior.response(calc_base, calc_ubi18d)


# In[183]:

diff_dynamic_18 = create_difference_table(calc_base.records, dynamic_18.records, groupby='weighted_deciles',
                                                income_to_present='combined')
diff_dynamic_18


# In[184]:

h1_df = restricted_table(diff_dynamic_18, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'h1_df', 
                 reindex = True
                )


# In[185]:

# make macros for top and bottom ten percent
dist_macro(h1_df, 'h')


# In[186]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubi18d.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubi18d.records.s006[neg_combined < 0]).sum() /
calc_ubi18d.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubi18d.records.ubi[neg_combined < 0] * calc_ubi18d.records.s006[neg_combined < 0]).sum() /
calc_ubi18d.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part H)', units(stat1), 'hatd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part H)', units(stat2), 'hasd')
def_macro('Average UBI to those who see tax decrease with UBI (part H)', units(stat3), 'haud')


# In[187]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diff_dynamic_18['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diff_dynamic_18['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[188]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diff_dynamic_18['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diff_dynamic_18['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[189]:

# generate bar charts
makebar(avg_change_data, 'h1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'h2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[190]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi18d, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'h3')

# average secondary earner MTR change by percentile of AGI
makeline(calc_base, 
         calc_ubi18d, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'h4')


# In[191]:

mtr_macros(calc_ubi18d, sec = 'h')


# In[192]:

# Primary earner's MTR Change
mtrp_dynamic_18 = pd.DataFrame()
mtrp_dynamic_18['c00100'] = dynamic_18.records.c00100
mtrp_dynamic_18['s006'] = dynamic_18.records.s006
mtrp_dynamic_18['mtr'] = dynamic_18.mtr()[2]
mtrp_dynamic_18['1 - mtr'] = 1. - mtrp_dynamic_18['mtr']
mtrp_dynamic_18['pct change'] = ((mtrp_dynamic_18['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_dynamic_18 = utils.add_weighted_income_bins(mtrp_dynamic_18, num_bins=100, income_measure='c00100')
mtrp_dynamic_18g = mtrp_dynamic_18.groupby('bins')
mtr1dynamic18 = mtrp_dynamic_18g.apply(utils.weighted_mean, 'pct change')
agi = mtrp_dynamic_18g.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_dynamic_18g.apply(utils.weighted_mean, 's006')

lines_dynamic_18 = pd.DataFrame()
lines_dynamic_18['primary'] = mtr1dynamic18
lines_dynamic_18['avg-agi'] = agi
lines_dynamic_18['s006'] = s006


# In[193]:

# Secondary earner
mtrs_dynamic_18 = pd.DataFrame()
mtrs_dynamic_18['c00100'] = dynamic_18.records.c00100
mtrs_dynamic_18['s006'] = dynamic_18.records.s006
mtrs_dynamic_18['MARS'] = dynamic_18.records.MARS
mtrs_dynamic_18['mtr'] = dynamic_18.mtr('e00200s')[2]
mtrs_dynamic_18 = mtrs_dynamic_18[mtrs_dynamic_18['MARS'] == 2]
mtrs_dynamic_18['1 - mtr'] = 1. - mtrs_dynamic_18['mtr']
mtrs_dynamic_18['pct change'] = ((mtrs_dynamic_18['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_dynamic_18 = utils.add_weighted_income_bins(mtrs_dynamic_18, num_bins=100, income_measure='c00100')
mtrs_dynamic18 = mtrs_dynamic_18.groupby('bins')
mtr2dynamic18 = mtrs_dynamic18.apply(utils.weighted_mean, 'pct change')
lines_dynamic_18['secondary'] = mtr2dynamic18


# In[194]:

# generate dataframe for graph
lines_dynamic_18['bins'] = lines_dynamic_18.index
del lines_dynamic_18.index.name

plines = lines_dynamic_18['primary'].values
slines = lines_dynamic_18['secondary'].values
agi = lines_dynamic_18['avg-agi'].values
s006 = lines_dynamic_18['s006'].values
idlines = lines_dynamic_18.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[195]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[196]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'h5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[197]:

plines_dynamic_18 = lines_dynamic_18['primary'].values
slines_dynamic_18 = lines_dynamic_18['secondary'].values
idlines_dynamic_18 = lines_dynamic_18.index.values

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_dynamic_18, plines_dynamic_18, legend='Primary Earner')
fig.line(idlines_dynamic_18, slines_dynamic_18, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
show(fig)


# ## Section 10, Part I: Tax, Welfare/Transer, and UBI 21+ - Dynamic

# Tax and welfare reform along with a UBI for all those above 21 - dynamic

# In[198]:

# Function to determine UBI levels
def ubi_amt21d(revenue):
    ubi_21d = revenue / abv21
    return ubi_21d


# In[199]:

# Initial UBI
ubi_21d = ubi_amt21d(dynamic_rev)
print ('UBI for those above 21: {:.2f}'.format(ubi_21d))


# In[200]:

# define macros
def_macro('UBI for those above 21 (part I)', '\${:,.2f}'.format(ubi_21d), 'iuog')


# In[201]:

# UBI all Calculator - Initial UBI tax revenue - behavioral reform
recs_ubi_21b = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi_21b = Policy()
pol_ubi_21b.implement_reform(tax_reform)
ubi_reform_21b = {
    2014: {
        '_UBI3': [ubi_21d]
    }
}
pol_ubi_21b.implement_reform(ubi_reform_all)
# Behavioral reform
behavior21 = Behavior()
behavior21.update_behavior(behavioral_reform)

calc_ubi_21b = Calculator(records=recs_ubi_21b, policy=pol_ubi_21b, behavior=behavior21,
                           verbose=False)
calc_ubi_21b.records.e02400 = np.zeros(len(calc_ubi_21b.records.e02400))
calc_ubi_21b.advance_to_year(2014)
calc_ubi_21b.calc_all()

calc_dynamic_21 = Behavior.response(calc_base, calc_ubi_21b)

# Initial UBI tax revenue
ubi_tax_revb = ((calc_dynamic_21.records.combined - calc_dynamic.records.combined) * calc_dynamic_21.records.s006).sum()
ubi_tax_revb


# In[202]:

# Function to find total UBI and compare to additional revenue from tax and welfare reform
def ubi_finderb(ubi_21b):
    # Build a calculator with the specified UBI levels
    recs_finderb = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
    pol_finderb = Policy()
    pol_finderb.implement_reform(tax_reform)
    ubi_finder_reformb = {
        2014: {
            '_UBI3': [ubi_21b]
        }
    }
    pol_finderb.implement_reform(ubi_finder_reformb)
    # Behavioral reform
    behavior_finder = Behavior()
    behavior_finder.update_behavior(behavioral_reform)
    
    calc_finderb = Calculator(records=recs_finderb, policy=pol_finderb, behavior=behavior_finder,
                              verbose=False)
    calc_finderb.records.e02400 = np.zeros(len(calc_finderb.records.e02400))
    calc_finderb.advance_to_year(2014)
    calc_finderb.calc_all()
    
    calc_dynamic_finder = Behavior.response(calc_base, calc_finderb)

    # Revenue from tax reform
    ubi_tax_revb = ((calc_dynamic_finder.records.combined - calc_dynamic.records.combined) *
                     calc_dynamic_finder.records.s006).sum()
    total_revb = ubi_tax_revb + dynamic_rev
    ubib = (calc_dynamic_finder.records.ubi * calc_dynamic_finder.records.s006).sum()
    diffb = ubib - total_revb
    return diffb, ubi_tax_revb


# In[203]:

# While loop to call ubi_finder function until optimal UBI is found
diffb = 9e99
prev_ubi_tax_revb = ubi_tax_revb
while abs(diffb) >= 100:
    ubi_21b = ubi_amt21d(dynamic_rev + ubi_tax_revb)
    diffb, ubi_tax_revb = ubi_finderb(ubi_21b)
    if diffb > 0:
        ubi_tax_revb = prev_ubi_tax_revb * .97
    prev_ubi_tax_revb = ubi_tax_revb
print (ubi_21b)


# In[204]:

# Dynamic UBI calculator - UBI for 21+
recs_ubi21d = Records('puf_benefits.csv', weights='puf_weights_new.csv', adjust_ratios='puf_ratios copy.csv')
pol_ubi21d = Policy()
pol_ubi21d.implement_reform(tax_reform)
ubi_reform_21d = {
    2014: {
        '_UBI3': [ubi_21b]
    }
}
pol_ubi21d.implement_reform(ubi_reform_21d)
behavior_ubi21d = Behavior()
behavior_ubi21d.update_behavior(behavioral_reform)
calc_ubi21d = Calculator(records=recs_ubi21d, policy=pol_ubi21d, behavior=behavior_ubi21d, verbose=False)
calc_ubi21d.records.e02400 = np.zeros(len(calc_ubi21d.records.e02400))
calc_ubi21d.advance_to_year(2014)
calc_ubi21d.calc_all()

dynamic_21 = Behavior.response(calc_base, calc_ubi21d)


# In[205]:

diff_dynamic_21 = create_difference_table(calc_base.records, dynamic_21.records, groupby='weighted_deciles',
                                                income_to_present='combined')
diff_dynamic_21


# In[206]:

i1_df = restricted_table(diff_dynamic_21, 
                 ['tot_change', 'mean', 'perc_inc', 'share_of_change'], 
                 ['Total Change ($)', 'Average Change ($)', 'Increase (%)', 'Share of Change (%)'],
                 'i1_df', 
                  reindex = True
                )


# In[207]:

# make macros for top and bottom ten percent
dist_macro(i1_df, 'i')


# In[208]:

# Average Social Security from people with falling tax liabilities

# Average tax liability decrease for those who see it
neg_combined = (calc_ubi21d.records.combined - calc_base.records.combined)
stat1 = ((neg_combined[neg_combined < 0] * calc_ubi21d.records.s006[neg_combined < 0]).sum() /
calc_ubi21d.records.s006[neg_combined < 0].sum())

# Average Social Security benefit to those who see tax decrease with UBI
stat2 = ((calc_base.records.e02400[neg_combined < 0] * calc_base.records.s006[neg_combined < 0]).sum() /
calc_base.records.s006[neg_combined < 0].sum())

# Average UBI to those who see tax decrease with UBI
stat3 = ((calc_ubi21d.records.ubi[neg_combined < 0] * calc_ubi21d.records.s006[neg_combined < 0]).sum() /
calc_ubi21d.records.s006[neg_combined < 0].sum())

def_macro('Average tax liability decrease for those who see it (part I)', units(stat1), 'iatd')
def_macro('Average Social Security benefit to those who see tax decrease with UBI (part I)', units(stat2), 'iasd')
def_macro('Average UBI to those who see tax decrease with UBI (part I)', units(stat3), 'iaud')


# In[209]:

avg_change_data = pd.DataFrame()
avg_change_data['Benefit Loss'] = diff_dynamic_21['mean'].drop('sums')
avg_change_data['Income Percentile'] = agi_bins
avg_change_data['Average AGI'] = diff_dynamic_21['avg-agi']

avg_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
avg_change_data = avg_change_data.set_index(avg_change_data['Income Bins'])
avg_change_data = avg_change_data.drop('Income Bins', 1)
del avg_change_data.index.name


# In[210]:

tot_change_data = pd.DataFrame()
tot_change_data['Benefit Loss'] = diff_dynamic_21['tot_change'].drop('sums') * in_billions
tot_change_data['Income Percentile'] = agi_bins
tot_change_data['Average AGI'] = diff_dynamic_21['avg-agi']

tot_change_data['Income Bins'] = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']                      
tot_change_data = tot_change_data.set_index(tot_change_data['Income Bins'])
tot_change_data = tot_change_data.drop('Income Bins', 1)
del tot_change_data.index.name


# In[211]:

# generate bar charts
makebar(avg_change_data, 'i1', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Average Change in Tax Liability')
makebar(tot_change_data, 'i2', x1label = 'AGI Percentile', x2label = 'Average AGI by Percentile', ylabel = 'Total Change in Tax Liability (billions)')


# In[212]:

# Primary earner MTR
# dynamic_mtrp_21 = utils.mtr_graph_data(calc_base, dynamic_21)
# dynamic_plot_21 = utils.xtr_graph_plot(dynamic_mtrp_21)
# show(dynamic_plot_21)

# Secondary earner MTR
# dynamic_mtrs_21 = utils.mtr_graph_data(calc_base, dynamic_21, mars=2, mtr_variable='e00200s')
# dynamic_plot_21s = utils.xtr_graph_plot(dynamic_mtrs_21)
# show(dynamic_plot_21s)


# In[213]:

# calculate the average primary earner MTR change by percentile of AGI
makeline(calc1 = calc_base, 
         calc2 = calc_ubi21d, 
         mars='ALL', 
         mtr_measure='combined', 
         mtr_variable='e00200p', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'i3')

# average secondary earner MTR change by percentile of AGI
makeline(calc1 = calc_base, 
         calc2 = calc_ubi21d, 
         mars=2, 
         mtr_measure='combined', 
         mtr_variable='e00200s', 
         alt_e00200p_text='', 
         mtr_wrt_full_compen=False, 
         income_measure='agi', 
         dollar_weighting=False, 
         x1label = 'AGI Percentile', 
         x2label = 'Average AGI by Percentile', 
         ylabel = 'Combined Marginal Tax Rate', 
         plotname = 'i4')


# In[214]:

mtr_macros(calc_ubi21d, sec = 'i')


# In[215]:

# Primary earner's MTR Change
mtrp_dynamic_21 = pd.DataFrame()
mtrp_dynamic_21['c00100'] = dynamic_21.records.c00100
mtrp_dynamic_21['s006'] = dynamic_21.records.s006
mtrp_dynamic_21['mtr'] = dynamic_21.mtr()[2]
mtrp_dynamic_21['1 - mtr'] = 1. - mtrp_dynamic_21['mtr']
mtrp_dynamic_21['pct change'] = ((mtrp_dynamic_21['1 - mtr'] - mtrp_base['1 - mtr']) / mtrp_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrp_dynamic_21 = utils.add_weighted_income_bins(mtrp_dynamic_21, num_bins=100, income_measure='c00100')
mtrp_dynamic_21g = mtrp_dynamic_21.groupby('bins')
mtr1dynamic21 = mtrp_dynamic_21g.apply(utils.weighted_mean, 'pct change')
agi = mtrp_dynamic_21g.apply(utils.weighted_mean, 'c00100')
s006 = mtrp_dynamic_21g.apply(utils.weighted_mean, 's006')

lines_dynamic_21 = pd.DataFrame()
lines_dynamic_21['primary'] = mtr1dynamic21
lines_dynamic_21['avg-agi'] = agi
lines_dynamic_21['s006'] = s006


# In[216]:

# Secondary earner
mtrs_dynamic_21 = pd.DataFrame()
mtrs_dynamic_21['c00100'] = dynamic_21.records.c00100
mtrs_dynamic_21['s006'] = dynamic_21.records.s006
mtrs_dynamic_21['MARS'] = dynamic_21.records.MARS
mtrs_dynamic_21['mtr'] = dynamic_21.mtr('e00200s')[2]
mtrs_dynamic_21 = mtrs_dynamic_21[mtrs_dynamic_21['MARS'] == 2]
mtrs_dynamic_21['1 - mtr'] = 1. - mtrs_dynamic_21['mtr']
mtrs_dynamic_21['pct change'] = ((mtrs_dynamic_21['1 - mtr'] - mtrs_base['1 - mtr']) / mtrs_base['1 - mtr']) * 100

# Create graph of 1 - MTR
mtrs_dynamic_21 = utils.add_weighted_income_bins(mtrs_dynamic_21, num_bins=100, income_measure='c00100')
mtrs_dynamic21 = mtrs_dynamic_21.groupby('bins')
mtr2dynamic21 = mtrs_dynamic21.apply(utils.weighted_mean, 'pct change')
lines_dynamic_21['secondary'] = mtr2dynamic21


# In[217]:

# generate dataframe for graph
lines_dynamic_21['bins'] = lines_dynamic_21.index
del lines_dynamic_21.index.name

plines = lines_dynamic_21['primary'].values
slines = lines_dynamic_21['secondary'].values
agi = lines_dynamic_21['avg-agi'].values
s006 = lines_dynamic_21['s006'].values
idlines = lines_dynamic_21.index.values

dataframe = pd.DataFrame()
dataframe['primary'] = plines
dataframe['secondary'] = slines
dataframe['agi'] = agi
dataframe['id'] = idlines
dataframe['c00100'] = agi
dataframe['s006'] = s006


# In[218]:

# generate labels for secondary x-axis
dataframe = add_weighted_income_bins(dataframe, num_bins=10,
                                     income_measure='c00100',
                                     weight_by_income_measure='AGI')

# split dfx into groups specified by 'bins' column
gdfx = dataframe.groupby('bins', as_index=False)

# apply the weighting_function to percentile-grouped mtr values
agi_series = gdfx.apply(agi_weighted, 'c00100')
agi_series[agi_series < 0] = 0

# add a zero to the beginning of 'agi_series'
zero = pd.Series(0)
agi_series = zero.append(agi_series)


# In[219]:

# generate a line graph

dataframe = dataframe
series1_label = 'Label 1'
series2_label = 'Label 2'
plotname = 'i5'
x1label = 'Average AGI by Percentile'
x2label = 'AGI Percentile'
ylabel = 'Ave. Pct. Change in (1-MTR) after Reform'

# begin plot
fig = plt.figure(figsize=(10, 5))
# legend = ax1.legend(loc='lower right', shadow=False)

ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.set_xlabel(x1label)
ax2.set_xlabel(x2label)
ax1.set_ylabel(ylabel)

ax1.set_xticks(np.arange(0, 110, 10))
ax2.set_xticks(np.arange(0, 110, 10))

ax1.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_xticklabels(agi_series.round())

ax1.plot(dataframe['primary'], color='red', label='Primary')
ax2.plot(dataframe['secondary'], color='blue', label='Secondary')
ax1.legend(bbox_to_anchor=(0.999, 0.18), loc=1)
ax2.legend(bbox_to_anchor=(0.999, 0.10), loc=1)     

# save plot
plotname = plotname + '.png'
plt.savefig(plotname, dpi=1000)
plt.show()


# In[220]:

plines_dynamic_21 = lines_dynamic_21['primary'].values
slines_dynamic_21 = lines_dynamic_21['secondary'].values
idlines_dynamic_21 = lines_dynamic_21.index.values

fig = figure(title='Mean Percent Change in 1 - MTR')
fig.line(idlines_dynamic_21, plines_dynamic_21, legend='Primary Earner')
fig.line(idlines_dynamic_21, slines_dynamic_21, color='red', legend= 'Secondary Earner')
fig.legend.location = 'bottom_right'
# show(fig)


# In[221]:

max(dynamic_21.records.expanded_income - dynamic_21.records.combined)


# ## Section 11: Welfare Received vs. Benefits Spent

# Using Will's welfare multiples,find what portion of the benefit is actually spent vs. what is received.
# Plot this by income percentile

# In[222]:

# Welfare multiples
welfare_mult = {
                'Medicare': 0.75,
                'Medicaid': 0.30,
                'SNAP': 0.95,
                'SS': 0.95,
                'SSI': 0.95,
                'VB': 0.95
                }


# In[223]:

# generate table

wm_tab = welfare_mult
wm_df = pd.DataFrame.from_dict(wm_tab, orient='index').reset_index()

wm_df[0] = wm_df[0].map('{:,.2f}'.format)

wm_df.rename(columns={'index': 'Program', 0: 'Welfare Multiple'}, inplace=True)

wm_df['index'] = ' '
wm_df = wm_df.set_index(wm_df['index'])
wm_df = wm_df.drop('index', 1)
del wm_df.index.name

# wm_df['Welfare Multiple'] = wm_df['Welfare Multiple'].map('{:,.2f}'.format)

# restricted_table(wm_df, 
#                  ['Program', 'Welfare Multiple'], 
#                  ['Program', 'Welfare Multiple'],
#                  'j1_df'
#                 )


# In[224]:

# calculate the dollar welfare

dollar_welfare = pd.DataFrame()
dollar_welfare['Medicare Dollar Welfare'] = cps_benefits['MedicareX']
dollar_welfare['Medicaid Dollar Welfare'] = cps_benefits['MEDICAID']
dollar_welfare['SSI Dollar Welfare'] = cps_benefits['SSI']
dollar_welfare['SS Dollar Welfare'] = cps_benefits['SS']
dollar_welfare['SNAP Dollar Welfare'] = cps_benefits['SNAP']
dollar_welfare['VB Dollar Welfare'] = cps_benefits['VB']
dollar_welfare['Total Dollar Welfare'] = (dollar_welfare['Medicare Dollar Welfare'] 
                                          + dollar_welfare['Medicaid Dollar Welfare'] 
                                          + dollar_welfare['SSI Dollar Welfare'] 
                                          + dollar_welfare['SS Dollar Welfare'] 
                                          + dollar_welfare['SNAP Dollar Welfare'] 
                                          + dollar_welfare['VB Dollar Welfare'])
dollar_welfare['Total Income'] = cps_benefits['tot_inc']
dollar_welfare['Total Benefits'] = cps_benefits['tot_benefits']
dollar_welfare['s006'] = cps_benefits['s006']

# Weighted bins of welfare multiplier

welfare_bins = utils.add_weighted_income_bins(dollar_welfare, num_bins=10, income_measure='Total Income')
dollar_welfare_group = pd.DataFrame(welfare_bins.groupby('bins', as_index=False).apply(utils.weighted_mean, 'Total Dollar Welfare'))
dollar_welfare_group.columns = ['Average Dollar Welfare']
dollar_welfare_group['Total Dollar Welfare'] = pd.DataFrame(welfare_bins.groupby('bins', as_index=False).apply(utils.weighted_sum, 'Total Dollar Welfare'))
dollar_welfare_group['Income Bins'] = agi_bins
dollar_welfare_group = dollar_welfare_group.set_index(dollar_welfare_group['Income Bins'])
dollar_welfare_group = dollar_welfare_group.drop('Income Bins', 1)
del dollar_welfare_group.index.name
# dollar_welfare_group


# In[225]:

# calculate adjusted welfare

adjusted_welfare = pd.DataFrame()
adjusted_welfare['Medicare Adjusted Welfare'] = cps_benefits['MedicareX'] * welfare_mult['Medicare']
adjusted_welfare['Medicaid Adjusted Welfare'] = cps_benefits['MEDICAID'] * welfare_mult['Medicaid']
adjusted_welfare['SSI Adjusted Welfare'] = cps_benefits['SSI'] * welfare_mult['SSI']
adjusted_welfare['SS Adjusted Welfare'] = cps_benefits['SS'] * welfare_mult['SS']
adjusted_welfare['SNAP Adjusted Welfare'] = cps_benefits['SNAP'] * welfare_mult['SNAP']
adjusted_welfare['VB Adjusted Welfare'] = cps_benefits['VB'] * welfare_mult['VB']
adjusted_welfare['Total Adjusted Welfare'] = (adjusted_welfare['Medicare Adjusted Welfare'] 
                                              + adjusted_welfare['Medicaid Adjusted Welfare'] 
                                              + adjusted_welfare['SSI Adjusted Welfare'] 
                                              + adjusted_welfare['SS Adjusted Welfare'] 
                                              + adjusted_welfare['SNAP Adjusted Welfare'] 
                                              + adjusted_welfare['VB Adjusted Welfare'])
adjusted_welfare['Total Income'] = cps_benefits['tot_inc']
adjusted_welfare['Total Benefits'] = cps_benefits['tot_benefits']
adjusted_welfare['s006'] = cps_benefits['s006']

# Weighted bins of welfare multiplier
welfare_bins = utils.add_weighted_income_bins(adjusted_welfare, num_bins=10, income_measure='Total Income')
adjusted_welfare_group = pd.DataFrame(welfare_bins.groupby('bins', as_index=False).apply(utils.weighted_mean, 'Total Adjusted Welfare'))
adjusted_welfare_group.columns = ['Average Adjusted Welfare']
adjusted_welfare_group['Total Adjusted Welfare'] = pd.DataFrame(welfare_bins.groupby('bins', as_index=False).apply(utils.weighted_sum, 'Total Adjusted Welfare'))
adjusted_welfare_group['Income Bins'] = agi_bins
adjusted_welfare_group = adjusted_welfare_group.set_index(adjusted_welfare_group['Income Bins'])
adjusted_welfare_group = adjusted_welfare_group.drop('Income Bins', 1)
del adjusted_welfare_group.index.name
# adjusted_welfare_group


# In[226]:

# compare dollar and adjusted welfare calculations

joint_welfare = dollar_welfare_group.join(adjusted_welfare_group, on=None, how='left', lsuffix='', rsuffix='', sort=False)
joint_welfare = joint_welfare[['Average Dollar Welfare', 'Average Adjusted Welfare', 'Total Dollar Welfare', 'Total Adjusted Welfare']]
joint_welfare['mean'] = 1
joint_welfare['perc_inc'] = 1

joint_welfare = restricted_table(joint_welfare, 
                 ['Average Dollar Welfare', 'Average Adjusted Welfare', 'Total Dollar Welfare', 'Total Adjusted Welfare'], 
                 ['Average Dollar Welfare', 'Average Adjusted Welfare', 'Total Dollar Welfare', 'Total Adjusted Welfare'],
                 'j2_df', 
                 reindex = False
                )

# add sum row
sum1 = (joint_welfare['Total Dollar Welfare']['0-10%'] 
     + joint_welfare['Total Dollar Welfare']['10-20%'] 
     + joint_welfare['Total Dollar Welfare']['20-30%'] 
     + joint_welfare['Total Dollar Welfare']['30-40%'] 
     + joint_welfare['Total Dollar Welfare']['40-50%'] 
     + joint_welfare['Total Dollar Welfare']['50-60%'] 
     + joint_welfare['Total Dollar Welfare']['60-70%'] 
     + joint_welfare['Total Dollar Welfare']['70-80%'] 
     + joint_welfare['Total Dollar Welfare']['80-90%'] 
     + joint_welfare['Total Dollar Welfare']['90-100%'])

sum2 = (joint_welfare['Total Adjusted Welfare']['0-10%'] 
     + joint_welfare['Total Adjusted Welfare']['10-20%'] 
     + joint_welfare['Total Adjusted Welfare']['20-30%'] 
     + joint_welfare['Total Adjusted Welfare']['30-40%'] 
     + joint_welfare['Total Adjusted Welfare']['40-50%'] 
     + joint_welfare['Total Adjusted Welfare']['50-60%'] 
     + joint_welfare['Total Adjusted Welfare']['60-70%'] 
     + joint_welfare['Total Adjusted Welfare']['70-80%'] 
     + joint_welfare['Total Adjusted Welfare']['80-90%'] 
     + joint_welfare['Total Adjusted Welfare']['90-100%'])

joint_welfare_sum = pd.DataFrame({'Average Adjusted Welfare':[''],
                                  'Average Dollar Welfare':[''],
                                  'Total Dollar Welfare':[sum1],
                                  'Total Adjusted Welfare':[sum2]},
                                 index = ['Sum'])

joint_welfare = pd.concat([joint_welfare, joint_welfare_sum])
joint_welfare


# In[227]:

def_macro('Difference between dollar and adjusted welfare (0-10%) (part J)', 
          units(joint_welfare['Average Dollar Welfare']['0-10%'] - joint_welfare['Average Adjusted Welfare']['0-10%']), 
          'jwav')


# In[228]:

def_macro('Total Adjusted Welfare (part J)', units(joint_welfare['Total Adjusted Welfare']['Sum']), 'jwag')
def_macro('Total Dollar Welfare (part J)', units(joint_welfare['Total Dollar Welfare']['Sum']), 'jwdg')


# In[229]:

# df for dynamic calculator UBI all

ubi_df_all = pd.DataFrame()
ubi_df_all['ubi'] = dynamic_all.records.ubi
ubi_df_all['s006'] = dynamic_all.records.s006
ubi_df_all['c00100'] = dynamic_all.records.c00100
ubi_bins_all = utils.add_weighted_income_bins(ubi_df_all, num_bins=10, income_measure='c00100')
ubi_group_all = pd.DataFrame(ubi_bins_all.groupby('bins', as_index=False).apply(utils.weighted_mean, 'ubi'))
ubi_group_all.columns = ['Average UBI (all) Benefit']
ubi_group_all['Total UBI (all) Benefit'] = pd.DataFrame(ubi_bins_all.groupby('bins', as_index=False).apply(utils.weighted_sum, 'ubi'))
ubi_group_all['Income Bins'] = agi_bins
ubi_group_all = ubi_group_all.set_index(ubi_group_all['Income Bins'])
ubi_group_all = ubi_group_all.drop('Income Bins', 1)
del ubi_group_all.index.name

ubi_group_all['mean'] = 1
ubi_group_all['perc_inc'] = 1

ubi_group_all

ubi_group_all = restricted_table(ubi_group_all, 
                 ['Average UBI (all) Benefit', 'Total UBI (all) Benefit'], 
                 ['Average UBI (all) Benefit', 'Total UBI (all) Benefit'],
                 'j3_df',
                 reindex = False
                )


# In[230]:

# df for dynamic calculator 18+

ubi_df18 = pd.DataFrame()
ubi_df18['ubi'] = dynamic_18.records.ubi
ubi_df18['s006'] = dynamic_18.records.s006
ubi_df18['c00100'] = dynamic_18.records.c00100
ubi_bins18 = utils.add_weighted_income_bins(ubi_df18, num_bins=10, income_measure='c00100')
ubi_group18 = pd.DataFrame(ubi_bins18.groupby('bins', as_index=False).apply(utils.weighted_mean, 'ubi'))
ubi_group18.columns = ['Average UBI (18+) Benefit']
ubi_group18['Total UBI (18+) Benefit'] = pd.DataFrame(ubi_bins18.groupby('bins', as_index=False).apply(utils.weighted_sum, 'ubi'))

ubi_group18['Income Bins'] = agi_bins
ubi_group18 = ubi_group18.set_index(ubi_group18['Income Bins'])
ubi_group18 = ubi_group18.drop('Income Bins', 1)
del ubi_group18.index.name

ubi_group18['mean'] = 1
ubi_group18['perc_inc'] = 1

ubi_group18

ubi_group18 = restricted_table(ubi_group18, 
                 ['Average UBI (18+) Benefit', 'Total UBI (18+) Benefit'], 
                 ['Average UBI (18+) Benefit', 'Total UBI (18+) Benefit'],
                 'j4_df',
                 reindex = False
                )


# In[231]:

# df for dynamic calculator 21+

ubi_df21 = pd.DataFrame()
ubi_df21['ubi'] = dynamic_21.records.ubi
ubi_df21['s006'] = dynamic_21.records.s006
ubi_df21['c00100'] = dynamic_21.records.c00100
ubi_bins21 = utils.add_weighted_income_bins(ubi_df21, num_bins=10, income_measure='c00100')
ubi_group21 = pd.DataFrame(ubi_bins21.groupby('bins', as_index=False).apply(utils.weighted_mean, 'ubi'))
ubi_group21.columns = ['Average UBI (21+) Benefit']
ubi_group21['Total UBI (21+) Benefit'] = pd.DataFrame(ubi_bins21.groupby('bins', as_index=False).apply(utils.weighted_sum, 'ubi'))

ubi_group21['Income Bins'] = agi_bins
ubi_group21 = ubi_group21.set_index(ubi_group21['Income Bins'])
ubi_group21 = ubi_group21.drop('Income Bins', 1)
del ubi_group21.index.name

ubi_group21['mean'] = 1
ubi_group21['perc_inc'] = 1

ubi_group21

ubi_group21 = restricted_table(ubi_group21, 
                 ['Average UBI (21+) Benefit', 'Total UBI (21+) Benefit'], 
                 ['Average UBI (21+) Benefit', 'Total UBI (21+) Benefit'],
                 'j5_df',
                 reindex = False
                )


# In[232]:

"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""

plotname = 'j1'

N = 10
ind = np.arange(N)  # the x locations for the groups
width = 0.115       # the width of the bars
fig, ax = plt.subplots(figsize=(10,5))

space = 0.05

dollar_welf = dollar_welfare_group['Average Dollar Welfare']
bar1 = ax.bar(ind-(2*width)-(2*space), dollar_welf, width, color='red')

adj_welf = adjusted_welfare_group['Average Adjusted Welfare']
bar2 = ax.bar(ind-(1*width)-space, adj_welf, width, color='orange')

ubi_all = ubi_group_all['Average UBI (all) Benefit']
bar3 = ax.bar(ind+(0*width), ubi_all, width, color='blue')

ubi_18 = ubi_group18['Average UBI (18+) Benefit']
bar4 = ax.bar(ind+(1*width)+space, ubi_18, width, color='purple')

ubi_21 = ubi_group21['Average UBI (21+) Benefit']
bar5 = ax.bar(ind+(2*width)+(2*space), ubi_21, width, color='navy')

# add some text for labels, title and axes ticks
ax.set_ylabel('Mean Benefit')
ax.set_xlabel('Income Percentile')

# x axis
ind = np.arange(10)
plt.xticks(ind, ('0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'))
plt.tick_params(labelsize=10)

ax.legend((bar1[0], bar2[0], bar3[0], bar4[0], bar5[0]), ('Dollar Welfare', 'Adjusted Welfare', 'UBI (all) Welfare', 'UBI (18+) Welfare', 'UBI (21+) Welfare'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()    
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)

plt.savefig(plotname)

plt.show()


# In[233]:

# average welfare table

avg_comp_df = pd.DataFrame()
avg_comp_df['Adjusted Welfare'] = adjusted_welfare_group['Average Adjusted Welfare']
avg_comp_df['UBI (all)'] = ubi_group_all['Average UBI (all) Benefit']
avg_comp_df['UBI (18+)'] = ubi_group18['Average UBI (18+) Benefit']
avg_comp_df['UBI (21+)'] = ubi_group21['Average UBI (21+) Benefit']
avg_comp_df.index = agi_bins

# add sum row
sum1 = (avg_comp_df['Adjusted Welfare']['0-10%'] 
     + avg_comp_df['Adjusted Welfare']['10-20%'] 
     + avg_comp_df['Adjusted Welfare']['20-30%'] 
     + avg_comp_df['Adjusted Welfare']['30-40%'] 
     + avg_comp_df['Adjusted Welfare']['40-50%'] 
     + avg_comp_df['Adjusted Welfare']['50-60%'] 
     + avg_comp_df['Adjusted Welfare']['60-70%'] 
     + avg_comp_df['Adjusted Welfare']['70-80%'] 
     + avg_comp_df['Adjusted Welfare']['80-90%'] 
     + avg_comp_df['Adjusted Welfare']['90-100%'])

sum2 = (avg_comp_df['UBI (all)']['0-10%'] 
     + avg_comp_df['UBI (all)']['10-20%'] 
     + avg_comp_df['UBI (all)']['20-30%'] 
     + avg_comp_df['UBI (all)']['30-40%'] 
     + avg_comp_df['UBI (all)']['40-50%'] 
     + avg_comp_df['UBI (all)']['50-60%'] 
     + avg_comp_df['UBI (all)']['60-70%'] 
     + avg_comp_df['UBI (all)']['70-80%'] 
     + avg_comp_df['UBI (all)']['80-90%'] 
     + avg_comp_df['UBI (all)']['90-100%'])

sum3 = (avg_comp_df['UBI (18+)']['0-10%'] 
     + avg_comp_df['UBI (18+)']['10-20%'] 
     + avg_comp_df['UBI (18+)']['20-30%'] 
     + avg_comp_df['UBI (18+)']['30-40%'] 
     + avg_comp_df['UBI (18+)']['40-50%'] 
     + avg_comp_df['UBI (18+)']['50-60%'] 
     + avg_comp_df['UBI (18+)']['60-70%'] 
     + avg_comp_df['UBI (18+)']['70-80%'] 
     + avg_comp_df['UBI (18+)']['80-90%'] 
     + avg_comp_df['UBI (18+)']['90-100%'])

sum4 = (avg_comp_df['UBI (21+)']['0-10%'] 
     + avg_comp_df['UBI (21+)']['10-20%'] 
     + avg_comp_df['UBI (21+)']['20-30%'] 
     + avg_comp_df['UBI (21+)']['30-40%'] 
     + avg_comp_df['UBI (21+)']['40-50%'] 
     + avg_comp_df['UBI (21+)']['50-60%'] 
     + avg_comp_df['UBI (21+)']['60-70%'] 
     + avg_comp_df['UBI (21+)']['70-80%'] 
     + avg_comp_df['UBI (21+)']['80-90%'] 
     + avg_comp_df['UBI (21+)']['90-100%'])

avg_comp_df_sum = pd.DataFrame({'Adjusted Welfare':[sum1],
                                  'UBI (all)':[sum2],
                                  'UBI (18+)':[sum3],
                                  'UBI (21+)':[sum4]},
                                 index = ['Sum'])

avg_comp_df = pd.concat([avg_comp_df, avg_comp_df_sum])

text_file = open('j6_df.txt', "w")
text_file.write(avg_comp_df.to_latex())
text_file.close()

avg_comp_df


# In[234]:

# total welfare table

total_comp_df = pd.DataFrame()
total_comp_df['Adjusted Welfare'] = adjusted_welfare_group['Total Adjusted Welfare']
total_comp_df['UBI (all)'] = ubi_group_all['Total UBI (all) Benefit']
total_comp_df['UBI (18+)'] = ubi_group18['Total UBI (18+) Benefit']
total_comp_df['UBI (21+)'] = ubi_group21['Total UBI (21+) Benefit']
total_comp_df.index = agi_bins

# add sum row
sum1 = (total_comp_df['Adjusted Welfare']['0-10%'] 
     + total_comp_df['Adjusted Welfare']['10-20%'] 
     + total_comp_df['Adjusted Welfare']['20-30%'] 
     + total_comp_df['Adjusted Welfare']['30-40%'] 
     + total_comp_df['Adjusted Welfare']['40-50%'] 
     + total_comp_df['Adjusted Welfare']['50-60%'] 
     + total_comp_df['Adjusted Welfare']['60-70%'] 
     + total_comp_df['Adjusted Welfare']['70-80%'] 
     + total_comp_df['Adjusted Welfare']['80-90%'] 
     + total_comp_df['Adjusted Welfare']['90-100%'])

sum2 = (total_comp_df['UBI (all)']['0-10%'] 
     + total_comp_df['UBI (all)']['10-20%'] 
     + total_comp_df['UBI (all)']['20-30%'] 
     + total_comp_df['UBI (all)']['30-40%'] 
     + total_comp_df['UBI (all)']['40-50%'] 
     + total_comp_df['UBI (all)']['50-60%'] 
     + total_comp_df['UBI (all)']['60-70%'] 
     + total_comp_df['UBI (all)']['70-80%'] 
     + total_comp_df['UBI (all)']['80-90%'] 
     + total_comp_df['UBI (all)']['90-100%'])

sum3 = (total_comp_df['UBI (18+)']['0-10%'] 
     + total_comp_df['UBI (18+)']['10-20%'] 
     + total_comp_df['UBI (18+)']['20-30%'] 
     + total_comp_df['UBI (18+)']['30-40%'] 
     + total_comp_df['UBI (18+)']['40-50%'] 
     + total_comp_df['UBI (18+)']['50-60%'] 
     + total_comp_df['UBI (18+)']['60-70%'] 
     + total_comp_df['UBI (18+)']['70-80%'] 
     + total_comp_df['UBI (18+)']['80-90%'] 
     + total_comp_df['UBI (18+)']['90-100%'])

sum4 = (total_comp_df['UBI (21+)']['0-10%'] 
     + total_comp_df['UBI (21+)']['10-20%'] 
     + total_comp_df['UBI (21+)']['20-30%'] 
     + total_comp_df['UBI (21+)']['30-40%'] 
     + total_comp_df['UBI (21+)']['40-50%'] 
     + total_comp_df['UBI (21+)']['50-60%'] 
     + total_comp_df['UBI (21+)']['60-70%'] 
     + total_comp_df['UBI (21+)']['70-80%'] 
     + total_comp_df['UBI (21+)']['80-90%'] 
     + total_comp_df['UBI (21+)']['90-100%'])

total_comp_df_sum = pd.DataFrame({'Adjusted Welfare':[sum1],
                                  'UBI (all)':[sum2],
                                  'UBI (18+)':[sum3],
                                  'UBI (21+)':[sum4]},
                                 index = ['Sum'])

total_comp_df = pd.concat([total_comp_df, total_comp_df_sum])

text_file = open('j7_df.txt', "w")
text_file.write(total_comp_df.to_latex())
text_file.close()

total_comp_df


# In[235]:

# assemble macro dictionary

macro_dict['labels'] = labels
macro_dict['values'] = values
macro_dict['macros'] = macros

macro_dict.to_csv('macro_dict.txt', header=None, index=None, sep=' ', mode='a')

macro_dict


# In[ ]:


