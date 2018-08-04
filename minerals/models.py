from django.db import models


# Create your models here.

class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255, default="",
                                     blank=True)
    category = models.CharField(max_length=255, default="",
                                blank=True)
    formula = models.CharField(max_length=400)
    strunz_classification = models.CharField(max_length=255, default="",
                                             blank=True)
    crystal_system = models.CharField(max_length=255, default="",
                                      blank=True)
    unit_cell = models.CharField(max_length=255, default="",
                                 blank=True)
    color = models.CharField(max_length=255, default="",
                             blank=True)
    crystal_symmetry = models.CharField(max_length=255, default="",
                                        blank=True)
    cleavage = models.CharField(max_length=255, default="",
                                blank=True)
    mohs_scale_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255, default="",
                              blank=True)
    streak = models.CharField(max_length=255, default="",
                              blank=True)
    diaphaneity = models.CharField(max_length=255, default="",
                                   blank=True)
    optical_properties = models.CharField(max_length=255, default="",
                                          blank=True)
    refractive_index = models.CharField(max_length=255, default="",
                                        blank=True)
    crystal_habit = models.CharField(max_length=255, default="",
                                     blank=True)
    specific_gravity = models.CharField(max_length=255, default="",
                                        blank=True)
    group = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name,
               image_filename,
               image_caption,
               category,
               formula,
               strunz_classification,
               crystal_system,
               unit_cell,
               color,
               crystal_symmetry,
               cleavage,
               mohs_scale_hardness,
               luster,
               streak,
               diaphaneity,
               optical_properties,
               refractive_index,
               crystal_habit,
               specific_gravity,
               group):


        mineral = cls(
            name=name,
            image_filename=image_filename,
            image_caption=image_caption,
            category=category,
            formula=formula,
            strunz_classification=strunz_classification,
            crystal_system=crystal_system,
            unit_cell=unit_cell,
            color=color,
            crystal_symmetry=crystal_symmetry,
            cleavage=cleavage,
            mohs_scale_hardness=mohs_scale_hardness,
            luster=luster,
            streak=streak,
            diaphaneity=diaphaneity,
            optical_properties=optical_properties,
            refractive_index=refractive_index,
            crystal_habit=crystal_habit,
            specific_gravity=specific_gravity,
            group=group)


