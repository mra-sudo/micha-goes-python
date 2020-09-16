from datetime import timedelta, datetime
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    publish_time = models.DateTimeField()
    days_running = models.IntegerField(default=7)
    unique_views = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "{0} (Slug: {1}) (Views: {2})".format(self.name, self.slug, self.views)

    def is_active(self):
        end_time = self.publish_time + timedelta(days=self.days_running)
        if timezone.now() >= self.publish_time and timezone.now() <= end_time:
            return True
        else:
            return False

    def poll_raise_view(self):
        self.views += 1
        self.save()


class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1})".format(self.poll.name, self.name)


