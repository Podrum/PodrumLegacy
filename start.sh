#!/usr/bin/env sh

DIR="$(cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd "$DIR"

if [ -f ./src/podrum/Podrum.py ]; then
  PODRUM_FILE="./src/podrum/Podrum.py"
else
  echo "Podrum not found"
	echo "Downloads can be found at https://github.com/podrum/podrum/releases"
	exit 1
fi

python3 -O ${PODRUM_FILE}
