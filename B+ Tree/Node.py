# Class Node defthresholdion

threshold = None


class Node:
    '''
        Objective : To represent a node of B+ Tree. 
    '''
    
    def __init__(self,no,n=4):
        '''
        Objective : To define constructor of class Node
        Input Parameters :
            self : Implicit object
              no : Node number
          parent : Parent of the node
               n : Number of keys in a node
        '''

        # Keys :
        #   data type - Tuple
        #   (key,record no)
        self.keys = [(threshold,threshold)]*n

        # Ptrs :
        #   data type - int
        #   node no
        self.ptrs = [threshold]*(n+1)

        # Node Number:
        self.nodeNo = no

        #Parent :
        self.parent = threshold
        

    def __str__(self):
        '''
        Objective : To define string representation of class Node
        Input Parameters :
            self : Implicit object
        '''
        
        return " KEYS : " + str(self.keys) + "\n LINKS : "+ str(self.ptrs)
