from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = "apps.pagestud"

    def ready(self):
        import apps.students.signals
