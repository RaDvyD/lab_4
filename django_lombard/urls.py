from django.contrib import admin
from django.urls import path, include
from pawnshop_app import views  # Import views from pawnshop_app
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pawnshop/', include('pawnshop_app.urls')),  # This points to the HTML template views
    path('api/', include('pawnshop_app.api_urls')),  # This points to the API views for DRF
    path('', views.home, name='home'),  # Homepage
]

handler404 = 'pawnshop_app.views.custom_page_not_found_view'
handler500 = 'pawnshop_app.views.custom_error_view'