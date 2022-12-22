from discussion.get_all_comments import get_all_comments

def test_get_all_comments():
    event = {
        "question": "How old are you"
    }
    print(get_all_comments(event,""))

if __name__ == "__main__":
    test_get_all_comments()