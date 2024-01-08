from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from vendor_app.models import Vendor,PurchaseOrder,HistoricalPerformance

class VendorViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="test@example.com",
            address="123 Test St",
            vendor_code="TEST123"
        )

    def test_vendor_list_view(self):
        url = reverse('vendor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one vendor is created in the setup

class PurchaseOrderViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO123",
            vendor=self.vendor,  # Assuming you have a Vendor instance
            #order_date=your_order_date,
            #delivery_date=your_delivery_date,
            #items=your_items,
            #quantity=your_quantity,
            status="pending",
            quality_rating=None,
            #issue_date=your_issue_date,
            acknowledgment_date=None,
        )

    def test_purchase_order_list_view(self):
        url = reverse('purchase-order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one purchase order is created in the setup

class HistoricalPerformanceViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,  # Assuming you have a Vendor instance
            #date=your_date,
            #on_time_delivery_rate=your_on_time_delivery_rate,
            #quality_rating_avg=your_quality_rating_avg,
            #average_response_time=your_average_response_time,
            #fulfillment_rate=your_fulfillment_rate,
        )

    def test_historical_performance_list_view(self):
        url = reverse('historical-performance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one historical performance entry is created in the setup        