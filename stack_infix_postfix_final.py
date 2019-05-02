# PROGRAM IMPLEMENTING STACK AS WELL AS USING IT FOR INFIX TO POSTFIX AND POSTFIX EVALUATION


class Stack:
    '''
    Objective: To implement a stack class and perform stack operations.
    '''
    stack = []                #Empty Stack
    def __init__(self):
        '''
        Objective: To initialize a stack.
        Input    : Object of class Stack
        Output   : None
        '''
        self.stack=[]
        
    def Push(self,ele):
        '''
        Objective : To push an element onto stack.
        Input     : Integer
        Output    : None
        '''
        #Approach : Make use of append() function.

        self.stack.append(ele)


    def isEmpty(self):
        '''
        Objective : To check whether stack is empty.
        Input     : Object of class Stack
        Output    : Boolean value ; True if stack is empty.
        '''

        if len(self.stack)==0:
            return True


    def Pop(self):
        '''
        Objective : To pop an element from stack.
        Input     : None
        Output    : Element popped out of stack.
        '''

        #Approach : Make use of pop() function.

        if self.isEmpty()!=True:
            return self.stack.pop()


    def Top(self):
        '''
        Objective : To return top element of stack.
        Input     : Object of class Stack
        Output    : Top element of stack.
        '''
        
        return self.stack[-1]
            
    def Display(self):
        '''
        Objective: To display stack.
        Input     : Object of class Stack
        Output    : None
        '''
        for ch in range(len(self.stack)-1,-1,-1):
            print(self.stack[ch])
            print('_____')


def InfixToPostfix(infix):
    '''
    Objective : To convert infix notation to postfix notation.
    Input     : Expression in infix form.
    Output    : Expression in postfix form.
    '''

    #Approach : if character is operand,append it with result string otherwise push it onto stack.
    #           If its precedence is low or equal to top element of stack,append that element with final string and push operator.


    s=Stack()           #Initialize the stack to be used
    postfix=[]          #List is used which will contain the postfix expression

    #Setting the operators priority a dictionary
    OpPriorities={
                    ')':0,
                    '+':1,
                    '-':1,
                    '*':2,
                    '/':2,
                    '^':3,
                    '(':4
                    }

    for c in infix:
    
        if c.isalnum()==True:           #checking if c is operand or not
            postfix.append(c)           # appending if c is operand

        elif s.isEmpty():               #now is it is operator then checking if stack is empty or not if empty then just push the operator
            s.Push(c)


        elif OpPriorities[c]>OpPriorities[s.Top()]:     #comparing the priority of operator with the operator on top if it is more then push
            s.Push(c)

        else:                                       

            while s.isEmpty()!=True and OpPriorities[c]<=OpPriorities[s.Top()]:

                if s.Top()!='(':
                    postfix.append(s.Pop())

                elif c==')':

                    while s.Top()!='(':
                        postfix.append(s.Pop())
                    s.Pop()
                    break

                else:
                    break

            if c!=')':
                s.Push(c)

    while s.isEmpty()!=True:
        postfix.append(s.Pop())

    print(''.join(postfix))


def PostFixEvaluation(postfix):
    '''
    Objective : Evaluate postfix notation.
    Input     : Expression in postfix form
    Output    : Result after evaluation.
    '''
    #Approach : If character is operand,push it onto the stack otherwise pop top two elements and perform corresponding operation and push result onto stack.

    s=Stack()

    for c in postfix:

        if c.isdigit()==True:
            s.Push(c)

        else:

            op1=s.Pop()
            op2=s.Pop()

            res=eval(op2+c+op1)
            s.Push(str(res))

    print(s.Pop())


def main():
    '''
    OBJECTIVE : To call the Infix to postfix and Postfix evaluation function with proper values
    Input : None
    Output : None
    '''

    #Approach : Call the function according to the choice of user for infix and postfix and evaluate the expression
    
    while True:
        print("**************************************************")
        print("Application of Stack: \n1. Convert Infix to Postfix \n2. Evaluate Postfix Expression \n3. Exit \nEnter your choice (1-3) : ")

        ch = input()

        if ch == "1":
            string = input("Enter the expression to be evaluated: ")
            #string = string.split()
            InfixToPostfix(string)


        elif ch == "2":
            #PostFixEvaluation("2131*+9-")
            inp = input("Enter the Postfix expression to be evaluated (Separate operand and operators by space): ")
            inp = inp.split()
            PostFixEvaluation(inp)


        elif ch == "3":
            print("Exiting.... ")
            break

        else:
            print("Kindly enter correct choice number! ")
    return


if __name__ == "__main__":
    main()
