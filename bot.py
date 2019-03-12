import tweepy
import time
import datetime
import random

consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'
access_token= 'access_token'
access_token_secret= 'access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


JJ = 28 #Elon
MM = 6 #Elon
AAAA = 1971 #Elon

i = 1
number = 1
while i <= 2:
        now = datetime.datetime.now()
        todaynostr = now.date()
        today = str(todaynostr)

        TSJJ = today[8] + today[9]
        TSMM = today[5] + today[6]
        floatTSMM = float(TSMM)
        TSAAAA = today[0] + today[1] +today[2] +today[3]
        tintJJ = int(TSJJ)
        tintMM = int(TSMM)
        tintAAAA = int(TSAAAA)
        difJJ = tintJJ - JJ
        difMM = tintMM - MM
        difAAAA = tintAAAA - AAAA

        if difJJ < 0:
                difJJ = difJJ + 30
                difMM = difMM - 1

        if difMM < 0:
                difMM = difMM + 12
                difAAAA = difAAAA - 1

        AS = "s , "
        MS = "s and "
        DS = "s"

        if difAAAA == 0:
                AS = " , "

        if difMM == 0:
                MS = " and "

        if difJJ == 0:
                DS = ""
                

        api.update_status('@ElonMusk is now ' + str(difAAAA) + ' year' + AS + str(difMM) + ' month' + MS + str(difJJ) + ' day' + DS + '.')
        time.sleep(3598)
