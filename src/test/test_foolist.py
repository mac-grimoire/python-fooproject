#!/usr/bin/env python3
import unittest
from collections.abc import Iterable
from carcano.foolist import *


class Foolist(unittest.TestCase):
    os_list = Foolist()

    def testFoolistIsIterable(self):
        self.assertIsInstance(self.os_list, Iterable)

    def testFoolistAppend(self):
        self.os_list.append('RedHat', True)
        self.os_list.append('CentOS', False)
        self.os_list.append('Suse', True)
        self.assertIn(FoolistItem('CentOS', False), self.os_list)

    def testFoolistRemove(self):
        self.os_list.remove('CentOS')
        self.assertNotIn(FoolistItem('CentOS', False), self.os_list)


if __name__ == '__main__':
    unittest.main()
