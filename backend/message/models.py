from django.db import models
from django.conf import settings

class (models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phoneNumber = models.CharField(max_length=100)
    msg = models.TextField()

 
# <div>name</div>
# <div>mail</div>
# <div>phoneNumber</div>
# <div>message</div>
# <button>submit</button>

###################################################################
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()