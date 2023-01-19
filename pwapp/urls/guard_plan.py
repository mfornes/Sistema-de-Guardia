from django.urls import path

from pwapp.views import GuardPlanDeleteView, GuardPlanCreateView, GuardPlanDetailView, GuardPlanListView, GuardPlanUpdateView

urlpatterns = [
    path('guard_plan', GuardPlanListView.as_view(), name='guard_plan-list'),
    path('guard_plan/create', GuardPlanCreateView.as_view(), name='guard_plan-create'),
    path('guard_plan/<int:pk>', GuardPlanDetailView.as_view(), name='guard_plan-detail'),
    path('guard_plan/<int:pk>/delete', GuardPlanDeleteView.as_view(), name='guard_plan-delete'),
    path('guard_plan/<int:pk>/update', GuardPlanUpdateView.as_view(), name='guard_plan-update'),
]