from django.db import models

# Create your models here.


class Rating(models.Model):
    rating_id = models.CharField(max_length=10, primary_key=True, null=False)
    evaluation = models.CharField(max_length=50)

    def __str__(self):
        return self.rating_id + '-' + self.evaluation


class Platform(models.Model):
    platform_id = models.CharField(max_length=5, primary_key=True)
    platform_name = models.CharField(max_length=55)
    platform_developer = models.CharField(max_length=69)

    def __str__(self):
        return self.platform_name


class Developer(models.Model):
    developer_id = models.AutoField(primary_key=True)
    developer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.developer_name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=69)

    def __str__(self):
        return self.region_name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=150)

    def __str__(self):
        return self.genre_name


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    year_released = models.IntegerField(null=False)
    game_img = models.ImageField(upload_to='images/', default='')
    # foreign keys
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.platform_id);


class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    sales = models.IntegerField(null=True)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)

    def __str__(self):
        return str(self.game_id) + ' - ' + str(self.region_id) + ' - '+ str(self.sales) + ' - '+ str(self.year)


#class Game_sales_id(models.Model):
#    id = models.AutoField(primary_key=True)
#    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
#    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE)

#    class Meta:
#        managed = False

#PAGBUHAT NALAG INSERT INTO NGA ROUTINE BRO OKAY PERO UNYA NA KAPOY PAKO RON