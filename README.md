# Enterprise Inventory Management System (IMS)

A full-stack web application designed to streamline IT asset management, hardware provisioning, and vendor invoice tracking. 

## Overview
Managing IT assets via spreadsheets or disconnected desktop applications leads to data silos and operational bottlenecks. This project solves that by providing a centralized, web-based dashboard for Help Desk technicians and System Administrators to track the entire lifecycle of company hardware—from initial vendor invoicing to final department deployment.

### Architecture Evolution
This project represents an architectural evolution from a legacy monolithic desktop application. 
* V1 (Legacy): A tightly coupled Tkinter desktop application utilizing localized CSV files for data persistence.
* V2 (Current): Refactored into a decoupled Django (MVT) web architecture. The data layer was migrated to a relational SQL database, the interface was rebuilt using responsive HTML/Bootstrap templates, and CRUD logic was abstracted into secure server-side views.

## Key Features
* Full CRUD Capabilities: Add, view, update, and securely delete hardware assets.
* Legacy Data Pipeline: Includes a custom Django Management Command (import_legacy_data) to parse, sanitize, and migrate historical CSV data directly into the SQL database.
* Role-Based Access Control (RBAC): Leverages Django's built-in authentication and admin panel to separate base-level technician views from administrative procurement controls.
* Responsive UI: Built with Bootstrap 5 to ensure technicians can check asset tags or update work orders on the fly from a mobile device or tablet.

## Tech Stack
* Backend: Python, Django
* Frontend: HTML5, CSS3, Bootstrap 5
* Database: SQLite (Development) / Ready for PostgreSQL (Production)
* Architecture: Model-View-Template (MVT)

## Local Development Setup

To run this project locally, ensure you have Python installed, then follow these steps:

1. Clone the repository
   git clone https://github.com/yourusername/ims-django.git
   cd ims-django

2. Create and activate a virtual environment
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply database migrations
   python manage.py migrate

5. (Optional) Import legacy CSV data
   python manage.py import_legacy_data inventory.csv

6. Create an admin user and run the server
   python manage.py createsuperuser
   python manage.py runserver

   Navigate to http://127.0.0.1:8000/ to view the application, or http://127.0.0.1:8000/admin/ to access the backend dashboard.

## License
Copyright (c) 2022-2026 Michael Speer. All Rights Reserved.
