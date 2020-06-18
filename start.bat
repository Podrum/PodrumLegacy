@echo off
TITLE Podrum server software for Minecraft: Bedrock Edition
cd /d %~dp0

if exist src\podrum\Podrum.py (
	set PODRUM_FILE=src\podrum\Podrum.py
)


python %PODRUM_FILE% %*
