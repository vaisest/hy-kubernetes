$ver = "2.6"

docker build . -t turtvaiz/todo-app:$ver -f front.Dockerfile
docker build . -t turtvaiz/todo-app:be-$ver -f back.Dockerfile
docker push turtvaiz/todo-app:$ver
docker push turtvaiz/todo-app:be-$ver