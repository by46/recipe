#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

sirius docker_deploy:{{cookiecutter.project_slug}},${IMAGE},server=DEPLOY_SERVER,ports="9200;8080"

