set -o errexit

# Upgrade pip/setuptools/wheel so that modern manylinux wheels (e.g. Pillow) are
# recognized and installed as wheels instead of forcing a source build.
python -m pip install --upgrade pip setuptools wheel
pip --version

# Intentar instalar Pillow primero como rueda binaria para evitar compilación
# costosa/errores en entornos sin dependencias de sistema.
# Usamos --prefer-binary para preferir wheel cuando esté disponible.
python -m pip install --prefer-binary "Pillow==10.1.0" || \
python -m pip install --prefer-binary "Pillow==10.0.1" || \
echo "Pillow pre-install falló: seguiremos y pip intentará instalarlo desde requirements (ver logs)"

# Instalar dependencias del sistema necesarias para compilar/instalar Pillow y
# otras librerías de imágenes en entornos Debian/Ubuntu (Render builders).
# Si tu builder no usa apt, estas líneas pueden fallar si el sistema es read-only;
# por eso no abortamos la build si apt falla.
if apt-get update >/dev/null 2>&1; then
  apt-get install -y build-essential libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff5-dev pkg-config || true
else
  echo "apt-get no disponible o falla: omitiendo instalación de dependencias de sistema"
fi

# Asegurar setuptools_scm para evitar errores de versión durante el build (necesario en algunos casos)
python -m pip install --upgrade setuptools_scm

# Instalar requerimientos (si Pillow ya está instalado, pip la saltará)
pip install -r requirements.txt || {
  echo "pip install falló — mostrando pip debug info";
  pip -v install -r requirements.txt || exit 1;
}

python manage.py collectstatic --noinput

# Handle database setup more robustly
echo "Setting up database..."
python manage.py migrate --run-syncdb || echo "Sync failed, trying regular migrate..."
python manage.py migrate || echo "Migrations had issues, but continuing with deployment..."

# Populate database with sample data
echo "Populating database with sample data..."
python manage.py populate_data

