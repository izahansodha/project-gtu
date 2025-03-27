from django.db import models

# Create your models here.
class exam_name(models.Model):
    exam = models.CharField(max_length=50)
    center_incharge = models.CharField(max_length=50)
    gtu_co = models.CharField(max_length=50)
    sr_sup = models.CharField(max_length=50)
    jr_sup = models.CharField(max_length=50)
    st_sup = models.CharField(max_length=50)
    num_sup = models.CharField(max_length=50)
    peon = models.CharField(max_length=50)
    st_peon = models.CharField(max_length=50)
    sweeper = models.CharField(max_length=50)
    page_amount = models.CharField(max_length=50)

    
class faculty(models.Model):
    pancard = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class department(models.Model):
    department_name = models.CharField(max_length=50)

class time(models.Model):
    session_id = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

class duty_type(models.Model):
    duty = models.CharField(max_length=50)

class semester(models.Model):
    sem = models.CharField(max_length=50)

class session(models.Model):
    session = models.CharField(max_length=50)
