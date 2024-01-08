from django.test import TestCase
from vendor_app.models import Vendor,PurchaseOrder,HistoricalPerformance
from vendor_app.serializers import VendorSerializer,PurchaseOrderSerializer

class VendorSerializerTest(TestCase):
    def test_vendor_serializer(self):
        vendor_data = {
            'name': 'Test Vendor',
            'contact_details': 'test@example.com',
            'address': '123 Test St',
            'vendor_code': 'TEST123'
        }
        serializer = VendorSerializer(data=vendor_data)
        self.assertTrue(serializer.is_valid())

class PurchaseOrderSerializerTest(TestCase):
    def test_purchase_order_serializer(self):
        purchase_order_data = {
            'po_number': 'PO123',
            #'vendor': your_vendor_data,
            #'order_date': your_order_date,
           # 'delivery_date': your_delivery_date,
            #'items': your_items,
            #'quantity': your_quantity,
            'status': 'pending',
            'quality_rating': None,
            #'issue_date': your_issue_date,
            'acknowledgment_date': None,
        }
        serializer = PurchaseOrderSerializer(data=purchase_order_data)
        self.assertTrue(serializer.is_valid())        