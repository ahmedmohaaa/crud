from django.shortcuts import render, get_object_or_404, redirect
from .models import Crud
from .forms import ProductForm

def manage(request, pk=None):
    crud_instance = None
    if pk:
        crud_instance = get_object_or_404(Crud, pk=pk)
        form = ProductForm(instance=crud_instance)
    else:
        form = ProductForm()

    if request.method == 'POST':
        if 'delete_all' in request.POST:
            Crud.objects.all().delete()
            return redirect('manage')

        elif 'delete' in request.POST:
            item_id = request.POST.get('delete')
            Crud.objects.filter(pk=item_id).delete()
            return redirect('manage')

        elif 'save' in request.POST:
            if crud_instance:
                form = ProductForm(request.POST, instance=crud_instance)
            else:
                form = ProductForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('manage')

    # البحث
    query = request.GET.get('query')
    cruds = Crud.objects.all()
    if query:
        if 'search_title' in request.GET:
            cruds = cruds.filter(title__icontains=query)
        elif 'search_category' in request.GET:
            cruds = cruds.filter(category__icontains=query)

    return render(request, 'manage.html', {
        'form': form,
        'cruds': cruds,
        'edit_id': pk,
    })
