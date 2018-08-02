
from django.views.generic import TemplateView
from django.shortcuts import render,redirect,reverse
from home.forms import HomeForm
from home.models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



from django.shortcuts import render,redirect
from home.forms import HomeForm
from home.models import Post

class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form = HomeForm()
        posts=Post.objects.all()
        args={'form':form,'posts':posts}
        return render(request,self.template_name,args)

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text=form.cleaned_data['text']
            form = HomeForm()
            return redirect('/home/view/')

        args={'form':form}
        return render(request,self.template_name,args)

def view_post(request):
    view = Post.objects.all()
    return render(request,'home/viewhome.html',{'view':view})


class EditPost(UpdateView):
    model = Post
    form_class = HomeForm
    template_name = 'home/edithome.html'
    def get_success_url(self, *args, **kwargs):
        return reverse("view_post")

class DetailPost(DetailView):
    model = Post
    template_name = 'home/pv.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'home/deletepost.html'
    def get_success_url(self, *args, **kwargs):
        return reverse("view_post")
