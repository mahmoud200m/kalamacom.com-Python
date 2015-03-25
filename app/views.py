"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from app.models import Twitte
from django.utils import timezone

def index(request):
    """Renders the home page."""
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
    if 'error' in request.session:
        message = request.session['error']
        del request.session['error']

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'message': message if 'message' in locals() else "",
            'error': message if 'error' in locals() else "",
        })
    )

#@login_required
def home(request):
    from twython import Twython
    global twitter
    twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")

    return render(
        request,
        'app/home.html',
        context_instance = RequestContext(request,
        {
            'title':'Home',
            #'twittes': twittes,
        })
    )

#@login_required
@ajax
def get_twittes(request):
    twittes = twitter.search(q=request.POST['query'], result_type='recent')
    for twitte in twittes['statuses']:
        try:
            item = Twitte()
            item.twitter_id = twitte['id']
            item.user_id = twitte['user']['id']
            item.text = twitte['text']
            item.created_at = twitte['created_at']
            item.user_followers_count = twitte['user']['followers_count']
            item.user_profile_image_url = twitte['user']['profile_image_url']
            item.pub_date = timezone.now()
            item.save()
        except: 
          pass

    return twittes

@login_required
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

@login_required
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def login_user(request):

    if request.method == 'POST':
        #logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/about')
                #return HttpResponseRedirect('/about/')
    return redirect('/')

def register(request):
    
    if request.method == 'POST':
        from app.forms import UserForm
        user_form = UserForm(data=request.POST)

        if user_form.is_valid() :
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            request.session['message'] = 'registration done please login'
            return redirect("/")
            #return render(request, 'app/site_layout.html', {'message':'registration done please login'})
        else:
            request.session['error'] = user_form.errors
            return redirect("/")
           #return render(request, 'app/site_layout.html', {'error':user_form.errors})

