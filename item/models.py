from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=15)
    owner = models.ForeignKey('auth.User')
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
