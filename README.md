# weather-comparison
A simple application utilizing Matplotlib to compare high and low temperatures between 2 locations.

This application utilizes Matplotlib to plot high and low temperatures to compare 2 locations. This is an extension created from exercise 16-2 of the Python Crash Course book by Eric Matthes.

Exercise 16-2 is as follows: *The temperature scales on the Sitka and Death Valley graphs reflect the different data ranges. To accurately compare the temperature range in Sitka to that of Death Valley, you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6. Then make a direct comparison between temperature ranges in Sitka and Death Valley (or any two places you want to compare).*.

I further challenged myself to add an additional file to the code (Sitka) to be able to compare both cities within the same program and plot.

The files within this repository are as follows:
`sitka_death_valley_compairson.py` - The main executable file for this program. Contains the code that reads through each files, stores the needed data in lists, and then plots them using Matplotlib.
`sitka_weather_2018.csv` - The source of data for Sitka.
`death_valley_2018_simple.csv` - The source of data for Death Valley.

**NOTE:** For the code to work as is, the data files should be added into a folder 'data' in the same directory the executable python file is stored. If this should be avoided, remove `data/` from both filenames in the Python in the file.
