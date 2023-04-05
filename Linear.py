# In mathematics a function is used to relate one variable to another variable.
# A linear function has one independent variable (x) and one dependent variable (y),
# and has the following form:
# y = f(x) = ax+b
# f(x) = the output (the dependant variable)
# x = the input (the independant variable)
# a = slope = is the coefficient of the independent variable.
# It gives the rate of change of the dependent variable
# b = intercept = is the value of the dependent variable when x = 0.
# It is also the point where the diagonal line crosses the vertical axis.

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv("bigdata.csv")
sb.regplot(x = "Pulse", y = "Calories", data = df)
plt.xlim(0,150)
plt.ylim(200,500)
plt.show()