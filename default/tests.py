#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.tests.scripted import TestScript
from app import App


class TestApp (TestScript):
    apps = (App,)

    testDefaultResponse = """
        1 > LOL
        1 < Sorry, RapidSMS didn't understand that. You said: LOL
    """
