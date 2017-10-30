# sklearn_benchmarking
A tool to benchmarking several sklearn methods against your data with very little code.

The sklearn_benchmarking file contains two methods that can be used to quickly benchmark sklearn algorithms against a dataset.

Methods:
	- get_regression_params : returns a list with all sklearn regression methods that are currently available for use 
	- get_classification_params: returns a list with all sklearn classification methods that are currently available for use 
	- classification_methods : executes the classification methods selected by the user, and returns a dictionary
	- regression_methods : executes the regressions methods selected by the user, and returns a dictionary

To use classification_methods or regression_methods the user will need to pass their dataset, a list of methods to run, and a scoring function. The user has the ability to pass a dictionary, instead of a list, if they want to use non-default parameters. 

The user can pass a custom scorer, or use an out-of-box scorer from sklearn.metrics
