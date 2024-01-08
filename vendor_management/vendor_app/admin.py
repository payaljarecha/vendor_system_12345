from django.contrib import admin
from vendor_app.models import Vendor,PurchaseOrder,HistoricalPerformance
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate')
    search_fields = ('name', 'vendor_code')

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'status', 'quality_rating')
    search_fields = ('po_number', 'vendor__name')

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate')
    search_fields = ('vendor__name', 'date')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
