"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from io import StringIO

class Properties:
    @staticmethod
    def loads(data):
        return Properties.load(StringIO(data))

    @staticmethod
    def load(file):
        data = {}
        lines = file.readlines()
        for line in lines:
            kv = line.split("=", 1)
            key = kv[0].strip()
            value = kv[1].strip()
            if value.lower() == "true" or value.lower() == "on":
                value = True
            if value.lower() == "false" or value.lower() == "off":
                value = False
            data.update({key: value})
        return data

    @staticmethod
    def dumps(data):
        props = ""
        for key, value in data.items():
            if isinstance(value, bool):
                value = "true" if value == True else "false"
            props += f"{key} = {value}\n"
        return props.strip()

    @staticmethod
    def dump(data, file):
        file.write(Properties.dumps(data))
