from discussion.respond_discussion import respond_discussion

event1 = {
    "question": "What is your favorite animal",
    "started_by": "Christian",
    "comment": "Gotta be the shark"
}

event2 = {
    "question": "What is your favorite color",
    "started_by": "Graham",
    "comment": "Blue is my favorite"
}

event3 = {
    "question": "How old are you",
    "started_by": "Raphael",
    "comment": "I am 15 years old"
}

event4 = {
    "question": "How old are you",
    "started_by": "Layla",
    "comment": "I am 16 years old"
}

event5 = {
    "question": "How old are you",
    "started_by": "Chris",
    "comment": "I am 15"
}

def test_respond_discussion():
    print(respond_discussion(event5,""))

if __name__ == "__main__":
    test_respond_discussion()