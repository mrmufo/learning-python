ipAddress = input("Please enter your IP address: ")
segmentNum = 1
segmentLen = 0
for i in range(0, len(ipAddress)):
    if ipAddress[i] == ".":
        print("Segment number {0} is {1} characters long. ".format(segmentNum, segmentLen))
        segmentLen = 0
        if (i + 1) == len(ipAddress):
            break
        segmentNum += 1
        continue
    segmentLen += 1
if segmentLen != 0:
    print("Segment number {0} is {1} characters long. ".format(segmentNum, segmentLen))
print("Your IP address consists of {0} segments. ".format(segmentNum))
