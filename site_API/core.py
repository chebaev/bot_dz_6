from site_API.urils.site_api_handler import SiteApiInterface
from settings import SiteSettings

site = SiteSettings()

headers = {
	"X-RapidAPI-Key": site.api_key_num.get_secret_value(),
	"X-RapidAPI-Host": site.host_api_num
}

url = "https://" + site.host_api_num
params = {"fragment": "true", "json": "true"}

site_api = SiteApiInterface()

if __name__ == '__main__':
    site_api()

