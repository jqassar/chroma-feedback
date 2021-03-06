from typing import Any
from chroma_feedback import wording

API = None


def get_api(ip : str) -> Any:
	global API

	if not API:
		API = api_factory(ip)
	return API


def api_factory(ip : str) -> Any:
	api = None

	try:
		from yeelight import Bulb, BulbException

		try:
			api = Bulb(ip)
		except BulbException:
			exit(wording.get('connection_no').format('XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
		try:
			api.turn_on()
		except BulbException:
			exit(wording.get('enable_feature').format('LAN CONTROL', 'XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('YEELIGHT') + wording.get('exclamation_mark'))
