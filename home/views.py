from django.views.generic import TemplateView
from django.shortcuts import render,redirect,reverse,get_object_or_404
from home.forms import HomeForm,CommentForm
from home.models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



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


def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'home/comments.html', {'form': form,'post':post})
