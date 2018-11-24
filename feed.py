"""
Problem: Feed de noticias
Author: nilsonsales
"""


def join_string(my_list):
    text = ""
    for element in my_list:
        text += element + " "
    return text


# Receives size of the feed and number of friends

feed_size = int(input())
n_friends = int(input())

friends_proximity = [{'id':0, 'proximity':0} for x in range(n_friends)]

for i in range(n_friends):
    id, proximity = input().split(" ")
    friends_proximity[i]['id'] = id
    friends_proximity[i]['proximity'] = proximity


# Receives the number of updates and followed by the updates

n_updates = int(input())
updates = [{'id':0, 'time':0, 'text':'', 'score':0} for x in range(n_updates)]

for i in range(n_updates):
    buffer = input()
    split_buffer = buffer.split()

    # Splits the text and adds the values to a dictionary
    updates[i]['id'] = split_buffer[0]
    updates[i]['time'] = split_buffer[1]

    # Number of characters to remove
    offset = len(join_string([split_buffer[0], split_buffer[1]]))

    updates[i]['text'] = buffer[offset:]


for i in range(n_updates):
    # Finds the correspondent column in the 'proximity table' to calculate the 'score'
    friend_column = 0
    for key in range(n_friends):
        if friends_proximity[key]['id'] == updates[i]['id']:
            friend_column = key

    updates[i]['score'] = (0.8 * float(friends_proximity[friend_column]['proximity'])) + (0.2 * float(updates[i]['time']))


# Sort the list of dictionaries in reverse order
updates_ordered = sorted(updates, key=lambda k: k['score'], reverse=True)

# Prints the best ranked posts
for i in range(feed_size):
    print(str(updates_ordered[i]['id']) + " " + updates_ordered[i]['text'])
