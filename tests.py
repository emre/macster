import unittest
import os
from macster import macster
import shutil


class MacsterTests(unittest.TestCase):

    TEST_DIRECTORY = '/tmp/macster/'
    TEST_SUBDIRS = []

    def setUp(self):
        if not os.path.exists(self.TEST_DIRECTORY):
            os.makedirs(self.TEST_DIRECTORY)

        sub_dir_names = ["a", "b", "c", "d/e"]

        for sub_dir in sub_dir_names:
            sub_dirs = os.path.join(self.TEST_DIRECTORY, sub_dir)
            self.TEST_SUBDIRS.append(sub_dirs)
            os.makedirs(sub_dirs)

    def test_macster(self):
        macster(self.TEST_DIRECTORY)

        all_dirs = [self.TEST_DIRECTORY, ] + self.TEST_SUBDIRS
        for dir_ in all_dirs:
            dsstore_file = os.path.join(dir_, '.DS_Store')
            self.assertEqual(os.path.exists(dsstore_file), True)

    def tearDown(self):
        shutil.rmtree(self.TEST_DIRECTORY)

if __name__ == '__main__':
    unittest.main()
