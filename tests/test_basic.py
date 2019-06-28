
# added to demonstrate `find_packages` example in
# setup.py that excludes installing the "tests" package

from robotdialog import helpers
from robotdialog import core

import unittest

class TestHelpers(unittest.TestCase):
    def test_directory_mp3_parse(self):
        self.assertTrue(sorted(helpers.directory_mp3_parse("./sound/"))
         == sorted(
         [
         "./sound/apple_juice.mp3",
         "./sound/guten_morgen.mp3",
         "./sound/guten_tag.mp3",
         "./sound/hallo.mp3",
         "./sound/negative_orange.mp3",
         "./sound/orange_juice.mp3",
         "./sound/positive_orange.mp3",
         "./sound/wait_a_moment.mp3",
         "./sound/wait.mp3",
         "./sound/water.mp3",
         "./sound/water2.mp3",
         "./sound/your_apple_juice.mp3",
         "./sound/your_orange_juice.mp3",
         "./sound/your_water.mp3",
         "./sound/your_water2.mp3"
         ]))


    def test_config_parse(self):
        config = "./config.json"

        parsed_conf = helpers.config_parse(config)

        self.assertEqual(parsed_conf["sound_directory"], "./sound")

    def test_search_pool_name_in_config(self):
        config = "./config.json"

        parsed_conf = helpers.config_parse(config)

        pool = helpers.search_pool_name_in_config("greetings", parsed_conf)

        self.assertEqual(pool["pool_name"], "greetings")

        pool = helpers.search_pool_name_in_config("apple_juice", parsed_conf)

        self.assertEqual(pool["pool_name"], "apple_juice")

        pool = helpers.search_pool_name_in_config("aaasdds", parsed_conf)

        self.assertIsNone(pool)


class TestManager(unittest.TestCase):
    def test_manager_creation(self):
        pass

    def test_random_sample_pool(self):
        manager = core.Manager("./config.json")

        self.assertIsInstance(manager.random_sample_pool("apple_juice"), str)

        self.assertIn(manager.random_sample_pool("water2"),
         ["your_water.mp3","water.mp3"])

    def test_filter_pool_children_for_person(self):
        manager = core.Manager("./config.json")

        self.assertEqual(
             manager.filter_pool_children_for_person("items", "jennifer")[0]["allowed_people"][0],
             "jennifer")

    def test_filter_pool_children_for_person(self):
        manager = core.Manager("./config.json")

        self.assertEqual(sorted(manager.get_soundfiles__pool("water2")),
         sorted(["your_water.mp3","water.mp3"]))

class TestTalker(unittest.TestCase):
    def test_talker_creation(self):
        manager = core.Manager("./config.json")

        talker = core.Talker(manager)

        with self.assertRaises(Exception):
             core.Talker("aaa")



if __name__ == '__main__':
    unittest.main()
