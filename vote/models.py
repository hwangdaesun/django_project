from django.db import models
from acc.models import User
# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vwriter")
    pubdate = models.DateTimeField()
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")
    # 한 클래스에 동시에 같은 클라스를 참조하면 각각의 이름을 써야함 구별하기 위해서
 
    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) <10:
            return self.content
        else:
            return self.content[:10] + "..."

class Choice(models.Model):
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote/%y") # vote/%y/%m/%d 의 의미는 2022년 01월 10일 이라는 폴더가 만들어지고 거기에 사진이 업로드 된다.
    comment = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"






