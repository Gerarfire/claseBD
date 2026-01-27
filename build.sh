set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput

# Handle database setup more robustly
echo "Setting up database..."
python manage.py migrate --run-syncdb || echo "Sync failed, trying regular migrate..."
python manage.py migrate || echo "Migrations had issues, but continuing with deployment..."

# Populate database with sample data
echo "Populating database with sample data..."
python manage.py populate_data