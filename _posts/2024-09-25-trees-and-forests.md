---
layout: post
title: "Regression Trees"
date: 2024-09-25
description: How to implement regression trees in R and Python
image: "/assets/img/forest.jpg"
display_image: false  # change this to true to display the image below the banner
---

# intro



### Why Not Just Use Linear Regression?

Linear Regression is a commonly used tool for predictive analysis, and for good reason. The computational efficiency and interpretability of linear regression make for a simple, easy-to-use model.

But this technique also comes with some blind spots. Most real-world relationships don't come in exactly linear patterns, and even with model transformations, linear regression often isn't equipped to deal with all of the complexities inherent in these relationships. That's where Regression Trees come in.

### Regression Trees

Regression trees are useful because they help us deal with some of those complexities that linear regression can't, and they usually result in better predictions. The idea is that rather than trying to follow a trend in the data, a tree will designate splitting points, called branches, over and over until all we have are a bunch of small clusters of similar data points. We call these clusters "leaves".

![Regression Tree]("https://github.com/jerhomie2/My-Blog/blob/main/assets/img/tree.png")

### Regression Trees in R

So how do we implement Regression trees in R code? Let's go through it step by step using the built in 'mtcars' dataset. 

First, we'll want to load all of our necessary libraries

```python
library(ggfortify)
library(rpart)
library(rpart.plot)
```

Now we can read in our data.

```{r}
# Load example data (using the built-in mtcars dataset)
data(mtcars)
```

It's always a good idea to plot the data we're interested to get an idea of what we're looking at. In r, I prefer to use ggplot (in the ggfortify library) to plot my data.

```{r}
# Plot the variables we're interested in
ggplot(data = mtcars,
       mapping = aes(x = hp, y = wt, col = mpg)) +
  geom_point() +
  xlab("Horsepower") +
  ylab("Weight") +
  ggtitle("MPG by Horsepower and Weight")
```

Next, we'll want to make a regression tree model, which will split the data into branches and leaves according to our specifications. Note that regression trees are exceptionally susceptible to overfitting, so we want to make sure to "prune" it back so it doesn't grow too many brances. You can do this using the minsplit, maxdepth, or cp arguments when initializing the model.

```{r}
# Fit a regression tree model
# Here, we predict 'mpg' based on horsepower and weight
# Each leaf node will have a minimum of 8 data points in it
model <- rpart(mpg ~ hp + wt, data = mtcars, minsplit = 8)

# View the model summary
summary(model)
```

The rpart.plot library is great for visualizing the tree that your model has fit and where it decided to split into seperate branches.

```{r}
rpart.plot(model)
```

You can then use your model to make predictions on new data, perhaps a testing dataset. (I just reused the mtcars dataset, but in a real world situation, you'd obviously predict on something else)

```{r}
# Make predictions
predictions <- predict(model, newdata = mtcars)
```

### Regression Trees in Python

I'll now show you how to do the same thing in Python.

Again, we'll want to load all of the necessary libraries

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
```

Then we can load in our data. For this example I'll use the built in 'mpg' dataset which is similar to R's mtcars data. I'll call the dataset mtcars for uniformity. 

```python
# Load the built-in mtcars dataset (you can use seaborn to load it)
mtcars = sns.load_dataset('mpg').dropna()  # use mpg dataset, drop null values
mtcars
```

We'll plot the data using the seaborn library.

```python
# Plot the variables we're interested in
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(x=mtcars['horsepower'], y=mtcars['weight'], hue=mtcars['mpg'])
scatter.set(title="MPG by Horsepower and Weight", xlabel="Horsepower", ylabel="Weight")
plt.show()
```

In Python, we have to split our data into explanatory variables (called features) and response variables (called targets) before we can set up our model.

```python
# Split data into features and target
x = mtcars[['horsepower', 'weight']]  # Features: horsepower and weight
y = mtcars['mpg']  # Target: miles per gallon (mpg)
```

Then we can set up the model. Once again, we're using horsepower and weight to predict the mpg (miles per gallon) of the cars in the dataset. We use the DecisionTreeRegressor function to set up this model.
Also not that I'm setting a minimum number of data points to 50 this time because this dataset is much bigger than the one we used in R and will still have plenty of splitting points.

```python
# Fit a regression tree model
model = DecisionTreeRegressor(min_samples_split=50)  # Each leaf node will have at least 50 samples
model.fit(x, y)
```

Using the matplotlib.pyplot library and the plot_tree function from the mklearn.tree library, we can plot our tree.

```python
# View the model summary (visualize the decision tree)
plt.figure(figsize=(15, 8)) # these parameters just make the figure a bit bigger
plot_tree(model, feature_names=['horsepower', 'weight'], filled=True, rounded=True)
plt.show()
```

We can now use our model to make predictions. I'm again just using the data we already have (x), but in another situation, you'll likely want to put in outside data to see how well your model predicts.

```python
# Make predictions
predictions = model.predict(x) # this function takes just the input values as arguments

# View predictions
print(predictions[:5])  # View first 5 predictions
```