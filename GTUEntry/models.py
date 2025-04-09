from django.db import models
from faculty.models import *


class gtu_th_exam_data(models.Model):
    exam_id = models.ForeignKey(exam_name, on_delete=models.CASCADE)
    date = models.DateField()
    session_id = models.ForeignKey(session, on_delete=models.CASCADE)
    time_id = models.ForeignKey(time, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(semester, on_delete=models.CASCADE)
    duty_type_id = models.ForeignKey(duty_type, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(faculty, on_delete=models.CASCADE)
    block = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.exam_id}"


class gtu_th_CP_data(models.Model):
    exam_id = models.ForeignKey(exam_name, on_delete=models.CASCADE)
    date = models.DateField()
    session_id = models.ForeignKey(session, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(semester, on_delete=models.CASCADE)

    sub_1_code = models.CharField(max_length=10, blank=True, null=True)
    sub_1_name = models.CharField(max_length=50, blank=True, null=True)
    sub1_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub1_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_2_code = models.CharField(max_length=10, blank=True, null=True)
    sub_2_name = models.CharField(max_length=50, blank=True, null=True)
    sub2_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub2_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_3_code = models.CharField(max_length=10, blank=True, null=True)
    sub_3_name = models.CharField(max_length=50, blank=True, null=True)
    sub3_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub3_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_4_code = models.CharField(max_length=10, blank=True, null=True)
    sub_4_name = models.CharField(max_length=50, blank=True, null=True)
    sub4_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub4_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_5_code = models.CharField(max_length=10, blank=True, null=True)
    sub_5_name = models.CharField(max_length=50, blank=True, null=True)
    sub5_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub5_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_6_code = models.CharField(max_length=10, blank=True, null=True)
    sub_6_name = models.CharField(max_length=50, blank=True, null=True)
    sub6_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub6_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_7_code = models.CharField(max_length=10, blank=True, null=True)
    sub_7_name = models.CharField(max_length=50, blank=True, null=True)
    sub7_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub7_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_8_code = models.CharField(max_length=10, blank=True, null=True)
    sub_8_name = models.CharField(max_length=50, blank=True, null=True)
    sub8_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub8_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_9_code = models.CharField(max_length=10, blank=True, null=True)
    sub_9_name = models.CharField(max_length=50, blank=True, null=True)
    sub9_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub9_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_10_code = models.CharField(max_length=10, blank=True, null=True)
    sub_10_name = models.CharField(max_length=50, blank=True, null=True)
    sub10_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub10_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_11_code = models.CharField(max_length=10, blank=True, null=True)
    sub_11_name = models.CharField(max_length=50, blank=True, null=True)
    sub11_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub11_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    sub_12_code = models.CharField(max_length=10, blank=True, null=True)
    sub_12_name = models.CharField(max_length=50, blank=True, null=True)
    sub12_no_of_student = models.PositiveIntegerField(default=0, blank=True, null=True)
    sub12_no_of_pages = models.PositiveIntegerField(default=0, blank=True, null=True)

    total_pages = models.PositiveIntegerField(default=0, blank=True, null=True)
