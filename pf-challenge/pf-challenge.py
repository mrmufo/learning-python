ipAddress = input("Please enter your IP address. "
                  "IP address should consist of 4 numbers, separated from each other with a full stop. \n")
if ipAddress[-1] != '.':
    ipAddress += '.'

segmentNum = 1
segmentLen = 0
errorsInIP = 0
for character in ipAddress:  # for i in range(0, len(ipAddress)):
    if character == '.':        # if ipAddress[i] == ".":
        if segmentLen == 0 and errorsInIP == 0 and segmentNum == 1:
            print("NOTE: IP address should not begin with a dot. ")
            errorsInIP += 1
            continue
        print("Segment number {0} is {1} characters long. ".format(segmentNum, segmentLen))
        segmentLen = 0
        segmentNum += 1
        continue
    segmentLen += 1

print("Your IP address consists of {0} segments. ".format(segmentNum - 1))
