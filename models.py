from django.db import models 
from django.contrib.auth.models import User

class location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    

class Accident(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    narration = models.TextField()
    photo = models.ImageField(upload_to='accidents/photos/')
    reason = models.CharField(max_length=50, choices=[
        ('negligence', 'Driver Negligence'),
        ('drunk', 'Drunken Driving'),
        ('speed', 'Excess Speed'),
        ('overtake', 'Improper Overtake'),
        ('environment', 'Adverse Environmental Conditions'),
        ('mechanical', 'Mechanical Failure'),
        ('road_condition', 'Poor Road Conditions'),
        ('animals', 'Animals Crossing'),
        ('other', 'Other')
    ])
    severity = models.CharField(max_length=10, choices=[
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ])
    weather_conditions = models.CharField(max_length=20, choices=[
        ('clear', 'Clear'),
        ('rainy', 'Rainy'),
        ('foggy', 'Foggy'),
        ('snowy', 'Snowy'),
        ('other', 'Other'),
    ])
    road_conditions = models.CharField(max_length=20, choices=[
        ('dry', 'Dry'),
        ('wet', 'Wet'),
        ('icy', 'Icy'),
        ('under_construction', 'Under Construction'),
        ('potholes', 'Potholes'),
        ('other', 'Other'),
    ])
    VIN = models.CharField(max_length=50, blank=True)
    make = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    license_plate = models.CharField(max_length=50, blank=True)
    insurance_info = models.TextField(blank=True)
    num_casualties = models.PositiveSmallIntegerField(default=0)
    death_count = models.PositiveSmallIntegerField(default=0)
    major_injuries = models.PositiveSmallIntegerField(default=0)
    minor_injuries = models.PositiveSmallIntegerField(default=0)

    @property
    def total_injuries(self):
        return self.major_injuries + self.minor_injuries

    def __str__(self):
        return f"{self.location}: {self.date}"

class Casualty(models.Model):
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE, related_name='casualties')
    age_group = models.CharField(max_length=10, choices=[
        ('18-25', '18-25 Years Old'),
        ('26-35', '26-35 Years Old'),
        ('36-45', '36-45 Years Old'),
        ('46-60', '46-60 Years Old'),
        ('60+', '60 Years Old and Above'),
    ])
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer Not to Say'),
    ])

    def __str__(self):
        return f"{self.accident}: {self.age_group} ({self.gender})"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=10, choices=[
        ('18-25', '18-25 Years Old'),
        ('26-35', '26-35 Years Old'),
        ('36-45', '36-45 Years Old'),
        ('46-60', '46-60 Years Old'),
        ('60+', '60 Years Old and Above'),
    ])
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer Not to Say'),
    ])

    def __str__(self):
        return f"{self.user.username}'s Profile"