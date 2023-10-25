from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

# Create your views here.
class ReservationInfoViewSet(viewsets.ModelViewSet):
    queryset = ReservationInfo.objects.all()
    serializer_class = ReservationInfoSerializer

reservationInfo_list = ReservationInfoViewSet.as_view({
    'get':'list',
    'post':'create',
})

reservationInfo_detail = ReservationInfoViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})

class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

parkingLot_list = ParkingLotViewSet.as_view({
    'get':'list',
    'post':'create',
})

parkingLot_detail = ParkingLotViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})

class ParkingZoneViewSet(viewsets.ModelViewSet):
    queryset = ParkingZone.objects.all()
    serializer_class = ParkingZoneSerializer

parkingZone_list = ParkingZoneViewSet.as_view({
    'get':'list',
    'post':'create',
})

parkingZone_detail = ParkingZoneViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})

class ReservationStateViewSet(viewsets.ModelViewSet):
    queryset = ReservationState.objects.all()
    serializer_class = ReservationStateSerializer

reservationState_list = ReservationStateViewSet.as_view({
    'get':'list',
    'post':'create',
})

reservationState_detail = ReservationStateViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})

class ParkingStateViewSet(viewsets.ModelViewSet):
    queryset = ParkingState.objects.all()
    serializer_class = ParkingStateSerializer

parkingState_list = ParkingStateViewSet.as_view({
    'get':'list',
    'post':'create',
})

parkingState_detail = ParkingStateViewSet.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})

@api_view(['POST'])
def get_parkingLot_list(request):
    try:
        data = list(ParkingLot.objects.all().values())
        result = {'resultData':data, 'count':len(data)}
        return JsonResponse(result, status=200)
    except KeyError as e:
        return JsonResponse(e, status=400)

@api_view(['POST'])
def get_parkableZone_list(request):
    try:
        data = list(ParkingZone.objects.filter(park_state=request.data['park_state']).values())
        result = {'resultData':data, 'count':len(data)}
        return JsonResponse(result, status=200)
    except KeyError:
        return JsonResponse("잘못된 접근입니다.", status=400)