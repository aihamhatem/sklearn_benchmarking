import regression, classification, helper_functions
from inspect import getmembers, isfunction

regression_params = [x[0] for x in getmembers(regression) if isfunction(x[1])]
classification_params = [x[0] for x in getmembers(classification) if isfunction(x[1])]

def get_regression_params():
	print (regression_params)
	return regression_params

def get_classification_params():
	print (classification_params)
	return classification_params

def classification_methods(X_train, y_train,X_test=None, y_test=None, params=classification_params, scorer='r2_score', custom_scorer=None):
	method_dict = {}
	scorer = helper_functions.define_scorer(scorer, custom_scorer)

	if type(params).__name__ == 'list':
		for method in params:
			print (method)
			estimator, time = eval("classification." + method + "(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)")
			score = helper_functions.predict_and_score(estimator, scorer, X_train, y_train, X_test, y_test)
			method_dict[method] = [estimator, score, time]
			print (method + " scored", '{0:.4f}'.format(float(score)), "and ran for", '{0:.4f}'.format(time), "seconds.\n")
	
	elif type(params).__name__ == 'dict':
		for method in params:
			value = str(params[method])
			print (method)
			estimator, time = eval("classification." + method + "(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, params=value)")
			score = helper_functions.predict_and_score(estimator, scorer, X_train, y_train, X_test, y_test)
			method_dict[method] = [estimator, score, time]
			print (method + " scored", '{0:.4f}'.format(float(score)), "and ran for", '{0:.4f}'.format(time), "seconds.\n")
	return method_dict


def regression_methods(X_train, y_train,X_test=None, y_test=None, params=regression_params, scorer='r2_score', custom_scorer=None):
	method_dict = {}
	scorer = helper_functions.define_scorer(scorer, custom_scorer)

	if type(params).__name__ == 'list':
		for method in params:
			print (method)
			estimator, time = eval("regression." + method + "(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)")
			score = helper_functions.predict_and_score(estimator, scorer, X_train, y_train, X_test, y_test)
			method_dict[method] = [estimator, score, time]
			print (method + " scored", '{0:.4f}'.format(float(score)), "and ran for", '{0:.4f}'.format(time), "seconds.\n")
	
	elif type(params).__name__ == 'dict':
		for method in params:
			value = str(params[method])
			print (method)
			estimator, time = eval("regression." + method + "(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, params=value)")
			score = helper_functions.predict_and_score(estimator, scorer, X_train, y_train, X_test, y_test)
			method_dict[method] = [estimator, score, time]
			print (method + " scored", '{0:.4f}'.format(float(score)), "and ran for", '{0:.4f}'.format(time), "seconds.\n")
	return method_dict
