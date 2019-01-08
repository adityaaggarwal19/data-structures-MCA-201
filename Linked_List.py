class Node:
    def __init__(self,value):
        '''
        OBJECTIVE:
        Input Parameter
        '''
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        '''

        '''
        self.head=None
    def insertAtBegin(self,value):
        '''
        '''
        if self.head==None:
            nod=Node(value)
            self.head=nod
        else:
            nod=Node(value)
            nod.next=self.head
            self.head=nod
    def delAtBegin(self):
        '''

        '''
        if self.head==None:
            return None
        else:
            nod=self.head
            value=self.head.data
            self.head=self.head.next
            del nod
            return value
    def delNode(self,value):
        '''

        '''
        if self.head==None:
            return "Empty List"
        if self.head.data==value:
            nod=self.head
            self.head=self.head.next
            ret =str(nod.data)
            del nod
            return ret
        else:
            curr=self.head
            prev=None
            while curr!=None and current.data!=value:
                prev=curr
                curr=curr.next
            if curr!=None:
                prev.next=curr.next
                ret=str(curr.data)
                del curr
                return ret
            else:
                return "Node with desired value is not there"
    def __str__(self):
        '''

        '''
        curr=self.head
        res=""
        if self.head==None:
            return "Empty List"
        else:
            while curr!=None:
                res+=str(curr.data) + "->"
                curr=curr.next
            return res

            
def main():
    '''

    '''
    lst=LinkedList()
    while True:
        ch=int(input("1.. Insert at Beginning \n2.. Delete at Beginning \n3.. Print the Linked List \n4.. Exit \n Tell your choice of operation "))
        if ch==1:
            value=int(input("Enter the value to be inserted"))
            lst.insertAtBegin(value)
        elif ch==2:
            value=lst.delAtBegin()
            print(value)
        elif ch==3:
            print(lst)
        elif ch==4:
            break
        else:
            print("You have entered a wrong choice. Kindly select your choice again")
if __name__=="__main__":
    main()






                                










