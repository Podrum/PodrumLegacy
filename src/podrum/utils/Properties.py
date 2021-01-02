"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
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
                value = "true" if value else "false"
            props += f"{key} = {value}\n"
        return props.strip()

    @staticmethod
    def dump(data, file):
        file.write(Properties.dumps(data))
