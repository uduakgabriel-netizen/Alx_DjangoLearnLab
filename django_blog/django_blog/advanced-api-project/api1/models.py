from django.db import models




class AuthorModel(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
    
class BookModel(models.Model):
    title = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
        
    