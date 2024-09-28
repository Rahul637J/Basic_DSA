'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program to print all unique values in a dictionary.  
'''
def uniqueValues(listOfValues):
          '''
          Description: 
              The function to return the unique value of in the dictionary  
          Parameters:
              listOfValue: list: The list of dictioary 
          Return :
              unique: set: the unique value in dictionary 
          '''
          unique=set()
          for dictionary in listOfValues:
                for value in dictionary.values():
                    unique.add(value)    
          
          return unique     
        
def main():
    listOfValues=[
          {"V":"S001"},
          {"V": "S002"},
          {"VI": "S001"},
          {"VI": "S005"},
          {"VII":"S005"},
          {"V":"S009"},
          {"VIII":"S007"}
          ]
    print(uniqueValues(listOfValues))
    
if __name__=="__main__":
    main()