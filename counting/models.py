from django.db import models


TYPE = (
    ("input", "Kirish"),
    ("output", "Chiqish"),
    ("group_input", "Guruh bo'lib kirish"),
)

FACE_TYPE = (
    ("customer", "Customer"),
    ("worker", "Worker"),
)


class Model(models.Model):
    camera_id = models.CharField(max_length=10, verbose_name="Kamera raqami")
    number_of_people = models.IntegerField(verbose_name="Odamlar soni")
    image = models.ImageField(upload_to="images/group", verbose_name="Rasm")
    type = models.CharField(max_length=20, verbose_name="Holati", choices=TYPE)
    created = models.DateTimeField(verbose_name="Sana vaqt")

    def __str__(self):
        return self.camera_id
    

class Worker(models.Model):
    uuid = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="workers")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    

class Face(models.Model):
    worker = models.ForeignKey(Worker, null=True, on_delete=models.SET_NULL, blank=True)
    type = models.CharField(max_length=20, choices=FACE_TYPE)
    image = models.ImageField(upload_to="images/faces")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)
