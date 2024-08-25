#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 03:22:13 2024

@author: codyphelps2_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    #Const Variable to toggle UPDATE_MANY & DELETE_MANY
    TOGGLE_UPDATE_MANY = False
    TOGGLE_DELETE_MANY = False

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
    
        self.USER = 'aacuser'
        self.PASS = 'SNHU1234'
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 31049
        self.DB = 'AAC'
        self.COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    


    def create(self, data):
        """ 
        Method is used to insert data into the DB
        @param data - dictinary value 
        @returns True or False
        """
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return True if result else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    def read(self,query=None):
        """ 
        Method is used to read data from DB
        @param query - Key/Value pair
        @returns List of found data or an empty list
        """
        if query is None:       
            read_data = self.database.animals.find()
            result = list(read_data)
            return result
        else:
            read_data = self.database.animals.find(query)
            result = list(read_data)
            return result

    def update(self, query, update_data):
        """ 
       Method is used to update data in the DB
       @param query - Key/Value pair
       @param update_data - data that will be updated or placed
       @returns number of modifed entities
       """
        if query and update_data is not None:
            if AnimalShelter.TOGGLE_UPDATE_MANY:
               result = self.database.animals.update_many(query, {'$set' : update_data})
            else:
               result = self.database.animals.update_one(query, {'$set' : update_data})
               changed_results = result.modified_count
            return changed_results
        
    def delete(self, query):
        """ 
       Method is used to delete data in the DB
       @param query - Key/Value pair
       @returns number of deleted entities
       """
        if query is not None:
            if AnimalShelter.TOGGLE_DELETE_MANY:
                result = self.database.animals.delete_many(query)
            else:
                result = self.database.animals.delete_one(query)
                num_deleted = result.deleted_count
            return num_deleted
      
    #Toggle Methods
    def toggle_update_many(self):
        """ 
       Method to toggle UPDATE_MANY
       @returns True or False
       """
        AnimalShelter.TOGGLE_UPDATE_MANY = not AnimalShelter.TOGGLE_UPDATE_MANY
        print(f"Update many set to {AnimalShelter.TOGGLE_UPDATE_MANY}")
        
    def toggle_delete_many(self):
        """ 
       Method to toggle DELETE_MANY
       @returns True or False
       """
        AnimalShelter.TOGGLE_DELETE_MANY = not AnimalShelter.TOGGLE_DELETE_MANY
        print(f"Update many set to {AnimalShelter.TOGGLE_DELETE_MANY}")