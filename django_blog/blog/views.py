from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserCreationForm ,CustomUserChangeForm,PasswordChangeForm, PostForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import generic
from .models import Post
from django.shortcuts import get_object_or_404

class ListView(generic.ListView):
    pass

class DetailView(generic.DetailView):
   
    def get(self,request,pk):
        user = self.request.user
       
        qs = Post.objects.filter(author=user)
        return render(request,'detail.html',{'qs':qs})

class CreateView(generic.CreateView):

    def get(self,request):
        form = PostForm()
        return render(request,'create.html',{'form':form})
    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
        return render(request,'create.html',{'form':form})


class UpdateView(generic.UpdateView):
   
    def get(self, request, pk):
   
        blog_post = get_object_or_404(Post, pk=pk)  
        form = PostForm(instance=blog_post)  
        return render(request, 'update.html', {'form': form})
    
    def post(self, request, pk):
      
        blog_post = get_object_or_404(Post, pk=pk)  
        form = PostForm(request.POST, instance=blog_post)  
        if form.is_valid():
            form.save()
            return redirect('home') 
        return render(request, 'update.html', {'form': form})


class DeleteView(generic.DeleteView):

    model = Post
    template_name = 'post_confirm_delete.html'


class ProfileView(LoginRequiredMixin,TemplateView):

        template_name= 'profile.html'

class ChangeView(View):
    
    def get(self,request):
        if request.method == 'GET':
            pass
        form = CustomUserChangeForm(instance=request.user)
        return render(request,'change.html',{'form':form})

    def post(self,request):
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request,'change.html',{'form':form})

class ChangePassword(View):
    def get(self,request):
        form = PasswordChangeForm(user=request.user)
        return render(request,'change_pass.html',{'form':form})

    def post(self,request):
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.warning(request,"Sorry the Password is weak try again!")
            return render(request,'change_pass.html',{'form':form})

class HomeView(View):

    def get(self,request):
        user = self.request.user
        return render(request,'home.html',{'user':user})

class RegisterView(View):

    def get(self,request):
        form = CustomUserCreationForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        return render(request,'register.html',{'form':form})
    
def logout_view(request):
    logout(request)
    return render(request,'logout.html')