{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":33},"end":{"row":19,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"0040e198d8f6310f8658bb391db35a12679d0478","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":33},"action":"remove","lines":["from django.db import models","from django.contrib.auth.models import User","","from django.db.models.signals import post_save","from django.dispatch import receiver","","# USER'S PROFILE:","class UserProfile(models.Model):","","    user = models.OneToOneField(User, on_delete=models.CASCADE)","","","@receiver(post_save, sender=User)","def create_or_update_user_profile(sender, instance, created, **kwargs):","    \"\"\"","    Create a user profile for all new users","    \"\"\"","    if created:","        UserProfile.objects.create(user=instance)","    instance.userprofile.save()  "],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User","","from django.db.models.signals import post_save","from django.dispatch import receiver","","","\"\"\"","Create a user profile model","\"\"\"","class UserProfile(models.Model):","","    user = models.OneToOneField(User, on_delete=models.CASCADE)","    description = models.CharField(max_length=255, blank=True, null=True)","    picture = models.ImageField(upload_to=\"img/user\", blank=True, null=True)","    account = models.CharField(max_length=40, default='free')","    ","    ","\"\"\"","Create a user profile for all new users","\"\"\"","@receiver(post_save, sender=User)","def create_or_update_user_profile(sender, instance, created, **kwargs):","","    if created:","        UserProfile.objects.create(user=instance)","    instance.userprofile.save() ",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["from django.db import models","from django.contrib.auth.models import User","","from django.db.models.signals import post_save","from django.dispatch import receiver","","","\"\"\"","Create a user profile model","\"\"\"","class UserProfile(models.Model):","","    user = models.OneToOneField(User, on_delete=models.CASCADE)","    description = models.CharField(max_length=255, blank=True, null=True)","    picture = models.ImageField(upload_to=\"img/user\", blank=True, null=True)","    account = models.CharField(max_length=40, default='free')","    ","    ","\"\"\"","Create a user profile for all new users","\"\"\"","@receiver(post_save, sender=User)","def create_or_update_user_profile(sender, instance, created, **kwargs):","","    if created:","        UserProfile.objects.create(user=instance)","    instance.userprofile.save() ",""],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":19,"column":33},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User","","from django.db.models.signals import post_save","from django.dispatch import receiver","","# USER'S PROFILE:","class UserProfile(models.Model):","","    user = models.OneToOneField(User, on_delete=models.CASCADE)","","","@receiver(post_save, sender=User)","def create_or_update_user_profile(sender, instance, created, **kwargs):","    \"\"\"","    Create a user profile for all new users","    \"\"\"","    if created:","        UserProfile.objects.create(user=instance)","    instance.userprofile.save()  "],"id":5}]]},"timestamp":1566492407803}