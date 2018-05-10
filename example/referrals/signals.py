import django.dispatch


create_flat_referral = django.dispatch.Signal(
    providing_args=["request", "user"])
create_multi_level_referral = django.dispatch.Signal(
    providing_args=["request", "user", "position"])
