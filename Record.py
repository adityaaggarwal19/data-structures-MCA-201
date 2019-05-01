import numpy
class Record:
    '''
    Objective: To represent a node/record entity
    '''
    def __init__(self, key):
        
        '''
        Objective: To initialise a Record/node object
        Input Parameters:
                    self : (implicit) Record/node object
                    key  : key value of Record/node
        '''
        self.key = numpy.int64(999000+key)
        self.others = str(self.key)*100  # constant size records
        
    def getKey(self):
        '''
        Objective: To return the key value of the object.
        Input Parameters:
                    self: (implicit) Record object
        Output: Key of the object
        '''
        return self.key

    def getOthers(self):
        '''
        Objective: To return the othets value of the object.
        Input Parameters:
                    self: (implicit) node object
        Output: others of the object
        '''
        return self.others

    def __str__(self):
        return ("Key => " + str(self.getKey()) + "\nOthers => " + str(self.getOthers()))


