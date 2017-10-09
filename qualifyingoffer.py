#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by Josh Davis
# A program that determines monetary value of an upcoming qualifying offer in the MLB

import requests
from lxml import html
import matplotlib.pyplot as plt
import numpy

# This section of code below will read in the HTML data from the webpage
# I used the Requests module to quickly read in information straight from
# the provided URL
webpage = requests.get("https://questionnaire-148920.appspot.com/swe/", stream=True)
# Below, I used the fromstring method from the lxml library to parse the HTML
# code of the webpage and store it as an html element in 'tree'
# Source: https://stackoverflow.com/questions/16870648/python-read-website-data-line-by-line-when-available
tree = html.fromstring(webpage.content)
# Now the HTML code from the webpage is stored in a tree-like structure
# in our tree variable. We will now parse this looking for very specific information
# using the xpath method
# Source: http://docs.python-guide.org/en/latest/scenarios/scrape/
salaries = tree.xpath('//td[@class="player-salary"]/text()')
players = tree.xpath('//td[@class="player-name"]/text()')
# A quick inspection of the HTML code shows that all player salaries
# are stored inside td elements with the title "player-salary". This section
# of code stores the element found at every "player-salary" title as a single item in a list.
# Now I have a list called salaries that contains all of the salary information
# for all of the players listed on the webpage. It's important to note that
# the elements in the salary list are an lxml type called 'ElementUnicodeResult'

valid_salaries = []
valid_players = []
for sal, play in zip(salaries, players):
    sal = str(sal) # cast the objects in the salaries list as strings
    play = str(play)
    sal = sal.replace('$', '') # gets rid of any '$' or ',' chars
    sal = sal.replace(',','')
    if sal.isdigit(): # we are only interested in the strings that contain just digits (some players have 'no salary data')
        valid_salaries.append(int(sal)) # cast the salary as an int and put it in a new list
        valid_players.append(play)
# I am only using the player name data and this dictionary to give anyone viewing this
# this data a better idea of the players with salaries similar to the Q.O.
dictionary = dict(zip(valid_players, valid_salaries))
valid_salaries = sorted(valid_salaries, key=int, reverse=True) # sort the salaries (descending order)
counter = 0
sum = 0
while counter < 125: # add up the first 125 highest salaries in the league
    sum = sum + valid_salaries[counter]
    counter = counter+1

qualifying_offer = sum / 125 # the qualifying offer is the average of the 125 highest paid salaries
# to contextualize our number, we will use our dictionary to find players
# with salaries near the qualifying offer (within $1,000,000)
close_players = []
# using closest_index here so that I can graph the Q.O. near the player with the salary
# closest to the Q.O.
closest_index = 0
closest_val = 1000000
for w in sorted(dictionary, key=dictionary.get, reverse=True):
# Source: https://stackoverflow.com/questions/613183/how-to-sort-a-dictionary-by-value
  if abs(qualifying_offer - dictionary[w]) <= 1000000:
      close_players.append(w)
      if (qualifying_offer - dictionary[w]) < closest_val:
          closest_val = qualifying_offer - dictionary[w]

z = 0  
while z < 125:
    if qualifying_offer - valid_salaries[z] == closest_val:
        closest_index = z
    z = z+1
# now I will format output that displays the information meaningfully
# all of the formatting techniques were learned using the following source
# Source: https://matplotlib.org/users/pyplot_tutorial.html
# I use numpy here so that I can display the data in millions of dollars more easily
# Source: https://stackoverflow.com/questions/8244915/how-do-you-divide-each-element-in-a-list-by-an-int
qual_string = '${:,.2f}'.format(qualifying_offer) #convert qualifying offer to a monetary string
myArray = numpy.array(valid_salaries)
myInt = 1000000
newArray = myArray/myInt
x = range(125)
plt.plot(x, newArray[:125], 'ro', closest_index+1, qualifying_offer/1000000, 'g^')
plt.ylabel('Yearly Salary (in millions of dollars)')
plt.xlabel('125 highest paid players')
plt.title('Upcoming Qualifying Offer in the MLB')
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,40))
plt.text(23, 36, 'Qualifying Offer = '+qual_string, fontsize=14, color='green')
plt.text(75, 33, 'Players with similar contracts: ',fontsize=8)
i = 0
while i < len(close_players):
    plt.text(75, 33-(i+1+.3), close_players[i] ,fontsize=6.5)
    i = i+1


plt.annotate('Qualifying Offer', xy=(closest_index+1, qualifying_offer/1000000), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.show()


