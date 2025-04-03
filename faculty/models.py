from django.db import models


# Create your models here.
class exam_name(models.Model):
    exam = models.CharField(max_length=50)
    center_incharge = models.IntegerField()
    gtu_co = models.IntegerField()
    sr_sup = models.IntegerField()
    jr_sup = models.IntegerField()
    st_sup = models.IntegerField()
    num_sup = models.IntegerField()
    peon = models.IntegerField()
    st_peon = models.IntegerField()
    sweeper = models.IntegerField()
    page_amount = models.IntegerField()


class department(models.Model):
    department_name = models.CharField(max_length=50)

    def _str_(self):
        return self.department_name

class faculty(models.Model):
    pancard = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class session(models.Model):
    session = models.CharField(max_length=50)

    def _str_(self):
        return self.session


class time(models.Model):
    session_id = models.ForeignKey(session, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)


class duty_type(models.Model):
    duty = models.CharField(max_length=50)


class semester(models.Model):
    sem = models.CharField(max_length=50)