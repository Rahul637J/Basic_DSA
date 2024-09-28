'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python script to sort (ascending and descending) a dictionary by value.    
'''

def sortByValues(dictionary):
          '''
          Description: 
              This fuction sort the dictionary in ascending and descending by values   
          Parameters:
              dictionary: dict: the input value for sorting 
          Return :
              None
          '''
        # Sort the dictionary by values in ascending order
          sorted_dict = sorted([(value, key) for key, value in dictionary.items()])
        #   print("sorted in ascending order",sorted_dict)

          print()

         # Sort the dictionary by values in descending order
          sorted_dict = sorted([(value, key) for key, value in dictionary.items()],reverse=True)
        #   print("sorted in descending order",sorted_dict)          
        
def main():
       dictionary={'D':2,'I':4,'C':1,'T':3}
       sortByValues(dictionary)
       for key,value in dictionary.items():
        print(key,value,end=" ,")
    #    print(dictionary)
    
if __name__=="__main__":
    main()