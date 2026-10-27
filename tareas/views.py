from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Tarea


def lista(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        if titulo:
            Tarea.objects.create(titulo=titulo)
        return redirect("lista")
    return render(request, "tareas/lista.html", {"tareas": Tarea.objects.all()})


@require_POST
def alternar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect("lista")


@require_POST
def eliminar(request, pk):
    get_object_or_404(Tarea, pk=pk).delete()
    return redirect("lista")
