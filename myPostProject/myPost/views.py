from django.shortcuts import render,get_object_or_404, redirect
from .models import userPost,userProfile
from django.contrib import messages
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as lgi
from django.contrib.auth import logout as lgo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def ownUserProfile(request):
    user = request.user
    profile_pic = get_object_or_404(userProfile, user=user)
    user_posts = userPost.objects.filter(user=user)
    context = {
        "UserProfilePic": profile_pic.user_pic,
        "UserData": user,
        "PostsUserData": user_posts,
    }

    return render(request, "myPost/ownUserProfile.html", context)


@login_required
def publishPost(request):
    user = request.user
    if request.method =='POST':
        post_description = request.POST['description']
        post_pic   = request.FILES.get('post_image')

        new_post = userPost.objects.create(user= user, post_pic = post_pic, content = post_description)
        return redirect('ownUserProfile')
    else:
        return render(request, 'myPost/publishPost.html')
    
@login_required
def deletePost(request, p_pid):
    userPost.objects.filter(id=p_pid).delete()
    return redirect('ownUserProfile')
        
        
def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth(request, username=username, password=password)
        if user is None:
            return render(request, 'myPost/userLogin.html',{'error': 'Invalid username or password'})
        else:
            lgi(request,user)
            return redirect('mainView')
    else:
        return render(request, 'myPost/userLogin.html')

def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        profile_pic = request.FILES.get('profile_picture')

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, 'myPost/userRegister.html', {'error': 'Username already exists'})

        
        user_created = User.objects.create_user(username=username, password=password)

        
        userProfile.objects.create(user=user_created, user_pic=profile_pic)

       
        user_created.save()

      
        return redirect('loginUser')
    

    return render(request, 'myPost/userRegister.html')


def mainView(request):
    posts = userPost.objects.all()
    users_profile = userProfile.objects.all()

    if request.user.is_authenticated:
        user = request.user
        context = {
            "OwnUserData": user,
            "PostsData": posts,
            "UsersData" : users_profile,
        }
        return render(request, "myPost/mainView.html",context)
    else:
        context = {
            "PostsData": posts,
            "UsersData" : users_profile,
        } 
        return render(request, "myPost/mainView.html",context)


def requestedUserProfile(request,p_username):
    if p_username == request.user.username:
       return redirect('ownUserProfile')
    
    users = get_object_or_404(User, username=p_username)
    posts = userPost.objects.filter(user=users)
    user_pic = get_object_or_404(userProfile, user=users)
    context = {
        "UserPosts": posts,
        "UserPfp": user_pic,
        "Username": users,
    }
    return render(request, 'myPost/requestedUserProfile.html',context)


@login_required
def logOut(request):
    lgo(request)
    return redirect('mainView')



@login_required
def userSettings(request):
    try:
        user_profile = userProfile.objects.get(user=request.user)
    except userProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        username = request.POST['username']
        user_bio = request.POST['userBio']
        profile_pic = request.FILES.get('profile_pic')  # Use FILES to get the uploaded file

        if User.objects.filter(username=username).exists() and username != request.user.username:
            return render(request, 'myPost/userSettings.html', {'error': 'Username already exists', 'UserProfile': user_profile})
        else:
            user = request.user
            user.username = username
            user.save()
            
            user_profile.user_bio = user_bio
            if profile_pic:
                user_profile.user_pic = profile_pic
            user_profile.save()
            
            return redirect('ownUserProfile')
    else:
        context = {
            "UserProfile": user_profile,
        }
        return render(request, 'myPost/userSettings.html', context)