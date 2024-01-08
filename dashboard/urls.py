from django.urls import path
from .views import (
    IndexView,    ActivateUser, DeactivateUser, UsersView, PostsView, PostDetailView,
    AddPostVideo, UpdatePostView, PostDeleteView, AddPostImage,  site_view,  NewPost, NewPress, UpdatePress, DeletePress, AboutEntry, UpdateAbout, DeleteAbout, WorkEntry, UpdateWork, DeleteWork, TeachingEntry, DeleteTeaching, UpdateTeaching
  
)


app_name = 'dashboard'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('activate/<int:pk>', ActivateUser.as_view(), name='activate_user'),
    path('deactivate/<int:pk>', DeactivateUser.as_view(), name='deactivate_user'),
    path('users', UsersView.as_view(), name='users'),
    path('posts', PostsView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add/video/<int:pk>', AddPostVideo.as_view(), name='add_video'),
    path('add/image/<int:pk>', AddPostImage.as_view(), name='add_image'),
    path('delete/post/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update_post'),   
    path('site/view', site_view, name='site_view'),
    path('new/post', NewPost.as_view(), name='new_post'),
    path('new/press', NewPress.as_view(), name='new_press'),
    path('update/press/<int:pk>', UpdatePress.as_view(), name='update_press'),
    path('delete/press/<int:pk>', DeletePress.as_view(), name='delete_press'),
    path('about/entry', AboutEntry.as_view(), name='about_entry'),
    path('update/about/<int:pk>', UpdateAbout.as_view(), name='update_about'),
    path('delete/about/<int:pk>', DeleteAbout.as_view(), name='delete_about'),
    path('work/entry', WorkEntry.as_view(), name='work_entry'),
    path('update/work/<int:pk>', UpdateWork.as_view(),  name='update_work'),
    path('delete/work/<int:pk>', DeleteWork.as_view(), name='delete_work'),
    path('teaching/entry', TeachingEntry.as_view(), name='teaching_entry'),
    path('update/teaching/<int:pk>', UpdateTeaching.as_view(), name='update_teaching'),
    path('delete/teaching/<int:pk>', DeleteTeaching.as_view(), name='delete_teaching'),
    

]

