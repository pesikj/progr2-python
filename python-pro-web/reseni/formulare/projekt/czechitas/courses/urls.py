from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("about", views.AboutView.as_view(), name="about"),
    path('kurzy/', views.CourseListView.as_view(), name='course_list'),
    path('pobocky/', views.BranchListView.as_view(), name='branch_list'),
    path('tym/', views.PersonListView.as_view(), name='branch_list'),
    # Verze z první poloviny
    #path('prihlaska/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('prihlaska/<int:pk>/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('prihlaska/potvrzeni/', views.ApplicationConfirmation.as_view(), name='application_confirmation'),
    path('prihlaska-clena-tymu/', views.PersonRegisterView.as_view(), name='person_register'),
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('pobocka/<int:pk>', views.BranchDetailView.as_view(), name='course_detail'),
]
