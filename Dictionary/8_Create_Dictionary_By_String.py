'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to create a dictionary from a string   
'''
def createDictionary(word):
          '''
          Description: 
              The function to create the dictionary from stirng   
          Parameters:
              word: string: The string to create dictionary   
          Return :
              dictionary: dict: The dictionary created from the string
          '''

          dictionary = {}
          for i in (word):
                if i not in dictionary:
                      dictionary[i] = 1
                else:
                      dictionary[i] += 1
          return dictionary            
        
def main():
    word="w3resource"
    print(createDictionary(word))
    
if __name__=="__main__":
    main()