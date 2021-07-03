#########################################################
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

import base64
import hashlib
import hmac
import json

class jwt:

    @staticmethod
    def decode(token: str) -> dict:
        r"""
        Decodes json web tokens to
        a json string
        :param token: The token to decode.
        :type token: str

        :return: The decoded token.
        :rtype: dict
        """
        header, payload, verifySigniture = token.split(".")
        payload += "=="
        json_data: str = base64.b64decode(payload.replace("-_", "+/").encode())
        return json.loads(json_data)
  
    # [encode]
    # :return: = str
    # Encodes a the json web token
    # header, json string and signiture 
    # back to a encoded json web token
    @staticmethod
    def encode(header: dict, payload: dict, verifySigniture: str) -> str:
        body: list = []
        body.append(base64.b64encode(json.dumps(header).encode()).decode())
        body.append(base64.b64encode(json.dumps(payload).encode()).decode())
        body.append(base64.b64encode(hmac.new(verifySigniture.encode(), ".".join(body).encode(), hashlib.sha256).hexdigest().upper().encode()).decode())
        return ".".join(body)
