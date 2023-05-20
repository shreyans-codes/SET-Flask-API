import joblib


def apiCallFunction(N, P, K, temp, humidity, ph, rainfall):
    joblib_file = "kn_classifier_model.pkl"
    kn_model = joblib.load(joblib_file)
    ans = kn_model.predict([[N, P, K, temp, humidity, ph, rainfall]])
    return ans[0]


print(apiCallFunction(N=104, P=33, K=32, temp=23.00,
                      humidity=66.00, ph=6.22, rainfall=140.000))
