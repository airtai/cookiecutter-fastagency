#!/bin/bash

docker run -d --name deploy_fastagency -e OPENAI_API_KEY=$OPENAI_API_KEY {% if "nats" in cookiecutter.app_type %}-e NATS_URL=$NATS_URL -e FASTAGENCY_NATS_PASSWORD=$FASTAGENCY_NATS_PASSWORD -p 8000:8000{% endif %}{% if "fastapi" in cookiecutter.app_type %} -p 8008:8008{% endif %} -p 8888:8888 {% if "nats" in cookiecutter.app_type %}--network=host{% endif %} deploy_fastagency