#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import re
from reporting.utils import extract_date
from rapidsms.contrib.handlers import KeywordHandler
from rwanda.models import PregnantPerson, PreBirthReport


class PreBirthReportHandler(KeywordHandler):
    """
    """

    keyword = "mrep"

    def must_register(self):
        self.respond("You must JOIN before reporting.")

    def handle(self, text):

        # abort if the user hasn't identified yet
        if self.msg.reporter is None:
            self.must_register()
            return True

        code = re.sub(r"[^0-9]", "", text.strip())
        #persons = PregnantPerson.objects.filter(
        #    code=code)

        #if len(persons) == 0:
        #    self.respond("You must register the pregnancy before reporting.")
        #    return True

        person, created = PregnantPerson.objects.get_or_create(
            code=code)

        #person = persons[0]

        resp = self.respond("Thank you for reporting.")
        report = PreBirthReport.objects.create(
            person=person)

        # save any tags extracted during
        # parse phase by the tagging app
        if hasattr(self.msg, "tags"):
            if len(self.msg.tags) > 0:
                for tag in self.msg.tags:
                    report.tags.add(tag)

                #resp += "Indicators: %s" %\
                #    (", ".join(map(unicode, self.msg.tags)))

        #self.respond("%s." % resp)
