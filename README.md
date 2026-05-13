# Donation Project

A simple Django donation application with a donation form, payment page, and success confirmation. Donations are saved to a local SQLite database.

## Features

- Donation form for name, email, mobile, and amount
- Payment confirmation page
- Success page with generated payment reference
- Donation records stored in `Donation` model

## Project Structure

- `donation_project/` - Django project configuration
- `donation/` - Django app with views, models, templates, and URLs
- `db.sqlite3` - SQLite database file
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.11+
- Django 5.2.14

## Setup

1. Clone the repository:
   ```powershell
   git clone https://github.com/poonamsweet/CharanVandan.git
   cd CharanVandan
   ```

2. Open a terminal in the project root:
   ```powershell
   cd donation_project
   ```

3. Create and activate the virtual environment:
   ```powershell
   python -m venv env
   .\env\Scripts\activate
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

5. Create the database schema:
   ```powershell
   python manage.py migrate
   ```

6. (Optional) Create a superuser for admin access:
   ```powershell
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```powershell
   python manage.py runserver
   ```

8. Open the app in your browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Usage

- Visit the home page and submit donor details.
- You will be redirected to the payment page.
- After submitting payment, you will see a success page with the generated payment ID.

## Notes

- The application currently simulates payment success.
