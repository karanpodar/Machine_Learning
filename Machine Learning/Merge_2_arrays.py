import numpy as np
import pandas as pd

#To merge/ join both arrays as 1 Dataframe 
X_test = np.array(X_test)
y_pred = np.array(y_pred)
predicted_output = pd.DataFrame(np.hstack((X_test, y_pred.reshape(-1, 1))))
print(predicted_output)