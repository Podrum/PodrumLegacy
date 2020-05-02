"""
PyRakLib networking library.
   This software is not affiliated with RakNet or Jenkins Software LLC.
   This software is a port of PocketMine/RakLib <https://github.com/PocketMine/RakLib>.
   All credit goes to the PocketMine Project (http://pocketmine.net)

   Copyright (C) 2015  PyRakLib Project

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import warnings
from pyraklib.PyRakLib import PyRakLib

try:
    import requests
    ableToCheck = True
except ImportError:
    warnings.warn("Could not check for latest version: library 'requests' not installed.")
    ableToCheck = False

if ableToCheck:
    def checkForLatestVersion():
        r = requests.get("https://pypi.python.org/pypi/PyRakLib/json")
        v = r.json()['info']['version']
        if v != PyRakLib.LIBRARY_VERSION:
            warnings.warn("You are not using the latest version of PyRakLib: The latest version is: "+v+", while you have: "+PyRakLib.LIBRARY_VERSION)

    checkForLatestVersion()

__all__ = ['PyRakLib', 'Binary']

from pyraklib.Binary import Binary
from pyraklib.PyRakLib import PyRakLib