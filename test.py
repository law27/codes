import docker

dockerClient = docker.DockerClient(base_url='unix://var/run/docker.sock')
