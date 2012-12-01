# -*- coding: utf-8 -*-
from django.contrib import admin
from email_auth_app.models import AuthUser, AuthToken

admin.site.register(AuthUser)
admin.site.register(AuthToken)