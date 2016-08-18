#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

# replace DEPLOY_SERVER with the release server

sirius docker_deploy:{{cookiecutter.project_slug}},${IMAGE},server=DEPLOY_SERVER,ports="9201;8080"