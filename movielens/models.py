from django.db import models

# Create your models here.

class Ratings(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return "[" + str(self.id) + "," \
                    + str(self.user_id) + "," \
                    + str(self.movie_id) \
                    + "," + str(self.rating) + "]"

    class Meta:
        db_table = "ratings"


class Movies(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return "[" + str(self.movie_id) + "," \
                    + str(self.title) + "," \
                    + str(self.title) + "," \
                    + str(self.genres) + "]"

    class Meta:
        db_table = "movies"