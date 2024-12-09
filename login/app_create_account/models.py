from django.db import models

# Create your models here.

class User(models.Model):
    name_user = models.CharField(max_length=50, blank=False, null=False)
    password_user = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name_user


class Horta(models.Model):
    specie_horta = models.CharField(max_length=50, blank=True, null=True)
    color_horta = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='horta')

    def __str__(self) -> str:
        return self.specie_horta if self.specie_horta else "None"
    
    def delete(self, using=None, keep_parents=False):
        self.specie_horta = "None"
        self.color_horta = "None"
        self.save()

class HortaNutriente(models.Model):
    horta = models.ForeignKey(Horta, on_delete=models.CASCADE, related_name='foods')
    food_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.food_name} ({self.horta.specie_horta})"

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