from .celery import app


@app.task
def banner_update():
    from home import serialize
    from home import models
    from django.conf import settings
    from django.core.cache import cache

    queryset_banner = models.Banner.objects.filter(is_delete=False,
                                                   is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]

    serialize_banner = serialize.BannerModelSerializer(instance=queryset_banner, many=True)

    for banner in serialize_banner.data:
        banner['img'] = 'http://127.0.0.1:8000' + banner['img']
    cache.set('banner_list', serialize_banner.data)
    return True

