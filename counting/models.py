from django.db import models


TYPE = (
    ("input", "Kirish"),
    ("output", "Chiqish"),
    ("group_input", "Guruh bo'lib kirish"),
)


class Model(models.Model):
    camera_id = models.CharField(max_length=10, verbose_name="Kamera raqami")
    created = models.DateTimeField(verbose_name="Sana vaqt")
    number_of_people = models.IntegerField(verbose_name="Odamlar soni")
    image = models.ImageField(upload_to="images/group", verbose_name="Rasm")
    type = models.CharField(max_length=20, verbose_name="Holati", choices=TYPE)

    def __str__(self):
        return self.camera_id
