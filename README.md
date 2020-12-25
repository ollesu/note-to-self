# note-to-self
Where we collect our learnings and experiments on all things tech.


Check wiki [here](https://github.com/ollesu/note-to-self/wiki). 


## Infrastructure

---

### Immutability

Mutable container images are an anti-pattern in Kubernetes. 

In traditionally mutable infrastructure, changes are applied incrementally on top of an existing system. For example, `apt-get update` (`apt-get` is a command-line tool in Ubuntu used for package management) downloads new binaries, copies them on top of of older binaries and makes incremental updates to configuration files. The current state of such infrastructure is not a single artifact but rather an accumulation of incremental changes over time, changelog often not being recorded (source: Kubernetes Up and Running book). 

**In immutable architecture, an entirely new image is deployed in the place of an old one and containers are not modified in their lifecycle.**

### Declarative configuration and self-healing

The declarative config describes the **desired state** of your application (unlike imperative configuration, which describes actions). Cool fact: Kubernetes continuously makes sure the current state matches the desired state (i.e. restarting failing containers, killing containers that do not respond to user-defined healthchecks). 


### Kubernetes components
A **cluster** consists of a minumim one node (worker machines). 

**Nodes** house **pods** - a set of running tightly-coupled ontainers. The containers share network namespace (IP address and ports; containers sitting inside one pod can communicate with each other through localhost), resources and configuration (and filesystem volumes).  

Pods are the smallest unit. 

**The control plane** (container orchestration layer API) manages nodes and pods. 

Control plane internals
1. kube-apiserver (front-end for the control plane)
2. etcd - key-value store for cluster data
3. kube-scheduler - assigns nodes to newly created pods
4. kube-controller-manager - runs controller processes (monitors for failing nodes, maintains the desired state, creates API tokens for new namespaces). 
5. cloud-controller-manager - embeds cloud-specific logic into your cluster (note: only runs if your app is hosted on cloud). 

Node internals
1. kubelet runs on each node, monitors and takes care of running containers
2. kube-proxy allow network communication to pods. 

Kubernetes supports several types of container runtimes (Docker, containerd and others). 

*Note*: Pods should be as small as possible ("one-container-per-Pod" model). One pod should run one instance of your application. Run multiple pods (*replication*) if you want to scale horizontally. From my experience, in production there are multiple replicated pods running for one service. 

**(Great!) sources:**

*Kubernetes: Up and Running*, 2nd edition, by B. Burns, J. Beda and K. Hightower (O'Reilly), 2019. 
https://kubernetes.io/docs/concepts/overview