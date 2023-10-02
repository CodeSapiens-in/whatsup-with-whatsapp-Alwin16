with open(r"_chat.txt", 'r') as fp:
    text=fp.readlines()
    import re
    deletedmsgcount=0
    Alwinmsg=-1; #since name will be shown once while joining
    message_edited=0
    d=dict()

    for line in text:
        if "This message was deleted" in line:
            deletedmsgcount+=1
        if "A7WiN✨:" in line:
            Alwinmsg+=1
        if "<This message was edited>" in line:
            message_edited+=1
        match = re.match(r'\[([\d/]+), ([\d:]+ [APMapm]+)\] (.+?): (.+)', line)

        if match:
            sender=match.group(3) #group(3) represents the third part of the regex
            print(match.group(3))
            if sender not in d:
                d[sender]=1
            else:
                d[sender]+=1


    print("The total number of messages deleted were:-",deletedmsgcount)
    print("Alwin messaged:-",Alwinmsg,"times")
    print("The number of messages that was edited were:-",message_edited)
    print(d)
