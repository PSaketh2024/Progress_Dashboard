
def tasks_lst(goal_id, topic_id, data):
    if str(goal_id) not in data["tasks"]:
        data["tasks"][str(goal_id)] = {}
    data["tasks"][str(goal_id)][str(topic_id)] = []
    
#------------------------------------------------------ 
def task_id_g(goal_id,topic_id,data):
    id_lst = [task["id"] for task in data["tasks"][str(goal_id)][str(topic_id)]]
    if len(id_lst) == 0:
        return 1
    #print("id_lst",id_lst)
    #id_lst.pop()
    return  max(id_lst)+1
#------------------------------------------------------
def add_task(goal_id,topic_id,data):
    task_id = task_id_g(goal_id,topic_id,data)
    title = input("Enter the title: ")
    task = {
        "id":task_id,
    "title":title,
    "status":"Not started"
    }
    data["tasks"][str(goal_id)][str(topic_id)].append(task)
    return

# -------------------------------------------------
def remove_task1(goal_id,topic_id,task_id,data):
    for task in data["tasks"][str(goal_id)][str(topic_id)]:
        if task["id"] == task_id:
            data["tasks"][str(goal_id)][str(topic_id)].remove(task)
            print("done")
    return
#----------------------------------------------------
def remove_task(goal_id, topic_id, task_id, data):
    tasks = data["tasks"][str(goal_id)][str(topic_id)]

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Done")
            return

    print("Task not found")
import storage as st
data = st.load_json()
remove_task(1,1,1,data)

st.store_json(data)
print(data)