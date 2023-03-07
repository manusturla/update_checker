#!/bin/bash
echo "Starting application"
flask --app application db upgrade
echo "Starting gunicorn"
gunicorn application -b 0.0.0.0:8080
