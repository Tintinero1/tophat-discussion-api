import json
from respond_comment import respond_comment
from discussion.start_discussion import start_discussion
from discussion.respond_discussion import respond_discussion
from tests.mock.mock_start_discussion import DISCUSSION_LIST
from tests.mock.mock_respond_discussion import RESPOND_DISCUSSION_LIST
from utils.delete_db_info import delete_db_info


def test_respond_comment():
    delete_db_info()
    for discussion in DISCUSSION_LIST:
        discussion_event = {
            "body": json.dumps(discussion)
        }
        out = start_discussion(discussion_event, "")
        assert out["statusCode"] == 201

    for respond in RESPOND_DISCUSSION_LIST:
        respond_event = {
            "body": json.dumps(respond)
        }
        out = respond_discussion(respond_event, "")
        out["body"] = json.loads(out["body"])
        assert out["statusCode"] == 201
        assert out["body"]["comment_id"] > 0
    
    # Comment 7
    event1 = {
        "body": json.dumps({
            "comment_id": "1",
            "started_by": "Ryan",
            "response": "I agree with Chris, sharks rock"
        })
    }

    out = respond_comment(event1,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 8
    event2 = {
        "body": json.dumps({
            "comment_id": out["body"]["comment_id"],
            "started_by": "Chris",
            "response": "Thats why we are best friends!"
        })
    }

    out = respond_comment(event2,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0
    
    # Comment 9
    event3 = {
        "body": json.dumps({
            "comment_id": out["body"]["comment_id"],
            "started_by": "Ryan",
            "response": "Totally!"
        })
    }

    out = respond_comment(event3,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 10
    event4 = {
        "body": json.dumps({
            "comment_id": 3,
            "started_by": "Michael",
            "response": "Cool tip, if you mix red and blue you will get purple, my favorite color"
        })
    }

    out = respond_comment(event4,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 11
    event5 = {
        "body": json.dumps({
            "comment_id": 3,
            "started_by": "David",
            "response": "Because of the sky?"
        })
    }

    out = respond_comment(event5,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 12
    event6 = {
        "body": json.dumps({
            "comment_id": 3,
            "started_by": "Lydia",
            "response": "You must like the ocean right?"
        })
    }

    out = respond_comment(event6,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 13
    event7 = {
        "body": json.dumps({
            "comment_id": 11,
            "started_by": "Graham",
            "response": "Actually yes, I want to be a pilot when I grow up, so I have to love the sky!"
        })
    }

    out = respond_comment(event7,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 14
    event8 = {
        "body": json.dumps({
            "comment_id": 12,
            "started_by": "Graham",
            "response": "The Ocean is neat too"
        })
    }

    out = respond_comment(event8,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    event9 = {
        "body": json.dumps({
            "comment_id": 0,
            "started_by": "Graham",
            "response": "The Ocean is neat too"
        })
    }

    out = respond_comment(event9,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid comment id. comment id must be a number"
    assert "comment_id" not in out["body"].keys()

    event10 = {
        "body": json.dumps({
            "comment_id": 14,
            "started_by": "Graham",
            "response": ""
        })
    }

    out = respond_comment(event10,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid response. Response must have text"
    assert "comment_id" not in out["body"].keys()

    # Comment 15
    event11 = {
        "body": json.dumps({
            "comment_id": "14",
            "started_by": "",
            "response": "Great animals leave there"
        })
    }

    out = respond_comment(event11,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0
    
    delete_db_info()

if __name__ == "__main__":
    test_respond_comment()