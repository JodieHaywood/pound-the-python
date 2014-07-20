import pandas as pd
import numpy as np


def firstFun(x):
    '''do some stuff!'''
    print x
    return x


class general:
    
    def __init__(self, param1, param2 = 'string', param3 = None, namedMethod = 'firstMethod', **kwargs):
        '''param1 is required
        param2 is default to the value "string"
        param3 is default to None
        namedMethod will run general.firstMethod() by default
        or you can give it the name of some other method you want to run!
        **kwargs along with the initParam method will 
        let you intantiate any parameter by the name you give it...
        obj = general(param1 = 1, x = 1, y = 2, z = 4)
        x, y, z will now exist as properties of the instance obj'''
        
        self.initParam(kwargs)
        self.param1 = param1
        self.param2 = param2
        if param3 is not None:
            self.param3 = param3
        self.runMethod(method = namedMethod) #this will run the method named in namedMethod
        
    def initParam(self, kwargs):
        '''initalize the given argument structure as properties of the class
        to be used by name in specific query execution'''
        self.argList = []
        for key, value in kwargs.items():
            self.argList.append(key)
            setattr(self,key,value)

    def runMethod(self, method):
        '''call the query method by name during the initialization procedure'''
        methodToCall = getattr(self, method)
        result = methodToCall()
        
    def firstMethod(self):
        '''this method will run by default by calling the runMethod from
        the namedMethod argument'''
        #do stuff!
        pass #pass is a good place holder for do stuff