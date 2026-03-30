import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict(hours, attendance, assignments, previous):
    data = np.array([[hours, attendance, assignments, previous]])
    result = model.predict(data)

    if result[0] == 1:
        return "Pass"
    else:
        return "Fail"