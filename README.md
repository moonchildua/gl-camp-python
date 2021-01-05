##This repository includes python script that based on python 3.8.5
##The docker image of the script you can find below

The python script collects and prints CPU or Memory information about Linux OS to console.

The script accepts a single parameter cpu or mem and outputs relevant metrics


##Requirements
- python3
- pip
- psutil
- loguru

##Usage
1. Clone repo git@github.com:moonchildua/gl-camp-python.git
2. Make executable `chmod +x python3-package.sh`
3. `/python3-package.sh`
4. `python3 metrics.py mem(or cpu)` 


##Examples:
`$ python3 metrics.py cpu`<br />
system.cpu.idle 26024.38<br />
system.cpu.user 14430.91<br />
system.cpu.guest 0.0<br />
system.cpu.iowait 83.7<br />
system.cpu.stolen 0.0<br />
system.cpu.system 4277.<br />

`$ python3 metrics.py mem`<br />
virtual total 33569067008<br />
virtual used 8036671488<br />
virtual free 2804436992<br />
virtual shared 1528705024<br />
swap total 1023406080<br />
swap used 0<br />
swap free 1023406080<br />


#Docker

Please install docker before run script in container.

Docker image you can find follow the [link](https://hub.docker.com/repository/docker/moonchild/gl-camp-python)

##Usage
Passing command to the container for execution
You can pass the command to the container from the command line:

`docker run -t --rm moonchild/gl-camp-python:tagname cpu`<br />
`docker run -t --rm moonchild/gl-camp-python:tagname mem`
