#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.db import models
from django.core.exceptions import ValidationError
from tags.models import Tag


class FeedbackTrigger(models.Model):
    title = models.CharField(max_length=100, blank=True)

    required_tags = models.ManyToManyField(Tag,
        related_name="feedbacktrigger_required_set",
        help_text=
            "These tags <strong>must</strong> be included " +\
            "in the report to trigger this feedback loop.")

    forbidden_tags = models.ManyToManyField(Tag, blank=True,
        related_name="feedbacktrigger_forbidden_set",
        help_text=
            "If any of these tags are present in the report," +\
            "this feedback loop will not be triggered.")

    class Meta:
        verbose_name = "trigger"


    def __unicode__(self):
        #if self.title:
        #    return self.title

        #else:
        tags = self.required_tags.all()
        return ", ".join(map(unicode, tags))

    @property
    def response_summary(self):
        return ""


class FeedbackResponse(models.Model):
    trigger = models.ForeignKey(FeedbackTrigger)
    text = models.TextField()

    class Meta:
        verbose_name = "response"
