# 🌐 KenMax Digital Solutions

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![Status](https://img.shields.io/badge/status-active-success)

**KenMax** is a Kenyan digital agency building professional websites and custom systems that empower businesses, institutions, and individuals to thrive online. The official site, built with Django, showcases services ranging from e-commerce platforms to school portals and fare tracking apps.

---

## 🚀 Features

- 🏢 Company & Personal Portfolio Websites  
- 🛒 E-commerce Platforms with Secure Checkout  
- 📰 News & Media Portals with SEO Optimization  
- 🏫 School Portals for Student and Fee Management  
- 📍 Business Directories with Location Tools  
- 🚌 Fare Tracking for Matatus & Bodas  
- 🎉 Event & Vendor Management Systems  
- 💼 Job Boards for Listings and Applications  
- 💰 SACCO & Chama Contribution Systems  
- 🧾 POS & Inventory Management Tools  
- 📈 Search Engine Optimization Services  

---

## 🛠️ Tech Stack

| Layer        | Tools Used                         |
|--------------|------------------------------------|
| Backend      | Django 4.x (Python)                |
| Frontend     | HTML5, CSS3, JavaScript            |
| Database     | SQLite (development) / PostgreSQL (production) |
| Deployment   | Gunicorn + NGINX on Linux Server   |
| Static Files | Django Staticfiles / WhiteNoise    |

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/kiptoo-097/kenmax.git
cd kenmax

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

# Start the development server
python manage.py runserver
