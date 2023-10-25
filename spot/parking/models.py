from django.db import models

# Create your models here.

# 예약정보
class ReservationInfo(models.Model):
    reservation_key = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, verbose_name='전화번호')
    vehicle_number = models.CharField(max_length=8, verbose_name='차량번호')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='시작시간')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='종료시간')
    zone_key = models.ForeignKey('ParkingZone', on_delete=models.CASCADE, db_column='zone_key', verbose_name='주차장번호')
    lot_key = models.ForeignKey('ParkingLot', on_delete=models.CASCADE, db_column='lot_key', verbose_name='주차장번호')

# 주차장
class ParkingLot(models.Model):
    lot_key = models.AutoField(primary_key=True)
    lot_name = models.CharField(max_length=30, verbose_name='주차장이름')

# 주차구역
class ParkingZone(models.Model):
    zone_key = models.CharField(max_length=15, primary_key=True, verbose_name='주차구역번호')
    lot_key = models.ForeignKey('ParkingLot', on_delete=models.CASCADE, db_column='lot_key', verbose_name='주차장번호')
    park_state = models.CharField(max_length=1, default='Y', verbose_name='주차가능여부')
    reserve_state = models.CharField(max_length=1, default='Y', verbose_name='예약가능여부')
    pre_state = models.CharField(max_length=1, null=True, blank=True, verbose_name='사전예약구역여부')

# 예약현황
class ReservationState(models.Model):
    reservation_key = models.ForeignKey('ReservationInfo', on_delete=models.CASCADE, db_column='reservation_key', verbose_name='예약번호')
    process_state = models.CharField(max_length=4, default='예약완료', verbose_name='진행상태')

# 주차현황
class ParkingState(models.Model):
    reservation_key = models.ForeignKey('ReservationInfo', on_delete=models.CASCADE, db_column='reservation_key', verbose_name='예약번호')
    in_time = models.DateTimeField(null=True, blank=True, verbose_name='입차시각')
    out_time = models.DateTimeField(null=True, blank=True, verbose_name='출차시각')