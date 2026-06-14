import storage as st

dbm = st.load_json()


# Generates new Goal Id
def goal_g_id(data):
    if len(data["goals"]) == 0:
        return 1
    max_id = max([goals["id"] for goals in data["goals"]])
    return max_id+1

#------------------------  Add new Goal
def add_goal(dbm):
    title = input("Enter the title: ")
    goal_id = goal_g_id(dbm)
    new_goal = {
        "id":goal_id,
        "title":title,
        "Progress":"Not Started"
    }
    dbm["goals"].append(new_goal)
    return

# -------------------------- View Goals
def veiw_goals(dbm):
    print("\n"+"="*40)
    print("             YOUR GOALS")
    print(f"{'ID':<5} {'TITLE':<20} {'STATUS'}")
    print("-"*40)

    if len(dbm["goals"]) == 0:
        print("             No Goals available")
        return
    for goal in dbm["goals"]:
        print(f"{goal["id"]:<5} {goal["title"]:<20} {goal["Progress"]}")
    return
# ------------------------------- get goal
def get_goal(dbm):
    user = int(input("Enter the Id of the goal : "))
    for goal in dbm["goals"]:
        if goal["id"] == user:
            return goal[id]
        return
# ------------------------------ Remove goal

def remove_goal(dbm):
    user = int(input("Enter the Id of the goal to  remove: "))
    for goal in dbm["goals"]:
        if goal["id"] == user:
            dbm["goals"].remove(goal)
            return 1
    return

#add_goal(dbm)
remove_goal(dbm)



st.store_json(dbm)


