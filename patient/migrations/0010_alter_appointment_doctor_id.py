# Generated by Django 3.2.7 on 2022-05-09 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_alter_registrationform_address'),
        ('patient', '0009_appointment_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.updateform'),
        ),
    ]
