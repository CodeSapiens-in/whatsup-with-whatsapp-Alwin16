
with open(r"_chat.txt", 'r') as fp:
    text = fp.readlines()
    lines = len(text)
    pollcount =0
    for eachline in text:
        if 'POLL' in eachline:
            pollcount=pollcount+1
    print('Total Number of lines:', lines)
    print('Total polls: '+str(pollcount))
    import re
    deletedmsgcount=0
    Alwinmsg=-1; #since name will be shown once while joining
    message_edited=0
    message_counts = defaultdict(int)
    image_count=0
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    link_count=0
    pattern = r'\[(\d{2}/\d{2}/\d{2}),'
    for line in text:
        if re.search(url_pattern, line):
            link_count += 1
        
        if "image omitted" in line:
            image_count += 1
        
        match = re.search(pattern, line)
        if match:
            date = match.group(1)
            message_counts[date] += 1
            
        if "This message was deleted" in line:
            deletedmsgcount+=1
        if "A7WiN✨:" in line:
            Alwinmsg+=1
        if "<This message was edited>" in line:
            message_edited+=1
        
        


    print("The total number of messages deleted were:-",deletedmsgcount)
    print("Alwin messaged:-",Alwinmsg,"times")
    print("The number of messages that was edited were:-",message_edited)
    print("Number of links:-",link_count)
    print(f"Total number of images shared: {image_count}")
    most_messages_day = max(message_counts, key=message_counts.get)
    message_count = message_counts[most_messages_day]

    print(f"The day with the most messages is {most_messages_day} with {message_count} messages.")
    
    