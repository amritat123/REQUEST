import requests 
import json 
def my_requests():
    res=requests.get("http://saral.navgurukul.org/api/courses")
    data1=json.loads(res.text)

    with open("meraki.json","w") as res:
        json.dump(data1,res,indent=3)

    store=data1["availableCourses"]
    id =[]
    name=[]
    for i in range (len(store)):
    
        print(i+1,store[i]["name"],end="--")

        print(store[i]["id"])

        id.append(store[i]["id"])

        name.append(store[i]["name"])
    # print(id)
    # print(name)

    #-------------------------secound API--------------------------------------*
    print("---------------------------------------------------------------------")

    n=int(input("please enter the serial number for geting id :- "))
    n1=id[n-1]
    print("-------------------------------------------------------------------")
    print()
    print("id number:--",n1)
    print()
    with open("navgurukul.json","r") as f1:
        b=json.load(f1)
    res2=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercises")
    print(res2)
    data2=res2.json()
    # print(data1)

    slug=[]
    count=1
    for var in data2["data"]:
        print(count,var["name"])
        slug.append(var["slug"])
        count+=1
        for child in  var["childExercises"]:
            print(" ",count,child[name])
            slug.append(child["slug"])
            count+=1
        # v=n1+json
        # with open (v+json,"w") as res3:
        #     var=json.dump(data2,res3,indent=3)

    #"*-----------------------------third API----------------------------------------*"
    print("----------------------------------------------------------------------------")

    var2=int(input("show slug=="))
    res4=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[var2-1]))
    # print(res4)
    data3=res4.json()
    print(data3["content"])
    while True:
        x=var2

        print()
        print("----------------------------------------------------------------------")
        options=input("if you want to go back ,exit=== ")

        if options =="next":
            x+=1
            req=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1,["content"])
            print(x)
            break
        elif options=="back":
            c=1
            for dict1 in data2["data"]:
                print(c,dict1["name"])
                c+=1
                for i in dict1 ["childExercises"]:
                    print("   ",c,i["name"])
                    c+=1
                    break
        else:
            break

my_requests()






    
























