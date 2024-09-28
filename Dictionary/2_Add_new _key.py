'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python script to add a key to a dictionary    
'''
def addKey(dictionary):
          '''
          Description: 
              The function to add new key in the existing dictionary   
          Parameters:
              dictionary: dict: The exisitng dictionary
          Return :
              dictionary: dict: existing dictionary with new key
          '''
          dictionary[len(dictionary)]=30
          return dictionary
        
def main():
    dictionary= {0: 10, 1: 20}
    print("Before Adding:",dictionary)
    dictionary=addKey(dictionary)
    print("After adding",dictionary)
    
if __name__=="__main__":
    main()