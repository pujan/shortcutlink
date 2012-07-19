#-*- coding: utf-8 -*-

'''
Created on 18-07-2012

@version: 0.1
@author: Lukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

import unittest
import os
from modules import file

class TestFile(unittest.TestCase):
    def setUp(self):
        self.path = '../data.dat' # temp data file for tests
        self.f = file.File(self.path)
        self.conv = file.DictString()
        
        self.sData = 'https://www.google.pl/#hl=pl&sclient=psy-ab&q=cyfrowy+polsat&'
        self.sData += 'oq=cyfrowy+&gs_l=hp.3.0.0l10.5633682.5635312.3.5636757.8.5.0.3.3.'
        self.sData += '0.267.743.0j4j1.5.0...0.0...1c.iwWnhQOStPc&psj=1&bav=on.2,or.r_gc'
        self.sData += '.r_pw.r_cp.r_qf.,cf.osb&fp=5ce4d70cb58fe2ee&biw=1275&bih=894\t'
        self.sData += 'c2b506acfb14de6eb89afd3041ed9aba\n'
        self.sData += 'https://sites.google.com/site/asciigamegrsh/\t02cf05145b179f964db60885f6c533cf\n'
        self.sData += 'http://jakis.link.pl/jakis-plik.html\t7ee63697ffc7906eec801e1c75098504'
        
        self.dData = {}
        self.dData['http://jakis.link.pl/jakis-plik.html'] \
            = '7ee63697ffc7906eec801e1c75098504'
        self.dData['https://sites.google.com/site/asciigamegrsh/'] \
            = '02cf05145b179f964db60885f6c533cf'
        self.dData['https://www.google.pl/#hl=pl&sclient=psy-ab&q=cyfrowy+polsat&'
              'oq=cyfrowy+&gs_l=hp.3.0.0l10.5633682.5635312.3.5636757.8.5.0.3.3.'\
              '0.267.743.0j4j1.5.0...0.0...1c.iwWnhQOStPc&psj=1&bav=on.2,or.r_gc'\
              '.r_pw.r_cp.r_qf.,cf.osb&fp=5ce4d70cb58fe2ee&biw=1275&bih=894'] \
            = 'c2b506acfb14de6eb89afd3041ed9aba'
        
        # create file for tests
        fp = open(self.path, 'w')
        fp.write(self.sData)
        fp.close()
        
        #self.f.open(self.path)

    def tearDown(self):
        # delete file
        os.unlink(self.path)
        
        # close file
        self.f.close()
        
    
    def testOpenFile(self):
        '''Test open file and member varialbles'''
        
        res = self.f.open(self.path)
        
        self.assertTrue(res, 'Error open file: ' + self.f.error)
        self.assertTrue(self.f.opened, 'Error variable oppened is False: ' + self.f.error)
        self.assertIsNotNone(self.f.file, 'Error variable file is None: ' + self.f.error)
        
    def testDictToString(self):
        '''Test convert dictionary to string'''
        
        Str = self.conv.dict2data(self.dData)
        
        #print str
        #print '-------------------------------------------------'
        #print self.sData
        
        self.assertIsNot(Str, '', 'Error convert dict to str: ' + self.f.error)
        
    def testStringToDict(self):
        '''Test convert string to dictionary'''
        
        dic = self.conv.data2dict(self.sData)
        
        self.assertIsNot(dic, {}, 'Error convert str to dict!')
        
    def testAppendFile(self):
        '''Test append string to end file'''
        
        self.f.open(self.path)
        res = self.f.append('http://localhost/\tc9db569cb388e160e4b86ca1ddff84d7')
        #self.f.close()
        
        self.assertTrue(res, 'Error append to file')
        
    def testSaveFile(self):
        '''Test save file'''
        
        self.f.open(self.path)
        res = self.f.save(self.dData)
        #self.f.close()
        
        self.assertTrue(res, 'Error save to file: ' + self.f.error)

    def testLoadFile(self):
        '''Test load data from file'''
        
        self.f.open(self.path)
        dic = self.f.load()
        #self.f.close()
        
        self.assertIsNotNone(dic, 'Error load data from file: ' + self.f.error)
        
# end class TestFile

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
