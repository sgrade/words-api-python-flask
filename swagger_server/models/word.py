# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Word(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, photo_urls: List[str]=None):  # noqa: E501
        """Word - a model defined in Swagger

        :param id: The id of this Word.  # noqa: E501
        :type id: int
        :param name: The name of this Word.  # noqa: E501
        :type name: str
        :param photo_urls: The photo_urls of this Word.  # noqa: E501
        :type photo_urls: List[str]
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'photo_urls': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'photo_urls': 'photoUrls'
        }
        self._id = id
        self._name = name
        self._photo_urls = photo_urls

    @classmethod
    def from_dict(cls, dikt) -> 'Word':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Word of this Word.  # noqa: E501
        :rtype: Word
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Word.


        :return: The id of this Word.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Word.


        :param id: The id of this Word.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Word.


        :return: The name of this Word.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Word.


        :param name: The name of this Word.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def photo_urls(self) -> List[str]:
        """Gets the photo_urls of this Word.


        :return: The photo_urls of this Word.
        :rtype: List[str]
        """
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, photo_urls: List[str]):
        """Sets the photo_urls of this Word.


        :param photo_urls: The photo_urls of this Word.
        :type photo_urls: List[str]
        """
        if photo_urls is None:
            raise ValueError("Invalid value for `photo_urls`, must not be `None`")  # noqa: E501

        self._photo_urls = photo_urls