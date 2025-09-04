#!/usr/bin/env bash
set -o errexit

poetry install --no-root --only main

python manage.py collectstatic --no-input

python manage.py migrate