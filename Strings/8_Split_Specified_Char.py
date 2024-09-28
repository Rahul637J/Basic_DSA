'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to get the last part of a string before a specified character    
'''

def splitString(word,character):
          '''
          Description: 
              The function will return the last part of a string by specifed character     
          Parameters:
              word: str: The input string
              character: str: The specified character to split 
          Return :
              str: The last part of the string before the specified character
          '''
        
          return word.rsplit(character,1)[0]

def main():
    word="https:/www.w3resource.com/python-exercises/String"
    character='/'
    print(splitString(word,character))
    
if __name__=="__main__":
    main()