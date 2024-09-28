'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to get a list, sorted in increasing order by the last
        element in each tuple   
'''

def sort_list_of_tuple(list1):
    '''
    Description: 
        The function sorts a list of tuples in increasing order based on the last element of each tuple using bubble sort.
    Parameters:
        list1: list - A list of tuples where each tuple contains elements.
    Return:
        list: The list of tuples sorted in increasing order by the last element of each tuple.
    '''

    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j][-1] > list1[j+1][-1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

def main():
    list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_of_tuple(list1))

if __name__ == "__main__":
    main()
