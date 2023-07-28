from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

USER = get_user_model()


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        messages.success(self.request, "Sign in Successfully")
        return HttpResponseRedirect(self.get_success_url())


class CustomLogoutView(LogoutView):
    method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = self.get_success_url()
        messages.success(self.request, "Sign out Successfully")
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)
