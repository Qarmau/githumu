# main/models.py
from django.db import models
from django.utils import timezone



TITLE_CHOICES = [
        ('Mr. ', 'Mr. '),
        ('Mrs. ', 'Mrs. '),
        ('Ms. ', 'Ms. '),
       
    ]

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField()

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News")









# main/models.py

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


"""class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()"""

class About(models.Model):
    history = models.TextField()
    population = models.IntegerField()
    motto = models.CharField(max_length=200)
    vision = models.TextField()
    mission = models.TextField()
    subjects = models.TextField()
    clubs = models.TextField()
    contact_info = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return "About Page Content"

class Administrator(models.Model):
    ROLE_CHOICES = [
        ('principal', 'Principal'),
        ('deputy_admin', 'Deputy Admin'),
        ('deputy_academic', 'Deputy Academic'),
    ]
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES, default= ' ' )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='teacher')
    photo = models.ImageField(upload_to='admin_photos/')
    order = models.IntegerField()
# main/models.py
class TeachingStaff(models.Model):
    ROLE_CHOICES = [
        ('principal', 'Principal'),
        ('deputy_admin', 'Deputy Admin'),
        ('deputy_academic', 'Deputy Academic'),
        ('HOD','HOD'),
        ('HOS','HOS'),
        ('teacher', 'Teacher'),
    ]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES, default= ' ' )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='teacher')
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff_photos/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'role', 'name']

    def __str__(self):
        return self.name










"""class TeachingStaff(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subjects = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='staff_photos/')
    order = models.IntegerField()"""

class Achievement(models.Model):
    year = models.IntegerField()
    university_admission_rate = models.FloatField()

"""class CoCurricularAward(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()"""





# main/models.py

class CoCurricularAward(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='awards/', blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} ({self.year})"







class HolidayAssignment(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=50)
    file = models.FileField(upload_to='assignments/')
    upload_date = models.DateTimeField(auto_now_add=True)

# main/models.py

class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# main/models.py

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Background Image {self.id}"






class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    specification = models.TextField()
    minimum_requirements = models.TextField()
    deadline = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    def is_active(self):
        return timezone.now() <= self.deadline
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    document = models.FileField(upload_to='job_applications/')
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"










