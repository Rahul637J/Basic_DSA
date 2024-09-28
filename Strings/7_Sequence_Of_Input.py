'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program that accepts a comma separated sequence of words as input
        and prints the unique words in sorted form    
'''

def sortedUniqueList(listOfString):
          '''
          Description: 
              This function will return the unique string in the sorted form    
          Parameters:
              listOfString: str: The list of string
          Return :
              unique_String: The set of unique string in sorted form
          '''
          unique_stirng=set()
          for word in listOfString:
                 unique_stirng.add(word)
          return sorted(unique_stirng)

def main():
       listOfString=[word for word in input("Enter the word in with ','").split(',')]
       print(sortedUniqueList(listOfString))
    
if __name__=="__main__":
    main()