set-variable -name DISPLAY -value 10.0.75.1:0.0
docker run -it  -e DISPLAY=$DISPLAY -u 0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro --name=ui vehicletracking