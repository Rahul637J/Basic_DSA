'''
@Author: Rahul 
@Date: 2024-08-04
@Last Modified by: Rahul 
@Last Modified time: 2024-08-04
@Title: Python program to print a dictionary in table format    
'''
from prettytable import PrettyTable
def dictionaryToTable(data):
          '''
          Description: 
              The function to create the table by dictionary using prettytable module
          Parameters:
              data: dict: The dictionary to create table  
          Return :
              table: The table by prettytable module
          '''

          table=PrettyTable()
          table.field_names=["Key","Value"]
          for key,value in data.items(): # data.items() return --> dict_items 
                table.add_row([key,value])
          return table      

def main():
    data={
          "name":"Rahul",
          "age":22,
          "Degree":"B.E",
          "Role":"Data Engineer"
          }
    table= dictionaryToTable(data)
    print(table)
    
if __name__=="__main__":
    main()