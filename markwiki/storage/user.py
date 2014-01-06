# Copyright (c) 2014, Matt Layman

from abc import ABCMeta
from abc import abstractmethod


class UserStorage(object):
    '''An abstract interface that all user storage services must implement'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, config):
        '''The constructor will be supplied the application's configuration.'''

    @abstractmethod
    def initialize(self):
        '''Initialization will occur shortly after construction so the service
        can perform any initial setup before it is used by the application.'''

    @abstractmethod
    def create(self, user):
        '''Create a new user. Raise ``UserStorageError`` on failure.'''