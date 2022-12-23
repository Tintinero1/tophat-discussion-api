import json
from discussion.start_discussion import start_discussion
from utils.delete_db_info import delete_db_info

def test_start_empty_discussion():
    delete_db_info()
    event = {
        "started_by": "",
        "question": ""
    }
    out = start_discussion(event,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Questions must have text"
    assert "discussion_id" not in out["body"].keys()

    delete_db_info()

def test_start_discussion():
    delete_db_info()
    event1 = {
        "started_by": "Thomas",
        "question": "What is your favorite color"
    }

    out = start_discussion(event1,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new discussion"
    assert out["body"]["discussion_id"] > 0

    event2 = {
        "started_by": "",
        "question": "How old are you"
    }

    out = start_discussion(event2,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new discussion"
    assert out["body"]["discussion_id"] > 0

    event3 = {
        "started_by": "Joel",
        "question": ""
    }

    out = start_discussion(event3,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Questions must have text"
    assert "discussion_id" not in out["body"].keys()

    delete_db_info()

if __name__ == "__main__":
    test_start_discussion()