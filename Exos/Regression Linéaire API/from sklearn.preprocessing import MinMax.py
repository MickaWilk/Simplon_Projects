from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split


def scaler_cat(features_cat, test=None):
    ohe = OneHotEncoder(sparse=False)
    if test is None:
        features_cat_scaled = ohe.fit_transform(features_cat)
    else:
        ohe.fit(features_cat)
        features_cat_scaled = ohe.transform(test)
    features_cat_scaled_df = pd.DataFrame(features_cat_scaled)
    return features_cat_scaled_df

def scaler_num(features_num, test=None):
    scaler = MinMaxScaler()
    scaler.fit(features_num)
    features_num_scaled = scaler.transform(features_num)
    features_num_scaled_df = pd.DataFrame(features_num_scaled)
    return features_num_scaled_df


def scaler_features(features, test=None):
    features_cat = features.select_dtypes(include=['category'])
    features_cat_scaled_df = scaler_cat(features_cat, test)

    features_num = features.select_dtypes(include=['float64','int64'])
    features_num_scaled_df = scaler_num(features_num, test)

    features_prep_df = pd.concat([features_cat_scaled_df, features_num_scaled_df], axis=1)
    return features_prep_df


data = sns.load_dataset('tips')


y = data['tip']

X = data.drop(columns=['tip'])


X_train_2,X_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.3, random_state=60)



X_train_2_prep_df = scaler_features(X_train_2)




lg_2 = LinearRegression()



lg_2.fit(X_train_2_prep_df,y_train_2)


from sklearn.model_selection import cross_validate


cross_validate(lg_2, X_train_2_prep_df, y_train_2, cv=5)['test_score'].mean()

# <img src="../images/cross-validate.png" alt="schema cross validation"/>


X_test_2_prep_df = scaler_features(X_train_2, X_test_2)
X_test_2_prep_df


lg_2.score(X_test_2_prep_df,y_test_2)
