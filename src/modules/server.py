#-*- coding: utf-8 -*-

'''
Created on 16-07-2012

@version: 0.1
@author: Łukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os
import cgi
import hashlib
import re
import file

# global variables
DEBUG = False
urls = {}
dbfile = file.File('../urls.dat')

if dbfile.open():
    res  = dbfile.load()
           
    if res == None:
        urls = {}
    else:
        urls = res.copy()

class MultiThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Threading server class"""
# end class MultiThreadedHTTPServer

class HTTPHandler(BaseHTTPRequestHandler):
    """Handler class"""

    def getOriginalURL(self):
        """Get original URL and return document"""
        
        path = self.path[1:]
        
        originalUrl = ''
        found = False
        
        for key, value in urls.items():
            if value == path:
                originalUrl = key
                found = True
        
        if not found:
            return None
        
        return originalUrl

    def do_GET(self):
        """Handler for the method GET"""

        if self.path == '/' or self.path == '/index.html':
            self.path = '/html/index.html'

        try:
            sendReply = False

            if self.path.endswith('.html'):
                mimetype = 'text/html'
                sendReply = True
            else:
                link = self.getOriginalURL()
                
                if link == None:
                    raise IOError
                else:
                    self.redirect(link)
                
            if sendReply:
                f = open(os.curdir + os.sep + self.path, 'rb')
                self.sendPage(f.read(), mimetype)
                f.close()

        except IOError:
                self.send_error(404, 'File not found: %s' % self.path)

    def do_POST(self):
        """Handler for the method POST"""

        #global urls, dbfile

        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                'CONTENT_TYPE':self.headers['Content-Type']}
                )
        
        url = form['url1'].value

        if not self.checkURL(url):
            message = 'Niepoprawny adres URL!'
            self.sendPage(self.generatePage(message))

            # exit function
            return
        
        ip, port = self.server.server_address

        if port == 80:
            port = ''
        else:
            port = ':' + `port`

        addr = 'http://' + ip + port + '/'

        # add url to dictionary urls
        if not urls.has_key(url):
            md5 = self.shortURL(url)
            urls[url] = md5
            
            # save to file
            dbfile.append(url + '\t' + md5 + '\n')
            
            message = 'Skrocony URL: ' + addr + md5
            message += '<br/>Oryginalny URL: ' + url
        else:
            message = 'Taki URL jest juz skrocony.<br>'
            message += 'Mozesz uzyc: '
            message += addr
            message += urls[url]
        
        self.sendPage(self.generatePage(message))

    def shortURL(self, longUrl):
        """Generated hash URL"""
        
        return hashlib.md5(longUrl).hexdigest()
    
    def checkURL(self, url):
        """Check address URL"""

        pattern = """
            ^
            (http|https|ftp)\://
            [a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/
            ?([a-zA-Z0-9\-\._\?\,\'/\\\
            +&amp;%\$#\=~])*[^\.\,\)\(\s]
            $
        """

        if re.search(pattern, url, re.VERBOSE) == None:
            return False
        
        return True

    def sendPage(self, page, mimetype='text/html'):
        """Sending page to client"""

        self.send_response(200)
        self.send_header('Content-type', mimetype)
        self.end_headers()
        self.wfile.write(page)

    def generatePage(self, string, title='Shortcut Link'):
        """Add HTML DOM to string and return"""
        page = '<html><head><title>'
        page += title
        page += '</title></head><body>'
        page += string
        page += '</body></html>'

        return page
    
    def redirect(self, url):
        self.send_response(301)
        self.send_header('Location', url)
        self.end_headers()

# end class MyHandler
