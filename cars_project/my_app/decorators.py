from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base') 
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func