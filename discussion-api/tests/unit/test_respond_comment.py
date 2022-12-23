import json
from respond_comment import respond_comment
from discussion.start_discussion import start_discussion
from discussion.respond_discussion import respond_discussion
from tests.mock.mock_start_discussion import DISCUSSION_EVENT, DISCUSSION_LIST
from tests.mock.mock_respond_discussion import RESPOND_DISCUSSION_LIST
from utils.delete_db_info import delete_db_info

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


def test_respond_comment():
    delete_db_info()
    for discussion in DISCUSSION_LIST:
        out = start_discussion(discussion, "")
        assert out["statusCode"] == 201

    for respond in RESPOND_DISCUSSION_LIST:
        out = respond_discussion(respond, "")
        out["body"] = json.loads(out["body"])
        assert out["statusCode"] == 201
        assert out["body"]["comment_id"] > 0
    
    # Comment 7
    event1 = {
        "comment_id": "1",
        "started_by": "Ryan",
        "response": "I agree with Chris, sharks rock"
    }

    out = respond_comment(event1,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 8
    event2 = {
        "comment_id": out["body"]["comment_id"],
        "started_by": "Chris",
        "response": "Thats why we are best friends!"
    }

    out = respond_comment(event2,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0
    
    # Comment 9
    event3 = {
        "comment_id": out["body"]["comment_id"],
        "started_by": "Ryan",
        "response": "Totally!"
    }

    out = respond_comment(event3,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 10
    event4 = {
        "comment_id": 3,
        "started_by": "Michael",
        "response": "Cool tip, if you mix red and blue you will get purple, my favorite color"
    }

    out = respond_comment(event4,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 11
    event5 = {
        "comment_id": 3,
        "started_by": "David",
        "response": "Because of the sky?"
    }

    out = respond_comment(event5,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 12
    event6 = {
        "comment_id": 3,
        "started_by": "Lydia",
        "response": "You must like the ocean right?"
    }

    out = respond_comment(event6,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 13
    event7 = {
        "comment_id": 11,
        "started_by": "Graham",
        "response": "Actually yes, I want to be a pilot when I grow up, so I have to love the sky!"
    }

    out = respond_comment(event7,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    # Comment 14
    event8 = {
        "comment_id": 12,
        "started_by": "Graham",
        "response": "The Ocean is neat too"
    }

    out = respond_comment(event8,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0

    event9 = {
        "comment_id": 0,
        "started_by": "Graham",
        "response": "The Ocean is neat too"
    }

    out = respond_comment(event9,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid comment id. comment id must be a number"
    assert "comment_id" not in out["body"].keys()

    event10 = {
        "comment_id": 14,
        "started_by": "Graham",
        "response": ""
    }

    out = respond_comment(event10,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid response. Response must have text"
    assert "comment_id" not in out["body"].keys()

    # Comment 15
    event11 = {
        "comment_id": "14",
        "started_by": "",
        "response": "Great animals leave there"
    }

    out = respond_comment(event11,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "Created new response"
    assert out["body"]["comment_id"] > 0
    
    delete_db_info()

if __name__ == "__main__":
    test_respond_comment()