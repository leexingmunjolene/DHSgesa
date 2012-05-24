#!/usr/bin/env python

import webapp2	# web application framework
import jinja2	# template engine
import os		# access file system
from google.appengine.api import users	# Google account authentication
from google.appengine.ext import db		# datastore

# initialize template
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Contact(db.Expando):
	''' User data model '''
	pid = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	email = db.EmailProperty(required=True)
	remark = db.TextProperty()

class MainHandler(webapp2.RequestHandler):
	''' Home page handler '''

	def get(self):
		''' Show home page '''
        # check if valid Google account
		user = users.get_current_user()
	
		if user:	# if valid logged in user
			self.redirect('/arrange')

		else:
			self.redirect('/login')
		
			

		# create index.html template
#			template = jinja_environment.get_template('index.html')
		# associate template values with template
#			self.response.out.write(template.render(template_values))

class Login(webapp2.RequestHandler):
	def get(self):
		template_values = {
			'contact': contact,
			'greeting': greeting,
			'url': users.create_login_url(self.request.uri),
			'url_linktext': url_linktext}
			# login link
		# create index.html template
		template = jinja_environment.get_template('index.html')
		# associate template values with template
		self.response.out.write(template.render(template_values))
		
			
class Arrange(webapp2.RequestHandler):
	''' Update contact '''
	def get(self):
		template = jinja_environment.get_template('seatingarr.html')
		template_values = {'url':users.create_logout_url(self.request.uri)}
	#	'contact': contact}
		self.response.out.write(template.render(template_values))

# main
#contact1 = Contact(pid='lee.xingmun.jolene', name='LEE XING MUN JOLENE', email='lee.xingmun.jolene@dhs.sg')
#contact1.put()
app = webapp2.WSGIApplication([('/', MainHandler), ('/arrange', Arrange),('/login',Login)],
                              debug=True)