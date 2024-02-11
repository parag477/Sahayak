from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UploadAudio

urlpatterns = [
    path('', views.index, name='index'),
    # path('genrate/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('doctor/', views.doctor, name='doctor'),
    path('safe/', views.safe, name='safe'),
    path('unsafe/', views.unsafe, name='unsafe'),
    path('login1/', views.login1, name='login1'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('create_meeting/', views.create_meeting, name='create_meeting'),
    path('upload_audio/', UploadAudio.as_view(), name='upload_audio'),
path('upload/', views.upload_image, name='upload_image'),
path('upload-voice/', views.upload_voice, name='upload_voice'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('l4/', views.l4, name='l4'),
    path('breast_cancer/', views.breast_cancer, name='breast_cancer'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
