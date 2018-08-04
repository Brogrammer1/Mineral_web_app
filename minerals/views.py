from django.shortcuts import get_object_or_404, render

from . import models


# Create your views here.

def mineral_detail(request, pk):
    mineral = get_object_or_404(models.Mineral, pk=pk)
    mineral_attributes = {
        'category': mineral.category,
        'formula': mineral.formula,
        'strunz classification': mineral.strunz_classification,
        'crystal system': mineral.crystal_habit,
        'unit cell': mineral.unit_cell,
        'color': mineral.color,
        'crystal symmetry': mineral.crystal_symmetry,
        'cleavage': mineral.cleavage,
        'mohs scale_hardness': mineral.mohs_scale_hardness,
        'luster': mineral.luster,
        'streak': mineral.streak,
        'diaphaneity': mineral.diaphaneity,
        'optical properties': mineral.optical_properties,
        'refractive index': mineral.refractive_index,
        'crystal habit': mineral.crystal_habit,
        'specific gravity': mineral.specific_gravity,
        'group': mineral.group}
    return render(request, 'mineral_detail.html',
                  {'mineral': mineral,
                   'mineral_attributes': mineral_attributes})


def random_mineral(request):
    mineral = models.Mineral.objects.order_by('?').first()
    return mineral_detail(request, mineral.pk)
