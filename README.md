# ASDC Attendance Platform

A modular NGO attendance and management platform built with Django, HTMX, and MySQL 8.

The goal of this project is to create a maintainable platform that starts with attendance management and can grow into a complete NGO management system.

---

# Project Vision

The current NGO attendance process uses manual Messenger-based attendance:

```
Attendance Today:

1. Juan Dela Cruz
2. Mary Cruz
3. Pedro Santos
```

This project aims to transform that process into a structured digital platform with:

* Member management
* Attendance tracking
* Event management
* Reports and analytics
* Future integrations

The system is designed with scalability and maintainability in mind so new features can be added without breaking existing functionality.

---

# Technology Stack

## Backend

| Technology      | Version |
| --------------- | ------- |
| Python          | 3.13    |
| Django          | 6.x     |
| Database        | MySQL 8 |
| Package Manager | uv      |

## Frontend

| Technology       | Purpose                  |
| ---------------- | ------------------------ |
| Django Templates | Server-side rendering    |
| HTMX             | Dynamic UI updates       |
| Bootstrap 5      | UI framework             |
| JavaScript       | Client-side enhancements |

## Testing

| Tool       | Purpose            |
| ---------- | ------------------ |
| Pytest     | Backend testing    |
| Playwright | End-to-end testing |

## Development Tools

| Tool   | Purpose         |
| ------ | --------------- |
| Git    | Version control |
| GitHub | Collaboration   |
| Ruff   | Linting         |
| Black  | Code formatting |

---

# Project Architecture

This project follows a modular monolith architecture.

Instead of building one large Django application, features are separated into independent modules.

```
asdc_attendance/

├── accounts/
├── core/
├── members/
├── chapters/
├── attendance/
├── events/
├── reports/
├── dashboard/
└── notifications/
```

Each module owns its:

* Models
* Business logic
* Views
* Templates
* Tests

---

# Architecture Principles

## 1. Thin Views

Views should handle HTTP requests only.

Business rules belong in services.

Example:

```
View

↓

Service

↓

Model

↓

Database
```

---

## 2. Service Layer

Business logic is separated from Django views.

Example:

```
attendance/

services/

    check_in.py

    validation.py

    reports.py
```

This makes the system easier to test and extend.

---

## 3. Feature-Based Development

Each feature has its own Django app.

Example:

```
attendance/

├── models.py
├── views.py
├── urls.py
├── services/
├── selectors/
├── forms.py
└── tests/
```

---

# Current Development Status

## Phase 1 - Foundation

Status: Completed

Completed:

* [x] Django project initialization
* [x] uv environment setup
* [x] Python 3.13 setup
* [x] Core application created
* [x] Accounts application created

Next:

* [x] BaseModel implementation
* [x] Custom User model
* [ ] Authentication system
* [x] MySQL 8 configuration

---

# Future Roadmap

## Phase 2 - Member Management

Status: In Progress

Completed:

* [x] Member list view
* [x] Member registration

Next:

* [ ] Member profiles
* [ ] Chapter assignment
* [ ] Member status tracking

---

## Phase 3 - Attendance System

Features:

* Manual attendance
* Event-based attendance
* Check-in/check-out
* Attendance history
* Attendance reports

Future options:

* QR attendance
* GPS validation
* RFID integration
* Mobile attendance

---

## Phase 4 - Events Management

Features:

* Create events
* Event schedules
* Attendance per event
* Event reports

---

## Phase 5 - Reports and Analytics

Features:

* Attendance dashboard
* Member activity
* Participation reports
* Export reports

---

# Development Setup

## Requirements

Install:

* Python 3.13+
* uv
* MySQL 8
* Git

---

## Clone Repository

```bash
git clone <repository-url>

cd asdc_attendance
```

---

## Install Dependencies

Using uv:

```bash
uv sync
```

---

## Activate Virtual Environment

Windows:

```powershell
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

---

## Environment Variables

Create:

```
.env
```

Example:

```env
DEBUG=True
SECRET_KEY=

DATABASE_NAME=asdc_attendance
DATABASE_USER=root
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

---

## Database Migration

After configuring the database:

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Administrator

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

Application:

```
http://127.0.0.1:8000/
```

Admin:

```
http://127.0.0.1:8000/admin/
```

---

# Git Workflow

Branches:

```
main

develop

feature/*

bugfix/*
```

Example:

```
feature/member-registration

feature/attendance-checkin

bugfix/login-error
```

---

# Commit Convention

Use conventional commits.

Examples:

```
feat(accounts): add custom user model

feat(attendance): add attendance check-in

fix(auth): resolve login issue

docs(readme): update setup guide
```

---

# Contribution Guidelines

Before submitting changes:

1. Run tests

```
pytest
```

2. Check code quality

```
ruff check .
```

3. Format code

```
black .
```

4. Create a pull request

---

# Project Goals

This project is not only an attendance system.

It is a practical software engineering project focused on:

* Django development
* Clean architecture
* Team collaboration
* Automated testing
* Production deployment
* Building maintainable software

---

# License

This project is currently private and intended for NGO development purposes.

---

# Maintainer

Project Lead:

Romar

Role:


