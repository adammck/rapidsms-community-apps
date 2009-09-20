#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import rapidsms


class App(rapidsms.App):
    """
    This app catches incoming messages which are not responded to by any other
    app, and sends a default response. This should be avoided where possible,
    since the default is necessarily very vague.
    """

    def catch(self, msg):
        if not msg.responses:

            msg.error("Sorry, we could not understand that message.")
            #msg.error(
            #    "Sorry, RapidSMS didn't understand that. You said: %(you_said)s",
            #    you_said=msg.text)

            return True
