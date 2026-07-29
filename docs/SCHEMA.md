# Database Schema

---

## BaseModel (abstract)

All tables inherit these fields.

| Column       | Type      | Notes                  |
| ------------ | --------- | ---------------------- |
| id           | UUID (PK) | Auto-generated         |
| created_at   | DateTime  | Auto set on create     |
| updated_at   | DateTime  | Auto set on update     |
| is_active    | Boolean   | Default: True          |

---

## accounts_user

Custom user model for system login (officers/admins only).

| Column       | Type         | Notes                  |
| ------------ | ------------ | ---------------------- |
| id           | UUID (PK)    | BaseModel              |
| email        | VARCHAR(254) | Unique, login field    |
| first_name   | VARCHAR(100) |                        |
| last_name    | VARCHAR(100) |                        |
| is_staff     | Boolean      | Default: False         |
| is_superuser | Boolean      | Default: False         |
| password     | VARCHAR(128) | Hashed                 |
| last_login   | DateTime     | Nullable               |

---

## chapters_region

| Column | Type        | Notes  |
| ------ | ----------- | ------ |
| id     | UUID (PK)   |        |
| name   | VARCHAR(100)|        |
| code   | VARCHAR(20) | Unique |

---

## chapters_province

| Column    | Type        | Notes                        |
| --------- | ----------- | ---------------------------- |
| id        | UUID (PK)   |                              |
| region_id | UUID (FK)   | → chapters_region            |
| name      | VARCHAR(100)|                              |

---

## chapters_municipality

| Column      | Type        | Notes                          |
| ----------- | ----------- | ------------------------------ |
| id          | UUID (PK)   |                                |
| province_id | UUID (FK)   | → chapters_province            |
| name        | VARCHAR(100)|                                |

---

## chapters_barangay

| Column          | Type        | Notes                            |
| --------------- | ----------- | -------------------------------- |
| id              | UUID (PK)   |                                  |
| municipality_id | UUID (FK)   | → chapters_municipality          |
| name            | VARCHAR(100)|                                  |

---

## members_member

| Column          | Type         | Notes                              |
| --------------- | ------------ | ---------------------------------- |
| id              | UUID (PK)    | BaseModel                          |
| member_id       | VARCHAR(20)  | Unique, e.g. ASDC-NCR-0001         |
| first_name      | VARCHAR(100) |                                    |
| middle_name     | VARCHAR(100) | Optional                           |
| last_name       | VARCHAR(100) |                                    |
| suffix          | VARCHAR(10)  | Optional                           |
| gender          | CHAR(1)      | M / F                              |
| birthdate       | Date         |                                    |
| civil_status    | VARCHAR(2)   | S / M / W / SE                     |
| mobile          | VARCHAR(15)  |                                    |
| email           | VARCHAR(254) | Optional                           |
| facebook        | VARCHAR(255) | Optional                           |
| street          | VARCHAR(255) | Optional                           |
| region_id       | UUID (FK)    | → chapters_region                  |
| province_id     | UUID (FK)    | → chapters_province                |
| municipality_id | UUID (FK)    | → chapters_municipality            |
| barangay_id     | UUID (FK)    | → chapters_barangay                |
| id_photo        | VARCHAR(255) | File path, optional                |
| status          | CHAR(1)      | A = Active, I = Inactive           |
| user_id         | UUID (FK)    | → accounts_user, nullable          |

---

## events_event (planned)

| Column      | Type         | Notes                              |
| ----------- | ------------ | ---------------------------------- |
| id          | UUID (PK)    | BaseModel                          |
| title       | VARCHAR(255) |                                    |
| description | TEXT         | Optional                           |
| event_date  | Date         |                                    |
| location    | VARCHAR(255) | Optional                           |
| type        | VARCHAR(20)  | e.g. meeting, seminar, outreach    |
| created_by  | UUID (FK)    | → accounts_user                    |

---

## attendance_attendance (planned)

| Column       | Type      | Notes                              |
| ------------ | --------- | ---------------------------------- |
| id           | UUID (PK) | BaseModel                          |
| member_id    | UUID (FK) | → members_member                   |
| event_id     | UUID (FK) | → events_event                     |
| checked_in   | DateTime  | Nullable                           |
| checked_out  | DateTime  | Nullable                           |
| recorded_by  | UUID (FK) | → accounts_user, nullable          |

Unique constraint: `(member_id, event_id)`

---

## Relationships Summary

```
accounts_user
    ↑ (OneToOne, nullable)
members_member
    ├── → chapters_region
    ├── → chapters_province
    ├── → chapters_municipality
    └── → chapters_barangay

events_event → accounts_user (created_by)

attendance_attendance
    ├── → members_member
    ├── → events_event
    └── → accounts_user (recorded_by)
```
