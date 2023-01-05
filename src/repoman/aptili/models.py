from django.db import models

# Create your models here.
class commands(models.Model):
    command = models.TextField(max_length=500, blank=False)
    # 0=fail, 1=success, 2=continuing
    status = models.SmallIntegerField(blank=False)
    output_file = models.FilePathField(blank=False)
    start_date = models.DateTimeField(blank=False)
    fnish_date = models.DateTimeField(blank=False)

#mirrolanabilir pardus repoları
class aptili_our_mirror(models):
    pardus_mirror = models.TextField(max_length=100, blank=False)

#mirrolanmış pardus repoları
class aptili_mirror(models.Model):
    mirror_name = models.TextField(max_length=100, blank=False)

#mirrolanmış pardus repolarının durumları = güncel/güncel değil-neler gelmiş güncel
class mirror_status(models.Model):
    #aptili_mirror = models.ForeignKey("aptili_mirror")
    #status = 
    #diff =
    pass 

#oluşturulmuş local repoları
class aptili_repo(models.Model):
    repo_name = models.TextField(max_length=100, blank=False)
    distribution = models.TextField(max_length=100, blank=False)
    comment = models.TextField(max_length=100, blank=False)
    number_of_packages = models.IntegerField(blank=False)

#pardus mirrorla 17 19 21
#local repo repo-name