'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to lowercase first n characters in a string   
'''

def to_Lower(word,length):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          if length>=len(word):
                return "Invalid range"
          new_word=word[:length].lower()
          return new_word+word[length:]

def main():
    word="ENVIRONMENT"
    length=3
    print(to_Lower(word,length))

if __name__=="__main__":
    main()