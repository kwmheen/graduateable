from django.shortcuts import render
from .models import Reservation
from django.views import View
from .models import Reservation
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def reserve(request):
    reservations = Reservation.objects.all()
    return render(request, 'reserve.html',{'reservations': reservations})

@method_decorator(csrf_exempt, name='dispatch')
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