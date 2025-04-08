# Generated by Django 5.1.7 on 2025-04-08 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='gtu_th_CP_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sub_1_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_1_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub1_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub1_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_2_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_2_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub2_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub2_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_3_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_3_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub3_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub3_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_4_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_4_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub4_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub4_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_5_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_5_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub5_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub5_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_6_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_6_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub6_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub6_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_7_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_7_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub7_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub7_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_8_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_8_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub8_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub8_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_9_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_9_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub9_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub9_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_10_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_10_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub10_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub10_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_11_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_11_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub11_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub11_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_12_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_12_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub12_no_of_student', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub12_no_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total_pages', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.exam_name')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.semester')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.session')),
            ],
        ),
        migrations.CreateModel(
            name='gtu_th_exam_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('block', models.PositiveIntegerField(default=0)),
                ('duty_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.duty_type')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.exam_name')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.semester')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.session')),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.time')),
            ],
        ),
    ]
