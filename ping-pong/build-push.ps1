$ver = "3.5"

docker build . -t "turtvaiz/ping-pong:$ver"
docker push "turtvaiz/ping-pong:$ver"