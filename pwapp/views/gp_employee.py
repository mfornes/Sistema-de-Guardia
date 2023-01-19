from django.http import HttpResponseBadRequest, JsonResponse
import json
from django.shortcuts import get_object_or_404
from pwapp.models import Employee, GuardPlan

def get_guard_plan_employees(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            employees = list(Employee.objects.all().values())
            return JsonResponse({'context': employees}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def employees_segundo_turno(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            if request.GET["local"] == "D":
                employees = list(Employee.objects.filter(sexo="M").values())
                return JsonResponse({'context': employees}, status=200)

            employees = list(Employee.objects.all().values())
            return JsonResponse({'context': employees}, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)

    else:
        return HttpResponseBadRequest('Invalid request')

def add_get_guard_plan_employee(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            gp = data.get('payload')
            g_plan = GuardPlan.objects.create(date = gp["date"], local = gp["local"])

            for e in gp["listPrimerTurno"]:
                employees = Employee.objects.get(pk=e)
                employees.save()
                g_plan.employees_first_turn.add(employees)

            for e in gp["listSegundoTurno"]:
                employees = Employee.objects.get(pk=e)
                employees.save()
                g_plan.employees_second_turn.add(employees)

            return JsonResponse({'status': 1}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def update_guard_plan_employee(request, pk):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        guard_plan = get_object_or_404(GuardPlan, id=pk)

        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('payload')

            for e in updated_values['listPrimerTurno']:
                employees = Employee.objects.get(pk=e)
                employees.save()
                guard_plan.employees_first_turn.add(employees)

            r = guard_plan.employees_first_turn.filter(pk__in=updated_values['listPrimerTurno'])
            a = guard_plan.employees_first_turn.all()

            p = a ^ r
            guard_plan.employees_first_turn.remove(*p)

            for e in updated_values['listSegundoTurno']:
                employees = Employee.objects.get(pk=e)
                employees.save()
                guard_plan.employees_second_turn.add(employees)
            
            r1 = guard_plan.employees_second_turn.filter(pk__in=updated_values['listSegundoTurno'])
            a1 = guard_plan.employees_second_turn.all()

            p1 = a1 ^ r1
            guard_plan.employees_second_turn.remove(*p1)

            guard_plan.save()

            return JsonResponse({'status': 1}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')