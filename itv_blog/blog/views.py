from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    # Your login logic here
    return HttpResponse("Login Page")

def registration_view(request):
    # Your registration logic here
    return HttpResponse("Registration Page")

def post_list_view(request):
    # Your post list logic here
    return HttpResponse("Post List Page")

def post_detail_view(request, post_id):
    # Your post detail logic here
    return HttpResponse(f"Post Detail Page - Post ID: {post_id}")

def login_view(request):
    # Your login logic here
    return render(request, 'login.html')

def registration_view(request):
    # Your registration logic here
    return render(request, 'registration.html')

def post_list_view(request):
    # Your post list logic here
    return render(request, 'post_list.html')

def post_detail_view(request, post_id):
    # Your post detail logic here
    # Assuming you pass a post object to the template
    post = {'id': post_id, 'title': 'Sample Post', 'content': 'Sample Content'}
    return render(request, 'post_detail.html', {'post': post})
