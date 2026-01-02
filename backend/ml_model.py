import numpy as np
from sklearn.linear_model import LinearRegression

class TrafficPredictor:
    def __init__(self):
        self.model = LinearRegression()
        # Mock Training Data: [Hour of Day] -> [Congestion Factor (1.0 = normal, 2.0 = double time)]
        X = np.array([[6], [8], [10], [12], [14], [17], [20], [23]])
        y = np.array([1.1, 1.8, 1.4, 1.2, 1.3, 1.9, 1.2, 1.0]) 
        self.model.fit(X, y)

    def predict_congestion(self, hour):
        # Predict congestion factor based on hour
        return self.model.predict(np.array([[hour]]))[0]