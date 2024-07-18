from functools import wraps
from django.http import HttpResponseForbidden


def role_required(required_roles):
    if not isinstance(required_roles, (list, tuple)):
        required_roles = [required_roles]

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You do not have permission to access this page.")
            if request.user.role not in required_roles:
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
