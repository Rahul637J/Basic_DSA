'''
@Author: Rahul 
@Date: 2024-08-01
@Last Modified by: Rahul 
@Last Modified time: 2024-08-01
@Title: Python program to create a histogram from a given list of integers    
'''

import matplotlib.pyplot as plt

def histogramPlot(data):
    '''
    Description:
        Creates and displays a histogram from the given list of integers.
    Parameters:
        data (list of int): A list of integers for which the histogram is to be plotted.
    Return:
        None
    '''
    plt.hist(data, bins=10, edgecolor='blue')
    plt.xlabel('X-Value')
    plt.ylabel('Y-Value')
    plt.title('Histogram of List Data')
    plt.show()

def main():
    data = [0, 0, 1, 2, 3, 2, 3, 5, 5, 5, 6, 1, 1, 2, 10, 10, 10]
    histogramPlot(data)

if __name__ == "__main__":
    main()
