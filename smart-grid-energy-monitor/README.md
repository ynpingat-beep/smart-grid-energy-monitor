# ⚡ Smart Grid Energy Monitoring System

A backend-based Smart Grid Energy Monitoring System built using **FastAPI**, **PostgreSQL**, **Redis**, **Celery**, and **WebSockets**. The project enables real-time monitoring of smart energy sensors, dashboard analytics, caching, background task processing, and live updates.

---

## 🚀 Features

* RESTful APIs using FastAPI
* PostgreSQL database integration with SQLAlchemy ORM
* Sensor Management (Create & View Sensors)
* Energy Reading Management
* Real-time Dashboard
* Dashboard Analytics
* Live WebSocket Updates
* Redis Caching for Dashboard Summary
* Celery Background Tasks
* Scheduled Analytics using Celery Beat
* Application Logging
* Docker Configuration
* Interactive Swagger API Documentation

---

## 🛠️ Tech Stack

**Backend**

* FastAPI
* Python 3

**Database**

* PostgreSQL

**ORM**

* SQLAlchemy

**Cache**

* Redis

**Background Tasks**

* Celery
* Celery Beat

**Real-Time Communication**

* WebSockets

**Frontend**

* HTML
* CSS
* JavaScript
* Jinja2 Templates

**Deployment**

* Docker
* Docker Compose

---

## 📂 Project Structure

```text
smart-grid-energy-monitor/
│
├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── db/
│   ├── static/
│   ├── templates/
│   ├── crud.py
│   ├── main.py
│   ├── analytics.py
│   ├── celery_app.py
│   ├── tasks.py
│   └── logger.py
│
├── logs/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ynpingat-beep/smart-grid-energy-monitor.git
```

Move into the project directory:

```bash
cd smart-grid-energy-monitor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Start Redis.

Start Celery Worker:

```bash
celery -A app.celery_app.celery worker --loglevel=info
```

Start Celery Beat:

```bash
celery -A app.celery_app.celery beat --loglevel=info
```

---

## 📡 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📊 Dashboard Features

* Total Sensors
* Active Sensors
* Inactive Sensors
* Average Voltage
* Average Current
* Average Power
* Total Energy Consumption
* Live Dashboard Updates
* Cached Dashboard Summary
* Automated Analytics

---

## 📈 Background Processing

The project uses Celery and Celery Beat to:

* Aggregate energy data automatically
* Execute scheduled analytics
* Improve scalability for future tasks

---

## 📜 Logging

Application logs are stored in:

```text
logs/app.log
```

Logged events include:

* Sensor creation
* Reading creation
* Analytics execution
* System events

---

## 🐳 Docker Support

The project includes:

* Dockerfile
* docker-compose.yml
* .dockerignore

for containerized deployment.

---

## 🔮 Future Enhancements

* User Authentication (JWT)
* Role-Based Access Control
* Email Notifications
* SMS Alerts
* Grafana Dashboard
* Kubernetes Deployment
* Cloud Deployment (AWS/Azure)
* AI-Based Energy Consumption Prediction

---

## 👨‍💻 Author

**Yash Pingat**

GitHub: https://github.com/ynpingat-beep
