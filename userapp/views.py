from django.contrib import messages, auth
from django.contrib.auth.models import User

from .forms import MovieForm,UserProfileForm
from django.shortcuts import render,redirect

from userapp.models import Movie,Category,Review
from django.db.models import Q


def search_by_category(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(category__name__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'search.html', {'query': query, 'movies': movies})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if username == 'taskadmin' and password == 'taskadmin':
                # Redirect to admin page
                return redirect('/admin')
            else:
                auth.login(request, user)
                # messages.info(request, "Welcome")
                return redirect('/user_movies')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")











def detail(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'result':obj})

def index(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'result':obj})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']

        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        # confirmpassword=request.POST['cpassword']
        if password==password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, last_name=lastname,
                                                email=email,
                                                first_name=firstname)
                user.save();
                messages.info(request,"You've successfully registered !!!")
                return redirect('/login')

        else:
            messages.info(request, "passwords not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def movie(request):
    obj = Movie.objects.all()
    return render(request,'movie.html',{'result':obj})


#
def view(request,movie_id):
    obj=Movie.objects.get(id=movie_id)
    return render(request,'view.html',{'result':obj})




def add(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        poster = request.FILES['poster']
        release_date = request.POST.get('release_date')
        description = request.POST.get('description')
        actors = request.POST.get('actors')
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        user=request.user

        trailer_link = request.POST.get('trailer_link')

        new= Movie(title=title, release_date=release_date, description=description, category=category,
                          actors=actors, trailer_link=trailer_link, poster=poster,user=user)
        new.save()
        return redirect('user_movies')

    return render(request, 'addmovie.html',{'categories':categories})





def review(request):
    ratings = Movie.objects.all()
    if request.method == 'POST':
        movie_id = int(request.POST.get('film'))
        movie = Movie.objects.get(pk=movie_id)

        user=request.user
        rating=request.POST.get('rating')
        comment=request.POST.get('review')

        reviews= Review(movie=movie, user=user, rating=rating,comment=comment)
        reviews.save()
        return redirect('/index')

    return render(request, 'review.html',{'ratings': ratings})

def category(request):
    if request.method=='POST':
        movie_cat=request.POST.get('category',)
        cat=Category(name=movie_cat)
        cat.save()
    return render(request,'category.html')

def user_movies(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movie.html', {'movies': movies})

def delete(request,id):

    if request.method=='POST':
        movie_delete=Movie.objects.get(id=id)
        movie_delete.delete()

        return redirect('user_movies')
    return render(request,'delete.html',)


def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user_movies')  # Redirect to the profile page
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit.html', {'form': form})




def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('user_movies')
    return render(request,'update.html',{'form':form,'movie':movie})
