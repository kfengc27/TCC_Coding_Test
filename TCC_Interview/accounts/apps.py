from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

def UserRegistration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            # if user that is registering is a doctor, token is their own email. otherwise their token is their doctor's email and
            # their relation is their doctor
            if data.__getitem__('user_type') == '1':
                data.__setitem__('token', data.__getitem__('email'))
            else:
                doctor = PHRUser.objects.get(email=data.__getitem__('token'))
                data.__setitem__('phr_relate', staker.id)
                data.__setitem__('token', '')
            new_user = form.save(data)
        return HttpResponseRedirect('/')