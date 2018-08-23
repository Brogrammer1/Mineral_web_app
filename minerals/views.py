from django.shortcuts import get_object_or_404, render
from django.db.models import Q, Count
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


def search(request):
    term = request.GET.get('q')
    minerals = models.Mineral.objects.filter(Q(name__icontains=term))
    return render(request, 'index.html', {'minerals': minerals})


def search_group(request, group):
    if group == 'OrganicMinerals':
        group = 'Organic Minerals'
    elif group == 'NativeElements':
        group = 'Native Elements'

    minerals = models.Mineral.objects.filter(Q(group=group))
    return render(request, 'index.html', {'minerals': minerals})


def search_letter(request, letter='a'):
    minerals = models.Mineral.objects.filter(Q(name__istartswith=letter))
    return render(request, 'index.html', {'minerals': minerals})
