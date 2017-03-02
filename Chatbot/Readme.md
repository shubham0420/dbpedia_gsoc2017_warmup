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
III IV

convert 6 and 5 but not 3 and 4.  
VI V

#Idea

I saw that every one is making regular bot which converts only numbers but donot take in consideration the sentence. So, I tried to add some meaning to sentence.
If not is present before a number then most probably the user donot want to convert that number.
I did some cleaning to get 'not' from the sentence Eg. don't :- do not
not can also be present before convert and translate.
