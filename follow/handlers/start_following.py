#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from handlers import KeywordHandler
from rapidsms.search import find_objects
from follow.utils import followable_models


class FollowHandler(KeywordHandler):
    keyword = "follow|watch"

    def help(self):
        self.respond("To start following something, send FOLLOW <NAME>")

    def handle(self, text):

        # fetch a list of objects (any model) that
        # match the query via the __search__ api
        to_follow = find_objects(
            followable_models(),
            text)

        # link this reporter to the "followers" reverse foreign key
        # of each object (whatever model it is -- they're all named
        # "followers"). this works with unidentified connections too,
        # even if that doesn't make much sense most of the time
        for obj in to_follow:
            obj.followers.get_or_create(
                **self.msg.persistance_dict)

        if to_follow:
            self.respond(
                "You are now following: %s" %
                (", ".join(map(unicode, to_follow))))

        # if we didn't understand _any_ of what the
        # caller asked us to follow, return an error
        else:
            self.respond("Sorry, I couldn't understand what you want to follow.")
