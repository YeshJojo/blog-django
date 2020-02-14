from django.urls import path
from django.conf.urls import url
from . import views as core_views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),

    url(r'^post/entry/$', core_views.AddPostView, name='write-post'),
    url(r'^politics/$', views.PoliticsListView.as_view(), name='politics'),
    url(r'^technology/$', views.TechnologyListView.as_view(), name='technology'),
    url(r'^lifestyle/$', views.LifeStyleListView.as_view(), name='lifestyle'),
    url(r'^profile/$', views.PostListProfileView.as_view(), name='profile'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='delete-post'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='update-post'),

]
