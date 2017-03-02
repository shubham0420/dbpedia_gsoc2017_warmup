#DBpedia_chatbot_warmup  
This repository contains the warm up task for the Google Summer of Code 2017 DBpedia Chatbot  

#Usage

run command :- python chatbot.py  
Now follow the instruction in console.

#Examples

Donot translate 3 in roman  
No output

Convert 3 but not 5.  
III

Convert 3 and 5  
III  V

convert 6 and 5 but not 3 and 4.  
VI  V

#Idea

Task was to make a regular bot which converts only numbers but donot take in consideration the sentence. But, I tried to add some additional functionality to simple bot. I tried to add sentiment to sentence.  
### Main Idea
If negetive words are present before number then  most probably the user donot want to convert that number.  
I did some cleaning to get 'not' from the sentence Eg. don't :- do not.  
Also not can also be present before convert and translate.
