# authentication/decorators.py
from django.http import HttpResponseForbidden
from functools import wraps
from django.shortcuts import redirect


def role_required(*allowed_roles):
    """
    Decorator to restrict access based on user role.
    Usage:
    @role_required('admin', 'gtu-coordinator')  # as arguments
    or
    @role_required(['admin', 'gtu-coordinator']) # as a list
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # Replace with your login URL name

            # Handle both list input and multiple arguments
            roles = allowed_roles[0] if len(allowed_roles) == 1 and isinstance(allowed_roles[0],
                                                                               (list, tuple)) else allowed_roles

            # Check if user has any of the allowed roles
            if not hasattr(request.user, 'role'):
                return HttpResponseForbidden("You don't have a role assigned.")

            if request.user.role.lower() in [role.lower() for role in roles]:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("You don't have permission to access this page.")

        return _wrapped_view

    return decorator