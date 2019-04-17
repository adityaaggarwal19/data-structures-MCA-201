import pickle,sys, os
class IndexNode:
    '''
    Objective : To create a node in index file.
    '''
    def __init__(self,Maxkeys=4):
        '''
        Objective        : To initialize an object of class IndexNode
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
            Maxkeys                 -> Maximum number of keys in a node.
        Output           : None
        '''
        self.keys = [99999]*Maxkeys
        self.pointers =[99999]*(Maxkeys + 1)

    def __str__(self):
        '''
        Objective        : To return string representation of object.
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
        Output           : String
        '''
        return str(self.keys)+'||'+str(self.pointers)
        

# Records to be inserted in the order
'''
1    2    3     4     5	    6     7     8     9     10
300  200  380   500   350   325   650   337   800   850
'''

threshold = 10000

# node for location of root node
root = IndexNode()
root.keys[0]=1

node1=IndexNode()
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()


# Insert 300
node1.keys[0]=(300 + threshold,1 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()



# Insert 200
node1.keys[0],node1.keys[1]=(200 + threshold,2 ),(300 + threshold,1 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()


# Insert 380
node1.keys[2]=(380 + threshold,3 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()



# Insert 500
node1.keys[3]= (500 + threshold,4 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()



# Insert 350
node2 = IndexNode()
node3 = IndexNode()
root.keys[0] = 3
node1.keys[2],node1.keys[3]=99999,99999
node1.pointers[0] = 2
node2.keys[0],node2.keys[1],node2.keys[2] = (350 + threshold,5),(380 + threshold,3),(500 + threshold,4)
node3.keys[0]= (350 + threshold,5)
node3.pointers[0],node3.pointers[1] = 1,2
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()


# Insert 325
node1.keys[2]= (325 + threshold,6 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()

# Insert 650
node2.keys[3]= (650 + threshold,7 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()


# Insert 337
node1.keys[3]= (337 + threshold,8 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()


# Insert 800
node4 = IndexNode()
node2.keys[2],node2.keys[3]=99999,99999
node2.pointers[0] = 4
node4.keys[0],node4.keys[1],node4.keys[2] = (500 + threshold,4),(650 + threshold,7),(800 + threshold,9)
node3.keys[0]= (350 + threshold,5)
node3.keys[1] = (500 + threshold,4)
node3.pointers[0],node3.pointers[1], node3.pointers[2] = 1,2,4
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
indexfile.close()


# Insert 450
node2.keys[2]= (450 + threshold,10 )
indexfile = open('IndexFile','wb')
pickle.dump(root,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
#pickle.dump(node3,indexfile)
indexfile.close()


# Final Index File
print('****************************INDEX FILE ***********************************')
indexfile = open('IndexFile','rb')
while True:
    try:
        print(pickle.load(indexfile))
    except:
        IOError
        break

print('****************************INDEX FILE 111111111111111111111111111 ***********************************')
indexfile = open('IndexFile','rb')
while True:
    try:
        a = pickle.load(indexfile)
        print("Location is: ", indexfile.tell())
    except:
        IOError
        break
indexfile.close()

print("*************** SEARCH CODE ***************************")
ind = open('IndexFile','rb')
srch = int(input("Enter the number to be searched: "))
ind.seek(0)
flag = 0
a = pickle.load(ind)
srch_n = a.keys[0]
if srch_n == 3:
    addr = 360
ind.seek(addr, os.SEEK_SET)
a = pickle.load(ind)
if srch < a.keys[0][0]:
    if a.pointers[0] == 1:
        addr = 113
    ind.seek(addr, os.SEEK_SET)
    a = pickle.load(ind)
    for i in range(0,3):
        if srch == a.keys[i][0]:
            print("Element found")
            flag = 1
    if flag == 0:
        print("None")
print(ind.tell())
if (srch < a.keys[1][0]) and (srch > a.keys[0][0]):
    if a.pointers[1] == 2:
        addr = 238
    ind.seek(addr, os.SEEK_SET)
    a = pickle.load(ind)
    for i in range(0,3):
        if srch == a.keys[i][0]:
            print("Element found")
            flag = 1
    if flag == 0:
        print("None")
print(ind.tell())

if srch > a.keys[1][0]:
    print("Hello")
    if a.pointers[2] == 4:
        addr = 473
    ind.seek(addr, os.SEEK_SET)
    print(ind.tell())
    a = pickle.load(ind)
    for i in range(0,3):
        if srch == a.keys[i][0]:
            print("Element found")
            flag = 1
    if flag == 0:
        print("None")
