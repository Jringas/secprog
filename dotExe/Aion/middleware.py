from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
import dateutil.parser

class LoggedInMiddleware(MiddlewareMixin):

	
	def process_request(self, request):
		if 'user' in request.session:
			if request.session['user'] > -1:
				# if request.session.get_expiry_age() == 0:
				# 	request.session['user'] = -1
				# else:
				# 	request.session.set_expiry(10)
				# print(datetime.now())

				try:
					if datetime.now() - dateutil.parser.parse(request.session['last_touch']) > timedelta(seconds=30):
						del request.session['last_touch']
						# request.session.flush()
						request.session['timeout'] = True

						return HttpResponseRedirect('/Aion/')


				except KeyError:
					pass

				request.session['last_touch'] = datetime.now().isoformat()
				# print("REQUEST: ",request.session['user'])
			else:
				return

		# if request.session['user'] == -1:
		# 	request.session['user'] = 1


