from io import StringIO

class Properties:
    def loads(data):
        return Properties.load(StringIO(data))

    def load(file):
        data = {}
        lines = file.readlines()
        for line in lines:
            kv = line.split(":", 1)
            key = kv[0]
            value = kv[1].strip()
            if value.lower() == "true" or value.lower() == "on":
                value = True
            if value.lower() == "false" or value.lower() == "off":
                value = False
            data.update({key: value})
        return data

    def dumps(data):
        props = ""
        for key, value in data.items():
            if isinstance(value, bool):
                value = "true" if value == True else "false"
            props += f"{key}: {value}\n"
        return props

    def dump(data, file):
        file.write(Properties.dumps(data))
