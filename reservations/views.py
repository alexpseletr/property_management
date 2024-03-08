from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Reservation
from rest_framework import status
from rest_framework.response import Response
from .serializers import ReservationSerializer

class ReservationListCreate(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'reservation_id'

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
