from django.db import models

# Create your models here.
class DadJoke(models.Model):
    """ Dad Joke"""
    joke_question = models.CharField(max_length=255, default="")
    joke_answer   = models.CharField(max_length=255, default="")
    groan_factor = models.IntegerField()
        # Add max value???
        # Add validator?????

    def get_DadJoke(self):
        """ retrieve full name of user"""
        return self.joke_question

    def __str__(self):
        """Return the model(joke) as a string"""
        return self.joke_question

# Add vote class?????


class DadJokeFeedItem(models.Model):
    """ Dad Joke"""
    joke_question = models.CharField(max_length=255)
    joke_answer   = models.CharField(max_length=255)
    groan_factor = models.IntegerField()
        # Add max value???
        # Add validator?????

    def __str__(self):
        """Return the model(joke) as a string"""
        return self.joke_question
