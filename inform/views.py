import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from inform.dialog_flow import get_answer


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'content': '안녕하세요 힐링타임 추천 서비스 입니다. 무엇을 도와드릴까요?'
    })


@csrf_exempt
def message(request):
    message = (request.body.decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    answer = get_answer(return_str)
    return JsonResponse({
        'message': {
            'text': answer,
        },

        'keyboard': {
            'type': 'text',
        }
    })


