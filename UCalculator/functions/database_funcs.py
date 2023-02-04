from ..forms import DeleteForm


def delete_composite(post, composites):
    form = DeleteForm(post)
    if form.is_valid():
        pk = post['to_delete']
        if composites.filter(pk=pk):
            composites.get(pk=pk).delete()
