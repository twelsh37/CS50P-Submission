# App-Bangers
#### Video Demo:  <URL HERE>
#### Description:

This is my final project submission for Harvard Universitys CS50P.
The application utilises an open-source application framework for building the web application. <br>
The application is frontended by a login page where only authorised users can gain access to the main application.
The login page is back-ended to the [Deta Base NoSQL database](https://www.deta.sh/), which is used to store our user credentials.<br> 
When the ur gains access to the main application Area they are presented with an opening page displaying a stock ticker for user selectable instraments, Some metric boxes for teh associated ticker symbols.<br>
There are then other selectable options available in the side bar that will allow the user to display different information.<br>

Examples of this kind of data are
* 7 Wonders of The World
* A selection of African Game Parks
* The 100 most populous cities on Earth

Below is the data for the 7 wonders of the world which will be plotted on a digital map.<br>
The locations are as follows:
#### _The 7 Wonders of the Ancient World_
| **Name**                         	| **Country** 	| **Latitude**           	| **Longitude**          	|
|------------------------------	|---------	|--------------------	|--------------------	|
| Statue of Zeus at Olympia    	| Greece  	| 37.63819915960268  	| 21.63011753949122  	|
| Temple of Artemis at Ephesus 	| Turkey  	| 37.94967735447476  	| 27.363909843917902 	|
| Mausoleum at Halicarnassus   	| Turkey  	| 37.03803297044549  	| 27.424116399008735 	|
| Colossus of Rhodes           	| Turkey  	| 36.45107354911518  	| 28.2257819413324   	|
| Hanging Gardens of Babylon   	| Iraq    	| 36.57693767402696  	| 41.869210073371086 	|
| Great Pyramid of Giza        	| Egypt   	| 29.97942034949402  	| 31.134244814303447 	|
| Lighthouse of Alexandria     	| Egypt   	| 31.214081589823174 	| 29.8855234134948   	|
Source: https://blog.batchgeo.com/seven-wonders-of-the-world-more-like-46-wonders/ <Accessed 2022-06-08>

### Design Decisions
Having decided that my project was going to be an gui app of some kind i wanted to use a sutible medium to sisplay this on. 
A Gui type interface was my first choice.

I considered the following four libraries for the GUI.
* Kivy - https://github.com/kivy/kivy - I discarded this as it seemed more
  focused on multi-touch devices.
* Tkinter - https://docs.python.org/3/library/tkinter.html - The grandad of
  the Python GUI frameworks. This turned out to be hard to test with pytest
  so I discounted it.
* Dash/Plotly - https://plotly.com/dash/ - A modern day gui tool used to
  build web based applications and dashboards. Integrates well with plotly and I haveused it before
* Streamlit - https://streamlit.io - Open source application Framework for developing web apps. 

**Decision** - Select Dash/Plotly to create our final project.

### **Project files**
project.py - Main application file that runs our dashboard.<br>
test_project.py - Pytest file containing our unit tests.<br>
README.md - The project readme file.<br>
requirements.txt - list of our pip installable libraries used in this project.<br>
7wonders.csv - File containing our 7 wonders of the ancient world data in a csv file.<br>
africanparks.csv - File containing co ordinates of a selection of African national Parks, lakes and forests.<br>
worldcities.csv - File containint the 100 most populous cities in the world.