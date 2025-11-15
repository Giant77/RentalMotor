# from django.http import HttpResponse

def unified_image_path(instance, filename):
    app = instance._meta.app_label
    return f"{app}/{filename}"
