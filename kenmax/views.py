from django.shortcuts import render

def maintenance(request):
    return render(request, 'kenmax/maintenance.html', {
        'email': 'kiptookennedymail@gmail.com',
        'phone': '0799382984',
    })