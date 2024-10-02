import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split

# Load the built-in mtcars dataset (you can use seaborn to load it)
mtcars = sns.load_dataset('mpg').dropna()  # mpg dataset is similar to mtcars

# Add 'hp' and 'wt' columns since 'mpg' dataset doesn't have them
# Manually creating horsepower (hp) and weight (wt) columns for demonstration purposes
mtcars['hp'] = np.random.randint(50, 300, size=len(mtcars))  # Random hp values
mtcars['wt'] = np.random.uniform(1.5, 5, size=len(mtcars))  # Random wt values

# Plot the variables we're interested in
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(x=mtcars['hp'], y=mtcars['wt'], hue=mtcars['mpg'], palette='coolwarm')
scatter.set(title="MPG by Horsepower and Weight", xlabel="Horsepower", ylabel="Weight")
plt.show()

# Split data into features and target
X = mtcars[['hp', 'wt']]  # Features: horsepower and weight
y = mtcars['mpg']  # Target: miles per gallon (mpg)

# Fit a regression tree model
model = DecisionTreeRegressor(min_samples_split=8)  # Each leaf node will have at least 8 samples
model.fit(X, y)

# View the model summary (visualize the decision tree)
plt.figure(figsize=(15, 8))
plot_tree(model, feature_names=['hp', 'wt'], filled=True, rounded=True)
plt.show()

# Make predictions
predictions = model.predict(X)

# View predictions
print(predictions[:5])  # View first 5 predictions