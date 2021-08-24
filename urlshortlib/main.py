import httpx, re
from typing import Optional


default_api_url: str = "https://s.itayki.com"


class SlugIsAlreadyExists(Exception):
    pass


class InvalidSlug(Exception):
    pass


class SlugIsNotExists(Exception):
    pass


class UnknownError(Exception):
    pass


class UrlShort:
    def __init__(self, api_url: Optional[str] = default_api_url):
        self.api_url = (
            api_url if re.match(r"^https?://", api_url) else "http://" + api_url
        )

    async def short_link(self, url: str, slug: Optional[str] = None):
        """
        Create a short link.
        parameters:
        url (str): the url to short,
        slug (str) (optional): the slug.
        """
        async with httpx.AsyncClient(http2=True) as http:
            request_params = dict(url=url, slug=slug) if slug else dict(url=url)
            send_request = await http.post(
                f"{self.api_url}/api/add", params=request_params
            )
            request_json = send_request.json()
            if send_request.status_code == 409:
                raise SlugIsAlreadyExists(request_json["detail"])
            elif send_request.status_code == 400:
                raise InvalidSlug(request_json["detail"])
            else:
                return request_json

    async def get_link(self, slug: str):
        """
        Get the short link.
        parameters:
        slug (str): the slug.
        """
        async with httpx.AsyncClient(http2=True) as http:
            request_params = dict(slug=slug)
            send_request = await http.post(
                f"{self.api_url}/api/get", params=request_params
            )
            request_json = send_request.json()
            if send_request.status_code == 404:
                raise SlugIsNotExists(request_json["detail"])
            else:
                return request_json

    async def get_links_count(self):
        """
        Get the links count.
        """
        async with httpx.AsyncClient(http2=True) as http:
            send_request = await http.post(f"{self.api_url}/api/all")
            request_json = send_request.json()
            return request_json["count"]

    async def get_link_qr(self, slug: str):
        """
        Get the qr code of the short link.
        parameters:
        slug (str): the slug.
        """
        async with httpx.AsyncClient(http2=True) as http:
            send_request = await http.post(f"{self.api_url}/{slug}/qr")
            if send_request.status_code == 404:
                request_json = send_request.json()
                raise SlugIsNotExists(request_json["detail"])
            elif send_request.status_code == 200:
                return send_request.read()
            else:
                raise UnknownError(f"status code: {send_request.status_code}")

    async def get_link_click_stats(self, slug: str):
        """
        Get the click stats of the short link.
        parameters:
        slug (str): the slug.
        """
        async with httpx.AsyncClient(http2=True) as http:
            request_params = dict(slug=slug)
            send_request = await http.post(
                f"{self.api_url}/api/click_stats", params=request_params
            )
            if send_request.status_code == 404:
                request_json = send_request.json()
                raise SlugIsNotExists(request_json["detail"])
            elif send_request.status_code == 200:
                return send_request.read()
            else:
                raise UnknownError(f"status code: {send_request.status_code}")
