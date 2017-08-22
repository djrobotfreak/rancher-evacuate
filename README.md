## Rancher Evacuate

This "evacuate"s a host of all user defined stacks using the AWS metadata service and rancher's v2-beta api.

### How to use
```sh
sudo docker run \
-e RANCHER_API_HOST=< base url of rancher api ex: http://my.rancherhost.com:8080 > \
-e RANCHER_ENVIRONMENT_ID=< id of the rancher environment this host is owned by. ex: 1h9 > \
-e RANCHER_ACCESS_KEY=< rancher access key > \
-e RANCHER_SECRET_KEY=< rancher secret access key > \
djrobotfreak/rancher-evacuate:latest
```
