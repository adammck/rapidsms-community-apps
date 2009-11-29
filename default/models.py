#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

"""
>>> from rapidsms import Message
>>> msg = Message(None, "one")
>>> msg.text
'one'

>>> msg.language = "de"
>>> msg.text
'ein'

>>> msg.language = "fr"
>>> msg.text
'un'

>>> msg = Message(None, "The %(site_name)s team", site_name="RapidSMS")
>>> msg.text
'The RapidSMS team'

>>> msg.language = "es"
>>> msg.text
'El equipo de RapidSMS'
"""
