The below notes were taken while going through the AWS Cloud Practitioner Certification Preparation on Cloud Academy

[TOC]

# What is Cloud Computing? 

Cloud computing is a remote virtual pool of on-demand shared resources offering Compute, Storage, Database and Network
services that can be rapidly deployed at scale.

**Virtualization** - The ability to run multiple VM's, possibly running different OS', on one physical server.
* Hardware is shared among the VM's - this sharing controlled by the Hypervisor, which sits between the hardware and the
  VM's. The Hypervisor is itself software.
	* "instance" == "VM"

* Benefits include reduced costs due to the ability for multiple VM's to run on one physical machine, which
  allows the business (or cloud infrastructure provider), to save electricty, storage (of the physical machines), etc.

The 4 main services offered by a cloud infrastructure provider are:
* Compute 
* Storage
* Database
* Network

**It makes sense to host your cloud as close to the users of the cloud as possible, to cut down on latency**

## Cloud Deployment Models

1. Public Cloud
* Shared responsibility between the user (business/individual) and the provider (AWS, Microsoft ( Azure ), Google (Cloud
  Platform), Snowflake, etc).
	* Provider handles the physical storage and maintainance of the machines while the user is responsible for
	  security within the cloud and maintaining whatever system they are running.
* Capital expenditure is low (don't need to hardware and people to maintain said hardware)
* Operational expenditure is variable - you only pay for the resources you use.

2. Private Cloud
* Hardware is typically kept on premise
	* Virtualization is still a part of the system, but the hardware is managed by the company/individual as well.
* Typically more secure
* Costs more (have to maintain the physical machines, electricty, *regardless of whether you use them or not*)

3. Hybrid Cloud
* Blend of both of the above (note that this does mean you get the *worst* of both in addition to the best of both)

## Key Cloud Concepts

* On-Demand Resourcing
	* When you want a resource (larger EC2 instance, another DB, etc.) it is *almost* always available.
* Scalability
	* 'Up' and 'down' scalability - alters the power and performance of an instance.
	* 'In' and 'out' scalability - adds/removes the numbers of instances your system is using.
* Economy of scale
	* Large cloud providers can pass the part of the savings associated with virtualization onto the customer.
* Flexibility and Elasticity
	* Choose the exact architecture you need (number of instances, OS', etc.)
* Growth
	* Global datacenters allow the user to reach their end users on a global scale, not having to worry about
	  latency since the cloud infrastructure provider usually has resources around the world.
* Utility Based Metering
	* Only pay for what you use (or leave on...)
* Shared Infrastructure
	* Virtualization allows multiple services to run on one machine, thus allowing multiple users to use the same
	  physical machine (allows for economies of scale for the cloud provider)
* Highly Available
	* Having data copied to different places allows a resilience that would otherwise need to be architected on its
	  own.
* Security
	* Cloud providers are usually more secure since they have to comply with worldwide regulations.

## Cloud Service Models

1. Software as a Service (SaaS)
	* (Most applications fit this model) - allows some customization, however that customization is within the
	  context of the application.
2. Platform as a Service (PaaS)
	* Allows customization from the OS level and up (network, host hardware etc. managed by provider).
3. Infrasture as a Service (IaaS)
	* Allows customization at the OS level and up (including virtual clouds). The hardware is typically managed by the provider.

## Common Use Cases of Cloud Computing 

* Migration of production services to the cloud (as opposed to on premises services)
* Peak season might but a strain on standard infrastructure; being based in the cloud would allow seasonal scaling
  ("Traffic Bursting")
* Backup & DR (Disaster Recovery)
* Web hosting of applications
* Test & Dev environments
* Low cost Proof of Concept
* Big Data & Data manipulation

## Data Center Architecture in the Cloud

* Location
	* public cloud providers will have regions worldwide, each region with multiple data centers
* Physical Security
	* Vendor is responsible for the physical security of their data center
* Mechanical & Electrical Infrastructure (CRAC (Computer Room Air Conditioning))
	* Generators, Fire Suppression, etc. are all on premise at the data center, and is therefore the responsibility
	  of the data center.
* Network Infrastructure (Switches/Routers/Firewalls)
	* The public cloud user is able to create configurations that simulate the logical effet of switches, routers
	  and firewalls.
	* In AWS, virtual clouds are called Virtual Private Networks (VPCs) and are configured by the end user. This
	  therefore means that the security & infrastructure *of the VPC* is the responsibility of the end user.
* Servers (Application/Directory/Database)
	* "instances" or "VMs" 
	* Providers offer services that are specific to hosting databases, or specific to high compute power
* Storage (NAS/SAN/Block Storage/Backup)
	* In the cloud, storage is effectively unlimited and highly scalable.

# Compute Fundamentals for AWS

* There are different types of compute resources on AWS - not only EC2

## EC2 - Elastic Cloud Compute

* EC2 is the "meat and potatoes" of AWS' compute infrastructure.

### AMIs - Amazon Machine Images

* An AMI is a template for a VM; this can include the OS, specific applications for your use case, custom configurations, etc.
* To create your own custom AMI:
	* Choose a basic AMI the first time you launch an EC2 instance (only specifying the OS you want for example),
	  and then once the instance is launched, you can install any applications related to your solution, configure
	  anything you like, install any applications that will need to be on all VM's of this type for your solution,
	  and save this entire setup as your own custom AMI.
	* This custom AMI can then be launched with all the configurations & installations already setup.
* AMI's are also available through the "Community AMIs" page and the "AWS Marketplace"

### Instance Types 

The key parameters of an instance type to pay attention to when launching are:
* vCPUs
* Memory (GB)
* Instance Storage
* Network Performance

* There are other parameters of lesser importance, all of which can be seen in the instance parameters table when
  launching your instance

* Instance types are grouped into families:
	* micro instances
		* very low cost - useful for low throughput purposes
	* general purpose
		* balanced mix of compute, memory and network capabilities
	* compute optimized
		* good for high performance front end servers, etc.
	* GPU
	* FPGA - ( Field Programmable Gate Arrays )
		* used to create application specific hardware accelerations
		* High CPU performance, large memory and high network performance make these the go to for solutions
		  that require massive parallel processing; data science/genomics/financial computing being some examples.
	* Memory optimized
		* lowest cost per GB of RAM than other instances
		* recommended for database applications/database components of a solution
	* Storage optimized
		* Use SSD backed instance storage, which offers high I/O thoughput.

### Instance Purchasing Options 

Different payment plans available:

* On-Demand Instances
	* launched at any time
	* flat rate per instance type
	* typically used for short term uses
* Reserved Instances
	* best applied to long term, predictable workloads (applications that you know need to be running for a set
	  period of time)
	* purchases for a set period of time for reduced cost (up to 75% reduced cost). Three options:
		1. All Upfront
			* complete payment for 1 or 3 year timeframe - highest discount.
		2. Partial Upfront
			* smaller upfront - smaller discount than All Upfront option.
		3. No Upfront
			* very small discount applied
* Scheduled Instances
	* pay for instances on a daily/weekly/monthly schedule 
	* **even if you don't use the instance, you will be charged**
	* less expensive than the On-Demand Instance, so good for recurring but predictably recurring use cases
* Spot Instances
	* Bid for unused EC2 resources.
	* Con: **Not guaranteed for a fixed period of time**
	* Pro: Can purchase large (expensive) EC2 instance types at a lower price
	* The "Spot Price" determines the price of an instance and bidding above that "gets" you the instance. If a
	  higher bid comes along while you are using the instance, **your instance will shut down**.
	  * Should only be used for tasks that can be interrupted/stopped - otherwise be prepared to continuously ensure
	    your bid price is above the spot price (either computationally or manually).
* On-Demand Capacity Reservations
	* allows you to reserve capacity (whether that is compute, memory, storage or network) within a particular
	  availability zone for any period of time.

### Tenancy 

"Tenancy" refers to the actual physical computer your VM is hosted on in the AWS data center.

* Shared Tenancy
	* your instance will be launched on any available host, most likely one that is shared with other AWS users.
	* AWS provides the security to ensure different users can't access each other's instances
	* this model is what allows "economies of scale" and makes cloud computing inexpensive.
* Dedicated Tenancy
	* Dedicated instances
		* hosted on hardware that no other AWS user can access
		* may be required by problem domain compliance requirements
		* more expensive
	* Dedicated Hosts
		* more visibility/control of the physical host than even the "Dedicated Instances" option.
		* again - may be required by problem domain compliance requirements

### User Data 

* commands that will run during the first boot cycle of the instance
* used to update software or OS'

### Storage Options

Two types:
1. Persistent Storage
	* attaching EPS (Elastic Block Storage) volumes
	* attached via AWS network - physically separated
	* can be detached from EC2 instances and maintain data 
	* data saved on EBS volumes are automatically copied to other volumes within the same availability zone for
	  backup purposes 
	* data can be encrypted and scheduled backup snapshots are possible
2. Ephemeral Storage
	* **deleted and gone forever when EC2 instance is stopped/terminated**
	* if instance is rebooted (think "continue instance use") - data is maintained
	* non-detachable

### Security

* Security group = "instance level firewall"
	* allows you to specify what traffic communicate with your instance (can be specified via IP range, protocol,
	  port range, inbound/outbound, etc.)
* Key-Pairs
	* Allows encrypted access to EC2 instances
	* Public Key = AWS keeps this to match to your private key
	* Private Key = your responsibility for safe keeping
	* **You can use the same key-pair for multiple instances** - this does mean that if your private key becomes
	  comprimised, whoever has the key would have access to all the instances associated with that key-pair.
* It is the user's responsibility to maintain and install latest OS updates & security patches released by the OS vendor
  - this is part of the shared responsibility model

## ECS - EC2 Container Service

ECS allows the user to run Docker-enabled applications packaged as containers across a cluster of EC2 instances,
**without requiring the user to manage a complex and administratively heavy cluster management system. **AWS Fargate**
manages this system for you.

Two different ECS Cluster deployement models:
1. Fargate Launch
	* the user is only required to specify CPU, memory and networking policies (in addition to having your
	  applications packaged in containers)
	* This is the option that trades lower customization for lower management overhead.
2. EC2 Launch
	* This is the option that trades higher management overhead for higher customization.
	* The user is responsible for patching and scaling instances, specifying instance types and how many
	  applications should be in a cluster.

* Monitoring of your ECS cluster and containers is provided by AWS CloudWatch
* An ECS Cluster is comprimised of multiple EC2 instances
* Security Groups, Elastic Load and Autoscaling can be applied.
* The cluster can be comprised of different EC2 instance types.
* **Clusters can only scale in a single region** (this is different from availability zones; clusters can span multiple
  zones).
* Containers can be scheduled to be deployed across the cluster.


## ECR - Elastic Container Registry

ECR provides a secure location to store and manage your docker images. This service allows developers to push, pull and
manage their library of docker images in a central and secure location

There are a few components used in ECR:

1. Registry
	* The component that hosts/stores docker images as well as create image repo's	
	* The default URL for the registry is:
	`https://<aws_account_id>.dkr.ecr.<region>.amazonaws.com`
2. Autorization Token 
	* **Before your docker client can access the registry (push & pull), it needs to be authenticated with an
	  Autorization token
	* To start the authorization process, run the following command using the AWS CLI (might need to be installed):
	`$ aws ecr get-login --region <region> --no-include-email`
	* The above command's output will be a docker login command:
	`docker login -u AWS -p <password>`
	* Authorization tokens last for 12 hours before the above process need to be performed again.
3. Repo 
	* Standard repo concept - allows grouping of docker images in whatever manner the user would like.
4. Repo Policy 
	* Repo policy's can be set up by the principal of the repo - who can then setup which actions different users
	  can perform on various repo's.
5. Image 
	* Once all the above has been completed, you/the user can push/pull docker images from your ECR.

