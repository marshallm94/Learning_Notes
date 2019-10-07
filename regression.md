---
title: "General Linear Models (GLMS)"
author: "Marshall McQuillen"
output: 
  pdf_document:
    toc: true
    toc_depth: 3
    latex_engine: xelatex
urlcolor: blue
---

## Linear Regression

* With linear regression, each coefficient can be interpreted as the the change in the response for a one unit change in the predictor, holding all else constant.

* When there are interaction terms in the equation, such as $$y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \beta_3X_1X_2$$ you can rewrite the equation to be $$y = \beta_0 + \tilde{\beta_1}X_1 + \beta_2X_2~~where~~\tilde{\beta_1} = \beta_1 + \beta_3X_2$$ where $\beta_3$ can be interpreted as the change in the **effectiveness of $X_1$ on y for a one unit change in $X_2$.**

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline

mod = LinearRegression()
mod.fit(x_train, y_train)
y_hat = mod.predict(x_test)

rmse = np.sqrt(mean_squared_error(y_test, y_hat))

lin_reg_pipe = Pipeline([
    ('column', ColumnSelector(name='column')),
    ('regression', LinearRegression())
])

y_hat = lin_reg_pipe.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_hat))
```

## Logistic Regression

Logistic regression is used in a classification setting, namely when the response is dichotomous (binary). When this is the case, one seeks to model the probability of an observation being a "success" (or "of interest", encoded as a 1) or a failure (encoded as a 0).

Logistic regression is similar to linear regression in that it still assumes the relationship between the attributes **X** and the response **y** is linear, however with one small caveat; logistic regression assumes that the log odds of a success are linear in **X**.

### Reasoning

Since the response in logistic regression is dichotomous, and one would like to model the probability of an observation being a success, a good place to start would be:

$$
P(Y=1|X=x) = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_px_p
$$

$$
P(Y=1|X=x) = \beta_0 + \sum_{j=1}^P \beta_jx_j
$$

However, this opens up the possibility of the output $P(Y=1|X=x)$ taking on a value greater than 1 or less than 0, which violates probabilities. To remedy this, one makes use of the *logistic function* (hence the name), which restricts all output to be within the bounds of 0 and 1, and therefore a valid probability (note that there are two ways to write the logistic function, but they are equivalent and will lead to the same result):

$$
\frac{1} {1 + \epsilon^{-x}} = f(x) =  \frac{\epsilon^x}{\epsilon^x + 1}
$$

So, knowing that one would like the output to be a valid probability, we simply substitute $P(Y=1|X=x)$ into the above equation in place of $f(x)$, where $x$ is equal to the linear model $\beta_0 + \sum_{j=1}^P \beta_jx_j$:

$$
\frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} = P(Y=1|X=x) =  \frac{\epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j}}{\epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j} + 1}
$$

#### Quick Aside on Probability and Odds

In order to illustrate how everything comes together, it is important to note the relationship between the *probability* of an event occurring and the *odds* of an event occurring, given below:

$$
Odds = \frac{P}{1 - P} ~~~ and ~~~ P = \frac{Odds}{Odds + 1}
$$

### Reasoning (continued)

#### Method 1

Now knowing the relationship between probabilities and odds, is clear how the right hand side of the two equations above are related, reproduced below:

$$
\frac{Odds}{Odds + 1} = P(Y=1|X=x) =  \frac{\epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j}}{\epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j} + 1}
$$

Therefore, we can express the odds of a success as:

$$
Odds = \epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j}
$$

Using the natural logarithm on both sides of the equation, it is evident that **the log odds of a succes are linear in the attributes X**.

$$
log(Odds) = log(\epsilon^{\beta_0 + \sum_{j=1}^P \beta_jx_j})
$$

$$
log(Odds) = \beta_0 + \sum_{j=1}^P \beta_jx_j
$$

#### Method 2

The other way to reconcile logistic regression is to look at the other expression of logistic regression, reproduced below:

$$
P(Y=1|X=x) = \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}}
$$

Knowing the above, one can substitute the right side of the equation into the odds ratio and solve for $\beta_0 + \sum_{j=1}^P \beta_jx_j$:

$$
Given ~~~ Odds = \frac{P}{1 - P} ~~~ and ~~~ P(Y=1|X=x) = \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \\
$$
Then:

$$
\begin{aligned}
Odds & = \frac{ \left( \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right)}{1 - \left( \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right)} \\
& = \frac{ \left( \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right)}{\left( \frac{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}}{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right) - \left( \frac{1} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right)} \\
& = \frac{ \left( \frac{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right) }{\frac{\left( 1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)} \right)^2}{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} - \left( \frac{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} {1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \right)} \\
& = \frac{1}{1 + \epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)} - 1} \\
& = \frac{1}{\epsilon^{-(\beta_0 + \sum_{j=1}^P \beta_jx_j)}} \\
& = \epsilon^{(\beta_0 + \sum_{j=1}^P \beta_jx_j)} \\
Log(Odds) & = Log(\epsilon^{(\beta_0 + \sum_{j=1}^P \beta_jx_j)})
\end{aligned}
$$

\pagebreak

**And, once again, the conclusion is made that the log odds of a succes are linear in the attributes X**.

$$
Log(Odds) = \beta_0 + \sum_{j=1}^P \beta_jx_j
$$

### Loss Function

The loss function (or cost function) for logistic regression, called the log loss, is given below:

$$
Log~Loss = - \left( \frac{\sum_{i=1}^N \left(y_ilog(\hat{y_i}) + (1 - y_i)log(1 - \hat{y_i}) \right)}{N} \right)
$$

#### Walkthrough

The key to understanding the loss function is to look at each term in the numerator, reproduced below:

$$
Log~loss = y_i log(\hat{y_i}) + (1 - y_i)log(1 - \hat{y_i})
$$

Since logistic regression is used in a *binary* setting, the response **y** will be a vector of 1's and 0's. Therefore, $y_i$ will be either a 1 or a 0. With that in mind, it is clear that the first part of both terms in the above equation, $y_i$ and $(1 - y_i)$, serve the same functionality that an indicator function serves; if $y_i$ is a 1, the second term in the equation will zero out, and conversely, if $y_i$ is a 0, the first term in the equation will zero out:


$$
If ~~~ y_i = 1, ~~~ Log~loss
\begin{cases}
    = (1)log(\hat{y_i}) +  (1 - 1)log(1 - \hat{y_i}) \\
    = (1)log(\hat{y_i}) \\
    = log(\hat{y_i})
\end{cases}
$$
$$
If ~~~ y_i = 0, ~~~ Log~loss
\begin{cases}
    = (0)log(\hat{y_i}) +  (1 - 0)log(1 - \hat{y_i}) \\
    = (1)log(1 - \hat{y_i}) \\
    = log(1 - \hat{y_i})
\end{cases}    
$$

Now, the output of logistic regression is a **probability**, which is to say $\hat{y_i}$ will be the probability that observation $i$ is a 1. Therefore, the loss function will always be taking the log of a probability. Referencing the formulas above, if $y_i = 1$, $Log~loss = log(\hat{y_i})$ and if $y_i = 0$, $Log~loss = log(1 - \hat{y_i})$.

Since all models seek to **minimize the loss**, ideally the log loss is as close to 0 as possible. As it turns out, $log(1) = 0$. So, when $y_i = 1$, $Log~loss = log(1)$ will minimize the loss, and if $y_i = 0$, $Log~loss = log(1 - 0)$ will minimize the loss. **It is clear that this setup minimizes the error when $\hat{y_i}$ is as close to $y_i$ as possible, averaged over all observations**.

### Interpretation

* Each coefficient of logistic regression is interpreted as the change in the **log of the odds** of a success for a one unit change in the predictor, holding all else constant. To translate this to a probability of a success:

    1.  Plug each predictor value of a test observation into the linear equation, using the respective coefficients and the intercept; this returns the **log odds** of a success for that test observation.$$log(Odds) = \beta_0 + \beta_1X_1 + \beta_2X_2...$$

    2. Exponentiate this value; this removes the log and **returns the odds of a success** for the test observation.$$Odds = \epsilon^{log(Odds)}$$

    3. Divide the odds by one plus the odds (odds / (1 + odds)) and you have the **probability that the test observation is a success**.$$Prob(y_i = 1) = \frac{Odds}{1 + Odds}$$

* *Note that your X matrix (NOT your y vector) must be scaled before being used by sklearn's LogisticRegression() class (it utilizes Lasso, which must have scaled data)*

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metric import accuracy_score, precision_score, recall_score

mod = LogisticRegression
mod.fit(x_train, y_train)
# return predicted probability of being a success
y_hat_probs = mod.predict_proba(x_test)[:, 1]
# returns the predicted class (success or failure)
y_hat = mod.predict(x_test)

acc = accuracy_score(y_test, y_hat)
prec = precision_score(y_test, y_hat)
recall = recall_score(y_test, y_hat)

def log_odds_to_prob(log_odds):
    """
    Converts the log odds of a success into the probability of a success.

    Input:
        log_odds: (int) The log odds of a success / the output of a logistic regression model
    Output:
        Probability: (float) The probability of a success
    """
    odds = np.exp(log_odds)
    prob = odds / (1 + odds)
    return prob
```

