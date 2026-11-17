# Kubernetes

Kubernetes (), also known as K8s, is an open-source container orchestration system for automating software deployment, scaling, and management. Originally designed by Google, the project is now maintained by a worldwide community of contributors, and the trademark is held by the Cloud Native Computing Foundation.

The name Kubernetes comes from the Ancient Greek term κυβερνήτης, kubernḗtēs (helmsman, pilot), which is also the origin of the words cybernetics and (through Latin) governor. "Kubernetes" is often abbreviated with the numerical contraction "K8s", meaning "the letter K, followed by 8 letters, followed by s".

Kubernetes assembles one or more computers, either virtual machines or bare metal, into a cluster which can run workloads in containers. It works with various container runtimes, such as containerd and CRI-O. Its suitability for running and managing workloads of all sizes and styles has led to its widespread adoption in clouds and data centers. There are multiple distributions of this platform—from independent software vendors (ISVs) as well as hosted-on-cloud offerings from all the major public cloud vendors.

The software consists of a control plane and nodes on which the actual applications run. It includes tools like kubeadm and kubectl which can be used to interact with its REST-based API.

Kubernetes was announced by Google on June 6, 2014. The project was conceived and created by Google employees Joe Beda, Brendan Burns, and Craig McLuckie. Others at Google soon joined to help build the project including Ville Aikas, Dawn Chen, Brian Grant, Tim Hockin, and Daniel Smith. Other companies such as Red Hat and CoreOS joined the effort soon after, with notable contributors such as Clayton Coleman and Kelsey Hightower.

The design and development of Kubernetes was inspired by Google's Borg cluster manager and based on Promise Theory. Many of its top contributors had previously worked on Borg; they codenamed Kubernetes "Project 7" after the Star Trek ex-Borg character Seven of Nine and gave its logo a seven-spoked ship's wheel (designed by Tim Hockin). Unlike Borg, which was written in C++, Kubernetes is written in the Go language.

Kubernetes was announced in June, 2014 and version 1.0 was released on July 21, 2015. Google worked with the Linux Foundation to form the Cloud Native Computing Foundation (CNCF) and offered Kubernetes as the seed technology.

Google was already offering a managed Kubernetes service, GKE, and Red Hat was supporting Kubernetes as part of OpenShift since the inception of the Kubernetes project in 2014. In 2017, the principal competitors rallied around Kubernetes and announced adding native support for it:

VMware (proponent of Pivotal Cloud Foundry) in August,

Mesosphere, Inc. (proponent of Marathon and Mesos) in September,

Docker, Inc. (proponent of Docker) in October,

Microsoft Azure also in October,

AWS announced support for Kubernetes via the Elastic Kubernetes Service (EKS) in November.

On March 6, 2018, Kubernetes Project reached ninth place in the list of GitHub projects by the number of commits, and second place in authors and issues, after the Linux kernel.

Until version 1.18, Kubernetes followed an N-2 support policy, meaning that the three most recent minor versions receive security updates and bug fixes. Starting with version 1.19, Kubernetes follows an N-3 support policy.

Kubernetes defines a set of building blocks ("primitives") that collectively provide mechanisms that deploy, maintain, and scale applications based on CPU, memory or custom metrics. Kubernetes is loosely coupled and extensible to meet the needs of different workloads. The internal components as well as extensions and containers that run on Kubernetes rely on the Kubernetes API.

The platform exerts its control over compute and storage resources by defining resources as objects, which can then be managed as such.

Kubernetes follows the primary/replica architecture. The components of Kubernetes can be divided into those that manage an individual node and those that are part of the control plane.

The Kubernetes control plane manages its workload and directs communication across the system. It consists of various components such as TLS encryption, role-based access control (RBAC) and a strong authentication method, network separation, each its own process, that can run both on a single node or on multiple nodes supporting high-availability clusters. The various components of the Kubernetes control plane are as follows.

Etcd is a persistent, lightweight, distributed, key-value data store (originally developed as part of CoreOS). It reliably stores the configuration data of the cluster, representing the overall state of the cluster at any given point of time. Etcd favors consistency over availability in the event of a network partition (see CAP theorem). The consistency is crucial for correctly scheduling and operating services.

The API server serves the Kubernetes API using JSON over HTTPS, which provides both the internal and external interface to Kubernetes. The API server processes, validates REST requests, and updates the state of the API objects in etcd, thereby allowing clients to configure workloads and containers across worker nodes. The API server uses etcd's watch API to monitor the cluster, roll out critical configuration changes, or restore any divergences of the state of the cluster back to the desired state as declared in etcd.

As an example, a human operator may specify that three instances of a particular "pod" (see below) need to be running, and etcd stores this fact. If the Deployment controller finds that only two instances are running (conflicting with the etcd declaration), it schedules the creation of an additional instance of that pod.

The scheduler is an extensible component that selects the node that an unscheduled pod (the basic unit of workloads to be scheduled) runs on, based on resource availability and other constraints. The scheduler tracks resource allocation on each node to ensure that workload is not scheduled in excess of available resources. For this purpose, the scheduler must know the resource requirements, resource availability, and other user-provided constraints or policy directives such as quality-of-service, affinity/anti-affinity requirements, and data locality. The scheduler's role is to match resource "supply" to workload "demand".

Kubernetes allows running multiple schedulers within a single cluster. As such, scheduler plug-ins may be developed and installed as in-process extensions to the native vanilla scheduler by running it as a separate scheduler, as long as they conform to the Kubernetes scheduling framework. This allows cluster administrators to extend or modify the behavior of the default Kubernetes scheduler according to their needs.

A controller is a reconciliation loop that drives the actual cluster state toward the desired state, communicating with the API server to create, update, and delete the resources it manages (e.g., pods or service endpoints).

Source: https://en.wikipedia.org/wiki/Kubernetes (Wikipedia, CC BY-SA 4.0)
