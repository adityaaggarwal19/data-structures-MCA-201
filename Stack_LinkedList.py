class Node:
    def __init__(self,value):
        '''
        OBJECTIVE:
        Input Parameter
        '''
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        '''

        '''
        self.top=None
    def push(self,value):
        if self.top == None:
            self.top=Node(value)
        else:
            nod=Node(value)
            nod.next=self.top
            self.top=nod
        def pop(self):
            if self.top==None:
                return "Stack Underflow"
            else:
                nod=self.top
                value=self.top.data
                self.top=self.top.next
                del temp
                return value
            def isEmpty(self):
                return self.top==None
            def top(self):
                if not(self.isEmpty()):
                    return self.top.data
                else:
                    return "Empty Stack"
            def __str__(self):
                nod=self.top
                res=""
                if self.top==None:
                    return "Empty Stack"
                else:
                    while(nod!=None):
                        res+=str(nod.data)+"->"
                        nod=nod.next
                    return res
                
