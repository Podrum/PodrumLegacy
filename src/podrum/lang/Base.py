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

from io import BytesIO
from podrum.utils.Config import Config
import os
from podrum.utils.Config import Config
from podrum.utils.Utils import Utils
from zipfile import ZipFile

class Base:
    languages = {}

    @staticmethod
    def addFromFile(file):
        newConfig = Config()
        newConfig.load(file)
        config = newConfig.config
        langId = config["languageInfos"]["langId"]
        Base.languages[langId] = config

    @staticmethod
    def addFromPath(path):
        Base.addFromFile(open(path, "rb"))

    @staticmethod
    def addFromDir(dir):
        for path in os.listdir(dir):
            fullDir = dir + "/" + path
            if os.path.isfile(fullDir):
                Base.addFromPath(fullDir)

    @staticmethod
    def addFromZipFile(zip, path):
        file = zip.open(path)
        Base.addFromFile(file)

    @staticmethod
    def addFromZipPath(path, path2):
        Base.addLanguageFromZipFile(ZipFile(path, "r"), path2)

    @staticmethod
    def addFromZipDir(path, dir):
        zip = ZipFile(path, "r")
        for filePath in zip.namelist():
            if filePath.startswith(dir) and filePath != (dir + "/"):
                Base.addFromZipFile(zip, filePath)

    @staticmethod
    def translate(lang, translation):
        if lang in Base.languages:
            if translation in Base.languages[lang]:
                return Base.languages[lang][translation]

    @staticmethod
    def printLanguages():
        for langId, content in Base.languages.items():
            print(f"{langId} -> {content['langName']}")

    @staticmethod
    def getTranslation(content):
        config = Utils.getDefaultConfig()
        langId = config.config["language"]
        return Base.translate(langId, content)
