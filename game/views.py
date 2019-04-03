from django.shortcuts import render
from .models import Click
from django.shortcuts import redirect

def home_page(request, id):

    obj = Click.objects.get(id=id)

    return render(request, 'game/hello.html', {'data': obj})


def update_clicks(request, id):

    obj = Click.objects.get(id=id)
    obj.click_count += 1
    obj.save()


    return redirect('/{}'.format(id))
