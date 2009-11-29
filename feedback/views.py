#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.views.decorators.http import require_GET, require_http_methods
from django.shortcuts import get_object_or_404
from rapidsms.djangoproject.utils import render_to_response, paginated
from models import *

from tags.models import Tag


@require_GET
def index(req):
    return render_to_response(req,
        "feedback/index.html", {
            "triggers": paginated(req, FeedbackTrigger.objects.all())
        })


@require_http_methods(["GET", "POST"])
def add(req):
    return True


@require_http_methods(["GET", "POST"])  
def edit(req, pk):
    trigger = get_object_or_404(FeedbackTrigger, pk=pk)

    return render_to_response(req,
        "feedback/edit.html", {
            "trigger": trigger,
            "all_tags": Tag.objects.all(),
            "triggers": paginated(req, FeedbackTrigger.objects.all())
        })
