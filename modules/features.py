#--------------------------------------- skill functions
def skill_Id(data):
    if len(data["skills"].keys()) == 0:
        return 1
    else:
       return int(list(data["skills"].keys())[-1])+1


def add_skill(data):
    title = input("Enter the Skill: ")
    skill_id = skill_Id(data)
    skill_D = {"Id":skill_id,
    "title":title,
    "status":0}
    data["skills"][str(skill_id)] = skill_D

    data["TTD"][skill_id] = []
    return 

def remove_skill(data):
    user = list(map(int,input("Select the Id's you want to delete: ").split()))
    for i in user:
        if str(i) not in data["skills"].keys():
            print(f"Skill with Id no {i}is not avaliable")
        else:
            data["skills"].pop(str(i))
            data["TTD"].pop(str(i))
#--------------------------------------- TTD functions 
def ttd_id(data,s_id):
    if len(data["TTD"][str(s_id)]) == 0:
        return 1
    else:
        return data["TTD"][str(s_id)][-1]["id"]+1
def add_TTD(data,s_id):
    ttd = input("Enter ttd :")
    ttd_d = {"id":ttd_id(data,s_id),
            "ttd":ttd,
            "status": "Not started"

    }  
    data["TTD"][str(s_id)].append(ttd_d)


def remove_TTD(data,s_id):
     user = list(map(int,input("Enter the Id's: ").split()))
     for i in user:
        for ttd in data["TTD"][str(s_id)]:
            if  i == ttd["id"]:
                data["TTD"][str(s_id)].remove(ttd)
                break

#----------------------------------------------------- other functions
def mark_completed(data,s_id):
    user = list(map(int,input("Enter the Id's :").split()))
    for ttd in data["TTD"][str(s_id)]:
        if ttd["id"] in user:
            ttd["status"] = "Completed"
def progress(data,s_id):
    count = 0
    for ttd in data["TTD"][str(s_id)]:
        if ttd["status"] == "Completed":
            count+=1
    data["skills"][str(s_id)]["status"] = int((count/len(data["TTD"][str(s_id)]))*100)

def update(data):
    for skill_id in data["skills"].keys():
        progress(data,skill_id)




#-----------------------------------------------------


        
       




