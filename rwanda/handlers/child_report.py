#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from reporting.utils import extract_weight, extract_length
from rapidsms.contrib.apps.handlers import KeywordHandler
from rwanda.models import PregnantPerson, BirthReport, ChildReport


class ChildReport(KeywordHandler):
    keyword = "childreport|crep"

    def help(self):
        self.respond("To report on a child, repond CREP <WEIGHT> <TAGS>")

    def _extract_weight(self):
        self.weight, remainder = get_weight(text)

    def handle(self, text):
        kg, text = get_weight(text)
        if kg is not None:
            self.respond("Child Report: %d kg, tags: %s" %
                (kg, ", ".join(map(unicode, self.msg.tags))))

        else:
            self.help()
