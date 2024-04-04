# Generated by Django 5.0.3 on 2024-04-04 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workshops', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eoi_type', models.CharField(choices=[('Organise', 'Organise'), ('Attend', 'Attend'), ('Mentor', 'Mentor')], default='Attend', max_length=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eois', to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eois', to='workshops.workshop')),
            ],
        ),
    ]
