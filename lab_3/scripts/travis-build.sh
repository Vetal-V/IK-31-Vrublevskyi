#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run python monitoring.py &
sleep 60
kill `jobs -p`
exit 0
