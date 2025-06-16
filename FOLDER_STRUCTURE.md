# Folder Structure Explanation

This document provides a brief explanation of the folder and file structure for the Django TODO app.

---

## Root Directory

- **manage.py**  
  Django's command-line utility for administrative tasks (runserver, migrate, etc).
- **db.sqlite3**  
  Default SQLite database file (auto-generated after migrations).
- **README.md**  
  Main project documentation and setup instructions.
- **FOLDER_STRUCTURE.md**  
  This file. Explains the folder and file structure.
- **TODO/**  
  Main Django project folder (contains settings, URLs, and configuration).
- **main/**  
  Main Django app for the home page and core features.

---

## TODO/ (Project Configuration)

- \***\*init**.py\*\*  
  Marks this directory as a Python package.
- **settings.py**  
  Main settings/configuration for the Django project (apps, database, middleware, etc).
- **urls.py**  
  Root URL configuration for the project.
- **wsgi.py**  
  WSGI entry point for deployment.
- **asgi.py**  
  ASGI entry point for asynchronous support.

---

## main/ (Main App)

- \***\*init**.py\*\*  
  Marks this directory as a Python package.
- **admin.py**  
  Register models for Django admin (default, can be customized).
- **apps.py**  
  App configuration for Django.
- **models.py**  
  Define database models (empty by default).
- **tests.py**  
  App-specific tests (empty by default).
- **views.py**  
  Contains view functions (e.g., `home`) that handle requests and return responses.
- **urls.py**  
  App-specific URL configuration (routes requests to views).
- **migrations/**  
  Database migration files (auto-generated, tracks model changes).
- **templates/**  
  Contains HTML templates for the app.
  - **main/**  
    App-specific template folder.
    - **home.html**  
      Responsive, theme-compatible home page template.

---

## main/migrations/

- \***\*init**.py\*\*  
  Marks the migrations directory as a Python package.
- _(other migration files)_  
  Auto-generated files for tracking database schema changes.

---

## main/templates/main/

- **home.html**  
  The main home page template, fully responsive and styled.

---

If you add new apps or features, follow the same structure for clarity and maintainability.
