r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team. 

 This file is licensed under the GPL v2.0 license. 
 The license file is located in the root directory
 of the source code. If not you may not use this file. 
"""

from podrum.geometry.vector_2 import vector_2
from podrum.geometry.vector_3 import vector_3

class geometry:
    @staticmethod
    def lerp_vector_3(a: object, b: object, t: float) -> object:
        return vector_3(
            a.x + t * (b.x - a.x),
            a.y + t * (b.y - a.y),
            a.z + t * (b.z - a.z),
        )
      
    @staticmethod
    def lerp_vector_2(a: object, b: object, t: float) -> object:
        return vector_2(
            a.x + t * (b.x - a.x),
            a.z + t * (b.z - a.z),
        )
