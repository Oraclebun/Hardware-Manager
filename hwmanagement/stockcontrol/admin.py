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
#class ProbeCardReportAdmin(admin.ModelAdmin):
#    list_display = ('probecard', 'probehead_rebuild_num', 'probehead_num', 'da#te_measured', 'tip_length', 'crown_height', 'probehead_touchdown', 'pcb_touchd#own', 'iqa_date', 'iqa_tip_length', 'crown_iqa_height', 'remarks')
#    list_filter = ('status_log', 'status_pc', 'date_added')
#    fieldsets = (
#        (None, {
#        'fields': ('probecard', 'probehead_rebuild_num', 'probehead_num')
#            }),
#        ('Measure Details', {
#            'fields': ('date_measured', 'tip_length', 'crown_height', 'probehe#ad_touchdown', 'pcb_touchdown'),
#            }),
#        ('IQA', {
#            'fields': ('iqa_date', 'iqa_tip_length', 'crown_iqa_height'),
#            }),
#        ('Availability', {
#            'fields' : ('remarks', 'status_log', 'status_pc', 'status_prod'),
#            }),
#        )
        

#Register the admin class with the associated model
#admin.site.register(ProbeCard, ProbeCardAdmin)
#admin.site.register(ProbeCardReport, ProbeCardReportAdmin)