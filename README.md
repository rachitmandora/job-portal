# CareerHub — Job Portal

A modern, single-page job portal built with **Django**, **Django REST Framework**, and vanilla **HTML/CSS/JavaScript**. Recruiters and admins can publish job listings from a modal interface, while job seekers can browse openings and submit applications with instant visual confirmation.

## Features

- **Streamlined Authentication:** JWT-based login powered by SimpleJWT.
- **Quick Job Posting:** Modal-based "+ Post New Job" workflow accessible right from the landing view.
- **Live Job Feed:** Responsive card layout displaying job title, company, location, salary, and description.
- **One-Click Applications:** Submit applications with an optional cover letter and receive an instant confirmation modal.
- **Admin Management:** Full CRUD management of jobs, users, and applications via the Django Admin panel.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework, SimpleJWT
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API / FormData)
- **Database:** SQLite (default development database)

## Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rachitmandora/job-portal.git](https://github.com/rachitmandora/job-portal.git)
   cd job-portal
