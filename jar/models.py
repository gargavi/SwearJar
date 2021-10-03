from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField()
    number_jars = models.IntegerField(default=0)
    photo_url = models.URLField()

    def add_jar(self):
        self.number_jars += 1

    def return_name_upper(self):
        return self.name.upper()

    def return_number_jars(self):
        return len(self.jar_set.all())


class Jar(models.Model):
    current_balance = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    name = models.CharField(max_length=200)

    def update_description(self, new_description):
        assert type(new_description) == str
        assert len(new_description) <= 200
        self.description = new_description

    def add_to_balance(self, amount):
        assert type(amount) == int
        self.current_balance += amount

    def create_log(self, content, penalty, submitter = "None"):
        self.log_set.create(content = content, date_created = timezone.now(), penalty= penalty, submitter = submitter)
        self.add_to_balance(penalty)

    @property
    def sorted_log(self):
        return self.log_set.order_by('-date_created')


class Log(models.Model):
    jar_id = models.ForeignKey(Jar, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    penalty = models.IntegerField()
    submitter = models.CharField(max_length = 200)





