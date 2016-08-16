# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Auth(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=32)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=64)
    instno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Institutions(models.Model):
    instno = models.AutoField(primary_key=True)
    institution = models.CharField(max_length=255)
    library = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    st = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    depno = models.CharField(max_length=255)
    genphone = models.CharField(db_column='genPhone', max_length=255)  # Field name made lowercase.
    genemail = models.CharField(db_column='genEmail', max_length=255)  # Field name made lowercase.
    dateinventory = models.CharField(db_column='dateInventory', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'institutions'


class Inventory(models.Model):
    newid = models.AutoField(primary_key=True)
    instno = models.IntegerField()
    servolno = models.CharField(max_length=255)
    held = models.CharField(max_length=4)
    deptl = models.CharField(max_length=4)
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'inventory'


class Servols(models.Model):
    newid = models.IntegerField(primary_key=True)
    ppno = models.CharField(max_length=255)
    servolno = models.CharField(max_length=255)
    orderno = models.CharField(max_length=255)
    congsess = models.CharField(max_length=255)
    title = models.TextField()
    docrptnos = models.CharField(max_length=255)
    annot = models.CharField(max_length=255)
    notissued = models.CharField(max_length=255)
    congress = models.CharField(max_length=255)
    siteroot = models.CharField(db_column='siteRoot', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servols'


class SsiCongress(models.Model):
    congress_number = models.IntegerField()
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssi_congress'


class SsiDocumenttype(models.Model):
    house = models.CharField(max_length=2)
    document_type = models.CharField(max_length=100)
    document_name = models.CharField(unique=True, max_length=106)

    class Meta:
        managed = False
        db_table = 'ssi_documenttype'


class SsiInstitution(models.Model):
    institution_name = models.CharField(max_length=255)
    library_name = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    depository_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.CharField(max_length=254)
    date_inventoried = models.DateField()
    hidden = models.IntegerField()
    address_1 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssi_institution'


class SsiInventory(models.Model):
    departmental_edition = models.IntegerField()
    note = models.CharField(max_length=255)
    institution = models.ForeignKey(SsiInstitution)
    volume = models.ForeignKey('SsiVolume')

    class Meta:
        managed = False
        db_table = 'ssi_inventory'


class SsiSession(models.Model):
    session_number = models.CharField(max_length=2)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    congress = models.ForeignKey(SsiCongress)

    class Meta:
        managed = False
        db_table = 'ssi_session'


class SsiVolume(models.Model):
    serial_number = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_numbers = models.CharField(max_length=255)
    annotation = models.CharField(max_length=255)
    not_issued = models.IntegerField()
    document_type = models.ForeignKey(SsiDocumenttype)
    session = models.ForeignKey(SsiSession)

    class Meta:
        managed = False
        db_table = 'ssi_volume'
