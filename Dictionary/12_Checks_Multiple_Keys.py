'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to check multiple keys exists in a dictionarye    
'''
def checksKeysExist(dictioanry,keys):
          '''
          Description: 
              The functon to check the multiple keys present in the dictionary   
          Parameters:
              dictionary: dict: The dictionary to check for the keys present
              keys: list: The list of keys
          Return :
              boolean: The boolean value if all keys are present or not
              
          '''
          for key in keys:
                if key not in dictioanry:
                      return False
          return True      
        
def main():
    dictionary={
          1:'R',
          2:'A',
          3:'H',
          4:'U',
          5:'L'
          }
    keys=[2,4]
    result=checksKeysExist(dictionary,keys)
    print(result)
    
if __name__=="__main__":
    main()