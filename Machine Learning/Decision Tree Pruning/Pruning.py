from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load breast cancer dataset
X, y = load_breast_cancer(return_X_y=True)

# Separating Training and Testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)

# Train decision tree model
model = DecisionTreeClassifier(criterion="gini", random_state=2)
model.fit(X_train, y_train)

# Plot original tree
plt.figure(figsize=(15, 10))
plot_tree(model, filled=True)
plt.title("Original Decision Tree")
plt.show()

# Model Accuracy before pruning
accuracy_before_pruning = model.score(X_test, y_test)
print("Accuracy before pruning:", accuracy_before_pruning)


# parameter = {
#     'criterion' :['entropy','gini','log_loss'],
#     'splitter':['best','random'],
#     'max_depth':[1,2,3,4,5],
#     'max_features':['auto','sqrt','log2']
# }
# model = DecisionTreeClassifier()
# from sklearn.model_selection import GridSearchCV
# cv = GridSearchCV(model,param_grid = parameter,cv = 5)
# cv.fit(X_train,y_train)
# from sklearn.tree import export_graphviz
# import graphviz
# best_estimator = cv.best_estimator_
# feature_names = features

# dot_data = export_graphviz(best_estimator, out_file=None, filled=True, rounded=True,
# feature_names=feature_names, class_names=['0', '1', '2'])
# graph = graphviz.Source(dot_data)
# graph.render("decision_tree", format='png', cleanup=True)
# graph



# Cost-complexity pruning (Post-pruning)
path = model.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Train a series of decision trees with different alpha values
pruned_models = []
for ccp_alpha in ccp_alphas:
    pruned_model = DecisionTreeClassifier(criterion="gini", ccp_alpha=ccp_alpha, random_state=2)
    pruned_model.fit(X_train, y_train)
    pruned_models.append(pruned_model)

# Find the model with the best accuracy on test data
best_accuracy = 0
best_pruned_model = None
for pruned_model in pruned_models:
    accuracy = pruned_model.score(X_test, y_test)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_pruned_model = pruned_model
# Model Accuracy after pruning
accuracy_after_pruning = best_pruned_model.score(X_test, y_test)
print("Accuracy after pruning:", accuracy_after_pruning)