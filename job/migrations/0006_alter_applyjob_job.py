# Generated by Django 4.2.7 on 2023-11-30 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_applyjob_company_applyjob_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
    ]