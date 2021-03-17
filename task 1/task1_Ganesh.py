s = open("htmlFile.txt")
s = s.readlines()
l = list()
givenString = ""
for i in s:
    l.append(i.strip("\n").strip("\t").strip("\r"))
for i in l:
    givenString += i


def oc(id):
    ope, clos, si, ei = 1, 0, 0, 0

    for i in l:
        if("\""+str(id)+"\"" in i):
            if (not "/>" in i):
                si = l.index(i)
                break

    j = si+1
    while True:
        if("id" in l[j] and not "/>" in l[j]):
            ope += 1
        if("</" in l[j]):
            clos += 1
        if(ope == clos):
            ei += j
            break
        j += 1
    return [si, ei]


def oc1(id, single):
    si = 1

    if (single):
        for i in l:
            if ("\""+str(id)+"\"" in i):
                if ("/>" in i):
                    si = l.index(i)
                    break
    return si


def append(gs, id, re):
    outputString = ""
    id = int(id)
    arr = oc(id)

    start = arr[0]
    end = arr[1]
    single=False
    
    for i in l:
        if("\""+str(id)+"\"" in i and "/>" in i):
            single = True
            outputString += "No Output"
            return outputString

  
    if(not single):
        for i in range(len(l)):
            if(i != end):
                outputString += l[i]
            if (i == end):
                outputString += re
                outputString += l[i]
    return outputString


def prepend(gs, id, re):
    outputString = ""
    id = int(id)
    arr = oc(id)
    single=False

    start = arr[0]
    end = arr[1]

    for i in l:
        if("\""+str(id)+"\"" in i and "/>" in i):
            single = True
            outputString += "No Output"
            return outputString
    if(not single):
        for i in range(len(l)):
            if(i != start):
                outputString += l[i]
            if (i == start):
                outputString += l[i]
                outputString += re

    return outputString


def after(gs, id, re):
    outputString = ""
    id = int(id)

    single = False

    for i in l:
        if("\""+str(id)+"\"" in i and "/>" in i):
            single = True
            break

    if(single):
        index = oc1(id, single)
        for j in range(len(l)):
            if(j != index):
                outputString += l[j]
            if(j == index):
                outputString += l[j]
                outputString += re
        return outputString

    else:
        arr = oc(id)
        start = arr[0]
        end = arr[1]

        for j in range(len(l)):
            if(j != end):
                outputString += l[j]
            if(j == end):
                outputString += l[j]
                outputString += re
        return outputString


def before(gs, id, re):
    outputString = ""
    id = int(id)

    single = False

    for i in l:
        if("\""+str(id)+"\"" in i and "/>" in i):
            single = True
            break

    if(single):
        index = oc1(id, single)
        for j in range(len(l)):
            if(j != index):
                outputString += l[j]
            if(j == index):
                outputString += re
                outputString += l[j]

        return outputString

    else:
        arr = oc(id)
        start = arr[0]
        end = arr[1]

        for j in range(len(l)):
            if(j != start):
                outputString += l[j]
            if(j == start):
                outputString += re
                outputString += l[j]

        return outputString


if __name__ == "__main__":
    print("Given String:")
    print(givenString)

    print("\nOutput for append:")
    print(append(givenString, "6", "<img id=\"appendSample2\" />"))
    print("\nOutput for prepand:")
    print(prepend(givenString, "10", "<br id=\"prependSample2\" />"))
    print("\nOutput for after:")
    print(after(givenString, "7", "<div id=\"afterSample2\"><div>"))
    print("\nOutput for before:")
    print(before(givenString, "13", "<span id=\"beforeSample2\"><span>"))
  
  
  