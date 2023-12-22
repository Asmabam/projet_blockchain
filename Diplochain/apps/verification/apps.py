from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = "apps.verification"

    def ready(self):
        import apps.students.signals
