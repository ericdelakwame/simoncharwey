from django.contrib import admin
from .models import (
    Press, Teaching, About, Work
)

admin.site.register(Press)
admin.site.register(Teaching)
admin.site.register(Work)
admin.site.register(About)