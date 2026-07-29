# ASDC Attendance — Task Tracker

This file tracks all development tasks per phase.
Update the checkboxes as you complete each task.

---

# Phase 1 — Foundation
> Goal: Project setup, base models, authentication

- [x] Django project initialization
- [x] uv environment setup
- [x] Python 3.13 setup
- [x] MySQL 8 configuration
- [x] BaseModel (core app)
- [x] Custom User model (accounts app)
- [x] Chapters app — Region, Province, Municipality, Barangay models
- [x] Members app — Member model
- [x] Django admin for all models
- [x] Seed command — Philippine regions
- [x] Seed command — Region XII provinces, municipalities, barangays
- [X] Authentication — fix template loading issue
- [X] Authentication — login page working
- [X] Authentication — logout working
- [X] Authentication — redirect unauthenticated users to login
- [X] Base template — shared HTML layout (base.html)
- [X] Dashboard home page working after login

---

# Phase 2 — Member Management
> Goal: Full CRUD for members via the web UI

- [ ] Member list page — show all members in a table
- [ ] Member list — search by name or member ID
- [ ] Member list — filter by status (active/inactive)
- [ ] Member registration form — create new member
- [ ] Member registration — auto-generate member ID
- [ ] Member registration — cascading dropdowns (region → province → municipality → barangay) using HTMX
- [ ] Member detail page — view full member profile
- [ ] Member edit page — update member info
- [ ] Member deactivate — soft delete (set status to inactive)
- [ ] Member photo upload

---

# Phase 3 — Attendance System
> Goal: Record and track attendance per event

- [ ] Attendance model
- [ ] Manual attendance — record attendance for a member
- [ ] Attendance list — view attendance records
- [ ] Attendance per event — link attendance to an event
- [ ] Attendance history — view member's past attendance
- [ ] Attendance report — summary per event

---

# Phase 4 — Events Management
> Goal: Create and manage NGO events

- [ ] Event model
- [ ] Create event form
- [ ] Event list page
- [ ] Event detail page
- [ ] Edit and cancel event
- [ ] Attendance per event report

---

# Phase 5 — Reports and Analytics
> Goal: Dashboards and exportable reports

- [ ] Dashboard stats — total members, recent attendance
- [ ] Member activity report
- [ ] Attendance summary per event
- [ ] Export to CSV

---

# Technical Debt / Improvements
> Things to fix or improve as you go

- [ ] Add pagination to list pages
- [ ] Add form validation error messages
- [ ] Add success/error flash messages (Django messages framework)
- [ ] Write tests for member registration
- [ ] Write tests for authentication
- [ ] Ruff linting passing
- [ ] Black formatting passing

---

# Learning Notes
> Write what you learned after completing each task

| Task | What I Learned |
|---|---|
| BaseModel | UUID primary keys, abstract models |
| Custom User | AbstractBaseUser, UserManager, AUTH_USER_MODEL |
| Chapters models | ForeignKey, PROTECT, related_name |
| Seed commands | Management commands, get_or_create, bulk_create |
| Authentication | AuthenticationForm, login(), logout(), @login_required |
