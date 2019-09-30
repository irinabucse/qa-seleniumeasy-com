#!/usr/bin/env bash
ALLURE_REPORT_DIR="$(cd "$(dirname "$1")" && pwd)/allure-report/"
echo $ALLURE_REPORT_DIR
docker run --rm --name allure-server -v $ALLURE_REPORT_DIR:/usr/share/nginx/html:ro -d -p 8081:80 nginx
