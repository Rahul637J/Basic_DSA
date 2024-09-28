'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to convert a list into a nested dictionary of keys    
'''
def listToNestedDictionary(listOfValues):
          '''
          Description: 
                 
          Parameters:
              None 
          Return :
              None
          '''
          nested_Dictionary=current={}
          for i in listOfValues:
                current[i]={}
                current=current[i]

          return nested_Dictionary      
        
def main():
    listOfValues=[1,2,3,4,5]
    print(listToNestedDictionary(listOfValues))
    
if __name__=="__main__":
    main()