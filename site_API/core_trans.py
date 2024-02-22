import requests
from settings import SiteSettings

site = SiteSettings()
def get_translator(text: str):
	url = "https://text-translator2.p.rapidapi.com/translate"

	payload = {
		"source_language": "en",
		"target_language": "ru",
		"text": text
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": site.api_key_trans.get_secret_value(),
		"X-RapidAPI-Host": site.host_api_trans
	}
	return (requests.post(url, data=payload, headers=headers, timeout=5)).json()


