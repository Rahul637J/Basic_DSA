'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python script to concatenate following dictionaries to create a new    
'''
def concatinateDictionary(*dictionarys):
          '''
          Description: 
              The function to concatinate different dictionary to new disctionary
          Parameters:
              *dictionarys: dict: variable number of dictionaries to concatinate
          Return :
              new_dictionary: A single dictionary containing all key-value pairs from the input dictionaries.
          '''
          new_dictionary={}
          for dictionary in dictionarys:
                new_dictionary.update(dictionary)
          
          return new_dictionary
        
def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    new_dictionary=concatinateDictionary(dic1,dic2,dic3)
    print(new_dictionary)
    
if __name__=="__main__":
    main()