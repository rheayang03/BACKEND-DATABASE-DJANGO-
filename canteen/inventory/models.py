from django.db import models

from django.db import models


class Supplier(models.Model):
    supp_id = models.IntegerField(db_column='SUPP_ID', primary_key=True)
    supp_name = models.CharField(db_column='SUPP_NAME', max_length=100)
    supp_contact = models.IntegerField(db_column='SUPP_CONTACT')

    class Meta:
        managed = False
        db_table = 'supplier'


class Inventory(models.Model):
    inv_itm_id = models.IntegerField(db_column='INV_ITM_ID', primary_key=True)
    inv_itm_name = models.CharField(db_column='INV_ITM_NAME', max_length=100)
    inv_itm_unit = models.CharField(db_column='INV_ITM_UNIT', max_length=20)
    inv_itm_qty = models.IntegerField(db_column='INV_ITM_QTY')
    inv_itm_rolvl = models.IntegerField(db_column='INV_ITM_ROLVL')
    supp = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='SUPP_ID')

    class Meta:
        managed = False
        db_table = 'inventory'


class InventoryTransaction(models.Model):
    inv_txn_id = models.IntegerField(db_column='INV_TXN_ID', primary_key=True)
    inv_txn_qty_change = models.IntegerField(db_column='INV_TXN_QTY_CHANGE')
    inv_txn_type = models.CharField(db_column='INV_TXN_TYPE', max_length=50)
    inv_txn_timestamp = models.DateTimeField(db_column='INV_TXN_TIMESTAMP')
    inv_itm = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='INV_ITM_ID')

    class Meta:
        managed = False
        db_table = 'inventorytransaction'


class MenuItem(models.Model):
    menuitm_id = models.IntegerField(db_column='MENUITM_ID', primary_key=True)
    menuitem_name = models.CharField(db_column='MENUITEM_NAME', max_length=100)
    menuitem_desc = models.CharField(db_column='MENUITEM_DESC', max_length=255)
    menuitem_price = models.DecimalField(db_column='MENUITEM_PRICE', max_digits=5, decimal_places=2)
    menuitem_is_avail = models.IntegerField(db_column='MENUITEM_IS_AVAIL')
    menuitem_img_url = models.CharField(db_column='MENUITEM_IMG_URL', max_length=255)

    class Meta:
        managed = False
        db_table = 'menuitem'


class MenuItemIngredient(models.Model):
    menuitm = models.ForeignKey(MenuItem, models.DO_NOTHING, db_column='MENUITM_ID')
    inv_itm = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='INV_ITM_ID')
    mii_qty_req = models.DecimalField(db_column='MII_QTY_REQ', max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'menuitemingredient'
        unique_together = (('menuitm', 'inv_itm'),)
