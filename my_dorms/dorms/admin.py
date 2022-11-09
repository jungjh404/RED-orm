from django.contrib import admin
from .models import Context, Comment, Context_info, Comment_info, Context_free, Comment_free, Context_trade, Comment_trade, Comment_copur, Context_copur

# Register your models here.
admin.site.register(Context)
admin.site.register (Comment)
admin.site.register(Context_info)
admin.site.register (Comment_info)
admin.site.register(Context_free)
admin.site.register (Comment_free)
admin.site.register(Context_trade)
admin.site.register (Comment_trade)
admin.site.register(Context_copur)
admin.site.register (Comment_copur)