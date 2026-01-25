set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput

# Run migrations with fake-initial to handle existing tables
python manage.py migrate --fake-initial