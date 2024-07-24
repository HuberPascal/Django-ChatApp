from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at', 'author', 'receiver')
    list_display = ('created_at', 'author', 'text',  'receiver')
    search_fields = ('text',)


# Register the model with the admin site
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
