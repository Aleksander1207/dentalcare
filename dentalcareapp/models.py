from django.db import models


class Dentist(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    years_of_experience = models.IntegerField()
    practice_location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dentalcareapp/files/images/dentists', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    dentist = models.ForeignKey(Dentist, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='dentalcareapp/files/images/patients', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


class Appointment(models.Model):
    name = models.CharField(max_length=30)
    date_time = models.DateTimeField()
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
