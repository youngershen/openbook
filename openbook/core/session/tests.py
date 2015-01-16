# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen

from unittest import TestCase
from utils import generate_session_key_django
from errors import UnSafeSessionSettingError
from session import FileSession
from openbook.settings.settings import settings


class BaseSessionTestcCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


class BaseFileSessionTestCase(BaseSessionTestcCase):

    def setUp(self):
        self.session = FileSession(settings=settings['SESSION'])

    def tearDown(self):
        pass


class TestFileSession(BaseFileSessionTestCase):

    def test_create_session(self):
        session = FileSession(settings=settings['SESSION'])
        self.assertIsNotNone(session)

    def test_set_session(self):
        self.session.set('key1', 'value1')

    def test_get_session(self):
        self.session.set('key1', 'value1')
        self.assertEqual('value1', self.session.get('key1'))

    def test_exist_session(self):
        self.assertEqual(False, self.session.exists('session_id'))
        print self.session.session_id
        print self.session.session_path
        self.assertEqual(True, self.session.session_exists(self.session.session_id))

    def test_expire_time(self):
        time = self.session.get_expire()
        create_time = self.session.get_create_time()
        ex_time = time + create_time
        self.assertEqual(ex_time, self.session.get_expire_time())

    def test_set_expire_time(self):
        time = self.session.get_expire()
        create_time = self.session.get_create_time()
        ex_time = time + create_time
        self.assertEqual(ex_time, self.session.get_expire_time())

        self.session.set_expire_time(999)
        self.assertEqual(self.session.get_expire_time(), self.session.get_create_time() + 999)

    def test_safe_set(self):
        self.session.set('jack', 'rose')
        try:
            self.session.safe_set('jack', 'lucy')
        except UnSafeSessionSettingError as e:
            pass

        self.session.safe_set('jack', 'luck', force=True)
        self.assertEqual('luck', self.session.get('jack'))


class TestUtilsCase(BaseSessionTestcCase):

    def test_session_key_generate(self):
        key1 = generate_session_key_django()
        self.assertEqual(len(key1), 32)

        key2 = generate_session_key_django(length=10, allow_chars='123abc')
        self.assertNotIn('d', key2)
        self.assertNotIn('e', key2)
        self.assertNotIn('f', key2)

