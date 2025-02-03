from django.shortcuts import render
# from .models import MyAccount
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    myaccount, created = MyAccount.objects.get_or_create(user=request.user)
    return render(request, 'myaccount/profile.html', {'myaccount': myaccount})



