from .models import ViewersCount
from django.conf import settings

class ViewersCountMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR') 

        try:
            if "admin" == request.path.split('/')[1] or "media" == request.path.split('/')[1] or "ckeditor" == request.path.split('/')[1] or "favicon.ico" == request.path.split('/')[1]:
                pass
            else:
                request_list = request.path.split('/')[1:-1]
                if not settings.DEBUG and len(request_list) > 3:
                    viewer,created = ViewersCount.objects.get_or_create(path = request_list[3],ipaddress = ip_address)
                    if ip_address == counts.ipaddress:
                        viewer.views += 1
                        viewer.save()

        except Exception as e:
            pass

        response = self.get_response(request)
        return response
       
