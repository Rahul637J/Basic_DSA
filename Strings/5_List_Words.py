'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python function that takes a list of words and returns the length of the longest
        one.    
'''

def length_Of_Longest(listOWords):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          longest_Length=0
          for word in listOWords:
                if len(word) > longest_Length:
                      longest_Length=len(word) 
          return longest_Length

def main():
    listOfWords=["Hello","Worlding"]
    print(length_Of_Longest(listOfWords))
    
if __name__=="__main__":
    main()