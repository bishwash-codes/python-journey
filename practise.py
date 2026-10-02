distance_mi = 5
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = False


if distance_mi:
    if distance_mi <= 1 and not is_raining:
        print("True")
    elif 6 >= distance_mi > 1 and has_bike:
        print("True")
    elif (distance_mi > 6 and has_ride_share_app) or (distance_mi > 6 and has_car):
        print("True")
    else:
        print("False")
else:
    print("False")
