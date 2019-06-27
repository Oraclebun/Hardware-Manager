from django.contrib import admin
from .models import ProbeCard, ProbeCardReport

# Register your models here.
#admin.site.register(ProbeCard)
#admin.site.register(ProbeCardReport)

#Define the admin class
class ProbeCardReportInline(admin.TabularInline):
    model = ProbeCardReport

    
@admin.register(ProbeCard)
class ProbeCardAdmin(admin.ModelAdmin):
    list_display = ('probecard_id', 'device_num', 'device_name', 'aus_serial_num')
    inlines = [ProbeCardReportInline]

#@admin.register(ProbeCardReport)

#Register the admin class with the associated model
#admin.site.register(ProbeCard, ProbeCardAdmin)
#admin.site.register(ProbeCardReport, ProbeCardReportAdmin)
