try:
    from django.conf.urls import patterns
except ImportError: # django < 1.4
    from django.conf.urls.defaults import patterns

urlpatterns = patterns('paypal.standard.pdt.views',
    (r'^pdt/$', 'pdt'),
)
