# What is Kubernetes?

## From the "Within the Abstraction" Perspective:

### Components

* A *cluster* is a set of worker nodes (machines - virtual or physical) that run containerized applications.
    * The cluster usually runs across multiple nodes in order to provide fault tolerance.
* A *Pod* is a set of running containers in a cluster.
* The *control plane* manages the worker nodes and the pods.
    * This control plane is usually run across multiple machines.
* A *context* is an element of a kubeconfig file and is used to group access parameters under a convenient name. A
  context has 3 components:
    1. cluster
    2. namespace
    3. user

#### Within the Abstraction: Control Plane

#### Within the Abstraction: Nodes

## From the "Outside the Abstraction" Perspective:

## Helm Charts
