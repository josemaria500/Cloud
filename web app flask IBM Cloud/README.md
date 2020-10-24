# Simple web app with Flask in IBM Cloud

This is a simple example of web app using Flask and delivery in IBM Cloud Foundry. 
In this project, I am using an IBM Cloud Lite account.


## Files explanation
| File | Description |
| ------ | ------ |
| runtime.txt | Python version required to run on IBM Cloud |
| requirements.txt | The packages and versions that the application requires to run the app |
| manifest.yml | Displays the required application details, in this case, name of the app and memory allocated in th IBM Cloud|
| Procfile | Reference to the main Python program to run the application |
| `hello.py`| Python program written using Flask |
 
 ## Deploy the application to IBM Cloud Foundry
 
 Using IBM Cloud CLI log in to IBM Cloud: 
 
 ```sh
ibmcloud login
```

If appear:
>Grupo de recursos:          No se ha establecido ningún grupo como destino, utilice 'ibmcloud target -g RESOURCE_GROUP'

then:

 ```sh
ibmcloud target -g <resource_group>
```

Now we select as target Cloud Foundry service:
 ```sh
ibmcloud target --cf
```
Before running the next command,  we must be **in the folder of our app**:
 ```sh
ibmcloud cf push
```

If the following error message appears after executing the last command, a possible solution is to rename the application in the "manifest.yml" file.
>The app cannot be mapped to route webappflask.eu-gb.mybluemix.net because the route exists in a different space.

Finally, in the screen appears:
 
  ```sh
Waiting for app to start...

name:              webappflask
requested state:   started
routes:            webappflask.eu-gb.mybluemix.net
last uploaded:     Fri 23 Oct 21:48:19 CEST 2020
stack:             cflinuxfs3
buildpacks:        python

type:            web
instances:       1/1
memory usage:    64M
start command:   python hello.py
     state          since               cpu     memory        disk           details
#0   running   2020-10-23T19:48:44Z   0.0%   40K of 64M   183.1M of 1G
 ```
 
Now, you can see the web app [hello.py](https://webappflask.eu-gb.mybluemix.net) or in the URL:
 ```sh
<name app>.<selected IBM Cloud Foundry service region>.mybluemix.net
  ```
