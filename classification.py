import time

def KNeighborsClassifier(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.neighbors import KNeighborsClassifier
	if params is None:
		estimator = KNeighborsClassifier()
	else:
		estimator = eval('KNeighborsClassifier(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

def GaussianNB(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.naive_bayes import GaussianNB
	if params is None:
		estimator = GaussianNB()
	else:
		estimator = eval('GaussianNB(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta