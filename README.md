# TODO Django App

> **Educational Purpose Only**  
> This project is created exclusively for the students of PCPS, Kupondole, as a learning resource. Not intended for production use.

## Overview

A modern, responsive Django TODO starter app inspired by Airbnb's design principles. Built for performance, theme compatibility (light/dark), and professional, clean code using DRY principles. The app is fully responsive for all devices, including mobiles and tablets.

## Features

- Professional, clean, and modern UI (Airbnb-inspired)
- Responsive design for all devices
- Theme compatibility (light/dark mode)
- Django best practices (DRY, robust, maintainable code)
- Home page with navigation and call-to-action

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- (Recommended) Virtual environment tool: `venv` or `virtualenv`

### Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd TODO
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install django
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. **Open your browser**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the home page.

## Project Structure

```
TODO/
├── main/                  # Main app (home page)
│   ├── templates/
│   │   └── main/
│   │       └── home.html  # Responsive home page template
│   │
│   ├── views.py           # Home view
│   ├── urls.py            # App URLs
│   └── ...
├── TODO/                  # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3             # SQLite database (auto-generated)
├── manage.py              # Django management script
└── README.md              # Project documentation
```

## Customization

- To change the home page, edit `main/templates/main/home.html`.
- To add new features, create new apps and update `TODO/urls.py` and `settings.py` as needed.

## Credits

- **Created for:** PCPS Kupondole students
- **Maintainer:** Milan Yadav

## License

This project is for educational purposes only and is not licensed for commercial or production use.
