import datetime
import json
import os

class wellness_tracker():

    def __init__(self):
        self.entries = []
        self.load_data()

    def load_data(self):

        if os.path.exists("wellness_data.json"):

            with open("wellness.json","r") as f:
                self.entries = json.load(f)

    def save_data(self):

        with open("wellness_data.json","w") as f:
            json.dump(self.entries,f,indent=2)

    def daily_checkin(self):
        today = datetime.datetime.now().strftime("%a,%b %d")
        print(f"\n------{today}-----")
        print("Daily Check-in\n")

        entry = {
            'date': today,
            'overall_outlook': self.get_rating("How was your overall outlook today?", 
                                              ["Negative", "Neutral", "Positive"]),
            'productivity': self.get_rating("How productive were you today?", 
                                          ["Not at all", "Somewhat", "Fairly", "Very"]),
            'motivation': self.get_rating("How motivated did you feel today?", 
                                        ["Not at all", "Somewhat", "Fairly", "Very"]),
            'loneliness': self.get_rating("Did you feel lonely today?",["Not at all","Somewhat","Fairly","Very"]),
            'depression':self.get_rating("Did you feel depressed or hopless today?",["Not at all","Somewhat","Fairly","Very"]),
            'anxiety': self.get_rating("Did you feel anxious today?",["Not at all","Somewhat","Fairly","Very"])
        }

        self.entries.append(entry)
        self.save_data()
        print("\n Check-in Complete Thank you")

    def get_rating(self, question, options):
        print(question)
        for i, option in enumerate(options,1):
            print(f"{i}.{option}")

        while True:
            try:
                choice = int(input("Enter your choice(1-{}): ".format(len(options))))
                if 1 <= choice <= len(options):
                    return options[choice -1]
                print("invalid choice.Please try again")
            except ValueError:
                print("Please Enter a number:")

    def view_history(self):
        print("\n --Your Wellness History--")
        for entry in self.entries[-5:]:
            print(f"\nDate : {entry['date']}")
            print(f"Overall Outlook:{entry['overall_outlook']}")
            print(f"Productivity:{entry['productivity']}")
            print(f"Motivation:{entry['motivation']}")
            print(f"Loneliness:{entry['loneliness']}")
            print(f"Depression:{entry['depression']}")
            print(f"Anxiety:{entry['anxiety']}")

    def show_menu(self):
        while True:
            print("\n Moods Wellness Tracker")
            print("1. Daily Check In")
            print("2. View History")
            print("3. Exit")

            choice = input("Enter your choice:")

            if choice == '1':
                self.daily_checkin()
            elif choice == '2':
                self.view_history()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    tracker = wellness_tracker()
    tracker.show_menu()










