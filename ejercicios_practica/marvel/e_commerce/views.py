# Create your views here.
from django.http import JsonResponse
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        queryset = Comic.objects.all()
        data = list(queryset.values('description', 'id', 'marvel_id', 'picture', 'price', 'stock_qty', 'title', 'wishlist'))
        
        print("Endpoint: comic_list_api_view")
        
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)



def comic_filter_stock_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea

        queryset = Comic.objects.filter(stock_qty=5)

        data = list(queryset.values('description', 'id', 'marvel_id', 'picture', 'price', 'stock_qty', 'title', 'wishlist'))

        print("Endpoint: comic_filter_stock_api_view")

        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_price_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea

        queryset = Comic.objects.filter(price__gt=3)

        data = list(queryset.values('description', 'id', 'marvel_id', 'picture', 'price', 'stock_qty', 'title', 'wishlist'))

        print("Endpoint: comic_filter_price_api_view")

        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_list_order_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea

        queryset = Comic.objects.order_by('marvel_id')

        data = list(queryset.values('description', 'id', 'marvel_id', 'picture', 'price', 'stock_qty', 'title', 'wishlist'))

        print("Endpoint: comic_list_order_api_view")
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)
