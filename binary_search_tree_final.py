# PROGRAM TO IMPLEMENT BINARY SEARCH TREE

class Node:
    '''
    To make a node for Binary Search Tree
    '''
    def __init__(self,value):
        '''
        OBJECTIVE: To make constructor of class Node
        INPUT PARAMETERS:
                    self (implicit parameters): Object of class Node
                    value: Value to be inserted in the node being created
        SIDEEFFECT: A node is created
        '''
        self.right=None
        self.left=None
        self.data=value

class BSTree:
    '''
    To represent the Binary Search Tree
    '''

    def __init__(self):
        '''
        OBJECTIVE: To make constructor of class BSTree
        INPUT PARAMETERS:
                    self (implicit parameters): Object of class BSTree
                    lst: Default Parameter list which can be initialized with a list of numbers
        SIDE EFFECTS: A tree is initialized
        '''
        self.root=None

    def insertEltCall(self,value):
        '''
        OBJECTIVE: To insert the elements in a list wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    value: Value to be insert
        SIDE EFFECTS: A node with given value is inserted in the Binary Search Tree
        '''
        return self.insertElt(value,self.root)


    def insertElt(self,value,temp):
        '''
        OBJECTIVE: To insert the elements in a list
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    value: Value to be insert
                    temp
        SIDE EFFECTS: A node with given value is inserted in the Binary Search Tree
        '''
        if temp!=None:

            if temp.data<value:

                if temp.right==None:
                    nod=Node(value)
                    temp.right=nod
                    return

                else:
                    return self.insertElt(value,temp.right)
            else:

                if temp.left==None:
                    nod=Node(value)
                    temp.left=nod
                    return

                else:
                    return self.insertElt(value,temp.left)

        else:

            if temp==self.root:
                nod=Node(value)
                self.root=nod
                return
                

    def searchEltCall(self,value):
        '''
        OBJECTIVE: To search the elements in a list wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    value: Value to be insert
        OUTPUT : Print Element found if element is there in tree else print Element Not found
        '''
        return self.searchElt(value,self.root)


    def searchElt(self,value,temp):
        '''
        OBJECTIVE: To search the elements in a list
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    value: Value to be insert
                    temp
        SIDE EFFECTS: A node with given value is inserted in the Binary Search Tree
        '''
        if temp!=None:

            if temp.data == value:
                print("Element found ... ")
                return

            elif temp.data<value:
                if temp.right==None:
                    print("Element Not Found")
                    return
                else:
                    return self.searchElt(value,temp.right)

            else:
                if temp.left==None:
                    print("Element Not Found")
                    return
                else:
                    return self.searchElt(value,temp.left)

        else:
            return

    
    def inorder(self,temp):
        '''
        OBJECTIVE: To print the INORDER Traversal of tree
        INPUT:
            self: Implicit Parameter
            temp: The node currently being accessed
        Return: string to be printed with result
        '''
        res=""
        if temp!= None:
            res+=str(self.inorder(temp.left))
            res+=str(temp.data)+" "
            res+=str(self.inorder(temp.right))
            return res
        else:
            return res

    def countNodesCall(self):
        '''
        OBJECTIVE: To count the nodes in the binary search tree wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
        RETURN: A count with number of nodes in Binary Search Tree is return
        '''
        return self.countNodes(self.root)

    def countNodes(self,temp):
        '''
        OBJECTIVE: To count the nodes in the binary search tree
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    temp: The node currently being accessed
        RETURN: A count with number of nodes in Binary Search Tree is return
        '''
        count=0
        if temp!=None:
            count+=1
            count+=self.countNodes(temp.left)
            count+=self.countNodes(temp.right)
            return count
        else:
            return count

    def heightTreeCall(self):
        '''
        OBJECTIVE: To height of the binary search tree wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
        RETURN: A count with number of nodes in Binary Search Tree is return
        '''
        return self.heightTree(self.root)       

    def heightTree(self,temp):
        '''
        OBJECTIVE: To find height of the binary search tree
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
                    temp: The node currently being accessed
        RETURN: Height of Binary Search Tree is return
        '''
        if temp==None or (temp.left==None and temp.right==None):
            return 0
        else:
            return max(self.heightTree(temp.left),self.heightTree(temp.right)) + 1

    def __str__(self):
        '''
        OBJECTIVE: To print the binary search tree
        INPUT:
            self: Implicit Parameter
        Return: res
        '''
        res= self.inorder(self.root)
        return res

    def preorderCall(self):
        '''
        OBJECTIVE: To height of the binary search tree wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
        RETURN: A count with number of nodes in Binary Search Tree is return
        '''
        return self.preorder(self.root)  
    
    def preorder(self,temp):
        '''
        OBJECTIVE: To print the PREORDER Traversal of tree
        INPUT:
            self: Implicit Parameter
            temp: The node currently being accessed
        Return: string to be printed with result
        '''
        res=""
        if temp!= None:
            res+=str(temp.data)+" "
            res+=str(self.preorder(temp.left))
            res+=str(self.preorder(temp.right))
            return res
        else:
            return res

    def postorderCall(self):
        '''
        OBJECTIVE: To height of the binary search tree wrapper function
        INPUT PARAMETERS:
                    self (implicit parameter): Object of class
        RETURN: A count with number of nodes in Binary Search Tree is return
        '''
        return self.postorder(self.root)
    
    def postorder(self,temp):
        '''
        OBJECTIVE: To print the POSTORDER Traversal of tree
        INPUT:
            self: Implicit Parameter
            temp: The node currently being accessed
        Return: string to be printed with result
        '''
        res=""
        if temp!= None:
            res+=str(self.postorder(temp.left))
            res+=str(self.postorder(temp.right))
            res+=str(temp.data)+" "
            return res
        else:
            return res

def main():
    '''
    OBJECTIVE: To define main function
    Return: None
    '''
    b= BSTree()
    while True:
        print("*******************************************************\nOptions are:")
        print("1.. To insert in Binary Search Tree ")
        print("2.. To print the inorder traversal of Binary Search Tree")
        print("3.. To print number of nodes in Binary Search Tree")
        print("4.. To print the height of Binary Search Tree ")
        print("5.. To print the postorder traversal of Binary Search Tree")
        print("6.. To print the postorder traversal of Binary Search Tree")
        print("7.. To delete in binary Search Tree ")
        print("8.. To search a given node in binary Search Tree")
        print("9.. Exit\n")

        ch=input("Enter your choice (1-9): ")


        if ch == "1":
            val=int(input("Enter the value to be inserted: "))
            #for i in range(1,11):
                #b.insertEltCall(i)
            b.insertEltCall(val)

        elif ch == "2":
            if b.root == None:
                print("Tree is empty")
            else:
                print(b)

        elif ch == "3":
            if b.root == None:
                    print("Tree is empty")
            else:
                r = b.countNodesCall()
                print(r)

        elif ch == "4":
            if b.root==None:
                    print("Tree is empty!! ")
            else:
                r = b.heightTreeCall()
                print(r+1)

        elif ch == "5":
            if b.root == None:
                print("Tree is empty")
            else:
                res = b.postorderCall()
                print(res)

        elif ch == "6":
            if b.root == None:
                print("Tree is empty")
            else:
                res = b.preorderCall()
                print(res)

        elif ch == "7":
            pass

        elif ch == "8":
            val=int(input("Enter the value to be searched: "))
            b.searchEltCall(val)

        elif ch == "9":
            print("Exiting... ")
            break

        else:
            print("Kindly enter correct choice")
    return

if __name__=="__main__":
    main()
