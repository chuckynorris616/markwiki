# Copyright (c) 2014, Matt Layman
'''A model of MarkWiki users'''


class User(object):

    def __init__(self, name, email, login_type, password_digest):
        self.name = name
        self.email = email
        self.login_type = login_type
        self.password_digest = password_digest
