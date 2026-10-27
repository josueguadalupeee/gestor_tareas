from django.test import TestCase
from django.urls import reverse

from .models import Tarea


class TareaModelTest(TestCase):
    def test_str_devuelve_titulo(self):
        tarea = Tarea.objects.create(titulo="Estudiar CI/CD")
        self.assertEqual(str(tarea), "Estudiar CI/CD")

    def test_tarea_nueva_no_esta_completada(self):
        tarea = Tarea.objects.create(titulo="Pendiente")
        self.assertFalse(tarea.completada)


class TareaViewsTest(TestCase):
    def test_lista_responde_200(self):
        respuesta = self.client.get(reverse("lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Gestor de Tareas")

    def test_crear_tarea(self):
        self.client.post(reverse("lista"), {"titulo": "Configurar Docker"})
        self.assertTrue(Tarea.objects.filter(titulo="Configurar Docker").exists())

    def test_no_crea_tarea_vacia(self):
        self.client.post(reverse("lista"), {"titulo": "   "})
        self.assertEqual(Tarea.objects.count(), 0)

    def test_alternar_tarea(self):
        tarea = Tarea.objects.create(titulo="Probar pipeline")
        self.client.post(reverse("alternar", args=[tarea.pk]))
        tarea.refresh_from_db()
        self.assertTrue(tarea.completada)

    def test_eliminar_tarea(self):
        tarea = Tarea.objects.create(titulo="Borrar")
        self.client.post(reverse("eliminar", args=[tarea.pk]))
        self.assertFalse(Tarea.objects.filter(pk=tarea.pk).exists())
