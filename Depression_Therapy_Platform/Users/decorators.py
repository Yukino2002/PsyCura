from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_users=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            elif request.user.is_superuser:
                group = 'staff'

            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                if group == 'patient':
                    return redirect('Users:p_home')
                elif group == 'doctor':
                    return redirect('Users:d_home')
                elif group == 'sponsor':
                    return redirect('Users:s_home')
                else:
                    return redirect('Users:home')

        return wrapper_func
    return decorator

