from Record import Record
from createfile import *
from tryy import *

if __name__=="__main__":

    b = None
    
    while True:
                
        print("**************************** B+ TREE *********************************")
        print("1. Create record file")
        print("2. Create index file")
        print("3. Print whole index file")
        print("4. Search for a record")
        print("5. Exit")
        try:
            ch=int(input("\n Enter your choice:"))
        except ValueError:
            print("Invalid choice")
            break
        
        if ch == 1:
            createFile(int(input("Enter the number of records you want to create:")))
            print("Record file and position file created..")
            
        elif ch == 2:
            n = int(input("Enter the number of records you want to add in B+ tree:"))
            b = BPlus()
            f1 = open('Data','rb')
            for i in range(n):
                obj = pickle.load(f1)
                print("Inserting Key:",obj.getKey())
                b.insertRecord(obj)
            f1.close()
            
            f2 = open('IndexPos.txt','wb')
            pickle.dump(b.nodeAddress,f2)
            f2.close()

            print("Index file and index position file created..")
            

        elif ch == 3:
            f1 = open('indexfile.txt','rb')
            n = 0
            for i in b.nodeAddress:
                print("\nNODE "+ str(n)+":")    
                f1.seek(i)
                r = pickle.load(f1)
                print(r)
                n += 1

        elif ch == 4:
            n = int(input('Enter the key:'))
            search(n)
        
        else:
            break
