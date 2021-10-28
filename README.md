# Graphical User Interface for determination attitude parameters of a satellite

## Main author: Geovani Augusto Xavier Ribeiro
## Coordinators: William Reis Silva & Katia Cristiane Gandolpho Candioto

### University of São Paulo & University of Brasília

In this project, the user can manipulate some attitude parameters with a Graphical User Interface (GUI).

## Prerequisites
- numpy
- tkinter

## Brief explanation about the project

From the development of several attitude parameters, it was possible that the description of the movement rotation of the satellite was done in a simple way. In this context, the development of an interface graphic for analyzing the attitude coordinates of a satellite becomes important for the description of the kinematic characteristics of a rigid body of the satellite, as it will allow a quick analysis made by the user.

The present work aims to analyze and describe the attitude coordinates of a satellite through of an interactive graphical user interface. Through the use of Python software, a graphical interface that, based on initial information provided by the user, would provide results for Euler angles, principal rotation vector, classical Rodrigues parameters and modified Rodrigues parameters. In this way, the algorithm through information provided by the user the main attitude parameters were generated.

## How to use

For the development of the graphical interface, the attitude matrix (Direction Cosine Matrix - DCM) from which, based on information that the user has, it is in fact to do all the other coordinate changes with algebraic manipulations. In this work, a two-step algorithm for manipulating the data that the user has.

In the first step, the user selects the attitude parameter he has and is directed to another window which inside the data.

In the second step, the main satellite attitude parameters are calculated providing data for the Euler angles, principal rotation vector, classic Rodrigues parameters and modified Rodrigues parameters.

## License
The __attitude-parameters__ library is released and distributed on github as an open source package under the MIT license.
