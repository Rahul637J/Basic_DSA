'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple    
'''
        
def main():
    sequenceOf=[int(i) for i in input("Enter the sequence of character: ").split(",")]
    tupleSequence=tuple(sequenceOf)

    print(sequenceOf)
    print(tupleSequence)
    
if __name__=="__main__":
    main()