
def topic_id_g(goal_id,data):
    id_lst = [topic_id["id"] for topic_id in data["topics"][str(goal_id)]]
    if len(id_lst) == 0:
        return 1
    print(id_lst)
    return  max(id_lst)+1
#---------------------------------------------------------
def add_topics_list(goal_id,data):
    data["topics"][str(goal_id)] = []
    return
#--------------------------------------------- add topic
def add_topic(goal_id,data):
    title = input("Enter the topic name: ")
    topic_id = topic_id_g(str(goal_id),data)
    topic = {
        "id" : topic_id,
        "title":title,
        "Progress":"Not started"

    }
    if str(goal_id) not in data["topics"].keys():
        add_topics_list(str(goal_id),data)
    data["topics"][str(goal_id)].append(topic)
    return
# ----------------------------------------------------------- Remove topics
def remove_topic(goal_id,topic_id,data):
    for topic in data["topics"][str(goal_id)]:
        if topic["id"] == topic_id:
            data["topics"][str(goal_id)].remove(topic)
            return
#-----------------------------------------------------------veiw topics
def veiw_topics(goal_id,data):
    print("\n"+"="*40)
    print(f"             TOPICS {goal_id}")
    print(f"{'ID':<5} {'TITLE':<20} {'STATUS'}")
    print("-"*40)
    if len(data["topics"][str(goal_id)]) == 0:
        print(print("             No Topics available"))
        return
    for topic in data["topics"][str(goal_id)]:
         print(f"{topic["id"]:<5} {topic["title"]:<20} {topic["Progress"]}")
    return




