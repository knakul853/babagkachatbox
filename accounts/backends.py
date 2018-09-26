from django.contrib.auth.models import User

class EmailBackend(object):

    def authentication(self, username=None, password=None ,**kwargs):
        try:
            user=User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()



        except User.DoesNotExit:
            return None


