from django.db import models
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import ordinal

from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField
import googlemaps


class Institution(models.Model):
    institution_name = models.CharField(max_length=255)
    library_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = USStateField()
    zip_code = USZipCodeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    depository_number = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email_address = models.EmailField()
    date_inventoried = models.DateField()
    hidden = models.BooleanField(default=False)
    volumes = models.ManyToManyField('Volume', through='Inventory')

    def get_coordinates(self):
        address = '{address_1} {address_2}, {city}, {state} {zip_code}'.format(
            address_1=self.address_1,
            address_2=self.address_2,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code
        )
        api_key = settings.GOOGLE_API_KEY
        gmaps = googlemaps.Client(key=api_key)
        geocode_result = gmaps.geocode(address)

        if len(geocode_result) > 0:
            self.latitude = geocode_result[0]['geometry']['location']['lat']
            self.longitude = geocode_result[0]['geometry']['location']['lng']

    def save(self, *args, **kwargs):
        self.get_coordinates()
        super(Institution, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.institution_name


class Congress(models.Model):
    congress_number = models.IntegerField()
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '{} Congress'.format(ordinal(self.congress_number))


class Session(models.Model):
    # Selectable senate sessions.
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'
    SPECIAL = 'S'

    SESSION_CHOICES = (
        (FIRST, '1st'),
        (SECOND, '2nd'),
        (THIRD, '3rd'),
        (FOURTH, '4th'),
        (FIFTH, '5th'),
        (SPECIAL, 'Special')
    )

    session_number = models.CharField(max_length=2, choices=SESSION_CHOICES)
    congress = models.ForeignKey(Congress)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '{}, {} Session'.format(self.congress, self.session_number)


class DocumentType(models.Model):
    HOUSES = (
        ('House', 'H'),
        ('Senate', 'S')
    )

    # Document types to add:
    # House Journal
    # House Document
    # House Report
    # House Executive Document
    # House Miscellaneous Document
    # Senate Journal
    # Senate Document
    # Senate Executive Document
    # Senate Miscellaneous Document
    # Senate Report
    # Senate Treaty
    # Senate Executive Report

    house = models.CharField(max_length=2, choices=HOUSES)
    document_type = models.CharField(max_length=100)
    document_name = models.CharField(max_length=106, unique=True)

    def create_name(self):
        self.document_name = '{} {}'.format(self.house, self.document_type)

    def save(self, *args, **kwargs):
        self.create_name()
        super(DocumentType, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.create_name()


class Volume(models.Model):

    serial_number = models.CharField(max_length=255)
    session = models.ForeignKey(Session)
    document_type = models.ForeignKey(DocumentType)
    title = models.CharField(max_length=255, blank=True)
    publication_numbers = models.CharField(max_length=255, blank=True)
    annotation = models.CharField(max_length=255, blank=True)
    not_issued = models.BooleanField(default=False)

    def citation(self):
        return '{}, Serial No. {}, {}'.format(
            self.session,
            self.serial_number,
            self.title
        )

    def __unicode__(self):
        return '{} {}'.format(self.serial_number, self.document_type)


class Inventory(models.Model):
    institution = models.ForeignKey(Institution)
    volume = models.ForeignKey(Volume)
    departmental_edition = models.BooleanField(default=False)
    note = models.CharField(max_length=255)

#
# Old Database models generated by inspectdb
#


class OldAuth(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=32)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=64)
    instno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth'


class OldInstitutions(models.Model):
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


class OldInventory(models.Model):
    newid = models.AutoField(primary_key=True)
    instno = models.ForeignKey(OldInstitutions)
    servolno = models.ForeignKey('OldServols')
    held = models.CharField(max_length=4)
    deptl = models.CharField(max_length=4)
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'inventory'


class OldServols(models.Model):
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