import math

# x is the set of x-variables and y the set of y-variables
def calculateLinearRegressionLine(x, y):
    
    # First, calculate the variances and standard deviations of each set of variables.
    
    # Calculate the variance.
    x_mean = sum(x) / len(x)
    i = 0
    for j in x:
        i += (j - x_mean)**2
    # The standard deviation is the square root of the variance.
    x_standardDeviation = math.sqrt(i / len(x))
    
    y_mean = sum(y) / len(y)
    i = 0
    for j in y:
        i += (j - y_mean)**2
    y_standardDeviation = math.sqrt(i / len(y))