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

from io import BytesIO
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
    def addFromDir(langDir):
        for path in os.listdir(langDir):
            fullDir = langDir + "/" + path
            if os.path.isfile(fullDir):
                Base.addFromPath(fullDir)

    @staticmethod
    def addFromZipFile(zipFile, path):
        file = zipFile.open(path)
        Base.addFromFile(file)

    @staticmethod
    def addFromZipPath(path, path2):
        Base.addLanguageFromZipFile(ZipFile(path, "r"), path2)

    @staticmethod
    def addFromZipDir(path, langDir):
        zipFile = ZipFile(path, "r")
        for filePath in zipFile.namelist():
            if filePath.startswith(langDir) and filePath != (langDir + "/"):
                Base.addFromZipFile(zipFile, filePath)

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
