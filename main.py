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
    d={}
    
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    pattern = r'\[([\d/]+, [\d:]+ [APMapm]+)\] (.+?): (.+)'
    link_count=0
    for line in text:
        if re.search(url_pattern, line):
            link_count += 1

        if "This message was deleted" in line:
            deletedmsgcount+=1
        if "A7WiN✨:" in line:
            Alwinmsg+=1
        if "<This message was edited>" in line:
            message_edited+=1
        
        match = re.match(pattern, line)
        if match:
            parts = line.split('] ')
            if len(parts) == 2:
                timestamp, rest = parts
                sender, message = rest.split(': ')
                print(sender)
                if sender not in d:
                    d[sender]=1
                else:
                    d[sender]+=1


    print("The total number of messages deleted were:-",deletedmsgcount)
    print("Alwin messaged:-",Alwinmsg,"times")
    print("The number of messages that was edited were:-",message_edited)
    print("Number of links:-",link_count)
    for i,j in d.items():
        print(i,j)
    
    