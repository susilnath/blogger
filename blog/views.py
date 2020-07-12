from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from .models import User,Blogs
#from .forms import BlogForm


def index(request):
    blog = Blogs.objects.all()
    print("[+] Printing <blog> list")
    print(type(blog))
    print(blog[0])
    return render(request,"source1/index.html",{'post_list':blog})

def view_blog(request):
    blog = Blogs.objects.all()
    print("[+] Printing <blog> list")
    print(type(blog))
    print(blog[0])
    return render(request,"source1/view.html",{'post_list':blog})

def login(request):
    return HttpResponse("Please Login")

def delete_blog(request):
    print("[+] Delete Option Selected!")
    try:
        title=request.GET['title']
        if title:
            user=User.objects.get(id=1)
            blog=Blogs.objects.filter(blog_heading=title)

            blog_all=Blogs.objects.all()

            blog_head=blog[0].blog_heading

            print("[+] Found the Blog!")
            blog.delete()
            return HttpResponseRedirect('/blog/view')
        else:
            print("[+] Failed to Delete")
            return render(request,'source1/view.html',{'msg':"Failed to Delete",'post_list':blog_all})
        
    except:
        print("[+] Failed to Find the record")
        return render(request,'source1/view.html',{'msg':"Failed to Find the Record",'post_list':blog_all})

def submit_blog(request):
    print("[+] Submitted!")
    try:
        title=request.POST['title']
        blog=request.POST['blog']
        print("[+]...Title:"+title)
        print("[+]...Blog:"+blog)
        if title and blog:
            user=User.objects.get(id=1)
            blog=Blogs(user=user,blog_heading=title,blog_text=blog)
            blog.save()

    except:
        print("[+] Failed!")
    #if request.method=='POST':
        # form=BlogForm(request.POST)
        # if form.is_valid():
    return HttpResponseRedirect('/blog/')
    #else:
        # form=BlogForm()

def create_blog(request):
    return render(request,'source1/edit.html',{'mode':'create'})

def edit_blog(request):
    print("[+] Editing the Record!")
    try:
        title=request.GET['title']
        if title:
            user=User.objects.get(id=1)
            blog=Blogs.objects.filter(blog_heading=title)
            blog_all=Blogs.objects.all()

            blog_head=blog[0].blog_heading
            blog_body=blog[0].blog_text
            
            blog.delete()
            
            print("[+] Found the Blog!")
            return render(request,'source1/edit.html',{'title':blog_head,'blog_txt':blog_body})
        else:
            print("[+] Failed to Edit")
            return render(request,'source1/view.html',{'msg':"Failed to Edit",'post_list':blog_all})
        
    except:
        print("[+] Failed to Find the record")
        return render(request,'source1/view.html',{'msg':"Failed to Find the Record",'post_list':blog_all})