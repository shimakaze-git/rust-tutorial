# -*- coding: utf-8 -*-
'''
Created on 2018/06/27

@author: shimakaze-git
'''
class Komoju:
    """Komoju Base class"""

    def __init__(self):
        pass

    @classmethod
    def connect(self, api_key, options):
        print(api_key)
        print(options)
        options = self.custom_options(options)
        # uri = 

    def custom_options(self):
        pass

# class Komoju():

# require 'komoju/version'
# require 'komoju/client'
# require 'moneta'

# module Komoju
#   def self.connect(api_key, options=nil)
#     options = custom_options(options)
#     uri = URI.parse(options[:url])
#     uri.user = api_key
#     uri.password = ""
#     client = Heroics.client_from_schema(SCHEMA, uri.to_s, options)
#     Client.new(client)
#   end
# end