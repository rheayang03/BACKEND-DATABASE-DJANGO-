from django.db import models

# Create your models here.
from django.db import models


class Staff(models.Model):
    staff_id = models.IntegerField(db_column='STAFF_ID', primary_key=True)
    staff_fullname = models.CharField(db_column='STAFF_FULLNAME', max_length=100)
    staff_role = models.CharField(db_column='STAFF_ROLE', max_length=100)
    staff_contact = models.IntegerField(db_column='STAFF_CONTACT')
    staff_assnd_stn = models.CharField(db_column='STAFF_ASSND_STN', max_length=50)

    class Meta:
        managed = False
        db_table = 'staff'


class StaffActivityLog(models.Model):
    sal_id = models.IntegerField(db_column='SAL_ID', primary_key=True)
    sal_action = models.CharField(db_column='SAL_ACTION', max_length=255)
    sal_timestamp = models.DateTimeField(db_column='SAL_TIMESTAMP')
    staff = models.ForeignKey(Staff, models.DO_NOTHING, db_column='STAFF_ID')

    class Meta:
        managed = False
        db_table = 'staffactivitylog'
