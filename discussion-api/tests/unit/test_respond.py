from discussion.respond import respond

event1 = {
    "question": "What is your favorite animal",
    "comment_id": "14",
    "started_by": "Clair",
    "response": "Hey not true, Dogs are awesome"
}

event2 = {
    "question": "What is your favorite animal",
    "comment_id": "3",
    "started_by": "David",
    "response": "Cats are cooler than dogs, sorry not sorry"
}

event3 = {
    "question": "What is your favorite color",
    "comment_id": "3",
    "started_by": "David",
    "response": "Cats are cooler than dogs, sorry not sorry"
}

event4 = {
    "question": "How old are you",
    "comment_id": "21",
    "started_by": "Joshua",
    "response": "No you are not, you are 14!"
}

event5 = {
    "question": "How old are you",
    "comment_id": "22",
    "started_by": "Chris",
    "response": "No I'm not!"
}

event6 = {
    "question": "How old are you",
    "comment_id": "21",
    "started_by": "Michael",
    "response": "Chris don't lie, you are 14!"
}


def test_respond():
    
    
    print(respond(event6,""))

if __name__ == "__main__":
    test_respond()