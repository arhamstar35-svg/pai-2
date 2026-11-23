# Machine Learning Study Notes

Beginner-friendly notes and Python examples for introductory Machine
Learning.

## 1. What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence in which
computers learn patterns from data and use those patterns to make
predictions or decisions.

### Main types of Machine Learning

-   **Supervised Learning:** The model learns from examples that include
    the correct answers (labels).
-   **Unsupervised Learning:** The model finds patterns in data without
    supplied labels.
-   **Reinforcement Learning:** An agent learns by taking actions and
    receiving rewards or penalties.

## 2. Supervised Learning: Features and Target

A supervised dataset commonly contains:

-   **X (features):** The input information used to make a prediction.
-   **y (target/labels):** The correct output the model is learning to
    predict.

Example:

``` python
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]
```

Imagine `X` represents study hours and `y` represents results:

    Study hours (X) Result (y)
  ----------------- ------------
                  1 Fail (0)
                  2 Fail (0)
                  3 Fail (0)
                  4 Pass (1)
                  5 Pass (1)
                  6 Pass (1)

Each inner list in `X` represents one sample. Scikit-learn expects
feature input `X` to be two-dimensional: rows are samples and columns
are features. The target `y` is usually one-dimensional.

## 3. Classification

Classification is a supervised learning task in which a model predicts a
category or class.

Examples:

-   Email: Spam or Not Spam
-   Student result: Pass or Fail
-   Image: Cat, Dog, or Bird

### Types of classification

1.  **Binary classification:** Exactly two classes, such as Pass/Fail.
2.  **Multiclass classification:** More than two mutually exclusive
    classes, such as Apple/Banana/Orange.
3.  **Multilabel classification:** One sample can receive more than one
    label, such as an image tagged Car, Person, and Tree.

### Common classification algorithms

#### 3.1 Logistic Regression

Despite the word "Regression", Logistic Regression is commonly used for
classification. It estimates class probabilities. For binary
classification, the sigmoid function maps a score to a value between 0
and 1.

``` python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[5]])
probabilities = model.predict_proba([[5]])

print("Predicted class:", prediction[0])
print("Class probabilities:", probabilities)
```

#### 3.2 Decision Tree

A Decision Tree makes predictions by asking questions about features. It
has:

-   **Root node:** The first split or question.
-   **Branches:** The paths resulting from a split.
-   **Leaf nodes:** Final predicted classes or values.

``` python
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print(model.predict([[5]]))

plot_tree(
    model,
    feature_names=["Study hours"],
    class_names=["Fail", "Pass"],
    filled=True
)
plt.show()
```

Decision Trees are easy to interpret but can overfit if they become too
complex.

#### 3.3 K-Nearest Neighbors (KNN)

KNN predicts a class by finding the K closest training samples and using
their majority class.

``` python
from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print(model.predict([[5]]))
```

`n_neighbors=3` means the model considers the three nearest training
samples. Feature scaling is often important for KNN because it uses
distances.

#### 3.4 Random Forest

Random Forest combines predictions from many Decision Trees. For
classification, the trees vote and the most popular class is generally
selected.

``` python
from sklearn.ensemble import RandomForestClassifier

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print(model.predict([[5]]))
```

`n_estimators=100` means the forest contains 100 trees.

#### 3.5 Support Vector Machine (SVM)

SVM tries to find a decision boundary that separates classes while
maximizing the margin between the boundary and the closest training
points.

``` python
from sklearn.svm import SVC

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = SVC()
model.fit(X, y)

print(model.predict([[5]]))
```

#### 3.6 Naive Bayes

Naive Bayes is a family of probabilistic classifiers based on Bayes'
theorem. It makes a simplifying assumption that features are
conditionally independent given the class.

``` python
from sklearn.naive_bayes import GaussianNB

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

print(model.predict([[5]]))
```

### Classification algorithm comparison

  -----------------------------------------------------------------------
  Algorithm                           Main idea
  ----------------------------------- -----------------------------------
  Logistic Regression                 Estimates class probabilities

  Decision Tree                       Splits data using feature-based
                                      questions

  KNN                                 Uses the classes of nearby samples

  Random Forest                       Combines many Decision Trees

  SVM                                 Finds a separating boundary with a
                                      large margin

  Naive Bayes                         Uses Bayes' theorem and a
                                      conditional-independence assumption
  -----------------------------------------------------------------------

## 4. Regression

Regression is a supervised learning task in which a model predicts a
continuous numerical value.

Examples:

-   House price
-   Salary
-   Temperature
-   Sales amount

### Linear Regression

Linear Regression models a relationship between input features and a
numerical target using a linear equation.

For one feature:

\[ `\hat{y}`{=tex} = b_0 + b_1x \]

-   `x`: input feature
-   `ŷ`: predicted value
-   `b0`: intercept
-   `b1`: slope/coefficient

Example: if the learned equation is `marks = 10 + 10 * hours`, then 6
study hours gives a prediction of 70 marks.

``` python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Input feature: study hours (2D)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Target: marks
y = np.array([20, 30, 40, 50, 60])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted marks:", prediction[0])
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

plt.scatter(X, y, label="Actual data")
plt.plot(X, model.predict(X), label="Regression line")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
```

