from django.db import models

# Create your models here.

class Users(models.Model):
    userid = models.IntegerField(db_column='userId', primary_key=True)  # Field name made lowercase. The composite primary key (userId, username) found, that is not supported. The first column is selected.
    username = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    github = models.CharField(max_length=45, blank=True, null=True)
    linkedin = models.CharField(max_length=45, blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    experience = models.CharField(max_length=500, blank=True, null=True)
    skills = models.CharField(max_length=500, blank=True, null=True)
    achievements = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=45, blank=True, null=True)
    project1 = models.CharField(max_length=300, blank=True, null=True)
    project2 = models.CharField(max_length=300, blank=True, null=True)
    project3 = models.CharField(max_length=300, blank=True, null=True)
    place = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('userid', 'username'),)
