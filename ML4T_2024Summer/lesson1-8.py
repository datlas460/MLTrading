import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(X):
    #given a scalar X, return some value (a real number)
    Y = (X-1.5)**2 + 0.5
    print(f"X = {X}, Y= {Y}") # for tracing
    return Y


def error(line,data):
    # compute error between given line and data
    '''Parameters
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is the intercept
    data: 2D array where each row is a point (x,y)
    '''
    #metric sum of squared Y-axis difference
    err = np.sum((data[:,1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err


def fit_line(data, error_func):

    '''
    :param data: 2D arra where each row is a point (X0,Y)
    :param error_func: function that computes the error between a line and observed data
    :return:  line that minimizes the error function
    '''

    #Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])])

    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth = 2.0, label = 'Initial Guess')
    plt.show()
    print(f'l: {l}')
    print(f'x_ends: {x_ends}')
    # Call optimizer to minimize error function

    result = spo.minimize(error_func, l, args=(data,), method = 'SLSQP', options={'disp' : True})
    return result.x

def test_run():
    #define original line
    l_orig = np.float32([4, 2])
    print(f'Original line: C0 = {l_orig[0]}, C1 = {l_orig[1]}')
    xOrig = np.linspace(0, 10, 21)
    yOrig = l_orig[0] * xOrig + l_orig[1]
    plt.plot(xOrig, yOrig, 'b--', linewidth=2.0, label='Original line')



    #generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, yOrig.shape)
    data = np.asarray([xOrig, yOrig + noise]).T
    plt.plot(data[:,0], data[:, 1],  'go', label="Data points")


    #try to fit a line to this data
    l_fit = fit_line(data, error)
    print(f"Fitted line: C0 = {l_fit[0]}, C1 = {l_fit[1]}")
    plt.plot(data[:,0],  l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label='best-fit')


    # Add a legend and show plot
    plt.legend(loc='upper right')
    plt.show()







    # Xguess = 2.0
    # min_result = spo.minimize(f, Xguess, method='SLSQP',options={'disp': True})
    # print(f'Minima found at: X = {min_result.x}, Y = {min_result.fun}')
    #
    # #plot functions, mark minima
    # xPlot = np.linspace(0.5,2.5,21)
    # yPlot = f(xPlot)
    # plt.plot(xPlot, yPlot)
    # plt.plot(min_result.x, min_result.fun, 'ro')
    # plt.title('Minima of an objective function')
    # plt.show()



if __name__ == '__main__':
    test_run()