#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import os

# Making sure Python can find the other files
src_path = os.getcwd() + '/src' # Path = Current Directory/src
sys.path.insert(0, src_path)
from web_list_generator import *
from wordlist_manipulation import * # Import code from src/wordlist_manipulation.py

def colorWord(word, color):
	# Gives a word a nice color!
	default_color = bcolors.OKBLUE
	return Colors[color] + word + default_color

def printBanner():
	banner = bcolors.HEADER + """   __    __    ____  ____  _   _
  /__\  (  )  ( ___)(  _ \( )_( )
 /(__)\  )(__  )__)  )___/ ) _ (
(__)(__)(____)(____)(__)  (_) (_)
"""
	print(banner)

print(signs.STAR + " Welcome to " + colorWord("Aleph",0) + "!\n    The one word wordlist generator.")
printBanner()

def printHelp():
	# Prints out the help info
	print(signs.HELP + " Usage : python {} ".format(colorWord(sys.argv[0], 0))+ "<" + colorWord("keyword", 0)+ "> " + colorWord("--simple", 0) + "/" + colorWord("--normal", 0) + "/" + colorWord("--advanced", 0) )
  # [h] Usage : python Aleph.py <keyword> --simple/--normal/--advanced

def createWordlist(manipulator, mode):
	# Creates the wordlist
	if (mode == "simple"):
		manipulator.simpleManipulation()
	elif (mode == "normal"):
		manipulator.normalManipulation()
	elif (mode == "advanced"):
		manipulator.advancedManipulation()


if (len(sys.argv) < 3): # 2 Arguments required, word/url and mode (script name treated as argument 0)
	printHelp()
	exit(0)

keyword = sys.argv[1]
keywrds = keyword.split(',')
if (len(keywrds) > 1): # This tool isn't meant for multiple keywords.
	print("[+] Please use a different tool..")
	exit(0)

wordlist = []
keyword = keyword.replace(" ", "")

isurl = re.search(r'https?://', keyword) # Checking if user input is a URL
if (isurl is not None):
	# If it indeed is a URL the WebListGenerator will spider for keywords which
	# are then manipulated by the WordlistManipulator.
	max_results = int(StandardFunc.readFile()[2])
	if (sys.argv[2] == '--simple'):
		generator = WebListGenerator(sys.argv[1], 5, 12)
		manipulator = WordlistManipulator(generator.GetList(max_results), True)
		createWordlist(manipulator, "simple")
	elif (sys.argv[2] == '--normal'):
		generator = WebListGenerator(sys.argv[1], 5, 12)
		manipulator = WordlistManipulator(generator.GetList(max_results), True)
		createWordlist(manipulator, "normal")
	elif (sys.argv[2] == '--advanced'):
		generator = WebListGenerator(sys.argv[1], 5, 12)
		manipulator = WordlistManipulator(generator.GetList(max_results), True)
		createWordlist(manipulator, "advanced")

elif (isurl is None):
	# If it's just a regular keyword
	wordlist.append(keyword)
	manipulator = WordlistManipulator(wordlist, False)

	if (sys.argv[2] == '--simple'):
		createWordlist(manipulator, "simple")
	elif (sys.argv[2] == '--normal'):
		createWordlist(manipulator, "normal")
	elif (sys.argv[2] == '--advanced'):
		createWordlist(manipulator, "advanced")

else:
	printHelp()
