from django.db import models

# Create your models here.

class User(models.Model):
    name_user = models.CharField(max_length=50, blank=False, null=False)
    password_user = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name_user


class Animal(models.Model):
    specie_animal = models.CharField(max_length=50, blank=True, null=True)
    color_animal = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animal')

    def __str__(self) -> str:
        return self.specie_animal if self.specie_animal else "None"
    
    def delete(self, using=None, keep_parents=False):
        self.specie_animal = "None"
        self.color_animal = "None"
        self.save()

class AnimalFood(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='foods')
    food_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.food_name} ({self.animal.specie_animal})"

class Job(models.Model):
    company_job = models.CharField(max_length=50, blank=True, null=True)
    position_job = models.CharField(max_length=50, blank=True, null=True)
    salary_job = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job')

    def __str__(self) -> str:
        return self.position_job if self.position_job else "None"
    
    def delete(self, using=None, keep_parents=False):
       self.company_job = "None"
       self.position_job = "None"
       self.salary_job = 0  #CAMPO NUMÉRICO
       self.save()


class Document(models.Model):
    type_document = models.CharField(max_length=50, blank=True, null=True)
    number_document = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document')

    def __str__(self) -> str:
        return self.type_document if self.type_document else "None"
    
    def delete(self, using=None, keep_parents=False):
        self.type_document = "None"
        self.number_document = 0 #CAMPO NUMÉRICO
        self.save()