set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput

# Create tables if they don't exist (sync database)
python manage.py migrate --run-syncdb

# Then run any remaining migrations
python manage.py migrate || echo "Some migrations failed, but continuing..."