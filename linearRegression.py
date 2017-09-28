import math

# x is the set of x-variables and y the set of y-variables
def calculateLinearRegressionLine(x, y):
    
    # First, calculate the standard deviations of each set of variables.
    x_standardDeviation = math.sqrt(sum((i - sum(x) / len(x))**2 for i in x) / len(x))
    y_standardDeviation = math.sqrt(sum((i - sum(y) / len(y))**2 for i in y) / len(y))
    
    # Next, calculate the correlation between the x and y variables.
    