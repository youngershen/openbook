# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen

from unittest import TestCase
from utils import generate_session_key_django


class BaseSessionTestcCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestFileSession(BaseSessionTestcCase):

    def testConfiguration(self):
        print "test"


class TestUtilsCase(BaseSessionTestcCase):

    def test_session_key_generate(self):
        key1 = generate_session_key_django()
        self.assertEqual(len(key1), 32)

        key2 = generate_session_key_django(length=10, allow_chars='123abc')
        self.assertNotIn('d', key2)
        self.assertNotIn('e', key2)
        self.assertNotIn('f', key2)