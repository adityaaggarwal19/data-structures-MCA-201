import random, pickle
from Record import Record

def createFile(n=100):
    '''
    Objective: To write objects of record
    Input Parameter:
           n: no. of records to be written
    SIDE EFFECTS: A file is created
    '''
    f = open('Data', 'wb')
    f1 = open('Datafile', 'wb')
    keys=[]
    rec=[]
    for i in range(1,n+1):
        key=random.randint(0,n*10)
        while key in keys:
            key=random.randint(0,n*10)
        keys.append(key)
        r=Record(key)
        loc=f.tell()
        pickle.dump(r,f)
        rec.append(loc)
    pickle.dump(rec,f1)
    print(str(n) + " records created... ")
    f.close()
    f1.close()


def printFile(fileName):
    '''
    OBJECTIVE : To print the entire given file.
    INPUT :
        filename : Name of the file whose contents are to be printed.
    RETURN : None
    '''
    with open(fileName,'rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except EOFError:
                break

def printDataRange(start, end):
    '''
    OBJECTIVE : To print the data in the given file within the given range.
    INPUT :
        filename : Name of the file whose contents are to be printed.
        first : First record no.
        last  : Last record no.
    RETURN : None
    '''
    
    f = open('Datafile','rb')
    f1 = open('Data','rb')
    a = pickle.load(f)
    for i in range(start,end+1):
        rec1 = a[i]
        f1.seek(rec1)
        print(pickle.load(f1))

def indexrec(i):

    f = open('Datafile','rb')
    f1 = open('Data','rb')
    a = pickle.load(f)
    rec1 = a[i]
    f1.seek(rec1)
    print(pickle.load(f1))

def main():
    createFile()
    i = int(input("Enter the index for which you need to access the record: "))
    indexrec(i)
    start = int(input("Enter the starting index: "))
    end = int(input("Enter the ending index: "))
    printDataRange(start, end)
    print("100000 records creation started")
    #createFile(100000)
    
if __name__=="__main__":
    main()
