# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Averages(models.Model):
    averages = models.CharField(db_column='Averages', primary_key=True, max_length=45)  # Field name made lowercase.
    cse = models.DecimalField(max_digits=10, decimal_places=2)
    it = models.DecimalField(max_digits=10, decimal_places=2)
    ece = models.DecimalField(max_digits=10, decimal_places=2)
    eee = models.DecimalField(max_digits=10, decimal_places=2)
    csm = models.DecimalField(max_digits=10, decimal_places=2)
    aiml = models.DecimalField(max_digits=10, decimal_places=2)
    mec = models.DecimalField(max_digits=10, decimal_places=2)
    civ = models.DecimalField(max_digits=10, decimal_places=2)
    aids = models.DecimalField(max_digits=10, decimal_places=2)
    college = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'averages'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class HomeAnnouncement(models.Model):
    text_input = models.CharField(max_length=200)
    date_input = models.DateField()

    class Meta:
        managed = False
        db_table = 'home_announcement'


class StudentMaster(models.Model):
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    roll_no = models.OneToOneField('StudentScores', models.DO_NOTHING, db_column='ROLL_NO', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=39)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sec = models.CharField(db_column='Sec', max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_Username', max_length=48, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    codeforces_username = models.CharField(db_column='CodeForces_Username', max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    codechef_username = models.CharField(db_column='CodeChef_Username', max_length=92, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    spoj_username = models.CharField(db_column='Spoj_Username', max_length=22, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    interviewbit_username = models.CharField(db_column='InterviewBit_Username', max_length=42, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    leetcode_username = models.CharField(db_column='LeetCode_Username', max_length=29, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    gfg_username = models.CharField(db_column='GFG_Username', max_length=48, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_master'


class StudentScores(models.Model):
    roll_no = models.CharField(db_column='ROLL_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    hackerrank = models.TextField(db_column='HackerRank', blank=True, null=True)  # Field name made lowercase.
    hackerrank_score = models.IntegerField(db_column='HackerRank_Score')  # Field name made lowercase.
    codeforces = models.TextField(db_column='CodeForces', blank=True, null=True)  # Field name made lowercase.
    codeforces_score = models.IntegerField(db_column='CodeForces_Score')  # Field name made lowercase.
    codechef = models.TextField(db_column='CodeChef', blank=True, null=True)  # Field name made lowercase.
    codechef_score = models.IntegerField(db_column='CodeChef_Score')  # Field name made lowercase.
    spoj = models.TextField(db_column='Spoj', blank=True, null=True)  # Field name made lowercase.
    spoj_score = models.IntegerField(db_column='Spoj_Score')  # Field name made lowercase.
    interviewbit = models.TextField(db_column='InterviewBit', blank=True, null=True)  # Field name made lowercase.
    interviewbit_score = models.IntegerField(db_column='InterviewBit_Score')  # Field name made lowercase.
    leetcode = models.TextField(db_column='LeetCode', blank=True, null=True)  # Field name made lowercase.
    leetcode_score = models.IntegerField(db_column='LeetCode_Score')  # Field name made lowercase.
    gfg = models.TextField(db_column='GFG', blank=True, null=True)  # Field name made lowercase.
    gfg_score = models.IntegerField(db_column='GFG_Score')  # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_score')  # Field name made lowercase.
    daily_scores = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_scores'
