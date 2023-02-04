from ..forms import NewComponentForm, SaveForm, LoadForm, InsulatorForm
from ..constants import mean_K_inulation


def deactivate_instance(instance):
    instance.active = False
    instance.save()


def create_instance(user, form):
    instance = form.save(commit=False)
    instance.user = user
    instance.save()
    return instance


def add_component(post, user):
    form = NewComponentForm(post)
    if form.is_valid():
        create_instance(user, form)


def clear_material_view(components, composite):
    if composite:
        components.update(composite=composite)
        components.update(active=False)
        deactivate_instance(composite)
    else:
        components.delete()


def save_composite(post, user, components, active_composite):
    form = SaveForm(post)
    if form.is_valid():
        if active_composite:
            mock_instance = form.save(commit=False)
            active_composite.name = mock_instance.name
            active_composite.save()
        else:
            active_composite = create_instance(user, form)
        components.update(composite=active_composite)

    return active_composite


def calculate_insulation_requirement(post, R_total):
    form = InsulatorForm(post)
    if form.is_valid():
        target_U_value = float(post['target_U_value'])
        return round(mean_K_inulation * (1 / target_U_value - R_total) * 1000)


def load_composite(get, active_components, active_composite, composites):
    form = LoadForm(get)
    if form.is_valid():
        load_pk = get['composite']
        if load_pk.isdigit():
            clear_material_view(active_components, active_composite)
            composite = composites.get(pk=load_pk)
            composite.active = True
            composite.save()
            for component in composite.component_set.all():
                component.active = True
                component.save()
        active_composite = composite
        active_components = active_composite.component_set.all()

    return active_components, active_composite
