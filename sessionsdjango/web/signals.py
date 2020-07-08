from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.conf import settings
from .models import UserAcces

def remove_other_sessions(user,session_user,datetime,limits):
	if limits<=0:
		limits = 1
	if UserAcces.objects.filter(user=user).exists():
		UserAcces.objects.create(user=user,session_key=session_user,datetime=datetime)
		user_access = UserAcces.objects.filter(user=user,session_key__isnull=False).order_by('-datetime')

		if len(user_access)>limits:
			invalid_sessions = len(user_access)-limits
			for session in user_access.order_by('-datetime')[invalid_sessions:]:
				if Session.objects.filter(session_key=session.session_key).exists():
					Session.objects.get(session_key=session.session_key).delete()
				session.session_key = None
				session.save()
	else:
		UserAcces.objects.create(user=user,session_key=session_user,datetime=datetime)

@receiver(user_logged_in)
def check_users_sessions(sender, user, request, **kwargs):
	session_now = request.session.session_key
	datetime_now = timezone.now()
	remove_other_sessions(user,session_now,datetime_now,settings.SESSION_LIMITS)