import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error
import math
from joblib import dump

#read and split
df = pd.read_csv('train.csv')
X_train, X_test, y_train, y_test = train_test_split(df['excerpt'], df['target'] , test_size=0.2, random_state=1715)



#setup pipeline
text_comp_reg = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('mlpreg', MLPRegressor(verbose=True) ),
])


parameters = {
    'vect__ngram_range': [(1, 1), (1, 2), (2,2)],
    'tfidf__use_idf': (True, False),
    'mlpreg__max_iter': [100, 1000, 2000],
    'mlpreg__hidden_layer_sizes': [(50,), (100,), (50, 50)],
    'mlpreg__activation':  ('relu', 'tanh'),
    'mlpreg__solver': ('adam', 'sgd'),
}

#for faster train can just run already found params - otherwise comment out
parameters = {
    'vect__ngram_range': [(1, 1)],
    'tfidf__use_idf': [(False)],
    'mlpreg__max_iter': [(1000)],
    'mlpreg__hidden_layer_sizes': [(100,)],
    'mlpreg__activation':  [('relu')],
    'mlpreg__solver': [('adam')],
}


gs_reg = GridSearchCV(text_comp_reg, parameters, cv=5, n_jobs=-1)

#train
gs_reg.fit(X_train, y_train)


text_complexity_model = gs_reg.best_estimator_
y_pred = text_complexity_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
print("RMSE Score: {:.2f}".format(rmse))

dump(text_complexity_model, 'text_complexity_model.joblib')
print("Model file dump complete")
