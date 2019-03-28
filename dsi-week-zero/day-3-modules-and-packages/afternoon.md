# Afternoon assignment

## numpy


1. Write a function that takes in a one-dimensional numpy array and standardizes it (i.e. subtracts off the mean and divides by the standard deviation). Return the standardized array.

2. Now create a version of 1 that takes in a two-dimensional numpy array and standardizes it along the columns (i.e. for each column subtract off its mean and divide by its standard deviation). Return the standardized array. Hint: use the `axis` parameter of the `mean` method.

3. Write a function that creates a numpy array of an inputted shape, filled with an inputted number. Your function should have three parameters - num_cols, num_rows, and fill_value. As an example, if I called your function with num_cols=4, num_rows=3, and fill_value=2, then your function should return a 3 by 4 array of 2s. Return the newly created array. Hint: the function `np.zeros` might help.

4. Write a function that takes in one argument, an int, and creates a one-dimensional array that is the inputted number of elements long. Make the one-dimensional array full of random floating point numbers between 0 and 1 (Hint: Check out numpy.random.random()). Return the resulting array.

5. Alter your solution to 4 to take in two parameters that will denote the final shape of your array of random floating point numbers (so now you will potentially end up with a two-dimensional array). Name these parameters num_rows and num_cols. Return the resulting array.

6. Write a function that will take in a one-dimensional numpy array and replace the maximum element in it with a 0. Return the resulting array.

7. Write a function that takes in an int, creates a one-dimensional numpy array of the numbers from 0 up to the argument (but not including it), and then returns an array with the cumulative sum of all those numbers. For example, if the argument is 5, it should return `array([0, 1, 3, 6, 10])`.

8. Write a function that takes in a two-dimensional numpy array and returns the smallest 5 elements of each column (Hint: The axis parameter on the numpy function you use might come in handy here).


9. Calculating distances in an array.

For this problem you will be using the iris dataset, a classic set of 150 observations of three different species of iris flowers by Roland Fisher. For each the length and width of the petals and sepals were measured. We aren't going to worry around the species for this or which feature is which; just think of in at 150 data with four features each, or 150 points in four-dimensional space. In the questions below, n is the number of data points (150 in this case, but don't assume it in your functions) and p is the number of features (4 in this case, but don't assume this except when reading the data).

9.0.) The data is located in `data/iris.csv`. Write a function that will take a filehandle as an argument and read the csv into a `numpy array`, and return the array. Ignore the final column (the species name). For bonus points: don't assume the number of rows when reading it.

9.1. Write a function that takes two arguments, both rows in the dataset, both of shape (p,). Return the euclidean distance between those two points (the square root of the sum of the squares of the differences between the components). Try to do this without using a loop.

9.2. Write a function that takes two arguments, one a row the dataset (an array of shape (p,) and the entire data set (shape (n, p). It should return an array of shape (n,) giving distance from the first argument to each point in the dataset. For the first attempt feel free to use a loop, but do it without a loop if you can.

9.3. Write a function that takes one argument, the entire dataset of shape (n,p). In should return an array of shape (n, n) giving the distance from each point to each other point (the diagonal elements should be zero). Again, feel free to use loops, but it is possible to do without.



## matplotlib

For this we'll again be using the iris dataset.

0. Write a new function to load the data, but this time return two `array`s. The first should be of shape (150, 4) and include the first four columns; the second should be of shape (150,) and return the last column (the species name).

1. Create a scatter plot of the first column (the sepal length) against the second (the sepal width).

2. Select all the measurements corresponding to the species "setosa". Use a boolean mask (created from the second `array`) and use it to index the first.

3. Create a the same scatter plot, but in three colors corresponding to the species. For this you should iterate over the species names, select the appropriate rows, and plot them. Use the `label` parameter of plot and `ax.legend()` to label the species.

4. Write a function that takes an the two arrays and an axis as an argument and creates the plot the array on the axis. Add two optional arguments specifying which columns of the original array to plot against each other.
