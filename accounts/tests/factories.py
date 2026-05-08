from accounts.models import User, get_or_create_profile


def create_user_with_profile(**kwargs):
    profile_keys = {
        "institution",
        "country",
        "position",
        "is_author",
        "is_reviewer",
        "is_chair",
        "consent_privacy",
        "consent_image",
    }
    profile_data = {
        key: kwargs.pop(key)
        for key in list(kwargs)
        if key in profile_keys
    }
    password = kwargs.pop("password", None)
    user = User.objects.create_user(password=password, **kwargs)
    if profile_data:
        profile = get_or_create_profile(user)
        for key, value in profile_data.items():
            setattr(profile, key, value)
        profile.save()
    return user
