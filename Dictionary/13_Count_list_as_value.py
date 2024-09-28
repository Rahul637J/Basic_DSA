'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to count number of items in a dictionary value
        that is a list.    
'''
def countListasValue(dictionary):
          '''
          Description: 
              The function to count the number of list in the dictionary as a value   
          Parameters:
              dictionary: dict: The dictionary for the input 
          Return :
              listcount: The count of list as value
          '''

          listCount=0
          for key,values in dictionary.items():
                if isinstance(values,list):
                      listCount+=1
          return listCount

def main():
    dictionary={
          "fruits":"apple",
          "id":[1001,2001,3001,4001],
          "numbers":[1,2,3,4]
    }
    print(countListasValue(dictionary))
    
if __name__=="__main__":
    main()