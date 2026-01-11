import json
from urllib import parse, request
from .errors import APIKeyError, RequiredError
from .constants import PUBLIC_API_URL, STICKER_API_URL
from typing import Any, Dict, List, Optional


class APIBase:
    """
    Base class for API initializer.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key
        if api_key is None:
            raise APIKeyError
        self.params: Dict[str, Any] = {
            'api_key': self.api_key
        }


class GiphyPublicAPI(APIBase):
    """
    Wrapper class for Giphy public api.
    You can find api key from https://developers.giphy.com/dashboard/
    """

    def __get_json(self, url: str, sort_key: bool = False, indent: int = 4) -> str:
        """

        :param url: Giphy api endpoint with query parameters.
        :param sort_key:Sorting the keys when dumping saves the key-value pairs in
        alphabetical order by keys.
        :param indent:The indent parameter specifies the spaces that
         are used at the beginning of a line. By default, it's value is 4.

        """
        with request.urlopen(url) as response:
            data = json.loads(response.read())
        return json.dumps(obj=data, sort_keys=sort_key, indent=indent)

    def search(self, **kwargs: Optional[str | int]) -> str:
        """

        :param q: Search query term or phrase (required).
        :param limit: The maximum number of records to return.
        :param offset: An optional results offset.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        :param lang: specify default country for regional content.
        """
        if kwargs:
            self.params.update(**kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/search', '?', params))
        return self.__get_json(url)

    def translate(self, **kwargs: Optional[str]) -> str:
        """
        :param s:  Search query term or phrase (required).

        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/translate', '?', params))
        return self.__get_json(url)

    def trending(self, **kwargs: Optional[int | str]) -> str:
        """
        :param limit: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/trending', '?', params))
        return self.__get_json(url)

    def random(self, **kwargs: Optional[str]) -> str:
        """
        :param tag: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/random', '?', params))
        return self.__get_json(url)

    def get_by_id(self, id: Optional[str] = None) -> str:
        """
        :param id: Filter result by specific gif id (required).
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, f'/{id}', '?', params))
        return self.__get_json(url)

    def get_by_ids(self, ids: List[str] = []) -> str:
        """
        :param ids: List of specific ids (required).
        """
        if len(ids) < 0:
            raise RequiredError('list of ids')
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '?', params, f"{'&ids='}", "%2C".join(ids)))
        return self.__get_json(url)


class GiphyStickerAPI(APIBase):
    """
      Wrapper class for Giphy sticker api.
      You can find api key from https://developers.giphy.com/dashboard/
      """

    def __get_json(self, url: str, sort_key: bool = False, indent: int = 4) -> str:
        """

        :param url: Giphy api endpoint with query parameters.
        :param sort_key:Sorting the keys when dumping saves the key-value pairs in
        alphabetical order by keys.
        :param indent:The indent parameter specifies the spaces that
         are used at the beginning of a line. By default, it's value is 4.

        """
        with request.urlopen(url) as response:
            data = json.loads(response.read())
        return json.dumps(obj=data, sort_keys=sort_key, indent=indent)

    def search(self, **kwargs: Any[str | int]) -> str:
        """

        :param q: Search query term or phrase (required).
        :param limit: The maximum number of records to return.
        :param offset: An optional results offset.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        :param lang: specify default country for regional content.
        """
        if kwargs:
            self.params.update(**kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/search', '?', params))
        return self.__get_json(url)

    def translate(self, **kwargs: Optional[str]) -> str:
        """
        :param s:  Search query term or phrase (required).

        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/translate', '?', params))
        return self.__get_json(url)

    def trending(self, **kwargs: Optional[str | int]) -> str:
        """
        :param limit: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/trending', '?', params))
        return self.__get_json(url)

    def random(self, **kwargs: Optional[str]) -> str:
        """
        :param tag: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/random', '?', params))
        return self.__get_json(url)

    # FIXME: is setting id = None by default and then checking for the value necessary?
    def get_by_id(self, id: Optional[str] = None) -> str:
        """
        :param id: Filter result by specific gif id (required).
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, f'/{id}', '?', params))
        return self.__get_json(url)

    def get_by_ids(self, ids: List[str] = []) -> str:
        """
        :param ids: List of specific ids (required).
        """
        if len(ids) < 0:
            raise RequiredError('list of ids')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '?', params, f"{'&ids='}", "%2C".join(ids)))
        return self.__get_json(url)

    def stickers_listing(self) -> str:
        """Get all the stickers pack"""
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/packs', '?', params))
        return self.__get_json(url)

    def individual_stickers_pack(self, id: Optional[str] = None) -> str:
        """
        :param id: get individual sticker pack by id
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, f'/packs/{id}', '?', params))
        return self.__get_json(url)

    def stickers(self, id: Optional[str] = None, **kwargs: Optional[int]) -> str:
        """
        :param id: id of sticker pack.
        :param limit:The maximum number of records to return.
        :param offset:An optional results offset.

        """

        if id is None:
            raise RequiredError('id')
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, f'/packs/{id}/stickers', '?', params))
        return self.__get_json(url)

    def children_pack_listing(self, id: Optional[str] = None) -> str:
        """
        :param id: id of sticker pack.
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, f'/packs/{id}/children?', params))
        return self.__get_json(url)


