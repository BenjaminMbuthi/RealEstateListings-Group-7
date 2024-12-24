# Real Estate Listings API

## Overview
This is a Django-based REST API for managing real estate listings. The API provides endpoints for managing agents, properties, buyers, locations, and property listings, enabling CRUD operations for each.

## Features
- Manage real estate agents and their details.
- Manage locations (e.g., cities, states, and zip codes).
- Manage properties, including price, availability, and descriptions.
- Manage buyers and their contact information.
- Manage property listings, including status updates (Pending or Sold).
- RESTful endpoints for CRUD operations.

---

## Project Structure
```
real_estate_project/
    manage.py
    real_estate_project/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    listings/
        __init__.py
        admin.py
        apps.py
        models.py
        serializers.py
        views.py
        urls.py
```

---

## Models

1. **Agent**
   - Fields: `name`, `email`, `phone`

2. **Location**
   - Fields: `city`, `state`, `zip_code`

3. **Property**
   - Fields: `title`, `description`, `price`, `location`, `agent`, `is_available`, `listed_date`

4. **Buyer**
   - Fields: `name`, `email`, `phone`

5. **Listing**
   - Fields: `property`, `buyer`, `status`, `created_date`

### Model Relationships
- A `Property` belongs to a `Location` and an `Agent`.
- A `Listing` references a `Property` and a `Buyer`.

---

## Serializers
Each model has a corresponding serializer defined in `serializers.py`. These serializers handle data validation and transformation between Python objects and JSON.

---

## Endpoints

### **Agents**
- `GET /api/agents/` - List all agents.
- `POST /api/agents/` - Create a new agent.
- `GET /api/agents/<id>/` - Retrieve a specific agent.
- `PUT /api/agents/<id>/` - Update a specific agent.
- `DELETE /api/agents/<id>/` - Delete a specific agent.

### **Locations**
- `GET /api/locations/` - List all locations.
- `POST /api/locations/` - Create a new location.
- `GET /api/locations/<id>/` - Retrieve a specific location.
- `PUT /api/locations/<id>/` - Update a specific location.
- `DELETE /api/locations/<id>/` - Delete a specific location.

### **Properties**
- `GET /api/properties/` - List all properties.
- `POST /api/properties/` - Create a new property.
- `GET /api/properties/<id>/` - Retrieve a specific property.
- `PUT /api/properties/<id>/` - Update a specific property.
- `DELETE /api/properties/<id>/` - Delete a specific property.

### **Buyers**
- `GET /api/buyers/` - List all buyers.
- `POST /api/buyers/` - Create a new buyer.
- `GET /api/buyers/<id>/` - Retrieve a specific buyer.
- `PUT /api/buyers/<id>/` - Update a specific buyer.
- `DELETE /api/buyers/<id>/` - Delete a specific buyer.

### **Listings**
- `GET /api/listings/` - List all listings.
- `POST /api/listings/` - Create a new listing.
- `GET /api/listings/<id>/` - Retrieve a specific listing.
- `PUT /api/listings/<id>/` - Update a specific listing.
- `DELETE /api/listings/<id>/` - Delete a specific listing.

---

## Setup Instructions

### Prerequisites
- Python 3.11+
- pip
- Virtual environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd real_estate_project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Testing the API
Use `curl`, Postman, or any API testing tool to interact with the API.

Example `curl` command to list all properties:
```bash
curl -X GET http://127.0.0.1:8000/api/properties/
```

---

## Testing
- Unit tests are located in `listings/tests.py`.
- To run tests:
  ```bash
  python manage.py test
  ```


## Contributors
- Group 7 Members:
 151664 Mbuthi Benjamin
 150344 Naibei Timothy
 152439 Kaguai Daniel
 151115 Odhiambo Tyrone

---


