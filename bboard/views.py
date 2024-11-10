from django.shortcuts import render


from .models import BBoard as bb
from .models import Category as cat
# Create your views here.

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm

def index(request):
    bbs = bb.objects.all()
    categories = cat.objects.all()
    return render(request, 'bboard/index.html', { 'bbs' : bbs, 'categories' : categories })


def cats(request, cat_id):
    categories = cat.objects.all()
    current_cat = cat.objects.get(pk = cat_id)
    bbs = bb.objects.filter(category = cat_id)
    return render(request, 'bboard/cats.html', { 'categories' : categories, 'current_cat' : current_cat, 'bbs' : bbs })

class BbCreateView(CreateView):

    template_name = 'bboard/create_form.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = cat.objects.all
        return context