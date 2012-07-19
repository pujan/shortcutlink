#-*- coding: utf-8 -*-

'''
Created on 18-07-2012

@version: 0.1
@author: Łukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

class File(object):
    '''
    Operating for file
    '''

    def __init__(self, filename=''):
        '''
        Constructor
        '''
        
        self.filename = filename
        self.file = None # file descritor
        self.opened = False
        self.error = '' # last error message
    
    def append(self, data):
        '''Save data string to end file
        data - string type
        '''
        
        if self.opened == False:
            self.error = 'File not opened'
            return False
        
        if self.file == None:
            self.error = 'File is None'
            return False
        
        self.file.write(data)
        
        return True
    
    def save(self, data):
        '''Save data dictionary to file - truncates the file
        data - dictionary data'''
        
        if self.opened == False:
            self.error = 'File not opened'
            return False
        
        if self.file == None:
            self.error = 'File is None'
            return False
        
        ds = DictString()
        self.file.truncate()
        self.file.write(ds.dict2data(data))
        
        return True 
    
    def load(self):
        '''Load data from file and convert to dictionary
        and return dictionary'''
        
        if self.opened == False:
            self.error = 'File not opened'
            return None
            
        if self.file == None:
            self.error = 'File is None'
            return None
        
        ds = DictString()
        
        data = self.file.read()
        
        if data == '':
            return None
        
        return ds.data2dict(data.strip())
    
    def open(self, filename=''):
        '''Open file name'''
        
        if self.opened:
            self.error = 'File not opened'
            return False
        
        name = None
        
        if filename != '':
            name = filename
        elif self.filename != '':
            name = self.filename
        else:
            return False
        
        self.file = open(name, 'a+')
        
        if self.file != None:
            self.opened = True
        else:
            self.error = 'File is None'
            return False
    
        return True
    
    def close(self):
        '''Close file'''
        
        if self.file != None:
            self.file.close()
            self.opened = False
    
# end class File    

class DictString(object):
    '''Dictionary to data file strukture (string):
    url1    url2
    url1    url2
    ...
    and vice versa
    '''

    def dict2data(self, dict):
        '''Dictionary to string'''
        return '\n'.join(['%s\t%s' % (key,value) for (key,value) in dict.items()])
    
    def data2dict(self, string):
        '''String to dictionary'''
        
        return dict([entry.split('\t') for entry in string.split('\n')])

# end class DictString
