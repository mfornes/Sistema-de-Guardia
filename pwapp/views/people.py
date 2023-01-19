from django.http import HttpResponseBadRequest, JsonResponse
import json
from django.shortcuts import get_object_or_404
from pwapp.models import Student, GuardPlan

def todos(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            students = list(Student.objects.all().values())
            return JsonResponse({'context': students}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def segundo_turno(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            if request.GET["local"] == "D":
                students = list(Student.objects.filter(sexo="M").values())
                return JsonResponse({'context': students}, status=200)

            students = list(Student.objects.all().values())
            return JsonResponse({'context': students}, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)

    else:
        return HttpResponseBadRequest('Invalid request')

def add(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            gp = data.get('payload')
            g_plan = GuardPlan.objects.create(date = gp["date"], local = gp["local"])

            for e in gp["listPrimerTurno"]:
                student = Student.objects.get(pk=e)
                student.save()
                g_plan.students_first_turn.add(student)

            for e in gp["listSegundoTurno"]:
                student = Student.objects.get(pk=e)
                student.save()
                g_plan.students_second_turn.add(student)

            return JsonResponse({'status': 1}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def update(request, pk):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        guard_plan = get_object_or_404(GuardPlan, id=pk)

        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('payload')

            for e in updated_values['listPrimerTurno']:
                student = Student.objects.get(pk=e)
                student.save()
                guard_plan.students_first_turn.add(student)

            r = guard_plan.students_first_turn.filter(pk__in=updated_values['listPrimerTurno'])
            a = guard_plan.students_first_turn.all()

            p = a ^ r
            guard_plan.students_first_turn.remove(*p)

            for e in updated_values['listSegundoTurno']:
                student = Student.objects.get(pk=e)
                student.save()
                guard_plan.students_second_turn.add(student)
            
            r1 = guard_plan.students_second_turn.filter(pk__in=updated_values['listSegundoTurno'])
            a1 = guard_plan.students_second_turn.all()

            p1 = a1 ^ r1
            guard_plan.students_second_turn.remove(*p1)

            guard_plan.save()

            return JsonResponse({'status': 1}, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')