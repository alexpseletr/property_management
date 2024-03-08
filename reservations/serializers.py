from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        extra_kwargs = {
            'reservation_id': {'read_only': True},
        }
        
    def validate(self, data):
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        if check_in_date and check_out_date:
            if check_in_date >= check_out_date:
                raise serializers.ValidationError("The check-in date must be before the check-out date.")
        
        return data