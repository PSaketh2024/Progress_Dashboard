import storage as st
def get_goal(goal_id):
    data = st.load_json()
    for goal in data["goals"]:
        if goal["id"] == goal_id:
            return goal
    return None
#------------------------------------------------------------
def add_goal():
    data = st.load_json()
    title = input("Enter the Goal: ")
    topics = []
    n_topics = int(input("Enter number of topics: "))
    for i in range(n_topics):
        topic = input(f"Enter the topic {i+1}:")
        topics.append({"id":i+1,"title":topic,"status":False})

    if len(data["goals"]) == 0:
        goal_id = 1
    else :
        goal_id = data["goals"][-1]["id"]+1
    data["goals"].append({"id":goal_id,"title":title,"topics":topics})
    st.store_json(data)
    return
#--------------------------------------------------------------------------
def veiw_goals():
    data = st.load_json()
    print("\n","="*5,    "🎯YourGoals",    "="*5,"\n")
    if len(data["goals"]) == 0:
        print("No Goals Found")
        return
    for goal in data["goals"]:
        print(goal["id"],   goal["title"])
    return
#----------------------------------------------------------------------
def veiw_topics(goal_id):
    goal = get_goal(goal_id)
    if goal is None:
        print("Goal not found")
        return
    print("="*5,    "Topics",   "="*5)
    for topic in goal["topics"]:
        status = "✅" if topic["status"] == True else "❎"
        print(topic["id"],   topic["title"],    status)
    return
        
