# -*- coding: utf-8 -*-

# import from apps here


# import from lib
# ===============================================================================
from django.contrib import admin
# from apps.__.models import aaaa
#
# admin.site.register(ApplyForm)
# ===============================================================================
from home_application.models import *

admin.site.register(Award)

admin.site.register(Organization)

admin.site.register(Attachment)

admin.site.register(ApplyForm)
