# Generated by Django 3.2.9 on 2022-01-09 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vwri', to=settings.AUTH_USER_MODEL),
        ),
    ]
