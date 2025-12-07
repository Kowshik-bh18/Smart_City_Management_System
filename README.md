# 🌆 Smart City Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A centralized Smart City Management System developed using Django to digitalize and manage urban civic services such as complaints, infrastructure issues, utilities, and emergency reporting through a single platform.

The system helps improve efficiency, transparency, and responsiveness in city-level governance by enabling citizens to register issues online and administrators to monitor and resolve them through a unified dashboard.

FEATURES:
- Online complaint registration and tracking
- Road and infrastructure issue reporting
- Electricity, water, and waste management modules
- Emergency complaint handling
- Centralized admin dashboard
- Responsive Bootstrap-based UI

MODULES INCLUDED:
- complaint: general civic complaints
- dashboard: administrative overview
- road: road and infrastructure issues
- electricity: power-related issues
- water_management: water supply complaints
- waste_management: waste handling services
- waste_complaints: waste-specific complaints
- emergency: emergency reporting
- mapdata: location-based issue handling
- smart_city: main Django project configuration

SYSTEM ARCHITECTURE:
User → Django Views → Service Modules → SQLite Database → Admin Dashboard

TECH STACK:
Backend: Django, Python 3, SQLite  
Frontend: HTML, CSS, Bootstrap  

PROJECT STRUCTURE:
Smart_City_Management_System/
├── complaint/
├── dashboard/
├── electricity/
├── emergency/
├── mapdata/
├── road/
├── smart_city/
├── waste_complaints/
├── waste_management/
├── water_management/
├── templates/
├── media/
├── db.sqlite3
├── manage.py
└── README.md

INSTALLATION & SETUP:
1. Clone the repository  
   git clone https://github.com/Kowshik-bh18/Smart_City_Management_System.git  
   cd Smart_City_Management_System  

2. Create and activate virtual environment  
   python -m venv venv  
   venv\Scripts\activate  

3. Install dependencies  
   pip install django  

4. Setup database  
   python manage.py makemigrations  
   python manage.py migrate  

5. Run the server  
   python manage.py runserver  

Access the application at: http://127.0.0.1:8000

USAGE:
- Register or login as a user
- Submit civic complaints
- Track complaint status
- Admin monitors and resolves issues using dashboard

FUTURE ENHANCEMENTS:
- Role-based authentication
- GIS/map-based complaint visualization
- Email and SMS notifications
- REST API integration
- AI-based complaint prioritization
- Mobile application support

CONTRIBUTORS:
- Kowshik BH
- MD Ganesha

CONTACT:
Kowshik BH  
Email: kowshikbh18@gmail.com  
GitHub: https://github.com/Kowshik-bh18  
LinkedIn: https://www.linkedin.com/in/kowshikbh  

⭐ If you like this project, consider starring the repository.
