from django.views.generic import FormView, DetailView, View
from django.http import HttpResponseRedirect, Http404
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from core.forms import URLForm
from core.models import URL


class HomeView(FormView):

   form_class = URLForm
   template_name = "index.html"
   success_url = '/url/%d'

   def form_valid(self, form):
      if form.is_valid():
         result = form.save()
      return HttpResponseRedirect(self.get_success_url() % result.pk)


class URLDetailView(DetailView):
    context_object_name = "url"
    model = URL

    def get_context_data(self, **kwargs):
        ctx = super(URLDetailView, self).get_context_data(**kwargs)
        ctx['site'] = Site.objects.get_current()
        return ctx


class URLDetailByNameView(View):
    def get(self, request, *args, **kwargs):
        try:
            url = URL.objects.get(slug=kwargs['slug'])
        except URL.DoesNotExist:
            raise Http404
        return redirect(reverse('url-details', args=[url.pk]))  


class URLRedirectURLView(View):
    def get(self, request, *args, **kwargs):
        try:
            url = URL.objects.get(slug=kwargs['slug'])
        except URL.DoesNotExist:
            raise Http404
        return redirect(url.url)

