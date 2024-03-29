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
