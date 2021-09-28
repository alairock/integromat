# Integromat Api Wrapper
This is a python integromat wrapper. I am currently only supporting the Apps api's, as the Organizations and Scenarios api's are not fully supported by Integromat at the time of this writing. 

# Integromat deploy!
There is also a deploy command that you can use to deploy to integromat directly from the command line and a VERSION CONTROLLLED REPOSITORY. 

This is a big deal, since integromat does not offer a way to version control their apps. I will document this soon. 

### Progress
This project is currently in progress and is missing many endpoints. Feel free to submit a merge request to add endpoints.

#### Basic
- [X] GET Get user information

#### Apps
- [X] POST Create a new app
- [X] GET Get list of apps
- [ ] PUT Change app icon
- [ ] GET Get app icon
- [ ] GET Get app details
- [ ] PUT Change app details
- [ ] GET Get app common data
- [X] PUT Change app common data
- [ ] GET Get app docs
- [ ] PUT Change app docs
- [ ] GET Get app section
- [ ] PUT Change app section
- [ ] POST Publish app
- [ ] POST Privatize app
- [X] DEL Delete app

#### Modules
- [X] POST Create a new module
- [X] GET Get list of modules
- [ ] GET Get module details
- [ ] PUT Change module details
- [ ] PUT Change module section
- - [X] communications (api)
- - [X] parameters (static parameters)
- - [X] expect (mappable parameters)
- - [X] interface 
- - [X] samples
- - [X] scope
- [ ] GET Get module section
- [ ] PUT Change module parameters
- [ ] POST Publish module
- [ ] POST Privatize module
- [ ] DEL Delete module

#### RPCs
- [X] POST Create a new RPC
- [X] GET Get list of RPCs
- [ ] GET Get RPC details
- [ ] GET Get RPC section
- [X] PUT Change RPC section
- [X] PUT Change RPC parameters
- [ ] DEL Delete RPC


#### Functions
- [X] POST Create a new function
- [X] GET Get list of functions
- [ ] GET Get function details
- [ ] GET Get function code
- [X] PUT Change function code
- [ ] DEL Delete function

#### Connections
- [X] GET Get list of connections
- [X] POST Create a new connection
- [ ] GET Get connection details
- [ ] GET Get connection common data
- [X] PUT Change connection common data
- [X] PUT Change connection section
- [ ] GET Get connection section
- [X] PUT Change connection parameters
- [ ] DEL Delete connection

#### Webhooks
- [X] POST Create a new webhook
- [X] GET Get list of webhooks
- [ ] GET Get webhook details
- [X] PUT Change webhook section
- [ ] GET Get webhook section
- [X] PUT Change webhook parameters
- [ ] DEL Delete webhook
