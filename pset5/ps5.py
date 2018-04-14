# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
#from tkinter import *

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)    
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory():
    
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        
        return self.guid
    
    def get_title(self):
        
        return self.title
    
    def get_description(self):
        
        return self.description
        
    def get_link(self):
        
        return self.link
    
    def get_pubdate(self):
        
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    
    def __init__(self, phase):
        
        self.phase = phase.lower()
    
    def evaluate(self,story):
        
        Trigger.evaluate(self,story)
        
    def is_phrase_in(self,text):
 
        resultmax =''
        resultmin =''
        title_list =re.sub("[\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]", " ",text.lower()).split(' ')
#        word = story.title.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        for word in title_list :
            if word !='':
                resultmax +=word +' '
                if word in self.phase:
                    resultmin +=word + ' '
        return self.phase in resultmax and self.phase in resultmin 
    
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    
    def __init__(self, phase):
        
        PhraseTrigger.__init__(self, phase)
    
    def evaluate(self, story):
        
        if self.is_phrase_in(story.title):
            return True
        else:
            return False
        
    def is_phrase_in(self, text):
        return PhraseTrigger.is_phrase_in(self,text)
#        resultmax =''
#        resultmin =''
#        title_list =re.sub("[\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]", " ",story.title.lower()).split(' ')
##        word = story.title.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#        for word in title_list :
#            if word !='':
#                resultmax +=word +' '
#                if word in self.phase:
#                    resultmin +=word + ' '
#        return self.phase in resultmax and self.phase in resultmin 
                
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    
    def __init__(self, phase):
        
        PhraseTrigger.__init__(self, phase)
            
    def evaluate(self, story):
        
        if self.is_phrase_in(story.description):
            return True
        else:
            return False
        
    def is_phrase_in(self, text):
        
        return PhraseTrigger.is_phrase_in(self,text)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    
    def __init__(self, time):
#        try:
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
   
    def evaluate(self,story):
        
        Trigger.evaluate(self,story)
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    
    def __init__(self,time):
        TimeTrigger.__init__(self,time)
    
    def evaluate(self,story):
        if self.time > story.pubdate.replace(tzinfo=pytz.timezone("EST")):
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    
    def __init__(self,time):
        TimeTrigger.__init__(self,time)
    
    def evaluate(self,story):
        if self.time < story.pubdate.replace(tzinfo=pytz.timezone("EST")):
            return True
        else:
            return False    

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    
    def __init__(self, Trigger):
        self.Trigger = Trigger
        
    def evaluate(self,story):
        return not self.Trigger.evaluate(story)
        

# Problem 8

# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2
        
    def evaluate(self, story):
        return self.Trigger1.evaluate(story) and self.Trigger2.evaluate(story)
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2
        
    def evaluate(self, story):
        return self.Trigger1.evaluate(story) or self.Trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
#    result =[]
#    for trigger in triggerlist:
#        for story in stories:
#            if trigger.evaluate(story):
#                result.append(story)
    result = [story for story in stories for trigger in triggerlist if trigger.evaluate(story)]
    return result
#    return stories
#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    with open(filename, 'r') as trigger_file:
        lines = []
        for line in trigger_file:
            line = line.rstrip()
            if not (len(line) == 0 or line.startswith('//')):
                lines.append(line)
            
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
#    result={}
#    for line in lines:
#        newline = line.split(',')
#        if newline[0]!='ADD':
#            result[line[0]] = newline[1:]
#        if newline[0]=='ADD':
#            trigger_list=[word for word in newline[1:]]
    helpdict = {'AND':AndTrigger,
                'OR':OrTrigger,
                'NOT':NotTrigger,
                'TITLE':TitleTrigger,
                'DESCRIPTION':DescriptionTrigger,
                'AFTER':AfterTrigger,
                'BEFORE':BeforeTrigger
            }
    result ={lines[i].split(',')[0]: lines[i].split(',')[1:] for i in range(0, len(lines))}
    for i,v in result.items():
        if i !='ADD':
            if len(v)==2:
                result[i]= helpdict[v[0]](v[1])
            elif len(v)==3:
                result[i]= helpdict[v[0]](result[v[1]],result[v[2]])
    for i,v in result.items():
        if i=='ADD':
            trigger_list = [result[t] for t in v]
           
#    print(trigger_list)    
    return trigger_list
#    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("NASA")
        t2 = DescriptionTrigger("Space")
        t3 = DescriptionTrigger("AI")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("https://news.google.com/news/rss/headlines/section/topic/SCIENCE?ned=us&hl=en&gl=US")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("https://www.yahoo.com/news/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)



if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()





   