from django.core import serializers
from django.conf import settings
from importlib import import_module
from django.contrib.auth.models import User

engine = import_module(settings.SESSION_ENGINE)
sid = '.eJxVjEEOwiAQRe_C2pAAgzAu3XsGMgNTqRqalHbVeHdt0oVu_3vvbyrRutS0dpnTWNRFGXX63ZjyU9oOyoPafdJ5ass8st4VfdCub1OR1_Vw_w4q9fqtreMMEcw52AhYBu_BgjAiAgOJQe9yYLERQ_A-5AwogGCA4kDsnXp_ALtaNwk:1oa5KO:6Ux9_GsgG4Zs1id95hpCZcN8iitq9g5Km65v30Rx6SA'
session = engine.SessionStore(sid)
user_id = session.get('_auth_user_id')
user_list = [User.objects.get(id=user_id)]
serializers.serialize("json", user_list)