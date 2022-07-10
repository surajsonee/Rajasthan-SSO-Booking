from random import choice, choices
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


PROTECTED_AREA= [
    ('Select', 'Select'),
    ('Ranthambore National Park - Sawai Madhopur', 'Ranthambore National Park - Sawai Madhopur'),
    ]
ZONE= [
    ('Select', 'Select'),
    ('Zone 1', 'Zone 1'),
    ('Zone 2', 'Zone 2'),
    ('Zone 3', 'Zone 3'),
    ('Zone 4', 'Zone 4'),
    ('Zone 5', 'Zone 5'),
    ('Zone 6', 'Zone 6'),
    ('Zone 7', 'Zone 7'),
    ('Zone 8', 'Zone 8'),
    ('Zone 9', 'Zone 9'),
    ('Zone 10', 'Zone 10'),
    ]
SHIFT= [
        ('Select', 'Select'),
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]
VEHICHLE= [
    ('Select', 'Select'),
    ('Canter', 'Canter'),
    ('Gypsy', 'Gypsy'),
]
GENDER= [
    ('Select', 'Select'),
    ('Male', 'Male  '),
    ('Female', 'Female'),
    ('Transgender', 'Transgender'),
]
NATIONALITY= [
    ('Select', 'Select'),
    ('Indian', 'Indian'),
    ('Foreigner', 'Foreigner'),
]
ID_TYPE= [
    ('Select', 'Select'),
    ('Passport', 'Passport'),
    ('Aadhar', 'Aadhar'),
    ('Driving Licence', 'Driving Licence'),
    ('Voter Id', 'Voter Id'),
    ('PAN Card', 'PAN Card'),
    ('Office ID', 'Office ID'),
    ('Student ID', 'Student ID'),
]

class Visitor_Register(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    protected_area = models.CharField(max_length=100, choices=PROTECTED_AREA, default="Select")
    zone = models.CharField(max_length=10, choices=ZONE, default="Select")
    visit_date = models.DateField()
    choose_shift = models.CharField(max_length=20,choices=SHIFT, default="Select")
    vehicle_type = models.CharField(max_length=20,choices=VEHICHLE, default="Select")
    member_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=GENDER, default="Select")
    nationality = models.CharField(max_length=30, choices=NATIONALITY, default="Select")
    id_type = models.CharField(max_length=30, choices=ID_TYPE, default="Select")
    id_number = models.CharField(max_length=30)
    video_cam = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)