'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to calculate the length of a string    
'''

def string_Length(word):
          '''
          Description: 
              The function to return the length of string   
          Parameters:
              word: string: The string input for finding length
          Return :
              length of the word
          '''
        
          return len(word)

def main():
    word="Hello World"
    print(string_Length(word))
    
if __name__=="__main__":
    main()