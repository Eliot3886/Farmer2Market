# 🌾 Farmer2Market - Backend API

## 📌 Overview
Farmer2Market is a backend API built to connect farmers directly with buyers, reducing middlemen and improving market access for small-scale farmers.

This project is built using **Django**, **Django REST Framework**, **JWT Authentication**, and **PostgreSQL**.

---

## ⚙️ Tech Stack
- Backend Framework: Django
- API Layer: Django REST Framework (DRF)
- Authentication: JWT (JSON Web Tokens)
- Database: PostgreSQL
- Language: Python

---

## 🚀 Features
- User registration and login (JWT authentication)
- Secure token-based authentication
- RESTful API endpoints
- Product listing (farm produce)
- Basic business logic for marketplace operations
- PostgreSQL database integration
- Clean and modular Django architecture

---

## 🔐 Authentication
This project uses JWT Authentication.

After login, a token is generated and must be included in requests:

```
Authorization: Bearer <your_token>
```

---

## 📂 Project Structure
```
## 📁 Project Structure

Farmer2Market_Backend/
│
├── farmer2market/
│   ├── api/                  # API app (views, serializers, models, urls)
│   ├── farmer2market/        # Main Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py       # Project configuration
│   │   ├── urls.py           # Root URL configuration
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── media/
│   │   └── products/         # Uploaded product images/files
│   │
│   ├── build.sh              # Build script for deployment
│   ├── db.sqlite3            # SQLite database (development)
│   ├── manage.py             # Django management script
│   └── requirements.txt      # Project dependencies
│
└── README.md                 # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/your-username/farmer2market-backend.git
cd farmer2market-backend
```

### 2. Create virtual environment
```
python -m venv venv
```

### 3. Activate environment
```
venv\Scripts\activate   # Windows
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Configure PostgreSQL
Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 7. Start server
```
python manage.py runserver
```

---

## 📡 API Endpoints (Examples)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/register/ | Register user |
| POST | /api/login/ | Login & get token |
| GET | /api/products/ | Get all products |
| POST | /api/products/ | Add product (auth required) |

---

## 🎯 Purpose of Project
This project was built as a learning project to understand:
- REST API development
- Authentication using JWT
- Backend architecture with Django
- Database integration with PostgreSQL

---

## 👨‍💻 Author
Eliot Chitowamombe


---

## 📌 Future Improvements
- Payment integration
- Advanced search & filtering
- Web based app
- Improve overall layout to professional level
- Log in system to continue with email(google)
```
