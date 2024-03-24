# Generated by Django 5.0.3 on 2024-03-23 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('planned_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('attendee_target', models.PositiveIntegerField()),
                ('mentor_target', models.PositiveIntegerField()),
                ('support_target', models.PositiveIntegerField()),
                ('est_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('materials', models.TextField(blank=True)),
                ('is_open', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
