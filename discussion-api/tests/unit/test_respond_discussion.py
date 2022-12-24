import json
from discussion.respond_discussion import respond_discussion
from discussion.start_discussion import start_discussion
from tests.mock.mock_start_discussion import DISCUSSION_EVENT
from utils.delete_db_info import delete_db_info

def test_respond_discussion():
    delete_db_info()
    event = {
        "body": json.dumps(DISCUSSION_EVENT)
    }
    start_discussion(event, "")
    event1 = {
        "body": json.dumps({
            "question": "What is your favorite color",
            "started_by": "Clair",
            "comment": "Red"
        })
    }

    out = respond_discussion(event1,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    event2 = {
        "body": json.dumps({
            "question": "",
            "started_by": "Graham",
            "comment": "Blue is my favorite"
        })
    }

    out = respond_discussion(event2,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Questions must have text"
    assert "comment_id" not in out["body"].keys()

    event3 = {
        "body": json.dumps({
            "question": "What is your favorite color",
            "started_by": "",
            "comment": "My favorite color is Yellow!"
        })
    }

    out = respond_discussion(event3,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    event4 = {
        "body": json.dumps({
            "question": "What is your favorite color",
            "started_by": "Layla",
            "comment": ""
        })
    }

    out = respond_discussion(event4,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid comment. Comment must have text"
    assert "comment_id" not in out["body"].keys()

    event5 = {
        "body": json.dumps({
            "question": "What is your favorite color",
            "started_by": "Christian",
            "comment": "I LOVE black, so dark..."
        })
    }

    out = respond_discussion(event5,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    event6 = {
        "body": json.dumps({
            "question": "How old are you",
            "started_by": "Christian",
            "comment": "I am 15 years old"
        })
    }

    out = respond_discussion(event6,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Cannot respond an unexistent discussion"
    assert "comment_id" not in out["body"].keys()

    delete_db_info()

if __name__ == "__main__":
    test_respond_discussion()