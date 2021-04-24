import io

class properties:
    @staticmethod
    def load(file: object) -> dict:
        result: dict = {}
        for part in file.readlines():
            text: str = part.strip(" ").lstrip(" ")
            if text[0] != "#" and len(text) > 0:
                uckv: list = text.split("=")
                key: str = uckv[0].strip(" ").lstrip(" ")
                value: str = uckv[1].strip(" ").lstrip(" ").rsplit("\n", 1)[0]
                if value.lower() == "true" or value.lower() == "on":
                    result[key]: bool = True
                elif value.lower() == "false" or value.lower() == "off":
                    result[key]: bool = False
                elif value.isdigit():
                    result[key]: int = int(value)
                else:
                    result[key]: str = value
        return result
                      
    @staticmethod
    def loads(data: str) -> dict:
        return properties.load(io.StringIO(data))
