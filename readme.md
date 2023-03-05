# WELCOME   
Thank you for showing interest in our project, Signo. About 70 million people in this world are unable to communicate with us properly due to their inability to speak or hear. What we sought to create was an innovative product that would be accessible to all and would help them attend and communicate within a virtual meeting with ease. Our product is based on a virtual camera that runs locally on the user's machine and allows them to use the said virtual camera as the main video source on any platform that they wish to use. It uses machine learning-based technology to identify the hand gestures of the user and converts them to subtitles for everyone to read.

# The problem statement
About 70 million people in this world have speech and hearing impairement, this makes it really tough for them to communicate with their loved ones and coworkers. A platform that makes communication easier for them over the internet without the other person knowing sign language would help them out in their everyday lives.

# The solution
A software that converts ASL to plain english and displays it as subtitles on your everyday confrence apps like G-Meet and zoom would make it very easy for people with speech impairement to talk to everyone, without worrying about the other person not knowing sign language. Featues like adding your own slangs and phrases for signs, and a section to learn sign language makes it although more useful to use and acts as the complete suite of online communication platform for the speech impaired.

# Timeline:

The initial stage of this project might be considered as the ideation phase, as not a lot of work had been done on the project. We had a clear idea of the machine learning models and the type of data to use in order to implement it. We had a very basic RNN model trained with 5 words 30 videos each.

Now the model is trained with 15 classes with 60 videos of each class and 30 frames per video, with 126 datapoints in every frame and 3 coordinates per data point. we created the dataset over the course of this hackathon and it's entirely trained by us. Now the model can work on any conferencing apps by creating a virtual camera using pyvirtual cam. We optimised the entire software, to use lesser data points an reduce the drop in the frame rate when used in the browser.



# GETTING STARTED!

## Clone the repository
fork the repository and clone it by typing 
``` git clone <the url of your cloned repo>``` in your favourite editor.

## INSTALL OBS  
This project uses the open-source drivers provided by OBS studio. Hence we request you to download OBS studio from [here](https://obsproject.com/download).
After downloading the software, you are required to run the virtual camera once, this will make sure you have everything set to use Signo.

## install all the libraries
run ``` pip install -r requirements.txt ``` to get all the important dependencies.

## running the program
Start the program by running ```main.py``` and wait for the program to start completely.

## contribution guildlines
* Fork the repo
* Create a new branch named after the feature or the branch
* Please be respectful to the people of the community
* You can raise any queries and problems you are facing on the issues tab
* All pull requests are welcomed. Please give as much details possible on your PR.

