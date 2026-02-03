set -o errexit

# Upgrade pip/setuptools/wheel so that modern manylinux wheels (e.g. Pillow) are
# recognized and installed as wheels instead of forcing a source build.
python -m pip install --upgrade pip setuptools wheel
pip --version

# Instalar dependencias del sistema necesarias para compilar/instalar Pillow y
# otras librerías de imágenes en entornos Debian/Ubuntu (Render builders).
# Si tu builder no usa apt, puedes quitar estas líneas.
apt-get update && apt-get install -y build-essential libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff5-dev pkg-config

# Asegurar setuptools_scm para evitar errores de versión durante el build
python -m pip install --upgrade setuptools_scm

pip install -r requirements.txt

python manage.py collectstatic --noinput

# Handle database setup more robustly
echo "Setting up database..."
python manage.py migrate --run-syncdb || echo "Sync failed, trying regular migrate..."
python manage.py migrate || echo "Migrations had issues, but continuing with deployment..."

# Populate database with sample data
echo "Populating database with sample data..."
python manage.py populate_data

