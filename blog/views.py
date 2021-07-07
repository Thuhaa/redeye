import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Feedback
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

def homepage(request):
	featured = Article.objects.filter(featured=True)
	potland = Article.objects.filter(category='Potland')
	music = Article.objects.filter(category='Music')
	lifestyle = Article.objects.filter(category='Lifestyle')

	context = {
	'featured':featured,
	}
	return render(request, 'blog/home.html', context)

def blog(request):
	articles = Article.objects.all
	context = {'articles':articles}
	return render(request, 'blog/blog.html', context)

def post_detail(request, slug):
	post = get_object_or_404(Article, slug=slug)
	ordered_posts = Article.objects.order_by('-date')
	latest_post = ordered_posts.first()
	print(type(ordered_posts))
	return render(request, 'blog/detail.html',{'post':post, 'latest_post':latest_post})

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	return render(request, 'blog/contact.html')

def potland(request):
	articles = Article.objects.filter(category='Bud Solutionz')
	return render(request, 'blog/budsolutionz.html', {'articles':articles})

def music(request):
	articles = Article.objects.filter(category='Music')
	return render(request, 'blog/music.html', {'articles':articles})

def lifestyle(request):
	articles = Article.objects.filter(category='Lifestyle')
	return render(request, 'blog/lifestyle.html', {'articles':articles})

def feedback(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		date = datetime.datetime.now().strftime('%b %e %Y')
		Feedback.objects.create(name=name,email=email, subject=subject, message=message, date=date)
		try:
			send_mail(subject, message, 'josephthuha@gmail.com', ['josephthuha@gmail.com'])
			messages.success(request, 'Message sent successfully')
		except BadHeaderError:
			messages.error(request, 'There was an error sending your message')
			return HttpResponse('Invalid header found.')
		return redirect ("contact")
	else:
		messages.error(request, 'There was an error sending your message')
		return redirect('contact')
# Create your views here.
