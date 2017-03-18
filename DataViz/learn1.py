from sklearn import tree

X = [[161,23],[161,23],[161,23],[140,23],[161,23]]

Y = ["male","male","male","female","male"]

clf  = tree.DecisionTreeClassifier();

clf = clf.fit(X,Y)

predict = clf.predict([[120,34]])
print predict