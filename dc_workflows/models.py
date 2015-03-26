'''
Created on Mar 25, 2015

@author: placiana
'''
from django.db import models


class Workflow(models.Model):
    name = models.CharField('Nombre', max_length=200)


class Stage(models.Model):
    workflow = models.ForeignKey('Workflow', related_name="stages")
    name = models.CharField('Nombre', max_length=200)

    def __unicode__(self):
        return self.name


class StageTransition(models.Model):
    workflow = models.ForeignKey('Workflow', related_name="transitions")
    source = models.ForeignKey('Stage', verbose_name="source stage", related_name='outbound_transitions')
    target = models.ForeignKey('Stage', verbose_name="target stage", related_name='inbound_transitions')

