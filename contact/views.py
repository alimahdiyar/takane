from django.shortcuts import render,HttpResponse,redirect
from django.forms.models import modelform_factory,modelformset_factory
from .models import contact
from .forms import contactform

def Contact(request):
    template='Contact/contact.html'
    if request.method=="POST":
        form=contactform(request.POST,request.FILES)
        form.save()
        return redirect('home')
    else:
        form=contactform()
    context={
        'form':form
    }
    return render(request,template,context)
# Create your views here.