## Regularized Regression

* Both Ridge Regression and Lasso Regression both model the relationship between a set **X** of *p* predictors and a quantitative response **y** as a linear model (same as linear regression).

* However, both Ridge and Lasso have an additional term appended onto the loss function of a linear model, the RSS:

    * Ridge: **$\lambda$** multiplied by the summation of the *squares* of all coefficients. ($l2$ penalty)
        * So, the loss function becomes $$RSS + \lambda\sum_{j=1}^p\beta_i^2$$

    * Lasso: **$\lambda$** multiplied by the summation of the *absolute values* of all the  coefficients. ($l1$ penalty)
        * So, the loss function becomes $$RSS + \lambda\sum_{j=1}^p|\beta_i|$$

The tuning parameter **$\lambda$** is best selected using cross validation. The practical difference between Lasso and Ridge regression is that Lasso will set some of the coefficients equal to *exactly zero* while ridge regression shrinks the coefficients *towards zero*.

##### Lasso Regression

```python
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

lassie = Lasso()
lassie.fit(x_train, y_train)
y_hat = lassie.predict(x_test)
print(np.sqrt(mean_squared_error(y_test, y_hat)))
```

##### Ridge Regression

```python
import numpy as np
from sklearn.linear_model import Ridge()
from sklearn.metrics import accuracy_score

ridge = Ridge()
ridge.fit(x_train, y_train)
y_hat = ridge.predict(x_test)
print(np.sqrt(accuracy_score(y_test, y_hat)))
```

