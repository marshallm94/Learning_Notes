## Parametric Models

### GLMS

#### Linear Regression

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

#### Logistic Regression

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
y_hat =- mod.predict(x_test)

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

#### Regularized Regression

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
