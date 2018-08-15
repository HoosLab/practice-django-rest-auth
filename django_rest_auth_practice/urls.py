from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from authapp import views
from authapp.views import FacebookLogin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]