with open('filename.txt') as r:
    lines = r.readlines()
w = open("filename2.txt", "w")

sid = 2000000

for i in lines:
    sid += 1
    ioc = i.strip()
    if i[0] in ["0","1","2","3","4","5","6","7","8","9"]:
        rule = f"alert ip any any -> {ioc} any (msg: \"FLAG {ioc}\"; sid: {str(sid)};) "
        w.write(rule + "\n")    
    else:
        rule = f"alert udp any any -> any any (msg: \"{ioc}\"; content:\"{ioc}\"; sid: {str(sid)};) "
        w.write(rule + "\n")
