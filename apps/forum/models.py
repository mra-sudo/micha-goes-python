from django.db import models
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    posting = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    author = models.CharField(max_length=256, default="root")

    def __str__(self):
        return self.name

    def publish_topic(self):
        self.published_date = timezone.now()
        self.save()

    def topic_raise_view(self):
        self.views += 1
        self.save()

    def topic_is_active(self):
        if self.active:
            return True
        else:
            return False
    def topic_deactivate(self):
        self.active = False
        self.save()
    def topic_activate(self):
        self.active = True
        self.save()

    def topic_is_private(self):
        if self.private:
            return True
        else:
            return False
    def topic_set_private(self):
        self.private = True
        self.save()
    def topic_set_puplic(self):
        self.private = False
        self.save()



    #Potenziell denkbare weitere Funktionen: topic_change_name / topic_change_slug, ...


class Post(models.Model):
    topic = models.ForeignKey(to='Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    post = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=256)
    publish_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def post_raise_like(self):
        self.likes += 1
        self.save()
        #ggf. säter dann noch Rückgabe der Likes:
        #return self.likes

    def count_posts(self, name):
        count=self.objects.filter(topic__name=name).count()
        return count