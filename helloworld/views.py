# helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PasswordForm


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)



#Get password request
class passWord(TemplateView):
    def get_password(request):
        def get(self, request, **kwargs):
            return render(request, 'hasher.html', context=None)
        ## if this is a POST request we need to process the form data
        ##def get(self, request, **kwargs):
        ##    if request.method == 'POST':
        ##        # create a form instance and populate it with data from the request:
        ##        form = PasswordForm(request.POST)
        ##        # check whether it's valid:
        ##        if form.is_valid():
        ##            # process the data in form.cleaned_data as required
        ##            # ...
        ##            # redirect to a new URL:
        ##            return HttpResponseRedirect('/Hasher.html')
        ##
        ##    # if a GET (or any other method) we'll create a blank form
        ##    else:
        ##        form = PasswordForm()
        ##
        ##    return render(request, 'Hasher.html', context=None)

