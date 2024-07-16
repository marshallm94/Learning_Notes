The below notes were taken while going through the Introduction to Docker Learning Path on
Cloud Academy

[TOC]

# Installing Docker

## Windows

Surprise surprise, installing something on Windows is a pain in the ass.....

1. Download Docker Desktop for Windows [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
2. Run the installer - click close when prompted.
3. From the start menu (or using the Desktop Icon), start Docker Desktop.
4. **At this point, you will be prompted to install WSL2 Linux Kernel update**. You can download this
   [here](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
	* Side note: WSL = Windows Subsystem for Linux
5. Once the update is downloaded, run the installer - click close when prompted.
6. Run `wsl --set-default-version 2` from a PowerShell window.
7. Start Docker Desktop again - you should be prompted with a 'Get Started with Docker in a few easy steps!'.
   Alternatively, you can check the icons (might be hidden, click the '^' button) for the docker whale icon - it should
   be white in color and when you hover over it with the cursor is should say, 'Docker Desktop is running'.

# What is Docker?

* Docker is a container platform that allows you to package everything that your code needs to run (the source code
  itself, specific versions of third party libraries, binary files, OS, etc.) into **one** self contained identity that
  can be run on any machine with the Docker engine installed.
	* Can be thought of as having a single executable, regardless of the target OS.
* This greatly simplifies the deployment process - instead of checking that all dependencies are the same on a target
  server (in Production, for example), all you have to do is make sure Docker is installed.
* Containers are isolated from other containers that are running on the same machine.
* Docker can be installed on the 3 top OS' from [this link](https://docs.docker.com/get-docker/).
* Note that Docker is not the only container technology, and containers existed prior to docker.

## Docker Architecture

* Uses a client-server architecture:
	* Server = Docker daemon
		* Exposes REST API
	* Client = Docker binary (i.e. the `$ docker build`, `$ docker pull`, `$ docker run` are all calling the
	  `docker` binary)
* [Dockerhub](https://hub.docker.com/) is the 'main' repository/registry for docker images.

## Technologies

There are various technologies that make docker able to run processes in isolated environments. Some key technologies
are:

**Namespaces**
* pid namespace: Process isolation (PID = process ID).
* net namespace: Managing network interfaces (NET = Networking).
* ipc namespace: Managing access to IPC resources (IPC = InterProcess Communication).
* mnt namespace: Managing filesystem mount points (MNT = Mount).
* uts namespace: Isolating kernel and version identifiers (UTS = Unix Timesharing System).

**Control Groups (aka C Groups)**
* Resource limiting: groups can be set to not exceed a configured memory limit.
* Prioritization: some groups may get a larger share of CPU utilization of disk I/O throughput.
* Accounting: measures a group's resource usage.
* Control: freezing groups of processes.

**Union FS (File System)**
* Merging: overlay filesystem branches to merge changes.
* Read/Write: brances can be read-only or read-write.

# Images & Containers

## Images vs. Containers

* Containers are instances of images; another way of saying that is, "images are templates from which containers are
  built."
	* An important point here is that once a container is created (using `$ docker build`), any changes made to
	  the images **will not** affect the already built container.
	* Another way of saying this is, "Each time you create a container, that container is based on how the image
	  looks **at the moment the container is created.**"
* Images are based on "layers" - all layers together contain everything that is necessary to run your application.

## Images From the Dockerfile 

* **Creating images from a Dockerfile should be your default method for creating images.**
* Images are created from the Dockerfile.
* Dockerfiles are texts files with commands that are used to create images.
* A Dockerfile is called just that; no extenstion, just `Dockerfile`.
* The `CMD` instruction in the Dockerfile is the default command to run when a container first starts. **There should be
  one `CMD` instruction per Dockerfile.**

## Images From Containers 

* Although creating an image from a Dockerfile, and then creating a container from said image is the default way of
  creating a container, it isn't the only way.
* Images can be created from containers using the `$ docker commit` command:
	1. Start a container that will serve as the "base" for your new image. 
	2. Once you are "inside" the running container, make any changes you would like.
	3. Exit the running container.
	4. Run `$ docker commit <CONTAINER_ID> <NEW_IMAGE_NAME>`, which will create a new image <NEW_IMAGE_NAME> based
	   off the container <CONTAINER_ID>.
* Note that if you want to change the CMD of the container, you can do so while running the `$ docker commit` command by
  running `$ docker commit --change='CMD <whatever_you_want_the_CMD_to_be>'`

# Port Mapping 

* Port mapping, as it sounds, maps exposed ports on the container to available ports of the host machine on which the
  container is running.
* Port mapping can be done dynamically with the publish all flag,  `$ docker run -P`. When this is run, the exposed ports
  of the container are mapped to available ports of the host randomly.
* Port mapping can be done manually with the publish flag `$ docker run --p <host_port>:<container_port>`. When this is
  run, <container_port> is explicitly mapped to <host_port> of the host.

# Networking 

* The `bridge` network is the default - when a container is started without a network specified, it will use the
  `bridge` network.

# Persistent Storage in Docker

There are 3 options for persistent storage of data that is within a container, all of which can be created by passing
the `--mount` parameter to the `$ docker run` command.

The three storage types are:
1. Bind Mounts
	* Bind mounts are not new to Docker.
	* Bind mounts are a "portal" from the container to the host: a bind mount "mount" a specific file/directory from
	  the host to the container, which give the containter (and any systems within the container) access to that
	  file or directory of files.
	* When creating bind mounts, **the user is in charge of specifying the destination and source filepath.**
	* `$ docker run <IMAGE_NAME> --mount type=bind, source="<path_to_file_or_dir_on_host>", destination=<path_to_file_or_dir_in_container>`
2. Volumes
	* Volumes are similar to Bind Mounts, however **Docker manages the file system location of the volume on the host.**
	* `$ docker run <IMAGE_NAME> --mount type=volume, source="<volume_name>", destination=<path_to_file_or_dir_in_container>`
        * Note that the `<volume_name>` in `$ ...source=<volume_name>...` is **not** a filepath (and therefore shouldn't
          includes slashes `/`). This should have a human readable name (e.g. `app-volume`) and docker will handle the
          filepath of this volume in the VM.
3. tmpfs ( Temporary File Systems )
	* In-memory storage (**data in tmpfs will be deleted when the container is stopped**)

# Tagging 

* Tagging allows the identification of specific versions of an image.
* Images can have more than one tag
	* For example, there are different tags associated with various OS images that specify different OS versions.
* Any time you reference an images without specifying a tag, Docker will look for the image version with the tag
  "latest".
* **If you want to push your image to dockerhub, your image must be tagged with your account name.**
	`$ docker tag <dockerhub_account>/<image_name>:<tag>`

# Docker Command List

* `$ docker run` - run a docker containter.
	* `$ docker run -d` - run a docker containter *in detached mode* (allows the use of the terminal).
	* `$ docker run -d -P` - run a docker containter *in detached mode* (allows the use of the terminal) and maps the
	  container ports to ports of the host machine.
* `$ docker build -t <desired_repo_name> <path_to_directory_where_dockerfile_is_located>` - build a container from an
  image as outlined in the Docker file.
* `$ docker pull` - pull a container from a registry.
* `$ docker images` - list the images stored locally (stored in `/var/lib/docker/`).
* `$ docker start <container_name>` - started a container named <container_name>.
* `$ docker attach <container_name>` - make an already running container (named <container_name>) interactive.
* `$ docker ps` - list all *running* containers.
* `$ docker ps -a` - list all containers.
* `$ docker prune` - **permanently delete** all local, non-running containers.
* `$ docker rm <container_name>` - **permanently delete** the container named <container_name>.
* `$ docker commit `- Used to commit a conatiner's file changes or settings into a new images.
* `$ docker network ls`- List docker networks.
* `$ <CTRL+p><CTRL+q>`- Detach from a running container without stopping that container.
* `$ docker login`- Log in to your dockerhub account via the command line (allows pushing/pulling docker images).
* `$ docker push <image_name>`- Push <image_name> to dockerhub (unless a different).
* `$ docker tag <image_name>:<tag>` - Tag an already created image.
* `$ docker rm $(docker ps -aq)` - **remove all containers**
