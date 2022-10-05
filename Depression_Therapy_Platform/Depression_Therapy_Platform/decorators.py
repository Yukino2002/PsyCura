from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            group = request.user.groups.all()[0].name
            if group == 'patient':
                return redirect('Users:p_home')
            elif group == 'doctor':
                return redirect('Users:d_home')
            elif group == 'sponsor':
                return redirect('Users:s_home')
            else:
                return redirect('Users:home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func