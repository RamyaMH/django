from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),
    # path('all/', views.employeelist),
    path('all/', views.EmployeeAPIView.as_view()),
    # path('all/', views.GenericEmployeeAPIView.as_view()),
    # path('add/', views.employee_add),
    path('add/', views.GenericEmployeeAddAPIView.as_view()),
    # path('detail/<int:pkid>/', views.employee_detail)
    # path('detail/<int:id>/', views.EmployeeDetail.as_view())
    path('detail/<int:id>/', views.GenericEmployeeDetail.as_view()),
    path('user/', views.UserView.as_view()),


    path('article/create', views.GenericArticleCreate.as_view()),
    # path('article/<int:id>', views.ArticleModify.as_view()),
    # path('article/list', views.ArticleList.as_view()),
    # path('articles/review/list', views.ArticlesByReviewer.as_view()),
    # path('articles/author/list', views.ArticlesByAuthor.as_view()),
    path('conference/create', views.ConferenceCreate.as_view()),
    # path('conference/<int:id>', views.ConferenceModify.as_view()),
    # path('conference/list', views.ConferenceList.as_view()),
    # path('reviewers/all', views.ReviewersList.as_view()),
    # path('cps/all', views.CpsList.as_view())

]
