'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to count occurrences of a substring in a string    
'''

def count_substring(str1,str2):
          '''
          Description: 
              The function to return the count of the substirng   
          Parameters:
              str1: str - The main string
              str2: str - The sub string
          Return :
              count : int - The count of the substring
          '''
        
          return str1.count(str2)

def main():
    str1="Good blood bad blood"
    str2='blood'
    print(count_substring(str1,str2))
    
if __name__=="__main__":
    main()