#!/usr/bin/env python

from. import helpers

import random

class Manager(object):
    def __init__(self, config_file):
        self.config = helpers.config_parse(config_file)
        self.folder_name = self.config["sound_directory"]

    def random_sample_pool(self, pool_name):
        """
        Randomly select one sound file from the pool

        Input:
            string pool name
        Output:
            name of the sound file
        """

        pool = helpers.search_pool_name_in_config(pool_name, self.config)

        if pool is None:
            raise Exception("No such pool in the config!")

        file_names = pool["pool_items"]

        if file_names is None:
            raise Exception("Files not found")

        return random.choice(file_names)

    def get_soundfiles__pool(self, pool_name):
        """
        Get a list of sound files from the pool

        Input:
            string pool name
        Output:
            (list) names of the sound file
        """

        pool = helpers.search_pool_name_in_config(pool_name, self.config)

        if pool is None:
            raise Exception("No such pool in the config!")

        file_names = pool["pool_items"]

        if file_names is None:
            raise Exception("Files not found")

        return file_names


    def filter_pool_children_for_person(self, pool_name, person_name):
        """
        Filters the pool according the allowed_people attribute.

        Input:
            pool_name: (string) pool name
            person_name: (string) person name
        Output:
            (list) filtered pool
        """

        pool = helpers.search_pool_name_in_config(pool_name, self.config)

        if pool is None:
            raise Exception("No pool with this name!")

        pool_list = []

        for child in pool["child"]:
            if person_name in child["allowed_people"]:
                pool_list.append(child)

        return pool_list
