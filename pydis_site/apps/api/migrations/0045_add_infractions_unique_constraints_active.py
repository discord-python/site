# Generated by Django 2.2.6 on 2019-10-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_active_infractions_migration'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='infraction',
            constraint=models.UniqueConstraint(condition=models.Q(active=True), fields=('user', 'type'), name='unique_active_infraction_per_type_per_user'),
        ),
    ]
