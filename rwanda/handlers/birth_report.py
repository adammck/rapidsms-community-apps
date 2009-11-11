#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import re
from reporting.utils import extract_date, extract_weight
from rapidsms.contrib.handlers import KeywordHandler
from rwanda.models import PregnantPerson, BirthReport


class PreBirthReportHandler(KeywordHandler):
    """
    """

    keyword = "b[o0]rn|birth"

    def must_register(self):
        self.respond("You must JOIN before reporting.")

    def handle(self, text):

        # abort if the user hasn't identified yet
        if self.msg.reporter is None:
            self.must_register()
            return True

        resp = self.respond("Thank you for reporting a birth.")
        report = BirthReport()

        # extract and record the birth weight
        weight, text = extract_weight(text)
        if weight is not None:
            resp.append("Weight: %(weight)sKG", weight=("%.1f" % weight))
            report.weight = weight

        # extract and record the date of birth
        date, text = extract_date(text)
        if date is not None:
            resp.append("Date: %(date)s", date=format(date, "%d/%m/%Y"))
            report.date = date

        # now that the weight and date have been
        # removed, assume that the rest is the
        # mother's unique code (todo: __search__)

        #code = re.sub(r"[^0-9]", "", text.strip())
        code = self._national_id()
        person, created = PregnantPerson.objects.get_or_create(
            code=code)

        #if len(persons) == 0:
        #    self.respond("You must register the pregnancy before reporting a birth.")
        #    return True

        #person = persons[0]

        report.person = person
        report.save()

        # save any tags extracted during
        # parse phase by the tagging app
        if hasattr(self.msg, "tags"):
            if len(self.msg.tags) > 0:
                for tag in self.msg.tags:
                    report.tags.add(tag)

                #resp += "Indicators: %s" %\
                #    (", ".join(map(unicode, self.msg.tags)))

        #self.respond("%s." % resp)
