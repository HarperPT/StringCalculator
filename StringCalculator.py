import re

inputData = ["","1,2","1\n2,3","1,\n","//;\n1;2","//[***]\n1***2***3","1\n2,-2","//[*][%]\n1*2%3","//[**][%%%]\n1**2%%%3","//[***]\n1***2***3","2,1001"]

#check Addend is not \n
def checkLastNum(arNum):
    if (arNum[len(arNum)-1]==""):
        return False
    return True
        

# check if list include Negatives 
def checkPositiveNum(arNum):
    for i in arNum:
        num = int(i)
        if(num<0):
            return False
    return True

#Final Calculate 
def calNumbers(arNum):
    result=0
    for i in arNum:
        if(i==""):
            i=0
        countNum = int(i)
        countNum=0 if (countNum>1000) else countNum
        result+= countNum
    print (result)

#Main function
def Add(strNumbers):
    pa="^//.*"
    x = re.search(pa,strNumbers)

    if(x):
        temp = re.split(r"\n",strNumbers)
        isQuote = re.search(r"//\[.*\]",strNumbers)
        
        # custom Delimiters no use by []
        if isQuote is None:
            customD = re.split("//",temp[0])
            newArray = re.split(customD[1],temp[1])
            return calNumbers(newArray)
        else:
        # custom Delimiters use by [] ect."//[*][%]\n1*2%3"  ,  //[**][%%%]\n1**2%%%3"
            delimiters = temp[0][2:]
            arDelimters = re.split(r"\[(.*?)\]",delimiters)
            arDelimters = list(filter(lambda x : x != '', arDelimters))
            
            resultNums = []
            numbersList = temp[1]

            for i in arDelimters:
                escapeDelimter = re.escape(i)
                numbersList = re.sub(escapeDelimter,",",numbersList)
            Add(numbersList)


    else:
        #if there is no custom Delimiters 
        if (len(strNumbers)==0):
            print("0")
            return 0

        arSimple = re.split("[,\s]",strNumbers)

        #error Input
        checkLastNum(arSimple)
        if(not checkLastNum(arSimple)):
            print ("Error Input")
            return

        # check Negetive and Calcaulte
        if (checkPositiveNum(arSimple)):
            return calNumbers(arSimple)
        else:
            arNegatives = []
            # return Negatives number list
            for i in arSimple:
                if(int(i)<0):
                    arNegatives.append(i)
            print ("{}{}".format(arNegatives," Negatives not allowed!!" ))

#input test
for i in inputData:
    Add(i)