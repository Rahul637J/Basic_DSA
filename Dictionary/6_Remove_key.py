'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Finding the day by the date    
'''
def removeKey(dictionary,key):
          '''
          Description: 
              The function to remove the key from the existing    
          Parameters:
              dictionary: existing dictionary to remove key
              key: the key value to remove in dictioanry
          Return :
              dictionary: the updated dictionary
          '''
          del dictionary[key]
          return dictionary
          
        
def main():
       dictionary={
              1: 1,
              2: 4,
              3: 9,
              4: 16,
              5: 25
              }
       key=5
       print(removeKey(dictionary,key))
    
if __name__=="__main__":
    main()