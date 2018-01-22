## NWEA code challenge submission

This repository is my solution for the challenge found in [this repository](https://github.com/nwea-techops/blogpostapi)

### Deployment process

I would supply an Ansible file to provision the application to enough VM's to handle the specified load.  I would ensure an SSH deamon was baked into the image of the VM's to accept the Ansible commands.
The Ansible file would do the following
* Gather the facts of the particular machine
* Check if the system Python installed is 3.6
  * If not it would install Python 3.6
* Check for pip3
  * Install pip3 if needed.
* Check for Git
  * Install Git if needed.
  * Clone the repository
* If Git was already installed this means the repository has been cloned so a pull request will suffice.
* Install the required Python libraries with pip3.
  * pip3 Install requests
  * pip3 Install pyramid.
  * pip3 Install sqlite3
* Start the application by running *python3 pyramid_server.py*

### Different approaches on deployment process based on existing infrastructure

The way I would deploy this solution would be based on the existing infastructure for the company or team or porject.  I would ensure I adapt the deployment to fit both the performance and cost needs as well as keeping the entire firm on the technological road map as much as possible.  

For example if the entire company used Docker swarms I would deploy this application in the same way to take advantage of the knowledge in the firm to do this as quickly as and as easily as possible.  However if the main way of hosting software was to have VM's and the sizing of the VM's was done to ensure adequate overhead for any peaks in load then I would follow this deployment pattern.  In this case I would have the VM's behind a load balancer such as an F5 and then add or subtrac VM's from the cluster as needed to accomodate the changes in load.  

Addressing the latter example of VM's being provisioned either on premises with cloud VM's or a combination of both I would use Ansible to push out the needed packages to the desired VM's.  This would include the a check for the correct version of Python, in this case Python 3.6, pip3, and then pip install the rquired libraries by the particular application.  I would use either GitHub or rsync to pull down any revisions to the application and then 

Onto the former deployment strategy of using Docker to virtualize the application I would again use Ansible but I would first build a Docker file to hold most of the configuration settings and build the Docker image to pull down image from the chosen Docker repository.  In this use case I would use the load balancing in Docker Swarm and forgo using an F5 or other load balancer until such time as the load the for the application became such that the amount of VM's in the Docker swarm and overall traffic were creating a bottleneck in the communication channel between the swarm nodes (worker and master).  For persistent data the database file would be stored outside of the Docker container.  I would say sharding is beyond the scope of this code challenge (I adhere to the project specification and avoid scope creep).

If NWEA is interested in pursuing my employment further I will be happy to write the corresponding Ansible playbooks to deploy the application to a single VM.  