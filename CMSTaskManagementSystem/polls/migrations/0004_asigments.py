# Generated by Django 4.2.2 on 2023-06-16 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_rename_elements_tasks_alter_tasks_fcolumn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asigments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.boards')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
