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
