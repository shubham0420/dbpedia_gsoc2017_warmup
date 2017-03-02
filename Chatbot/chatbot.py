# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 05:54:10 2017

@author: Shubham Sharma
@email : sharma.shubham6522@gmail.com
"""

'''
This is a basic code for chat bot which convert numeric character to roman characters.
This chatbot is somewhat tricky because it only converts the number which you tell it to convert.
'''

from collections import OrderedDict
import string

def correcting_words(sentence):
    '''
    This function replaces the n't ending word with 'word stem + not'
    @sentence : input sentence
    return : the sentence with 'not' if n't or not was present in sentence.
    '''
    sentence  = sentence.split(' ')
    words = []
    for word in sentence:
        if word[-2:] == "n't":
            words.append(word[:-3] + ' ' + 'not')
        else:
            words.append(word)
    sentence =' '.join(words)
    return sentence

stopwords = string.punctuation
def preprocessing(string):
    '''
    This function removes the stopwords from the word and calls correcting word
    @string : The query given by user
    return : cleaned sentence
    '''
    string = correcting_words(string)
    words = string.split(' ')
    words = [w for w in words if w not in stopwords]
    words = ' '.join(words)
    return words
    
def _getRomanDict():
    '''
    This function contains ordered dictionary containing the roman value of few neumeric characters.
    return: IntToRoman : OrderedDict of integer
    '''
    from collections import OrderedDict
    IntToRoman = OrderedDict()
    IntToRoman[1000] = "M"
    IntToRoman[900] = "CM"
    IntToRoman[500] = "D"
    IntToRoman[400] = "CD"
    IntToRoman[100] = "C"
    IntToRoman[90] = "XC"
    IntToRoman[50] = "L"
    IntToRoman[40] = "XL"
    IntToRoman[10] = "X"
    IntToRoman[9] = "IX"
    IntToRoman[5] = "V"
    IntToRoman[4] = "IV"
    IntToRoman[1] = "I"

    return IntToRoman   
    
_IntToRomanOrder = _getRomanDict() # called once on import

def roman_num( iNum ):
    '''
    This function converts number from decimal to roman
    iNum: input number
    return : Roman number
    '''
    lRomanNumerals = []
    for iKey in _IntToRomanOrder:
        if iKey > iNum: continue
        iQuotient = iNum // iKey
        if not iQuotient: continue
        lRomanNumerals.append( _IntToRomanOrder[ iKey ] * iQuotient )
        iNum -= ( iKey * iQuotient )
        if not iNum: break

    return ''.join( lRomanNumerals )


def convert_to_roman(query):
    '''
    This function calls preprocessing and then send the numbers to get the roman output.
    @query : input given by user.
    return: numbers converted to roman
    '''
    query = preprocessing(query)
    query = query.split(' ')
    i = 0
    output = []
    flag = 0
    while(i<len(query)):
        if(query[i] == 'not'):
            flag = 1
        elif(query[i].isdigit()):
            if(flag == 1 or flag == 2):
                flag == 2
            else:
                output.append(roman_num(int(query[i])))
        elif(query[i] == 'and'):
            pass
        else:
            flag = 0
        i +=1
    return ' '.join(output)

if __name__=="__main__":
    print("""    *************************************************************
    Simple Chatbot which translates arabic number to roman numbers
    *************************************************************""")
    while(1):
        print("Enter the query. Press 'over' to exit")
        query = raw_input()
        if(query == 'over'):
            break
        output = convert_to_roman(query)
        if len(output)> 0:
            print(output)
        else:
            print("No output")