
# coding: utf-8

# In[118]:


from collections import deque
import datetime
import sqlite3

# Make the connection to the database
db = sqlite3.connect('/Users/sprihajha/events.db')
c = db.cursor()

#Execute the first time - to create table

# c.execute('''CREATE TABLE events(timestamp REAL)''')


# In[119]:


#Creating a Queue
queue = deque([])

#Incrementing events to the Queue
def increment():
    for i in range(100):
        event_time = datetime.datetime.now()
        queue.append(event_time)
    return (print('done')) #Added the events to the queue
 
increment()

#Printing the elements of the Queue
# print(queue)


# In[126]:


#Dumping the events into the database
for i in range(0,len(queue)):
    c.execute('''INSERT INTO events(timestamp) VALUES(?)''', (queue[i],))

print("Inserted")

#Removing the events from the queue
for i in range(0,len(queue)):
    queue.popleft()

print("Removed")

db.commit()


# In[127]:


# c.execute('''SELECT timestamp FROM events''')
# time1 = c.fetchall() #retrieve the first row
# print((time1))


# In[130]:


#Check count of events in Last Second
def numLastSecond():
    end = str(datetime.datetime.now()) 
    start = str(datetime.datetime.now() - datetime.timedelta(seconds = 1))

    c.execute('''SELECT timestamp FROM events WHERE timestamp BETWEEN (?) AND (?)''', (start, end,))
    time2 = c.fetchall()
#     print(time2)
    return len(time2)

print(numLastSecond())


# In[128]:


#Check count of events in Last Minute
def numLastMinute():
    end = str(datetime.datetime.now()) 
    start = str(datetime.datetime.now() - datetime.timedelta(minutes = 1))

    c.execute('''SELECT timestamp FROM events WHERE timestamp BETWEEN (?) AND (?)''', (start, end,))
    time2 = c.fetchall()
#     print(time2)
    return len(time2)

print(numLastMinute())


# In[129]:


#Check count of events in Last Hour
def numLastHour():
    end = str(datetime.datetime.now()) 
    start = str(datetime.datetime.now() - datetime.timedelta(hours = 1))

    c.execute('''SELECT timestamp FROM events WHERE timestamp BETWEEN (?) AND (?)''', (start, end,))
    time2 = c.fetchall()
#     print(time2)
    return len(time2)

print(numLastHour())

