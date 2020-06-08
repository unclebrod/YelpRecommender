# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import os
import os.path
import math
from surprise import (Reader, Dataset, NormalPredictor, BaselineOnly,
                     accuracy, SVD, SVDpp, NMF, KNNBasic, KNNWithMeans,
                     KNNWithZScore, KNNBaseline)
from surprise.model_selection import (cross_validate, KFold,
                                      train_test_split, GridSearchCV,
                                      RandomizedSearchCV)

# Always make it pretty.
plt.style.use('ggplot')
%matplotlib inline
sns.set_style(style="whitegrid")

def inner_to_raw_iid(row):
    '''
    Returns the raw item id associated with a given Surprise inner id
    
    Arguments:
    row: corresponds to a row in a dataframe
    
    Returns:
    output (float): raw item id
    '''
    output = trainset.to_raw_iid(row['iid'])
    return output

def inner_to_raw_uid(row):
    '''
    Returns the raw user id associated with a given Surprise inner id
    
    Arguments:
    row: corresponds to a row in a dataframe
    
    Returns:
    output (float): raw user id
    '''
    output = trainset.to_raw_uid(row['uid'])
    return output

def get_top_n(predictions, n=10):
    '''
    Return the top-N recommendation for each user from a set of predictions.

    Arguments:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def find_and_compare(user_id, top_n):
    '''
    Returns the raw user id associated with a given Surprise inner id
    
    Arguments:
    user_id (string): user_id string
    top_n (dict): top_n dictionary generated from get_top_n
    
    Returns:
    reviewed_businesses_df (dataframe): dataframe of businesses reviewed by
    the given user
    recommended_df (dataframe): dataframe of recommended restaurants
    '''
    reviewed_df = utility_3[utility_3['user_id'] == user_id]
    merged_reviewed_df = reviewed_df.merge(right=business_df,
                                           how='left',
                                           left_on='business_id',
                                           right_on='business_id')
    reviewed_businesses_df = merged_reviewed_df[['business_name',
                                                 'review_stars',
                                                 'categories']]
    
    top_n_df = pd.DataFrame(columns=['business_id', 'predicted'])
    i = 0
    for business, predicted in top_n[user_id]:
        top_n_df.loc[i] = [business, predicted]
        i += 1
    top_n_businesses_df = top_n_df.merge(right=business_df,
                                         how='left',
                                         left_on='business_id',
                                         right_on='business_id')
    recommended_df = top_n_businesses_df[['business_name',
                                          'predicted',
                                          'categories']]
    
    return reviewed_businesses_df, recommended_df

def get_user_totals(uid):
    '''
    Returns the number of items rated by given user
    
    Arguments: 
    uid (string): the id of the user
    
    Returns: 
    (int): the number of items rated by the user
    '''
    try:
        return len(trainset_3.ur[trainset_3.to_inner_uid(uid)])
    except ValueError: # user was not part of the trainset
        return 0
    
def get_item_totals(iid):
    '''
    Returns the number of users that have rated a given item
    
    Arguments:
    iid (string): the raw id of the item
      
    Returns:
    (int): the number of users that have rated the item.
    '''
    try: 
        return len(trainset_3.ir[trainset_3.to_inner_iid(iid)])
    except ValueError:
        return 0