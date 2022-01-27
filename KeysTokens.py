import os
import sys

API_FILE_TO_ACCESS = 'API.txt'
ACCESS_FILE_TO_ACCESS = 'ACCESS.txt'
API_TEXT_TO_WRITE = "Replace the next line with the consumer key!\nReplace me with consumer key!\nReplace the next " \
                    "line with consumer secret!\nReplace me with consumer secret! "
ACCESS_TEXT_TO_WRITE = "Replace the next line with the access key!\nReplace me with access key!\nReplace the next " \
                       "line with access secret!\nReplace me with access secret! "
TWITTER_DISCORD_FOLLOW_LIST = "Twitter/Discord.txt"
global fileEmpty


# If the file exists, do nothing. If it doesn't catch the error resulting from no file found and create it!
def check_files():
    global fileEmpty
    exitProgram = False
    try:
        fileEmpty = os.stat(API_FILE_TO_ACCESS).st_size == 0
    except OSError:
        print("File not found.Creating " + API_FILE_TO_ACCESS + ".Write down keys within the file. File "
                                                                "location=program was run.\n")
        consumerFileWrite = open(API_FILE_TO_ACCESS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(API_FILE_TO_ACCESS, "a")
        consumerFileWrite.write(API_TEXT_TO_WRITE)
        consumerFileWrite.close()
        exitProgram = True
    try:
        fileEmpty = os.stat(ACCESS_FILE_TO_ACCESS).st_size == 0
    except OSError:
        print("File not found.Creating " + API_FILE_TO_ACCESS + "Write down keys within the file. File "
                                                                "location=program was run.\n")
        consumerFileWrite = open(ACCESS_FILE_TO_ACCESS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(ACCESS_FILE_TO_ACCESS, "a")
        consumerFileWrite.write(ACCESS_TEXT_TO_WRITE)
        consumerFileWrite.close()
        exitProgram = True
    if exitProgram:
        print("Program closing, write down the proper keys in the files created.\n")
        sys.exit("Files created, do not rename file names.")


def get_api_variables():
    cfr = open(API_FILE_TO_ACCESS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck


def get_access_variables():
    cfr = open(ACCESS_FILE_TO_ACCESS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
