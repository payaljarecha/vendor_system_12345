# Vendor Management System

The Vendor Management System is a Django-based application that facilitates the management of vendor profiles, purchase orders, and vendor performance metrics.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/payaljarecha/vendor_system_12345.git

   pip install -r requirements.txt
2. Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Visit http://localhost:8000/ in your browser to access the application.

## API Endpoints

- `POST /vendors/`: Create a new vendor.
- `GET /vendors/`: List all vendors.
- `GET /vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- `PUT /vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /vendors/{vendor_id}/`: Delete a vendor.
- ...

- `POST /purchase_orders/`: Create a new purchase order.
- `GET /purchase_orders/`: List all purchase orders with an option to filter by vendor.
- `GET /purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /purchase_orders/{po_id}/`: Delete a purchase order.
- ...

## Examples

### Create a new vendor

```bash
curl -X POST -H "Content-Type: application/json" -d '{
        "name": "Mohit",
        "contact_details": "9840393466",
        "address": "strotten mudali street,sowcarpet",
        "vendor_code": "SN000201",}' http://localhost:8000/vendors/
Retrieve details:

curl http://localhost:8000/vendors/1/

### Create a new Purchase Order
{
    "id": 2,
    "po_number": "PON002",
    "order_date": "2023-12-04T13:16:00Z",
    "delivery_date": "2023-12-09T15:16:00Z",
    "items": [
        {
            "code": "123",
            "name": "Bag",
            "quantity": 100,
            "price": 1000.0
        }
    ],
    "quantity": 100,
    "status": "Open",
    "quality_rating": 3.5,
    "issue_date": "2023-12-06T13:18:00Z",
    "acknowledgment_date": "2023-12-07T13:18:00Z",
    "vendor": 2
}
Retrieve details:

curl http://localhost:8000/purchase_orders/1/

## Instructions for Running the Test Suite

1. Ensure that your virtual environment is activated.

2. Install the testing dependencies:

    ```bash
    pip install -r requirements-test.txt
    ```

3. Run the tests using the following command:

    ```bash
    python manage.py test
    ```