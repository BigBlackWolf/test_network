# Network app

## Quick start guide

1. Create virtual environment of python or use global
2. Install dependencies
    ```bash 
    pip install -r requirements.txt
    ```
3. Make migrations of database
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py makemigrations social_network
    python manage.py migrate social_network
    ```
4. Run application
    ```bash
    python manage.py runserver
   ```

## Bot

To run bot just set your own settings in config.py and run as usual python script
