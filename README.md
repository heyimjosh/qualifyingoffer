# Qualifying Offer Program

This is a Python program that allows the user to calculate the Upcoming Qualifying Offer value in the MLB. The program parses through a webpage that contains salary data for current MLB players in order to calculate the qualifying offer, which is equal to the mean of the top 125 highest salaries in the league. The program displays this information to the user in graph form, which allows the user to put the qualifying offer value in context visually with the rest of the league’s highest paid players. In addition, the program displays the names of players who have similar salaries to the qualifying offer in order to contextualize the figure even more. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
(Source: https://stackoverflow.com/questions/13270877/how-to-manually-install-a-pypi-module-without-pip-easy-install)

1.) You must have the latest version python3 downloaded on your machine. The download link for the latest version of python3 can be found at https://www.python.org/downloads/. Download the qualifyingoffer.py file onto your machine.

2.) I used 4 different packages in this program that must be downloaded. They are ‘requests’, ‘lxml’, ‘matplotlib’, and ‘numpy’.

4.) If you have a Mac, feel free to use pip in Terminal to install the packages. The command ‘pip install package_name’ should work just fine. If you’re using Windows, try the command ‘python -m pip install package_name’. This may not work for some packages on Windows (specifically lxml) depending on your machine. If you are using the latest version of Python, all of the libraries should download without an issue from the command line using the aforementioned commands.

3.) Just to be safe, here are the steps to take if you must download the packages manually:

	- Download the packages from the link above (unzip if need be)
	- cd into the directory containing setup.py
	- type ‘python setup.py install’ into the command line


## Deployment

Once you have all of the necessary files and packages installed, you should be able to just type this into the command line (make sure you are in the same directory that the qualifyingoffer.py file is saved in):

	python qualifyingoffer.py

A graph should appear on your screen.

## Built With

* [Spyder](https://www.anaconda.com/download/#macos) - The IDE used


## Authors

Josh Davis


## Acknowledgments

* Url to the salary data was provided by the Phillies