import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
import pickle

county_df = pd.read_csv('../data/county_df.csv', index_col='county')

# dropping unused column
county_df.drop(columns='med_patients', inplace=True)

# Encoding state column
county_df = pd.get_dummies(county_df, columns=['state'])

# setting X and y
X = county_df.drop(columns=['total_exp', 'medical_care_exp', 'edu_training_exp', 'exp_per_vet'])
y = county_df['total_exp']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)

# scaled X
sc = StandardScaler()
sc.fit(X_train)
X_train_sc = pd.DataFrame(sc.transform(X_train), columns=sc.get_feature_names_out())
X_test_sc = pd.DataFrame(sc.transform(X_test), columns=sc.get_feature_names_out())

lasso = Lasso()

params = {
    'alpha': [ 0, .000001, .00001, .0001, .001, .01, .1, .25, .5, .75, .9, .99, 1],
    'max_iter': [10000]
}

gs = GridSearchCV(lasso, param_grid=params, n_jobs=-1)

gs.fit(X_train_sc, y_train)
print(gs.score(X_train_sc, y_train), gs.score(X_test_sc, y_test))


print('success')

with open("saved_lasso_model.pkl", "wb") as file:
    pickle.dump(gs, file)