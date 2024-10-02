library(ggfortify)
library(rpart)
library(rpart.plot)

# Load example data (using the built-in mtcars dataset)
data(mtcars)

# Plot the variables we're interested in
plot <- ggplot(data = mtcars,
               mapping = aes(x = hp, y = wt, col = mpg)) +
  geom_point() +
  xlab("Horsepower") +
  ylab("Weight") +
  ggtitle("MPG by Horsepower and Weight")
plot


# Fit a regression tree model
# Here, we predict 'mpg' (miles per gallon) based on horsepower and weight
model <- rpart(mpg ~ hp + wt, data = mtcars, minsplit = 8) 
  # each leaf node will have a minimum of 8 data points in it

# View the model summary
summary(model)

# Plot the regression tree
rpart.plot(model)

# Make predictions
predictions <- predict(model, newdata = mtcars)

# View predictions
head(predictions)

