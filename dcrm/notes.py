# Saved code
# Step 1: Termianl Commands
# mkdir dcrm_app
# python3 -m venv .venv
# source .venv/bin/activate
# which python
# .venv/bin/python


# Step 2: Creating Application in Django
# django - admin startproject dcrm_app
# django-admin startproject dcrm_app

# Step 3: Configuring Django Application Settings
# psql --version
# psql -U postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'john',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# In Used Case we use SqLITE
# 'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
# }

# Step 4: Download pgadmin and postgres app
# Create the localhost connection to pgadmin to view the table

# Step 5: Testing Connection
# python manage.py makemigrations
# python manage.py migrate


# Step 6: Create the table for database
# python manage.py inspectdb view sample database
# python manage.py inspectdb > models.py (change database name)

# Step 7: Add to git repository (Public)
#
#
