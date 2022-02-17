# Generated by Django 3.2.11 on 2022-02-17 05:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('location', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('location', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('skill', models.CharField(choices=[('Junior', 'Junior'), ('Mid-Level', 'Mid-Level'), ('Expert', 'Expert')], max_length=100)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('hired', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Mechanic',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('two wheeler with gear', 'two wheeler with gear'), ('two wheeler without gear', 'two wheeler without gear'), ('three wheeler', 'three wheeler'), ('four wheeler', 'four wheeler')], max_length=100)),
                ('vehicle_no', models.PositiveIntegerField()),
                ('vehicle_name', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_brand', models.CharField(max_length=100)),
                ('problem_description', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.customer')),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.mechanic')),
            ],
            options={
                'verbose_name_plural': 'Request',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('present_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.mechanic')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
            },
        ),
    ]
