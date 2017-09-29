import math

# x is the set of x-variables and y the set of y-variables
def calculateLinearRegressionLine(x, y):
    
    # First, calculate the standard deviations of each set of variables.
    x_standardDeviation = math.sqrt(sum((i - sum(x) / len(x))**2 for i in x) / len(x))
    y_standardDeviation = math.sqrt(sum((i - sum(y) / len(y))**2 for i in y) / len(y))
    
    # Next, calculate the correlation between the x and y variables.
    avg_x = float(sum(x)) / len(x)
    avg_y = float(sum(y)) / len(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(len(x)):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff
    r_xy_correlation = diffprod / math.sqrt(xdiff2 * ydiff2)
    
    # Using the calculated standard deviations and correleation, calculate the slope of the regression line.
    