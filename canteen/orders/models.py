from django.db import models

from django.db import models
from users.models import User


class PickupSlot(models.Model):
    pickupslot_id = models.IntegerField(db_column='PICKUPSLOT_ID', primary_key=True)
    pickupslot_time = models.TimeField(db_column='PICKUPSLOT_TIME')
    pickupslot_cap = models.IntegerField(db_column='PICKUPSLOT_CAP')

    class Meta:
        managed = False
        db_table = 'pickupslot'


class Orders(models.Model):
    order_id = models.IntegerField(db_column='ORDER_ID', primary_key=True)
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=50)
    order_date = models.DateField(db_column='ORDER_DATE')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')
    pickupslot = models.ForeignKey(PickupSlot, models.DO_NOTHING, db_column='PICKUPSLOT_ID')
    staff = models.ForeignKey('staff.Staff', models.DO_NOTHING, db_column='STAFF_ID')

    class Meta:
        managed = False
        db_table = 'orders'


class OrderItem(models.Model):
    orderitm_id = models.IntegerField(db_column='ORDERITM_ID', primary_key=True)
    orderitm_qty = models.CharField(db_column='ORDERITM_QTY', max_length=50)
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='ORDER_ID')
    menuitm = models.ForeignKey('inventory.MenuItem', models.DO_NOTHING, db_column='MENUITM_ID')

    class Meta:
        managed = False
        db_table = 'orderitem'


class Payment(models.Model):
    pymt_id = models.IntegerField(db_column='PYMT_ID', primary_key=True)
    pymt_amount = models.DecimalField(db_column='PYMT_AMOUNT', max_digits=5, decimal_places=2)
    pymt_method = models.CharField(db_column='PYMT_METHOD', max_length=50)
    pymt_status = models.CharField(db_column='PYMT_STATUS', max_length=20)
    pymt_tiestamp = models.DateTimeField(db_column='PYMT_TIESTAMP')
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='ORDER_ID')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')

    class Meta:
        managed = False
        db_table = 'payment'
