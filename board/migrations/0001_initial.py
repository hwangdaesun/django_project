# Generated by Django 3.2.9 on 2021-12-28 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('pubdate', models.DateTimeField()),
                ('likey', models.ManyToManyField(blank=True, related_name='likey', to=settings.AUTH_USER_MODEL)),
                ('writer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wri', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
