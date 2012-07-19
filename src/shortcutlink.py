#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 16-07-2012

@version: 0.1
@author: Łukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

import sys
from modules import server

def main():
    try:
        port = 8080
        
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
        
        if port == 0:
            print "Port is not value 0!"
            sys.exit(1)
        
        svr = server.MultiThreadedHTTPServer(('127.0.0.1', port),
                                             server.HTTPHandler)
        print 'Starting...'
        print 'Ctrl+C to stop.'
        svr.serve_forever()
    except KeyboardInterrupt:
        print '\nStop server.'
        svr.socket.close()

if __name__ == "__main__":
    main()
