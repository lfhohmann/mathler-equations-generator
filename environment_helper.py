#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Enviroment Variables helper
--------------------------

This module defines variables based on the Current Working Directory (CWD), to
find out if we are in a "kaggle" or a "local" environment.
"""

import os

__author__ = "Lucas Hohmann"
__email__ = "lfhohmann@gmail.com"
__user__ = "@lfhohmann"

__status__ = "Production"
__date__ = "2022/03/06"
__version__ = "11.0.0"
__license__ = "MIT"


class Environment:
    """
    Enviroment variables class
    --------------------------

    Gets the Current Working Directory (CWD) and sets the `mode` and `dirpath`
    variable attributes accordingly. More attributes can be set, by passing a
    dictionary with the attributes and their values for each mode (kaggle or
    local).
    """

    def __init__(self, data: dict = {}) -> None:
        """
        Init environment variables
        --------------------------

        Initializes the environment variables based on the Current Working
        Directory (CWD).

        Parameters
        ----------

        #### data : dict (required)
        Dictionary containing the environment variables inside the keys:
        ("kaggle", "local").

        >>> {
        ...     "kaggle": {"token": 123},
        ...     "local": {"token": 321},
        ... }

        Returns
        -------

        >>> None
        """

        # Set the main attributes for "kaggle" mode
        if "kaggle" in os.getcwd():
            self.__mode = "kaggle"
            self.__dirpath = "/kaggle/working/"

            # Set the attributes for "kaggle" mode
            if data and "kaggle" in data:
                self.__set_data_attr(data["kaggle"])

        # Set the main attributes for "local" mode
        else:
            self.__mode = "local"
            self.__dirpath = ".\\data\\"

            # Set the attributes for "local" mode
            if data and "local" in data:
                self.__set_data_attr(data["local"])

    def __set_data_attr(self, data: dict) -> None:
        """
        Set attributes
        --------------

        Sets each attribute of the class with the key-value pair from the data
        dictionary.

        Parameters
        ----------

        #### data : dict (required)
        The dictionary passed to it from the constructor (__init__) function

        Returns
        -------

        >>> None
        """

        # Iterate over the passed data
        for attribute, value in data.items():

            # Set the attribute
            setattr(self, attribute, value)

    @property
    def mode(self) -> str:
        """
        "mode" property
        --------------

        Makes sure that the "mode" attribute is read-only.

        Returns
        -------

        #### str:
        A string containing the environment "mode"

        >>> "kaggle"
        >>> "local"
        """

        return self.__mode

    @property
    def dirpath(self) -> str:
        """
        "dirpath" property
        --------------

        Makes sure that the "dirpath" attribute is read-only.

        Returns
        -------

        #### str:
        A string containing the environment "dirpath"

        >>> ".//data//"
        >>> "/kaggle/working/"
        """

        return self.__dirpath