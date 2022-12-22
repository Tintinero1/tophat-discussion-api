from discussion.start_discussion import start_discussion

event1 = {
    "started_by": "Thomas",
    "question": "What is your favorite color"
}

event2 = {
    "started_by": "Michael",
    "question": "How old are you"
}

event3 = {
    "started_by": "Joel",
    "question": "How tall are you"
}

def test_start_discussion():
    print(start_discussion(event2,""))

if __name__ == "__main__":
    test_start_discussion()