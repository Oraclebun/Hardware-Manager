from django.urls import path, include
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns =[
    path('',views.index, name='index'),
    path('allpcs/', views.ProbeCardListView.as_view(), name='allpcs'),
    path('allpc/<int:pk>', views.ProbeCardDetailView.as_view(), name='probecard-detail'),
    path('active/', views.active, name='active'),
    path('merle/', views.merle, name='merle'),
    path('joec/', views.joec, name='joec'),
    path('joecocker/', views.joecocker, name='joecocker'),
    path('lespaul/', views.lespaul, name='lespaul'),
    path('jani/', views.jani, name = 'jani'),
    path('womack/', views.womack, name = 'womack'),
    path('bbking/', views.bbking, name='bbking'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]

urlpatterns += [
    path(r'tasks/', views.MyTasksView.as_view(), name = 'tasks'),
    path('probecardreport/create/', views.ProbeCardReportCreate.as_view(), name='probecardreport_create'),
    path('probecardreport/select/', views.select_probecard, name = 'select_probecard'),
    path('probecardreport/select/bbking', views.select_bbking, name = 'select_bbking'),
    path('probecardreport/select/merle', views.select_merle, name = 'select_merle'),
    path('probecardreport/select/joec', views.select_joec, name = 'select_joec'),
    path('probecardreport/select/joecocker', views.select_joecocker, name = 'select_joecocker'),
    path('probecardreport/select/lespaul', views.select_lespaul, name = 'select_lespaul'),
    path('probecardreport/select/jani', views.select_jani, name = 'select_jani'),
    path('probecardreport/select/womack', views.select_womack, name = 'select_womack'),
    path('probecardreport/edit_report/<int:pk>',views.UpdateReport.as_view(), name='pcreport-detail'),
    path(r'probecardreport/createupdatesuccess', views.MyTasksSuccess.as_view(), name = 'create-update-success'),
    ]


urlpatterns += [
    path('jsi18n/', JavaScriptCatalog.as_view(), name = 'javascript-catalog'),
    ]
