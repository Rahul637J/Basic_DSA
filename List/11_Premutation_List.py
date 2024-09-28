'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to generate all permutations of a list in Python   
'''
import itertools
def create_Permutation(list1):
          '''
          Description: 
              The function generates all possible permutations of the input list.
          Parameters:
              list1: list - The list of elements to generate permutations for.
          Return:
              iterator: An iterator that produces tuples, each representing a permutation of the input list.
          '''
          
          return itertools.permutations(list1)
          

def main():
    list1=[1,2,3]
    permutations=create_Permutation(list1)
    for permu in permutations:
          print(permu)
    
if __name__=="__main__":
    main()