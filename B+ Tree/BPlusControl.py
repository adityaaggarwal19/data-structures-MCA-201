from Record import *
from createfile import *
from createIndexFile import *
from Node import *

if __name__=="__main__":

    b = None
    
    while True:
                
        print("**************************** B+ TREE *********************************")
        print("1. Create record file")
        print("2. Create index file")
        print("3. Print whole index file")
        print("4. Search for a record")
        print("5. Index Position File ")
        print("6. Data Position File ")
        print("7. Exit")
        try:
            ch=int(input("\n Enter your choice (1-7): "))
        except ValueError:
            print("Invalid choice")
            break
        
        if ch == 1:
            createFile(int(input("Enter the number of records you want to create:")))
            print("Record file and position file created..")
            
        elif ch == 2:
            n = int(input("Enter the number of records you want to add in B+ tree:"))
            b = BPlus()
            f1 = open('Datafile.txt','rb')
            for i in range(n):
                obj = pickle.load(f1)
                print("Inserting Key:",obj.getKey())
                b.recordInsert(obj)
            f1.close()
            
            f2 = open('IndexPos.txt','wb')
            pickle.dump(b.nodeAddress,f2)
            f2.close()

            print("Index file and index position file created..")
            

        elif ch == 3:
            f1 = open('IndexFile.txt','rb')
            n = 0
            for i in b.nodeAddress:
                print("\nNODE "+ str(n)+":")    
                f1.seek(i)
                print(pickle.load(f1))
                n += 1

        elif ch == 4:
            try:
                f = open("IndexPos.txt","rb")
                print(pickle.load(f))
                f.close()
            except EOFError:
                pass

        elif ch == 5:
            try:
                f = open("Datapos.txt","rb")
                print(pickle.load(f))
                f.close()
            except EOFError:
                pass

        elif ch == 6:
            n = int(input('Enter the key:'))
            search(n)
        
        else:
            break

