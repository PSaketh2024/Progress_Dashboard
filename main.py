from modules.ui import *

data = {
    "skills": {
        "1": {
            "Id": 1,
            "title": "Artificial Intelligence",
            "status": 75
        },
        "2": {
            "Id": 2,
            "title": "Data Structures",
            "status": 40
        },
        "3": {
            "Id": 3,
            "title": "Machine Learning",
            "status": 20
        }
    },

    "TTD": {
        "1": [
            {"id": 1, "ttd": "Complete Mathematics", "status": "Completed"},
            {"id": 2, "ttd": "Learn Python", "status": "Completed"},
            {"id": 3, "ttd": "Build ML Project", "status": "Not started"},
        ],

        "2": [
            {"id": 1, "ttd": "Arrays", "status": "Completed"},
            {"id": 2, "ttd": "Linked Lists", "status": "Not started"},
            {"id": 3, "ttd": "Trees", "status": "Not started"},
        ],

        "3": [
            {"id": 1, "ttd": "Linear Regression", "status": "Completed"},
            {"id": 2, "ttd": "Logistic Regression", "status": "Not started"},
        ]
    }
}

while True:

    display_skills(data)

    choice = main_menu()

    if choice == "1":

        try:
            skill_id = int(input("\nEnter Skill ID : "))

            if str(skill_id) in data["skills"]:
                display_ttd(data, skill_id)
                input("\nPress Enter to return...")
            else:
                print("\nInvalid Skill ID")
                input("\nPress Enter...")

        except ValueError:
            print("\nPlease enter a valid number.")
            input("\nPress Enter...")

    elif choice == "2":

        header("ADD SKILL")

        input("Skill Name : ")

        print("\n✓ Demo Only")

        input("\nPress Enter...")

    elif choice == "3":

        header("DELETE SKILL")

        input("Enter Skill IDs : ")

        print("\n✓ Demo Only")

        input("\nPress Enter...")

    elif choice == "4":

        header("GOODBYE")

        print("Thanks for testing Skill Board!")

        break

    else:

        print("\nInvalid Choice!")

        input("\nPress Enter...")