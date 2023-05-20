import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

data_df = pd.read_csv('ml-model\dataset\crop_factors.csv')
data_df

X = data_df.drop(columns=['label'])
Y = data_df['label']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.20, shuffle=True, random_state=0)

kn_classifier = KNeighborsClassifier()
kn_classifier.fit(X_train, Y_train)

y_pred = kn_classifier.predict(X_test)

pred_kn = kn_classifier.predict(X_test)

newdata = kn_classifier.predict(
    [[60, 55, 44, 23.004459, 82.320763, 7.840207, 263.964248]])
print(newdata[0])

joblib_file = "kn_classifier_model1.pkl"
joblib.dump(kn_classifier, joblib_file)
