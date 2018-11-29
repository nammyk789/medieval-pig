#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:05:58 2018

@author: namratakasaraneni

medieval take on the game of pig
includes choice for player names, choice for number of die sides
warning: grand variations on homework assignment

PLEASE DO NOT READ FURTHER UNTIL YOU PLAY THE GAME
"""
import random

def roll_die(sides):
#creates an input-sided die and rolls
    
    roll = random.randrange(1, sides)
    return roll


def take_turn(die_sides):
    ''' 
    lets each player take a turn at the game of pig until a player
    inputs that they no longer want to keep rolling
    
    while the player elects to keep rolling, turn points are added 
    to the players turn score each roll unless the player rolls a one
    
    parameters: how many sides the dice has
    '''
    
    turn_points = 0
    keep_rolling = "potatus et molassus"
  
    while keep_rolling != "NAY":
        roll = roll_die(die_sides)
        print("You rolled a", roll)
        
        if roll == 1:
            turn_points = 0
            print("\nAlas! The dragon hath burned you. Your round is over.")
            return 0
       
        else:
            turn_points = turn_points + roll
            print("Your Turn Points are now", str(turn_points) + ".")
            keep_rolling = input("Continue rolling? (YEA/NAY) ")
        
    return turn_points


def show_instructions():
    #prints game instructions
    
    print("\nWelcome, brave knights, to Ye Old Cyber Tavern. Tonight our " +
          "featured game is the thrilling and high stakes Game of Dragon. " +
          "Are ye greedy or humble, hot-blooded or cunning thinkers? " +
          "Beware, for many knights before ye have had their deepest " +
          "and darkest qualities revealed by this bone-chilling and " +
          "blood-thrilling game. Only the most courageous in the " +
          "Cyber Kingdom are fit. Players beware. Perhaps those of you with " +
          "weaker stomachs would do better to grab a tankard of cyber mead " +
          "and let the real warriors show you how it's done.")
    print('')
    print("For those of you that have decided to continue on to the " +
          "instructions, congratulations! You have shown true chivalry. " +
          "The Game of Dragon is pretty simple, for I know that what " +
          "you lack in brains you make up for in brawn. Each of you will " +
          "take turns fighting the Fearsome Fire Dragon.")
    print('')
    print("On each round, you may roll the die as many times as you " +
          "please in order to accrue Chivalry Points. BUT BEWARE! " +
          "For if you roll a 1, the Fearsome Fire Dragon will burn you " +
          "and you will lose all of your Chivalry and your round.")
    print('\n\n') 
    print("I have saved the best for last. The knight that first accrues " +
          "at least 60 points defeats the dragon and gets access to " +
          "its hoard of treasure and the busty/hunky prince/princess/royal " +
          "that it has kidnapped.")
          
    print("\nSo, do ye have the chivalry, the guts, and the skills to take " +
          "the dragon on and compete for its hoard?")
    
    
def bsm(name1, name2):
    '''
    a game of rock paper scissors with more medieval names
    (boulder = rock, shield = paper, mace = scissors)
    
    parameters: names of the players
    
    assumes that both players input proper answers. repeats game if
    players tie
    '''
    
    knight1 = input(name1 + ": BOULDER, SHIELD, or MACE? ")
    knight2 = input(name2 + ": BOULDER, SHIELD, or MACE? ")
    
    while knight1 == knight2:
        print("Try again.")
        knight1 = input(name1 + ": BOULDER, SHIELD, or MACE? ")
        knight2 = input(name2 + ": BOULDER, SHIELD, or MACE? ")
    
    if knight1 == "BOULDER" and knight2 == "MACE" or knight1 == "MACE" and \
    knight2 == "SHIELD" or knight1 == "SHIELD" and knight2 == "BOULDER":
        return name1
    else:
        return name2


def bsm_instructions():
    #prints instructions for rock paper scissors storyline
    
    print('Though knights must be chivalrous, the also must be cunning. ' +
          'You have successfully defeated the dragon using wit, bravery, and' +
         ' a little dose of Lady Luck. Now you must use strategy, psychology,' +
          ' and integrity in order to triumph once and for all.' + 
          '\n\nYou will therefore partake in the game Boulder, Shield, Mace,' +
          ' which is coincidentally played exactly like rock, paper, scissors ' +
          'but with much cooler names. Both players must shout out ' +
          'their choice at the same time and then input their answers ' +
          'into the Cyber Contest. If the player with the most points wins, ' +
          'they get to be added to the Hall of Fame. If the losing player ' +
          "with triumphs, they get an addition of 25% of the winner's " +
         'chivalry points.\n\nBegin.')


def game_code(die_sides):
    '''
    the upgraded game of pig (renamed game of dragons)
    
    while both player's game points are under 60,  the function keeps calling
    take_turn() for each player
    
    if the final score is uneven, the function calls bsm() for a final round
    if the player with fewer points wins bsm() they get 25% of the winning
    player's points added to their score. if the player with higher points wins
    bsm() their name gets appended to the list Hall_Of_Fame. in either case,
    the player with the most points after bsm() wins the game
    
    if the final score is a tie. each possible outcome has its own slightly 
    variated script.
    
    parameters: die_sides
    inputs: names of players
    '''
    
    k1_points = 0
    k2_points = 0
    
    k1_name = input("Knight 1, what name willst thou choose? ")
    k2_name = input("Knight 2, what name dost thou want? ")
    
    while k1_points <= 60 and k2_points <= 60:  # cannot find why but there
        print("\nCHIVALRY: \n", k1_name + ":", k1_points, \
              k2_name + ":", k2_points)  # is a bug so that if 
                                        # k2_points >= 60 game continues
                                        # for two more rounds
        input(k1_name + ", hit enter to slay." )
        turn_points = take_turn(die_sides)
        k1_points = k1_points + turn_points
            
        print("CHIVALRY: \n", k1_name + ":", k1_points, \
              k2_name + ":", k2_points)
        
        input(k2_name + ", hit enter to slay." ) 
        turn_points = take_turn(die_sides)  
        k2_points = k2_points + turn_points
                                            
                                            
    if k1_points != k2_points:      #uneven final score storyline
        winner_points = max(k1_points, k2_points)
        if winner_points == k1_points:
            winner = k1_name
            loser = k2_name
            loser_points = k1_points
        else:
            winner = k2_name
            loser = k1_name
            loser_points = k1_points
        
        print("")
        print("CHIVALRY: \n", k1_name + ":", k1_points, \
              k2_name + ":", k2_points)
       
        print("\nCongratulations,", winner + ". You have successfully " \
              "slayed the--")   
        print('\n"BUT WAIT!" An wizened old man with a very long beard' +
              ' rises from the dim corner of the bar. Everyone hushes. ' +
              '''Clearly this man is very wise and respected. "Yeh've ''' + 
              'forgotten the most important part," cries the old wizard. ' +
             '"When the points are uneven, they have to play the game of ' +
              'Boulder, Shield, Mace!"')
        print('''\n"By jove, you're right!" said the barkeep, looking''' +
              ' flustered. Every knight wishing to win the hoard must' +
              ' end their battle with Boulder, Shield, Mace."')
        print('')
        
        bsm_instructions()
        result = bsm(k1_name, k2_name)
        
    
        if result == winner:
            Hall_Of_Fame = winner
            print("\n\nCongratulations,", winner + ". You have " \
              "successfully slayed the Fearsome Fire Dragon " \
              "and brought glory to your kingdom. You are now part of "\
              "the Cyber Tavern's Hall of Fame. \n\n" + \
              loser + ", would you like a Cyber Mead to nurse "\
              "your injuries?")
            print('''
                  HALL OF FAME:''')
            print("Sir Cadogan \n\nMerlin \n\nBarack Obama", \
                  "\n\nDumbledore \n\nLink \n\nKanye West\n\n" +
                  Hall_Of_Fame)
        
        elif result == loser:
            loser_points = loser_points + 1 / 4 * winner_points
            if loser_points > winner_points:
                print("\nAnd in a surprising turn of events that has taken",\
                 "the land by storm,",loser, \
                 "has won the game! Congratulations,", loser + "." \
                 "You have brought honor to your kingdom and redeemed you " \
                 "good name. But we still expect you to buy", winner, "a "\
                 "cyber drink for the sake of sportsmanship. Cheers!")
            elif loser_points < winner_points:
                print("\nCongratulations,", winner + "! Although", loser, \
                     "won Boulder, Shield, Mace, you still triumphed",
                     "in the end. Have a cyber drink and celebrate your", \
                     "victory!")
            else:
                print("\nAlthough", winner, "beat the Fearsome Fire Dragon", \
                      loser, "bested", winner, "in cunning and was the", \
                      "victor of Boulder, Shield, Mace and tied overall", \
                      "with", winner + ". Two knights are truly better", \
                      "than one.")
    else:
        print("It took both of your effort to destroy the Fearsome " \
              "Fire Dragon. Would you like to split the tab, like " \
              "you'll be splitting your newfound hoard?")

def play_game():
    '''
    runs the game of dragons. prints the instructions function
    and gives the players choice to either begin the game
    or back out. 
    
    parameters: none
    inputs: choice to play or not play
    '''
    show_instructions()
    begin_game = input("YEA or NAY? ")
   
    if begin_game == "YEA":
        die_sides = int(input("How many sides would you like your die" \
              " to have? Fewer sides means more bravery. "))
        game_code(die_sides)
    else:
        print("BEGONE, YE SCURVY COWARDS!")
    

def test():
    # i used this to test functions and python modules  
    
    for i in range(20):
        print(roll_die(10))
        
    points = take_turn()
    print("Returned points:", points)
    
    show_instructions()
    
    play_game()
    
    result = bsm("tom", "jerry")
    print(result)
    
    bsm_instructions()
    
    list = []
    list.append(7)
    print(list)


def main():
    play_game()

main()