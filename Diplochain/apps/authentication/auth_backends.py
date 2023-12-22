from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from apps.students.models import Student

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        # Check the default authentication table
        user = super().authenticate(request, username=username, password=password, **kwargs)
        
        if user is None:
            # If user is not found in the default authentication table, check the Student model
            student = Student.objects.filter(username=username, password=password).first()
            if student:
                # Create a user instance for the student
                user = user_model.objects.filter(username=username).first()
                if not user:
                    user = user_model(username=username)
                    user.set_password(password)
                    user.save()

        return user
