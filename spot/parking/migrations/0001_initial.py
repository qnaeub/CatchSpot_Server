# Generated by Django 4.2.6 on 2023-10-21 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('lot_key', models.AutoField(primary_key=True, serialize=False)),
                ('lot_name', models.CharField(max_length=30, verbose_name='주차장이름')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingZone',
            fields=[
                ('zone_key', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='주차구역번호')),
                ('park_state', models.CharField(default='Y', max_length=1, verbose_name='주차가능여부')),
                ('reserve_state', models.CharField(default='Y', max_length=1, verbose_name='예약가능여부')),
                ('pre_state', models.CharField(blank=True, max_length=1, null=True, verbose_name='사전예약구역여부')),
                ('lot_key', models.ForeignKey(db_column='lot_key', on_delete=django.db.models.deletion.CASCADE, to='parking.parkinglot', verbose_name='주차장번호')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationInfo',
            fields=[
                ('reservation_key', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, verbose_name='전화번호')),
                ('vehicle_number', models.CharField(max_length=8, verbose_name='차량번호')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='시작시간')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='종료시간')),
                ('lot_key', models.ForeignKey(db_column='lot_key', on_delete=django.db.models.deletion.CASCADE, to='parking.parkinglot', verbose_name='주차장번호')),
                ('zone_key', models.ForeignKey(db_column='zone_key', on_delete=django.db.models.deletion.CASCADE, to='parking.parkingzone', verbose_name='주차장번호')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_state', models.CharField(default='예약완료', max_length=4, verbose_name='진행상태')),
                ('reservation_key', models.ForeignKey(db_column='reservation_key', on_delete=django.db.models.deletion.CASCADE, to='parking.reservationinfo', verbose_name='예약번호')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField(blank=True, null=True, verbose_name='입차시각')),
                ('out_time', models.DateTimeField(blank=True, null=True, verbose_name='출차시각')),
                ('reservation_key', models.ForeignKey(db_column='reservation_key', on_delete=django.db.models.deletion.CASCADE, to='parking.reservationinfo', verbose_name='예약번호')),
            ],
        ),
    ]