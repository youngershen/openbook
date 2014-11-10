#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

import unittest

class AccountTestCase(unittest.TestCase):
    def test_is_ok(self):
        self.assertTrue(True)

class CreateTestCase(unittest.TestCase):
    def test_add_user(self):
        self.assertTrue(True)



def main():
    unittest.main()

if __name__ == '__main__':
    main()
