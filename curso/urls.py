import posts.views
import account.views
import login.views
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.post_list, name='post_list'),
    path('create/', login.views.create, name='create'),
    path('account/', account.views.account, name='account'),
    path('login/', login.views.user_login, name='user_login'),
    path('edit_info/', account.views.edit_info, name='edit_info'),
    path('logout/', login.views.user_logout, name='user_logout'),
    path('post/<int:pk>/edit/', posts.views.post_edit, name='post_edit'),
    path('editpassword/', account.views.edit_password, name='edit_password'),
    path('post/<int:pk>/delete/', posts.views.post_delete, name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
