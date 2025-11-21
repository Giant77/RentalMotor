# Vehicle Rental System

A modular Django prototype implementing a vehicle rental workflow with integrated state-machine logic, admin-controlled approval, deposit handling, and an in-app notification system for both administrators and end-users.

The project demonstrates:

- **Vehicle management**
- **Rental lifecycle** using State Design Pattern
- **Add-on pricing** using Decorator Pattern
- **Internal notifications** for admins and users
- **Admin approval and rejection flow**
- **Transaction visibility separation** (admin vs. user)
- **Template-based navigation** and restricted UI behavior
- **Safe rental availability enforcement**

Or you can check the test deployment [here](https://gi4nt.pythonanywhere.com/).

<!-- _This repository is intended as a structural prototype, not a full production deployment._ -->

---

## Features

### Vehicle Module

- Vehicle CRUD through Django admin.
- Vehicle image upload.
- Real-time vehicle availability checks.
- **Automatic status updates:**
  - `available → rented` upon approval.
  - `rented → available` upon completion.

### Rental Module

- Rental creation with date range and add-ons.
- Add-ons implemented using a **Decorator pattern**.
- Deposit upload and validation.
- Approval and rejection through Django admin.
- Rental state transitions through **State & Factory Design Pattern**.
- User-visible and admin-visible transaction pages.

### Notification System

- Internal notification model stored in the database.
- **User notifications for:**
  - Deposit submitted
  - Admin approval
  - Admin rejection
- **Admin notifications for:**
  - Pending approval requests
- Notification dropdown in navbar with unread counter.
- Individual dismissal and “mark as read” behavior.
- **Optional:** WebSocket real-time updates via Channels.

### Template/UI

- Global base template with navigation.
- Auth conditions in navbar.
- Notification bell with unread badge.
- Disabled “Rent” button for unavailable vehicles.
- Tooltip explaining vehicle status.

---

## Project Structure (Simplified)

```text
RentalMotor/
│
├── accounts/                # Authentication (login, signup)
├── vehicles/                # Vehicle models, views, templates
├── rentals/                 # Rental process, states, decorators
│   ├── states/              # State Design Pattern implementations
│   └── decorator/           # Add-on pricing
│
├── notifications/           # Internal notification system
│   ├── models.py
│   ├── views.py
│   ├── context_processors.py
│   └── consumers.py         # Optional WebSocket support
│
├── templates/
│   ├── base/                # Base layout
│   ├── vehicles/
│   ├── rentals/
│   └── notifications/
│
└── manage.py
```

---

## Requirements

- **Python:** 3.11+
- **Django:** 5.x
- **Pillow:** 12.x (For image uploads)
- **Bootstrap 5:** (Included via CDN in base templates)

**Optional (for WebSockets):**

- Redis
- `channels`, `channels-redis`

---

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/Giant77/RentalMotor.git
```

### 2. (Optional) Create and activate virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If a `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

### 4. Enter project directories

```bash
cd RentalMotor
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Seed vehicle dataset (opsional)

```bash
python manage.py seed_vehicles
```

### 8. Run development server

```bash
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000/`

---

## Usage

### Admin Usage

Visit `/admin/` to manage:

- **Vehicles**
- **Rentals** (Add approvals, rejections, finalizations)
- **Notifications**

**Admin actions invoke state transitions:**

- Approve rental → Vehicle becomes `rented`.
- Reject rental → Rental ends.
- Complete rental → Vehicle becomes `available`.

### User Workflow Summary

1. Browse available vehicles.
2. Start rental (only if `vehicle.status = available`).
3. Select dates and add-ons.
4. Upload SIM and deposit.
5. Rental enters `awaiting_verification`.
6. Admin approves or rejects.
7. User sees notifications through bell icon.

---

## Notes

> - This project is structured as a teaching and prototype reference.
> - UI is intentionally minimal.
> - Component interactions emphasize clarity of design patterns:
>   - **State Pattern** for rental and vehicle lifecycle.
>   - **Decorator Pattern** for add-on behavior.
>   - **Template inheritance** for UI consistency.
>   - **Internal notification model** for all communication.

## Contributions

Feel free to fork the project and submit pull requests. Contributions are welcome! Here’s how you can contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Make changes and commit them
4. Push the changes to your forked repository
5. Open a pull request with a description of your changes

## Contact

For questions or further details, feel free to contact me at:

- Email: [willy.ja@mhs.usk.ac.id](mailto:willy.ja@mhs.usk.ac.id)
- GitHub: [Willy Jonathan Arsyad](https://github.com/Giant77)
