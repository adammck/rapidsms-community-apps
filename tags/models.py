#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import re
from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    title   = models.CharField(max_length=100, unique=True)
    code    = models.CharField(max_length=30, unique=True)
    pattern = models.CharField(max_length=100, blank=True,
        help_text="Any incoming message containing a boundary-separated (\\b) " +
                  "string matching this regexp is assumed to be related to this " +
                  " tag. The CODE field is automatically prepended to this pattern.")

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return '<%s: %s (%s)>' %\
            (type(self).__name__, self.title, self.code)

    def save(self, *args, **kwargs):
        """Verifies that the pattern field can be compiled into a valid regex
           before saving (raising ValidationError if not), and saves the object
           as usual. This check is not required for the code field, since it is
           escaped before being compiled."""

        if self.pattern:
            try:
                re.compile(self.pattern)

            # boom. the regex is invalid, so don't let it into the
            # database. wrap the exception with a detailed error
            except:
                raise ValidationError(
                    "The pattern field must contain a valid " +\
                    "regex (or be empty) to save the object")

        # all is well; save the object as usual
        models.Model.save(self, *args, **kwargs)

    @property
    def regex(self):
        """Returns a regular expression to check a string (probably an incoming
           message, but anything is fine) for this tag. Returns None if this
           object contains a pattern that cannot be compiled."""

        try:
            pat = re.escape(self.code)

            # if there is a custom pattern, append
            # it to the code, to match alternatively
            if self.pattern:
                pat += "|(?:%s)" %\
                    (self.pattern)

            return re.compile(r"\b%s\b" % (pat), re.IGNORECASE)

        # something went wrong. probably an invalid
        # regex, even though that shouldn't have been
        # allowed into the database in the first place
        except:
            return None
