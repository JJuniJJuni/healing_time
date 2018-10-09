from django.http import JsonResponse


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1.healing time', '2.developers'],
    })
