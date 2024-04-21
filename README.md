# Data Science Notes :smile:
This is the beginning of a folder containing varied random stuff to do with data science and its implementation with Python and whatever else.

**Dependencies Imported** (I will update this over time)

* *Pandas* is a library used to import datasets and create data frames, which among other things we can use for analysis or prediction. 

* *Numpy* is a built in python library which helps in doing mathematical functions such as matrix multiplication and conversion.

* *Matplotlib* is a tool used for data visualization and representation.

* *%matplotlib inline* is for those using ipython notebook. It ensures the output (graph) is inside the notebook.


**Extras**

* pandas uses *head* function to give us an overview about the top part of the data frame... By default head() returns the first 5 rows of the data frame.
Similarly the *tail* function tail(15) would return the last 15 items.
* numpy.dot : is equivalent to matrix multiplication for 2-D arrays, to inner product of vectors for 1-D arrays(without complex conjugation). i.e
[1,2,3]*  [6]
		  [7]
		  [8]

* A data structure is a way of organizing data in a computer so it can be used efficiently.

pandas introduces two new data structures to Python - Series and DataFrame, both of which are built on top of NumPy

* A Series is a one-dimensional object similar to an array, list, or column in a table. 
* A DataFrame is a tabular data structure comprised of rows and columns like in a spreadsheet. You can think of a DataFrame as a group of Series objects that share column names.
* Reading a CSV is as simple as calling the read_csv function.

**Decision Trees**
A decision tree automates the process of slicing and dicing to find subsets and outputs a classification model or classifier.

Conceptually, the decision tree algorithm starts with all the data at the root node and scans all the variables for the best one to split on. Once a variable is chosen, you do the split and go down one level (or one node) and repeat. The final nodes at the bottom of the decision tree are known as terminal nodes, and the majority vote of the observations in that node determine how to predict for new observations that end up in that terminal node.

*scikit-learn* can be used to create *tree* objects from the *DecisionTreeClassifier* class.

Requirements to build a decision tree:

* target: A one-dimensional numpy array containing the target/response from the train data. 
* features: A multidimensional numpy array containing the features/predictors from the train data.

One way to quickly see the result of your decision tree is to see the importance of the features that are included. This is done by requesting the *.feature_importances_* attribute of your tree object. Another quick metric is the mean accuracy that you can compute using the *.score()* function with *features_one* and *target* as arguments.

Overfitting and how to control it:

In *DecisionTreeRegressor*, the depth of our model is defined by two parameters:

the *max_depth* parameter determines when the splitting up of the decision tree stops.
the *min_samples_split* parameter monitors the amount of observations in a bucket. If a certain threshold is not reached (e.g minimum 10 passengers) no further splitting can be done.
By limiting the complexity of your decision tree you will increase its generality and thus its usefulness for prediction!

Feature engineering: creatively engineering your own features by combining the different existing variables.

**Random Forest**

Random Forest technique handles the overfitting problem faced with decision trees. It grows multiple (very deep) classification trees using the training set. At the time of prediction, each tree is used to come up with a prediction and every outcome is counted as a vote. For example, if you have trained 3 trees with 2 saying a passenger in the test set will survive and 1 says he will not, the passenger will be classified as a survivor. This approach of overtraining trees, but having the majority's vote count as the actual classification decision, avoids overfitting.

Requirements to build a random forest analysis:

* Use *RandomForestClassifier()* class instead of the *DecisionTreeClassifier()* class.
* *n_estimators* needs to be set when using the *RandomForestClassifier()* class. This argument allows you to set the number of trees you wish to plant and average over.
