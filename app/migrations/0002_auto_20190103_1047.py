# Generated by Django 2.1.4 on 2019-01-03 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'articolo', 'verbose_name_plural': 'articoli'},
        ),
        migrations.AlterModelOptions(
            name='edition',
            options={'verbose_name': 'edizione', 'verbose_name_plural': 'edizioni'},
        ),
        migrations.AlterModelOptions(
            name='releaseyear',
            options={'verbose_name': 'anno', 'verbose_name_plural': 'anni'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'argomento', 'verbose_name_plural': 'argomenti'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReleaseYear'),
        ),
        migrations.AlterField(
            model_name='releaseyear',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
