from django.shortcuts import render
from django.http import Http404
from copy import deepcopy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def calculator_view(request, recipe_name):
    if recipe_name not in DATA:
        raise Http404(f'recipe {recipe_name} not found')

    persons_count = int(request.GET.get('servings', 1))
    recipe = {'name': recipe_name, 'composition': deepcopy(DATA[recipe_name])}

    for ingredient in recipe['composition']:
        recipe['composition'][ingredient] *= persons_count

    return render(request, "calculator/index.html", context={'recipe': recipe})
