# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen


class UnSafeSessionSettingError(Exception):

    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return "<UnSafeSessionSettingError>:{message}".format(message=self.message)

    def __str__(self):
        return self.__unicode__()


class SessionSettingsError(Exception):

    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return "<SessionSettingsError>:{message}".format(message=self.message)

    def __str__(self):
        return self.__unicode__()