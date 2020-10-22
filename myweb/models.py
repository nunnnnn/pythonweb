from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'


class Sneakerstype(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Sneakers(models.Model):
    sneakerstype= models.ForeignKey(Sneakerstype, on_delete=models.CASCADE)
    Size= models.CharField(max_length=10)
    brand = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'


