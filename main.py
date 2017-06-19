# -*- coding: utf_8 -*-
'''
Created on 2017/06/11

@author: ken
'''
import webapp2
import os
from google.appengine.ext.webapp import template

class Auth_User(webapp2.RequestHandler):

    def get(self):
        return

class Main_Page(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), './templates/index.html')
        self.response.out.write(template.render(path, template_values))
        return

app = webapp2.WSGIApplication([('/',Main_Page)
                               ],debug=True)