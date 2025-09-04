from django.db import models

from django.db import models


class User(models.Model):
    user_id = models.IntegerField(db_column='USER_ID', primary_key=True)
    user_firstname = models.CharField(db_column='USER_FIRSTNAME', max_length=50)
    user_lastname = models.CharField(db_column='USER_LASTNAME', max_length=50)
    user_email = models.CharField(db_column='USER_EMAIL', unique=True, max_length=100)
    user_pass = models.CharField(db_column='USER_PASS', max_length=255)
    user_type = models.CharField(db_column='USER_TYPE', max_length=20)
    user_joindate = models.DateField(db_column='USER_JOINDATE')

    class Meta:
        managed = False
        db_table = 'user'


class Points(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, db_column='USER_ID', primary_key=True)
    pts_bal = models.DecimalField(db_column='PTS_BAL', max_digits=5, decimal_places=2)
    pts_last_upd = models.DateTimeField(db_column='PTS_LAST_UPD')

    class Meta:
        managed = False
        db_table = 'points'


class PointTransaction(models.Model):
    pts_txn_id = models.IntegerField(db_column='PTS_TXN_ID', primary_key=True)
    pts_txn_change = models.DecimalField(db_column='PTS_TXN_CHANGE', max_digits=3, decimal_places=2)
    pts_txn_type = models.CharField(db_column='PTS_TXN_TYPE', max_length=50)
    pts_txn_timestamp = models.DateTimeField(db_column='PTS_TXN_TIMESTAMP')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')
    order = models.ForeignKey('orders.Orders', models.DO_NOTHING, db_column='ORDER_ID')

    class Meta:
        managed = False
        db_table = 'pointtransaction'


class Notification(models.Model):
    notif_id = models.IntegerField(db_column='NOTIF_ID', primary_key=True)
    notif_msg = models.CharField(db_column='NOTIF_MSG', max_length=255)
    notif_type = models.CharField(db_column='NOTIF_TYPE', max_length=50)
    notif_is_read = models.IntegerField(db_column='NOTIF_IS_READ')
    notif_timestamp = models.DateTimeField(db_column='NOTIF_TIMESTAMP')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')

    class Meta:
        managed = False
        db_table = 'notification'
