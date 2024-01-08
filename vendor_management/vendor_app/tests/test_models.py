from django.test import TestCase
from vendor_app.models import Vendor,PurchaseOrder,HistoricalPerformance

class VendorModelTest(TestCase):
    def test_vendor_creation(self):
        vendor = Vendor.objects.create(
            name="TestVendor",
            contact_details="9080389836",
            address="123 Test St",
            vendor_code="SN000201"
        )
        self.assertEqual(str(vendor), vendor.name)

class PurchaseOrderModelTest(TestCase):
    def test_purchase_order_creation(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number="PON123",
            vendor=self.vendor,  # Assuming you have a Vendor instance
           # order_date=your_order_date,
            #delivery_date=your_delivery_date,
           # items=your_items,
           # quantity=your_quantity,
            status="pending",
            quality_rating=None,
           # issue_date=your_issue_date,
            acknowledgment_date=None,
        )
        self.assertEqual(str(purchase_order), purchase_order.po_number)

class HistoricalPerformanceModelTest(TestCase):
    def test_historical_performance_creation(self):
        historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,  # Assuming you have a Vendor instance
           # date=your_date,
            #on_time_delivery_rate=your_on_time_delivery_rate,
            #quality_rating_avg=your_quality_rating_avg,
            #average_response_time=your_average_response_time,
            #fulfillment_rate=your_fulfillment_rate,
        )
        self.assertEqual(str(historical_performance), str(historical_performance.date))        