from django.shortcuts import render
from .models import Reservation
from django.views import View
from .models import Reservation
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def reserve(request):
    reservations = Reservation.objects.all()
    return render(request, 'reserve.html',{'reservations': reservations})

class ReserveView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        status = request.POST.get('status')
        time = request.POST.get('time')

        try:
            reservation = Reservation.objects.get(time=time)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'Time does not match',
                                 'data': {}}, status=404)
        
        reservation.name = name
        reservation.status = status

        reservation.save()
        return JsonResponse({'status': 'success',
                             'message': 'Updated',
                             'data': reservation}, status=201)
        
def update(request):
    print('asdf')
    return ''