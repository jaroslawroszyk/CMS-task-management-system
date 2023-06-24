# Generated by Django 4.2.2 on 2023-06-19 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_alter_tasks_asigneduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='asigneduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
