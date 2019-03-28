## Fill each each function stub according to the docstring.
## To run the unit tests: Make sure you are in the root dir:assessment-2
## Then run the tests with this command: "make test"

import numpy as np
import pandas as pd


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list

    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    lret=[]
    for a in zip(list1,list2):
        lret.append(max(a))
    return lret


def get_diagonal(mat):
    '''
    INPUT: 2 dimensional list
    OUTPUT: list

    Given a matrix encoded as a 2 dimensional python list, return a list
    containing all the values in the diagonal starting at the index 0, 0.

    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]

    You may assume that the matrix is nonempty.
    '''
    nplst = np.array(mat)
    return list(nplst.diagonal())


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary

    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''
    dret = {}
    for k1, v1 in d1.items():
        if d2.get(k1, None) is None:
            dret[k1] = v1
        else:
            dret[k1] = d2.get(k1, None) + v1
    for k2, v2 in d2.items():
        if d1.get(k2, None) is None:
            dret[k2] = v2

    return dret


def make_char_dict(filename):
    '''
    INPUT: string
    OUTPUT: dictionary (string => list)

    Given a file containing rows of text, create a dictionary whose keys
    are single characters. The value associated with each key is a list of all
    the line numbers which start with that letter. The first line should have
    line number 1.  Characters which never are the first letter of a line do
    not need to be included in your dictionary.
    '''
    dret={}
    idx=0
    with open(filename) as f:
        for line in f:
            idx+=1
            if dret.get(line[0], None) is None:
                dret[line[0]] = [idx]
            else:
                dret[line[0]].append(idx)
    return dret


### Pandas
# For each of these, you will be dealing with a DataFrame which contains median
# rental prices in the US by neighborhood. The DataFrame will have these
# columns:
# Neighborhood, City, State, med_2011, med_2014

def pandas_add_increase_column(df):
    '''
    INPUT: DataFrame
    OUTPUT: None

    Add a column to the DataFrame called 'Increase' which contains the
    amount that the median rent increased by from 2011 to 2014.
    '''
    df['Increase'] = df['med_2014'] - df['med_2011']
    return


def pandas_only_given_state(df, state):
    '''
    INPUT: DataFrame, string
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains the entries for the given
    state. Only include these columns:
        Neighborhood, City, med_2011, med_2014
    '''
    d1 = df.loc[df['State'] == 'CA']
    del d1['State']
    return d1


def pandas_max_rent(df):
    '''
    INPUT: DataFrame
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains every city and the highest
    median rent from that city for 2011 and 2014.

    Note that city names are not unique and you need to use the state as well
    so that Portland, ME and Portland, OR are recognized as different.

    Your DataFrame should contain these columns:
        City, State, med_2011, med_2014
    '''
    d1 = df.groupby(['City','State']).max()
    del d1['Neighborhood']
    d1 = pd.DataFrame(d1.reset_index())
    return  d1 


### SQL
# For each of these, your python function should return a string that is the
# SQL statement which answers the question.
# For example:
#    return '''SELECT * FROM rent;'''
# You may want to run "sqlite3 data/housing.sqlite" in the command line to test
# out your queries if the test is failing.
#
# There are two tables in the database with these columns:
# (this is the same data that you dealt with in the pandas questions)
#     rent: Neighborhood, City, State, med_2011, med_2014
#     buy:  Neighborhood, City, State, med_2011, med_2014
# The values in the date columns are integers corresponding to the price on
# that date.

def sql_count_neighborhoods():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the number of neighborhoods in each city
    according to the rent table. Keep in mind that city names are not always
    unique unless you include the state as well, so your result should have
    these columns (though you do not need to name them): city, state, cnt
    '''
    ##### there are definitely 177 rows:
    # bart=# SELECT COUNT(*) OVER () AS num
    # bart-# FROM rent
    # bart-# GROUP BY city, state
    # bart-# HAVING COUNT(*) >=0
    # bart-# LIMIT 1;
    #  num
    # -----
    #  177
    # (1 row)

     # I didn't put the columns in the corect order as shwon above
    #sqlite
    return "SELECT city, state, Count(neighborhood) as cnt FROM rent GROUP BY city, state;"


def sql_highest_rent_increase():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the 5 San Francisco neighborhoods with the
    highest rent increase.
    '''

    # ordered by increase and includes answers they dont want
    # return "SELECT med_2014 - med_2011 as incr, neighborhood from rent where med_2014 > 0 and med_2011 > 0 and lower(city) LIKE 'san francisco' order by incr DESC LIMIT 5;"
    #return "SELECT neighborhood from rent where med_2014 > 0 and med_2011 > 0 and lower(city) LIKE 'san francisco' order by med_2014 - med_2011 DESC LIMIT 5;"

    #sqlite
    return "SELECT neighborhood FROM rent WHERE city='San Francisco' ORDER BY med_2014 - med_2011 DESC LIMIT 5;"


def sql_rent_and_buy():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the rent price and buying price for 2014 for
    all the neighborhoods in San Francisco.
    Your result should have these columns (though you do not need to name
    them): neighborhood, rent, buy
    '''
    #sqlite
    return "select rent.neighborhood, rent.med_2014 as r2014, buy.med_2014 as b2014 FROM buy INNER JOIN rent ON (rent.city = buy.city AND rent.state=buy.state AND rent.neighborhood=buy.neighborhood) WHERE lower(rent.city) LIKE 'san francisco' ORDER BY rent.neighborhood;"
