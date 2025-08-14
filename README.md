# Large-Action-Model-OS

A Django web application for managing Telegram bot tasks and QA processes.

## Project Structure

```
FreyrQA_Portal/
├── app/                          # Main Django project directory
│   ├── config/                   # Project configuration
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py          # Main settings file
│   │   ├── urls.py              # URL routing
│   │   └── wsgi.py
│   ├── telegram_bot_task/        # Telegram bot app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── tests.py
│   │   ├── generate_gif.py      # Custom functionality
│   │   └── migrations/
│   ├── templates/                # HTML templates
│   │   └── base.html
│   ├── static/                   # Static files
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   ├── media/                    # User uploaded files (created when needed)
│   ├── manage.py                 # Django management script
│   └── db.sqlite3               # SQLite database
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
├── .env.example                 # Environment variables template
└── README.md                    # This file
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd FreyrQA_Portal
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy the example environment file
copy .env.example .env  # On Windows
# cp .env.example .env  # On macOS/Linux

# Edit .env file and add your configuration
```

### 5. Database Setup
```bash
# Navigate to the app directory
cd app

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Features

- **Django Admin Interface**: Access at `/admin/`
- **Telegram Bot Integration**: Ready for telegram bot implementation
- **Static Files Management**: CSS, JavaScript, and images
- **Template System**: Base template with extensible blocks
- **Environment-based Configuration**: Secure settings management

## Development

### Adding New Apps
```bash
cd app
python manage.py startapp your_app_name
```

Don't forget to add your new app to `INSTALLED_APPS` in `config/settings.py`.

### Database Migrations
```bash
cd app
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
cd app
python manage.py collectstatic
```

## Configuration

### Environment Variables

The following environment variables can be set in your `.env` file:

- `SECRET_KEY`: Django secret key (auto-generated if not provided)
- `DEBUG`: Debug mode (default: True)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string (optional)
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token (if applicable)

### Settings Structure

- `config/settings.py`: Main settings file with environment-based configuration
- Templates directory: `app/templates/`
- Static files directory: `app/static/`
- Media files directory: `app/media/`

## Apps

### telegram_bot_task
Contains the main functionality for telegram bot operations and task management.

## Security Notes

- Never commit your `.env` file to version control
- Generate a unique `SECRET_KEY` for production
- Set `DEBUG=False` in production
- Configure proper `ALLOWED_HOSTS` for production

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a Pull Request

## License

This project is private property