## Multicollinearity

### Variance Inflation Factor (VIF)

[Penn State VIF](https://onlinecourses.science.psu.edu/stat501/node/347/)

The VIF is a statistic that can help one determine whether multicollinearity exists in multivariate regression. By regressing each of the $k$ predictors on the remaining predictors, one can obtain an estimate of *how well the $k_{th}$ predictor can be estimated with the other predictors*:

$$
\begin{aligned}
Instead~of~...~\mathbf{y} & = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \cdots + \beta_px_p \\
Build~a~model~...~\mathbf{x_j} & = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \cdots + \beta_{p-1}x_{p-1}
\end{aligned}
$$

In the same manner that the $R^2$ value for a "normal" regression ($y = \beta_0 + \sum_{j=1}^P \beta_jx_j$) illustrates the percentage of the total variance in the response explained by the model, regressing the $k_{th}$ variable on the other predictors can determine if the $k_{th}$ predictor could be (somewhat accurately) predicted by the other predictors.

The VIF for the $k_{th}$ predictor, $VIF_k$, is a measure of how much the variance of the  coefficient for the $k_{th}$ predictor is inflated due to the existence of multicollinearity. Looking at the equation below, it is clear that if $R^2_k = 0$, which is to say there is zero multicollinearity between the $k_{th}$ predictor and the other predictors, the $VIF_k$ would be equal to 1. Alternatively, $VIF's$ exceeding 4 - 5 warrant further investigation, since that indcates there is some multicollinearity.

$$
VIF_k = \frac{1}{1 - R^2_k}
$$










