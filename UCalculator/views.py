from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Material, Composite, Component
from .forms import (
    NewComponentForm, ClearForm, SaveForm,
    LoadForm, InsulatorForm, DeleteForm
)
from .constants import Rsi, Rse
from .functions.database_funcs import delete_composite
from .functions.calculator_funcs import (
    clear_material_view, add_component, save_composite,
    calculate_insulation_requirement, load_composite
)


@login_required
def calculator(request):
    user = request.user

    if request.method == 'POST':
        if 'add_component' in request.POST:
            add_component(request.POST, user)

    active_components = Component.objects.filter(user=user).filter(active=True)
    user_composites = Composite.objects.filter(user=user)
    active_composite = user_composites.filter(active=True).first()

    if active_components:
        R_values = [component.R_value() for component in active_components]
        R_total = Rsi + sum(R_values) + Rse
        U_value = round(1 / R_total, 2)
    else:
        U_value = 'N/A'

    insulation_requirement = None

    if request.method == 'POST':
        if 'clear_material_view' in request.POST:
            clear_material_view(active_components, active_composite)
            active_components = []
            active_composite = None

        elif 'save_composite' in request.POST:
            active_composite = save_composite(
                request.POST, user, active_components, active_composite)

        elif 'calculate_insulation_requirement' in request.POST:
            insulation_requirement = calculate_insulation_requirement(
                request.POST, R_total)

    if request.method == 'GET':
        if 'load_composite' in request.GET:
            active_components, active_composite = load_composite(
                request.GET, active_components,
                active_composite, user_composites)

    materials = Material.objects.all()

    component_form = NewComponentForm()
    clear_form = ClearForm()
    save_form = SaveForm()
    load_form = LoadForm()
    load_form.fields["composite"].queryset = user_composites
    insulator_form = InsulatorForm()

    context = {
        'materials': materials,
        'active_components': active_components,
        'active_composite': active_composite,
        'component_form': component_form,
        'clear_form': clear_form,
        'save_form': save_form,
        'load_form': load_form,
        'insulator_form': insulator_form,
        'U_value': U_value,
        'insulation_requirement': insulation_requirement
    }

    return render(request, 'calculator.html', context)


@ login_required
def database(request):
    user_composites = Composite.objects.filter(user=request.user)

    if request.method == "POST":
        if 'delete_composite' in request.POST:
            delete_composite(request.POST, user_composites)

    delete = DeleteForm()
    materials = Material.objects.all()

    context = {
        'materials': materials,
        'user_composites': user_composites,
        'delete': delete
    }

    return render(request, 'database.html', context)
