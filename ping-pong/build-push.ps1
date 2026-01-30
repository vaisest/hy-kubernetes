$ver = "3.2"

docker build . -t "turtvaiz/ping-pong:$ver"
docker push "turtvaiz/ping-pong:$ver"