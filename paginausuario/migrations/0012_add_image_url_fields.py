from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginausuario', '0011_add_imagen_to_ventagarage'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='foto_perfil_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ventagarage',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
