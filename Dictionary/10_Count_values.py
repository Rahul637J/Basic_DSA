'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to count the values associated with key in a
        dictionary.    
'''
def valueCount(listOfDictionary):
          '''
          Description: 
              The function to count the key as success and true as value    
          Parameters:
              listOfDictionary: The list of Dictionary value
          Return :
              success_count: int: The count of the succes is True
          '''
          success_count=0
          for dictionary in listOfDictionary:
               if "success" in dictionary and dictionary['success']==True:
                    success_count+=1
                              
          return success_count                             
                            
def main():
    listOfDictionary=[
            {'id': 1, 'success': True, 'name': 'Lary'},
            {'id': 2, 'success': False, 'name': 'Rabi'}, 
            {'id': 3, 'success': True, 'name': 'Alex'}
            ]
    print(valueCount(listOfDictionary))
    
if __name__=="__main__":
    main()