# coding=utf-8

from __future__ import unicode_literals

from django.contrib import admin

from .models import Workflow, Stage, StageTransition


admin.site.register(Workflow)
admin.site.register(Stage)
admin.site.register(StageTransition)
