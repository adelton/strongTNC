# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.contrib import admin

from . import models


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'created')
    list_filter = ('product', 'trusted')


class EnforcementAdmin(admin.ModelAdmin):
    list_display = ('policy', 'group', 'fail', 'noresult')
    list_filter = ('group', 'fail', 'noresult')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class IdentityAdmin(admin.ModelAdmin):
    list_display = ('data', 'type')
    list_filter = ('type',)


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'fail', 'noresult')
    list_filter = ('type', 'fail', 'noresult')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'recommendation')
    list_filter = ('recommendation',)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('connection_id', 'device', 'time', 'recommendation')
    list_filter = ('recommendation',)


class VersionAdmin(admin.ModelAdmin):
    list_display = ('release', 'package', 'product')
    list_filter = ('security', 'product')


class WorkItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'session', 'enforcement')
    list_filter = ('type', 'session')


admin.site.register(models.Device, DeviceAdmin)
admin.site.register(models.Enforcement, EnforcementAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Identity, IdentityAdmin)
admin.site.register(models.Package)
admin.site.register(models.Policy, PolicyAdmin)
admin.site.register(models.Product)
admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.Version, VersionAdmin)
admin.site.register(models.WorkItem, WorkItemAdmin)
