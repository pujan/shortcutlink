#-*- coding: utf-8 -*-

'''
Created on 16-07-2012

@version: 0.1
@author: Łukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

from modules import server

def main():
    try:
        svr = server.MultiThreadedHTTPServer(('127.0.0.1', 8080),
                                             server.HTTPHandler)
        print 'Starting...'
        print 'Ctrl+C to stop.'
        svr.serve_forever()
    except KeyboardInterrupt:
        print '\nStop server.'
        svr.socket.close()

if __name__ == "__main__":
    main()