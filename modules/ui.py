import os


# ==========================================================
# Utility Functions
# ==========================================================

def clear():
    """Clear the terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def line():
    """Print a separator line."""
    print("-" * 70)


def header(title="SKILL BOARD"):
    """Display the page header."""

    clear()

    os.system("title Skill Board")      # Windows only

    print("=" * 70)
    print(title.center(70))
    print("=" * 70)
    print()
def footer():
    line()
    print("Skill Board v1.0")

def progress_bar(progress):
    """
    Returns a text progress bar.

    Example:
    ██████░░░░ 60%
    """

    total_blocks = 10

    filled = progress // 10
    empty = total_blocks - filled

    return f"{'█'*filled}{'░'*empty} {progress}%"
#------------------------------------------------------------

def display_skills(data):

    header()

    print("Your Skills")
    line()

    print(f"{'ID':<5}{'Skill':<35}{'Progress'}")

    line()

    if not data["skills"]:

        print("No Skills Available.")

    else:

        for skill in data["skills"].values():

            print(
                f"{skill['Id']:<5}"
                f"{skill['title']:<35}"
                f"{progress_bar(skill['status'])}"
            )
            print()

    line()

    print()

    print("Actions")
    line()

    print("1. Open Skill")
    print("2. Add Skill")
    print("3. Delete Skill")
    print("4. Save & Exit")

    print()
    footer()

def display_ttd(data, skill_id):
    """Display all Things To Do for a selected skill."""

    skill = data["skills"][str(skill_id)]

    header(f"Skill : {skill['title']}")

    print(f"Progress : {progress_bar(skill['status'])}")
    print()

    print("Things To Do")
    line()

    print(f"{'ID':<6}{'Status':<18}{'Description'}")
    line()

    tasks = data["TTD"][str(skill_id)]

    if not tasks:
        print("No Things To Do Available.")

    else:

        for task in tasks:                                               # some variables are not consistent make them

            status = "✓ Completed" if task["status"] == "Completed" else "○ Pending"

            print(
                f"{task['id']:<6}"
                f"{status:<18}"
                f"{task['ttd']}"
            )

    line()

    print("\nActions")
    line()

    print("1. Add Thing To Do")
    print("2. Delete Thing To Do")
    print("3. Mark Completed")
    print("4. Back")

    print()
    footer()
# ==========================================================
# Input Functions
# ==========================================================

def main_menu():
    """Get the user's choice from the main menu."""
    return input("Enter your choice : ").strip()


def skill_menu():
    """Get the user's choice from the skill menu."""
    return input("Enter your choice : ").strip()


