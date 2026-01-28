$ver = "2.5"

docker build . -t "turtvaiz/log-output:$ver" -f http.Dockerfile
docker build . -t "turtvaiz/log-output-timer:$ver" -f timer.Dockerfile
docker push "turtvaiz/log-output:$ver"
docker push "turtvaiz/log-output-timer:$ver"