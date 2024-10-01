---
layout: post
title: "How To: Regression Trees & Random Forests"
date: 2024-09-25
description: Implement trees and forests in R and Python
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

First, we'll want to read in our data.

```{r}
# Load example data (using the built-in mtcars dataset)
data(mtcars)
```

It's always a good idea to plot the data we're interested to get an idea of what we're looking at. In r, I prefer to use ggplot (in the ggfortify library) to plot my data.

```{r}
# Load necessary libraries
library(ggfortify)

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
library(rpart)

# Fit a regression tree model
# Here, we predict 'mpg' (miles per gallon) based on horsepower and weight
# Each leaf node will have a minimum of 8 data points in it
model <- rpart(mpg ~ hp + wt, data = mtcars, minsplit = 8)

# View the model summary
summary(model)
```

The rpart.plot library is great for visualizing the tree that your model has fit.

```{r}
library(rpart.plot)
rpart.plot(model)
```



```{r}
# Make predictions
predictions <- predict(model, newdata = mtcars)
```

### Regression Trees in Python

### Random Forests

### Random Forests in R

### Random Forests in Python