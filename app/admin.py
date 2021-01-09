from django.contrib import admin
from app.models import TODO
# Register your models here.
admin.site.register(TODO)

# We need to register the out User to the admin here