For this dataset, the model learns a slope of 10 and an intercept of 10,
so the prediction for 6 hours is 70.

## 5. Classification vs Regression

  Classification                      Regression
  ----------------------------------- ---------------------------------
  Predicts a class/category           Predicts a numerical value
  Example: Spam/Not Spam              Example: House price
  Example: Pass/Fail                  Example: Marks
  Common model: Logistic Regression   Common model: Linear Regression

A quick way to remember:

-   Classification asks: **Which category?**
-   Regression asks: **How much?**

## 6. Typical Scikit-learn workflow

A common supervised-learning workflow is:

1.  Import the required libraries.
2.  Load or prepare the dataset.
3.  Separate features (`X`) and target (`y`).
4.  Split data into training and testing sets.
5.  Scale features when the chosen algorithm benefits from scaling.
6.  Create the model.
7.  Train using `model.fit(X_train, y_train)`.
8.  Predict using `model.predict(X_test)`.
9.  Evaluate the predictions.

### Train-test split example

``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test)
print("Accuracy:", accuracy_score(y_test, predictions))
```

-   Training data is used to fit the model.
-   Testing data is held aside to evaluate performance on unseen
    samples.
-   `test_size=0.2` reserves 20% of the data for testing.
-   `random_state=42` makes the split reproducible.
-   `stratify=y` helps preserve class proportions in classification
    splits.

For real projects, use enough data and make sure the test set is not
used during model training or tuning.

## 7. Feature scaling

Feature scaling puts numerical features on comparable scales. It is
often useful for distance- or margin-based algorithms such as KNN, SVM,
and Logistic Regression.

Example using `StandardScaler`:

``` python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Important: fit the scaler on training data only, then use that fitted
scaler to transform the test data. This avoids data leakage.

## 8. Useful evaluation terms

### Classification

-   **Accuracy:** Proportion of predictions that are correct.
-   **Precision:** Of the samples predicted positive, how many were
    actually positive?
-   **Recall:** Of all actual positive samples, how many did the model
    find?
-   **F1-score:** Harmonic mean of precision and recall.
-   **Confusion matrix:** Table comparing actual classes with predicted
    classes.

``` python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, predictions))
print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
```

### Regression

-   **MAE:** Mean Absolute Error; average absolute prediction error.
-   **MSE:** Mean Squared Error; average squared prediction error.
-   **RMSE:** Square root of MSE, expressed in the target's units.
-   **R²:** A measure of how well the model explains variation in the
    target relative to a baseline.

## 9. Important Python / Scikit-learn methods

  -----------------------------------------------------------------------
  Method or attribute                 Purpose
  ----------------------------------- -----------------------------------
  `LinearRegression()`                Creates a Linear Regression model

  `LogisticRegression()`              Creates a Logistic Regression
                                      classifier

  `DecisionTreeClassifier()`          Creates a Decision Tree classifier

  `KNeighborsClassifier()`            Creates a KNN classifier

  `RandomForestClassifier()`          Creates a Random Forest classifier

  `SVC()`                             Creates an SVM classifier

  `GaussianNB()`                      Creates a Gaussian Naive Bayes
                                      classifier

  `model.fit(X, y)`                   Trains a model

  `model.predict(X)`                  Predicts outputs

  `model.predict_proba(X)`            Returns class probabilities when
                                      supported

  `model.score(X, y)`                 Returns the estimator's default
                                      score

  `model.coef_`                       Linear model coefficients, when
                                      available

  `model.intercept_`                  Linear model intercept, when
                                      available
  -----------------------------------------------------------------------

## 10. Quick revision

-   **Machine Learning:** Learning patterns from data.
-   **Supervised Learning:** Training with inputs and known target
    answers.
-   **X:** Input features.
-   **y:** Target values or labels.
-   **Classification:** Predicting categories.
-   **Regression:** Predicting numerical values.
-   **Linear Regression:** Fits a linear relationship to predict a
    number.
-   **Logistic Regression:** Estimates class probabilities for
    classification.
-   **Decision Tree:** Makes predictions through feature-based splits.
-   **KNN:** Uses nearby training examples.
-   **Random Forest:** Combines multiple Decision Trees.
-   **SVM:** Finds a separating boundary with a large margin.
-   **Naive Bayes:** Uses probability and Bayes' theorem.
-   **Overfitting:** A model fits training data too closely and may
    generalize poorly.
-   **Train-test split:** Separates data for model fitting and
    evaluation.

------------------------------------------------------------------------

## Suggested repository structure

``` text
machine-learning-notes/
├── README.md
├── classification/
│   ├── logistic_regression.py
│   ├── decision_tree.py
│   ├── knn.py
│   ├── random_forest.py
│   ├── svm.py
│   └── naive_bayes.py
├── regression/
│   └── linear_regression.py
└── requirements.txt
```

Suggested `requirements.txt`:

``` text
numpy
pandas
matplotlib
scikit-learn
```

These notes are a starting point. Add separate Python files, datasets,
experiments, and explanations as you learn more.
