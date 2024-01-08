from django.db import models
from django.utils import timezone
# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    def update_performance_metrics(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')

        # On-Time Delivery Rate
        on_time_delivery_count = completed_pos.filter(delivery_date__lte=timezone.now()).count()
        total_completed_pos = completed_pos.count()
        self.on_time_delivery_rate = (on_time_delivery_count / total_completed_pos) * 100 if total_completed_pos > 0 else 0

        # Quality Rating Average
        quality_ratings = completed_pos.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
        self.quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if len(quality_ratings) > 0 else 0

        # Average Response Time
        response_times = completed_pos.exclude(acknowledgment_date__isnull=True).annotate(
            response_time=models.F('acknowledgment_date') - models.F('issue_date')
        ).values_list('response_time', flat=True)
        self.average_response_time = sum(response_times, timezone.timedelta()) / len(response_times) if len(response_times) > 0 else timezone.timedelta()

        # Fulfillment Rate
        successful_fulfillments = completed_pos.filter(issues__isnull=True).count()
        self.fulfillment_rate = (successful_fulfillments / total_completed_pos) * 100 if total_completed_pos > 0 else 0

        self.save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.update_performance_metrics()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()