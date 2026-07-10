# Smart Grid Energy Monitoring System

## Overview

The Smart Grid Energy Monitoring System is a real-time backend application designed to collect, process, and monitor energy consumption data from smart grid sensors.

The system provides APIs for sensor registration, energy data ingestion, real-time monitoring, analytics, and alert generation.

---

## Features

- Sensor Registration
- Energy Data Collection
- Real-Time Monitoring
- WebSocket Support
- PostgreSQL Database
- Redis & Celery Background Tasks
- REST APIs using FastAPI
- Analytics Dashboard
- GitHub Actions CI/CD

---

## Technology Stack

### Backend
- FastAPI
- Python 3.14

### Database
- PostgreSQL

### Task Queue
- Celery
- Redis

### Real-Time Communication
- WebSockets

### Version Control
- Git
- GitHub

---

## Project Structure

```text
smart-grid-energy-monitor/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── websocket/
│   ├── workers/
│   └── main.py
│
├── tests/
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## Installation

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

```text
http://127.0.0.1:8000/docs
```

## Internship Project

Python Development Internship

Project: Smart Grid Energy Monitoring System

Status: Week 1 - Project Initialization