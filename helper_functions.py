def define_scorer(scorer, custom_scorer):
	if custom_scorer == None:
		import sklearn.metrics
		scorer = getattr(sklearn.metrics,scorer)
	else:
		scorer = custom_scorer
	return scorer

def predict_and_score(estimator, scorer, X_train, y_train, X_test=None, y_test=None):
	if X_test is not None and y_test is not None:
		Predictions = estimator.predict(X_test)
		score = scorer(y_test, Predictions)
	else:
		Predictions = estimator.predict(X_train)
		score = scorer(y_train, Predictions)
	return score