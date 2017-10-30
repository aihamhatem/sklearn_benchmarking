import time

def LinearRegression(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import LinearRegression
	if params is None:
		estimator = LinearRegression()
	else:
		estimator = eval('LinearRegression(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta	

def Ridge(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import Ridge
	if params is None:
		estimator = Ridge()
	else:
		estimator = eval('Ridge(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def Lasso(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import Lasso
	if params is None:
		estimator = Lasso()
	else:
		estimator = eval('Lasso(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def LassoCV(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import LassoCV
	if params is None:
		estimator = LassoCV()
	else:
		estimator = eval('LassoCV(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

def LassoLarsCV(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import LassoLarsCV
	if params is None:
		estimator = LassoLarsCV()
	else:
		estimator = eval('LassoLarsCV(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

def LassoLarsIC(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import LassoLarsIC
	if params is None:
		estimator = LassoLarsIC()
	else:
		estimator = eval('LassoLarsIC(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

def MultiTaskLasso(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import MultiTaskLasso
	if params is None:
		estimator = MultiTaskLasso()
	else:
		estimator = eval('MultiTaskLasso(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def ElasticNet(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import ElasticNet
	if params is None:
		estimator = ElasticNet()
	else:
		estimator = eval('ElasticNet(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def ElasticNetCV(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import ElasticNetCV
	if params is None:
		estimator = ElasticNetCV()
	else:
		estimator = eval('ElasticNetCV(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

def MultiTaskElasticNet(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import MultiTaskElasticNet
	if params is None:
		estimator = MultiTaskElasticNet()
	else:
		estimator = eval('MultiTaskElasticNet(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def MultiTaskElasticNetCV(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import MultiTaskElasticNetCV
	if params is None:
		estimator = MultiTaskElasticNetCV()
	else:
		estimator = eval('MultiTaskElasticNetCV(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def Lars(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import Lars
	if params is None:
		estimator = Lars()
	else:
		estimator = eval('Lars(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def LassoLars(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import LassoLars
	if params is None:
		estimator = LassoLars()
	else:
		estimator = eval('LassoLars(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def OrthogonalMatchingPursuit(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	from sklearn.linear_model import OrthogonalMatchingPursuit
	if params is None:
		estimator = OrthogonalMatchingPursuit()
	else:
		estimator = eval('OrthogonalMatchingPursuit(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, y_train)
	delta = time.time() - start_time
	return estimator, delta

def BayesianRidge(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import BayesianRidge
	if params is None:
		estimator = BayesianRidge()
	else:
		estimator = eval('BayesianRidge(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta

#### ERRORS IN THIS FUNCTION. NEEDS RESOLVING ####
# def LogisticRegression(X_train,y_train, X_test=None, y_test=None, params=None):
# 	start_time = time.time()
# 	import numpy as np
# 	from sklearn.linear_model import LogisticRegression
# 	if params is None:
# 		estimator = LogisticRegression()
# 	else:
# 		estimator = eval('LogisticRegression(' + params + ')')
# 	print ("Training...")
# 	estimator.fit(X_train, y_train)
# 	delta = time.time() - start_time
# 	return estimator, delta


def ARDRegression(X_train,y_train, X_test=None, y_test=None, params=None):
	start_time = time.time()
	import numpy as np
	from sklearn.linear_model import ARDRegression
	if params is None:
		estimator = ARDRegression()
	else:
		estimator = eval('ARDRegression(' + params + ')')
	print ("Training...")
	estimator.fit(X_train, np.ravel(y_train))
	delta = time.time() - start_time
	return estimator, delta
