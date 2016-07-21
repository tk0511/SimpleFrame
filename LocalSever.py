#-*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from fm import *

@get('/')
def index():
    return {'data':'Index'}

@get('/path1/*')
def haha_():
    return {'data':'* Match all'}

@get('/path1/path2')
def lala():
    return {'data':'Here is path2'}

@get('/haaaa')
def haa():
    return {'data':'haaaaaaaaaaaaaaaaaaaaaa'}

@get('/path1/counter','path_info','http_cookie')
def papa(path,cookie):
    count = int(cookie.split('=')[1])+1 if cookie else 0
    return {'data':path + ' | ' + cookie if cookie else '',
            'header':{'set-cookie':'count=%d'%count}}

@get('/favicon.ico')
def ico():
    return {'data':open('favicon.ico','rb').read(),
            'header':{'Content-Type':'image/x-icon',
                      'Cache-Control':'max-age=30'}}


#----------------Run sever---------------
port = 8080
httpd = make_server('', port, qs())
print("Sever runing at http://localhost:%d" % port)
httpd.serve_forever()
