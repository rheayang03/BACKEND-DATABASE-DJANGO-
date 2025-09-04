from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from inventory.models import MenuItem


class CateringRequest(models.Model):
    cater_req_id = models.IntegerField(db_column='CATER_REQ_ID', primary_key=True)
    cater_event_date = models.DateField(db_column='CATER_EVENT_DATE')
    cater_guest_cnt = models.IntegerField(db_column='CATER_GUEST_CNT')
    cater_status = models.CharField(db_column='CATER_STATUS', max_length=50)
    cater_deposit = models.DecimalField(db_column='CATER_DEPOSIT', max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')

    class Meta:
        managed = False
        db_table = 'cateringrequest'


class CateringMenuItem(models.Model):
    cater_req = models.ForeignKey(CateringRequest, models.DO_NOTHING, db_column='CATER_REQ_ID')
    menuitm = models.ForeignKey(MenuItem, models.DO_NOTHING, db_column='MENUITM_ID')
    cater_menuitem_qtyint = models.IntegerField(db_column='CATER_MENUITEM_QTYINT')

    class Meta:
        managed = False
        db_table = 'cateringmenuitem'
        unique_together = (('cater_req', 'menuitm'),)
