from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


# Load the breast cancer dataset
breast_cancer = load_breast_cancer()
X_bc, y_bc = breast_cancer.data, breast_cancer.target

# Split the dataset into training and test sets
X_train_bc, X_test_bc, y_train_bc, y_test_bc = train_test_split(X_bc, y_bc, test_size=0.2, random_state=42)

# Create the base estimators
svm_bc = SVC(probability=True)
dt_bc = DecisionTreeClassifier()

# Create the voting classifier
voting_clf_bc = VotingClassifier(estimators=[('svm', svm_bc), ('dt', dt_bc)], voting='soft')

# Train the voting classifier
voting_clf_bc.fit(X_train_bc, y_train_bc)

# Make predictions
y_pred_bc = voting_clf_bc.predict(X_test_bc)

# Evaluate the accuracy
accuracy_bc = accuracy_score(y_test_bc, y_pred_bc)
print(f'Accuracy on breast cancer dataset with Ensemble: {accuracy_bc}')

# Using Decision Tree
dt_clf = dt_bc.fit(X_train_bc, y_train_bc)

# Make predictions
y_pred_bc = dt_clf.predict(X_test_bc)

# Evaluate the accuracy
accuracy_bc = accuracy_score(y_test_bc, y_pred_bc)
print(f'Accuracy on breast cancer dataset with Decision Tree: {accuracy_bc}')

# Using SVM
svm_clf = svm_bc.fit(X_train_bc, y_train_bc)

# Make predictions
y_pred_bc = svm_clf.predict(X_test_bc)

# Evaluate the accuracy
accuracy_bc = accuracy_score(y_test_bc, y_pred_bc)
print(f'Accuracy on breast cancer dataset with SVM: {accuracy_bc}')