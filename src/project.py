from datetime import datetime
import json, random, time
from tabulate import tabulate
import matplotlib.pyplot as graph

def load_ref():
    try:
        with open("data/Reflexions.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

Reflexions = load_ref()

def main():
    Relax_time = 20 # It's the time that software gives you once you finish a task
    while True:
        print("1. Start\n2. Extras\n3. Exit")
        option = int(input("Select an option: "))
        To_do_list = Load_ToDo()
        match option:
            case 1:
                Start(To_do_list, Relax_time)
            case 2:
                new_relax = Extras(To_do_list, Relax_time)
                if new_relax is not None:
                    Relax_time = new_relax
            case 3:
                Save_ToDo(To_do_list)
                break

def Start(TD_List, Relax_time):
    End_relax = 0
    Blocksites = ["www.facebook.com", "www.youtube.com"]
    Path = r"C:\Windows\System32\drivers\etc\hosts"
    while True:
        now = datetime.now().timestamp()
        found = False
        if End_relax < now:
            Block(Path, Blocksites)
            See_goals(TD_List)
            Done_task = input("What's the name of the task that you've completed?(Write exit to exit) ")

            if Done_task.lower() == "exit":
                Unlock(Path, Blocksites)
                return 1
            
            for task in TD_List:
                if task["Name"] == Done_task and task["Finish day"] == None:
                    found = True
                    task["Finish day"] = datetime.now().strftime("%m-%d-%Y")
                    Save_ToDo(TD_List)
                    print(f"You've finished a task. You'll have a break of {Relax_time} minutes")
                    End_relax = now + Relax_time*60
                    break
                
            if found == False:
                print(f"Not found task named {Done_task}")
            print(random.choice(Reflexions))
        else:
            Unlock(Path, Blocksites)
            time.sleep(Relax_time*60)

def Block(Path, Blocksites):
    with open(Path, "r+") as f:
                    content = f.read()
                    for site in Blocksites:
                        if site not in content:
                            f.write(f"127.0.0.1 {site}\n")

def Unlock(Path, Blocksites):
    with open(Path, "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    found = False
                    for site in Blocksites:
                        if site in line:
                            found = True
                            break
                    if not found:
                        f.write(line)
                f.truncate()

def Load_ToDo():
    try:
        with open("data/Tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print('File not found, create a "Tasks.json".')
        return []

def Save_ToDo(TD_List):
    with open("data/Tasks.json", "w") as f:
        json.dump(TD_List, f)

def See_goals(TD_List, type=None):
    if type == None:
        headers = ["Name", "Priority","Category", "Deadline", "Assigned day"]
        table = [
                    [
                        row["Name"],
                        row["Priority"],
                        row["Category"],
                        row["Deadline"],
                        row["Assigned day"],

                    ] for row in TD_List if (row["Finish day"] == None)
                ]
    else: 
        headers = ["Name", "Priority","Category", "Deadline", "Assigned day", "Finish day"]
        table = [
                    [
                        row["Name"],
                        row["Priority"],
                        row["Category"],
                        row["Deadline"],
                        row["Assigned day"],
                        row["Finish day"]
                        
                    ] for row in TD_List if (row["Finish day"] != None)
                ]
    print(tabulate(table, headers))

def Extras(TD_List, Relax_time):
    option = 1
    while(option != 6):
        print("1. Add Goals\n2. Graphics\n3. Add a reflexion\n4. Modify relax time\n5. See done tasks\n6. Return to main menu")
        option = int(input("Select an option: "))
        match option:
            case 1:
                Add_goals(TD_List)
            case 2:
                Graphics(TD_List)
            case 3:
                Add_reflexion()
            case 4:
                Relax_time = int(input("Write the new relax time in minutes: "))
                return Relax_time
            case 5:
                See_goals(TD_List, 1)
            case 6:
                pass
            case _:
                print("Invalid option\n")

def Add_goals(TD_List, name=None, priority=None, category=None, deadline=None, test_mode=False):
    if not test_mode:
        name = input("What's the tasks name? ")
        priority = int(input("Type of priority from 1 to 5: "))
        category = input("What kind of category is this task? ")
        deadline = input("When has the task be finished? ")

    New_task = {
        "Name": name,
        "Priority": priority,
        "Category": category,
        "Deadline": deadline,
        "Assigned day": datetime.now().strftime("%m-%d-%Y %H:%M"),
        "Finish day": None
    }
    TD_List.append(New_task)
    Save_ToDo(TD_List)
    return New_task

def Graphics(TD_List):
    tasks = {}
    for i in TD_List:
        date = i.get("Finish day")
        if date != None:
            if date in tasks:
                tasks[date] += 1
            else:
                tasks[date] = 1
    if tasks:
        dates = list(tasks.keys())
        times = list(tasks.values())
        graph.figure(figsize=(10, 5))
        graph.bar(dates, times, color='red')
        graph.xlabel("Finish Day")
        graph.ylabel("Completed Tasks")
        graph.title("Tasks per day")
        graph.xticks(rotation=45)
        graph.tight_layout()
        graph.show()
    else:
        print("You've not completed any task")

def Add_reflexion(quote=None, author=None, test_mode=False):
    if not test_mode:
        quote = input("Write the new quote: ").strip()
        author = input("Who is the author? ").strip()

    with open("data/Reflexions.txt", "a", encoding="utf-8") as f:
        f.write(f"“{quote}.” ―{author}\n")
    print("Saved Reflexion")
    return f"“{quote}.” ―{author}"

if __name__ == "__main__":
    main()