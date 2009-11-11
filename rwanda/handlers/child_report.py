#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from reporting.utils import extract_weight, extract_length
from rapidsms.contrib.handlers import KeywordHandler
from rwanda.models import PregnantPerson, BirthReport, ChildReport


class ChildReportHandler(KeywordHandler):
    """
    """

    keyword = "child\s+report|creport|crep"

    def must_register(self):
        self.respond("You must JOIN before reporting.")

    def handle(self, text):

        # abort if the user hasn't identified yet
        if self.msg.reporter is None:
            self.must_register()
            return True

        resp = self.respond("Thank you for reporting.")
        report = ChildReport()

        # extract and record the weight
        weight, text = extract_weight(text)
        if weight is not None:
            resp.append("Weight: %(weight)sKG", weight=("%.1f" % weight))
            report.weight = weight

        # extract and record the muac
        muac, text = extract_length(text)
        if muac is not None:
            resp.append("MUAC: %(muac)sCM", muac=("%.1f" % muac))
            report.muac = muac


        code = self._national_id()
        person, created = PregnantPerson.objects.get_or_create(
            code=code)

        #if len(persons) == 0:
        #    self.respond("You must register the pregnancy before reporting.")
        #    return True

        #person = persons[0]


        birth_report = BirthReport.objects.get_or_create(
            person=person)

        #if len(birth_reports) == 0:
        #    self.respond("You must report the birth before reporting.")
        #    return True

        #birth_report = birth_reports[0]


        report.person = person
        report.save()


        # save any tags extracted during
        # parse phase by the tagging app
        if hasattr(self.msg, "tags"):
            if len(self.msg.tags) > 0:
                for tag in self.msg.tags:
                    report.tags.add(tag)

                #resp += " with indicators: %s" %\
                #    (", ".join(map(unicode, self.msg.tags)))

        #self.respond("%s." % resp)
