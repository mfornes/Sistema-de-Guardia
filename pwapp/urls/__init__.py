from django.urls import path

from pwapp.urls.student import urlpatterns as student_url
from pwapp.urls.employee import urlpatterns as employee_url
from pwapp.urls.guard_plan_employee import urlpatterns as guard_plan_employee_url
from pwapp.urls.guard_plan import urlpatterns as guard_plan_url

from pwapp.urls.user import urlpatterns as user_url

from pwapp.views import LoginView, HomePage, SearchResultsView, EmployeeSearchResultsView, todos, segundo_turno, add, update, guard_plan_page
from pwapp.views import get_guard_plan_employees, add_get_guard_plan_employee, update_guard_plan_employee, employees_segundo_turno

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path("homepage", HomePage.as_view(), name="homepage"),
    path("guard_plan_homepage", guard_plan_page, name="guard_plan-homepage"),
    path("search", SearchResultsView.as_view(), name="search_results"),
    path("employeesearch", EmployeeSearchResultsView.as_view(), name="employeesearch_results"),
    path('people', todos, name='all-people'),
    path('segundo_turno', segundo_turno, name='all-segundo_turno'),

    path('add', add, name='add-gp'),
    path('update/<int:pk>', update, name='update-gp'),

    path('guard_plan_employees', get_guard_plan_employees, name='get_guard_plan_employees-list'),
    path('ok', add_get_guard_plan_employee, name='add_get_guard_plan_employee-create'),
    path('guard_plan_employee_update/<int:pk>', update_guard_plan_employee, name='update_guard_plan_employee-update'),
    path('employees_segundo_turno', employees_segundo_turno, name='all-employees_segundo_turno'),

]

urlpatterns += student_url
urlpatterns += employee_url
urlpatterns += user_url
urlpatterns += guard_plan_url
urlpatterns += guard_plan_employee_url