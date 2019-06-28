#!/usr/bin/env python
import os
import glob
import json

def directory_mp3_parse(dir_name):
    """ This function parses the given directory for mp3 files
    Output:
         list of strings(directory names)
     """
    pattern = os.path.join(dir_name, "*.mp3")

    return glob.glob(pattern)


def config_parse(filepath):
    """
    Parses the config.json file

    Output:
          dict
    """
    with open(filepath) as json_file:
        data = json.load(json_file)
    return data

def search_pool_helper(pool_name, pool_list):
    pool_to_return = None

    if pool_list == None:
        return pool_to_return

    for pool in pool_list:

        if pool["pool_name"] == pool_name:
            pool_to_return = pool
            break

        pool_to_return = search_pool_helper(pool_name, pool["child"])

    return pool_to_return

def search_pool_name_in_config(pool_name, config):
    """
    Searches the pool name and returns it if it exists

    Input:
        pool_name: (string) pool name
        config: (dict) parsed config
    Output:
        (dict) pool
    """

    pool_list = config["sound_pool"]

    pool = search_pool_helper(pool_name, pool_list)

    return pool
