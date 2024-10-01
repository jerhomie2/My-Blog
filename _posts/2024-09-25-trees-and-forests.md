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

Imagine we have a dataset that looks like this.



### Regression Trees in R

To 

```{r}
library(tidymodels)
library(rpart)

my_mod <- decision_tree(tree_depth = tune(),
    cost_complexity = tune(),
    min_n=tune()) %>% #Type of model
    set_engine("rpart") %>% # What R function to use
    set_mode("regression")

## Create a workflow with model & recipe

## Set up grid of tuning values

## Set up K-fold CV

## Find best tuning parameters

## Finalize workflow and predict
```

### Regression Trees in Python

### Random Forests

### Random Forests in R

### Random Forests in Python