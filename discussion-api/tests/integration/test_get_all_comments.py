import requests
from discussion.get_all_comments import get_all_comments
from respond_comment import respond_comment
from discussion.start_discussion import start_discussion
from discussion.respond_discussion import respond_discussion
from tests.mock.mock_respond_comment import RESPOND_COMMENT_LIST
from tests.mock.mock_start_discussion import DISCUSSION_LIST
from tests.mock.mock_respond_discussion import RESPOND_DISCUSSION_LIST
from utils.delete_db_info import delete_db_info


QUESTION_1_RESULT = [
    {'id': 1, 'id_discussion_question': 1, 'started_by': 'Thomas', 'Question': 'What is your favorite animal', 'parent_id': 0}, 
    {'id': 2, 'comment_id': 1, 'started_by': 'Christian', 'comment': 'Gotta be the shark', 'parent_id': 1}, 
    {'id': 8, 'comment_id': 7, 'started_by': 'Ryan', 'comment': 'I agree with Chris, sharks rock', 'parent_id': 2}, 
    {'id': 9, 'comment_id': 8, 'started_by': 'Chris', 'comment': 'Thats why we are best friends!', 'parent_id': 8}, 
    {'id': 10, 'comment_id': 9, 'started_by': 'Ryan', 'comment': 'Totally!', 'parent_id': 9}, 
    {'id': 3, 'comment_id': 2, 'started_by': 'Chris', 'comment': 'I love chickens!', 'parent_id': 1}
]

QUESTION_2_RESULT = [
    {'id': 1, 'id_discussion_question': 3, 'started_by': 'Michael', 'Question': 'How old are you', 'parent_id': 0}, 
    {'id': 6, 'comment_id': 5, 'started_by': 'Raphael', 'comment': 'I am 15 years old', 'parent_id': 1}, 
    {'id': 7, 'comment_id': 6, 'started_by': 'Layla', 'comment': 'I am 16 years old', 'parent_id': 1}
]

QUESTION_3_RESULT = [
    {'id': 1, 'id_discussion_question': 2, 'started_by': 'Adrian', 'Question': 'What is your favorite color', 'parent_id': 0}, 
    {'id': 4, 'comment_id': 3, 'started_by': 'Graham', 'comment': 'Blue is my favorite', 'parent_id': 1}, 
    {'id': 11, 'comment_id': 10, 'started_by': 'Michael', 'comment': 'Cool tip, if you mix red and blue you will get purple, my favorite color', 'parent_id': 4}, 
    {'id': 12, 'comment_id': 11, 'started_by': 'David', 'comment': 'Because of the sky?', 'parent_id': 4}, 
    {'id': 14, 'comment_id': 13, 'started_by': 'Graham', 'comment': 'Actually yes, I want to be a pilot when I grow up, so I have to love the sky!', 'parent_id': 12}, 
    {'id': 13, 'comment_id': 12, 'started_by': 'Lydia', 'comment': 'You must like the ocean right?', 'parent_id': 4}, 
    {'id': 15, 'comment_id': 14, 'started_by': 'Graham', 'comment': 'The Ocean is neat too', 'parent_id': 13}, 
    {'id': 16, 'comment_id': 15, 'started_by': 'Anon', 'comment': 'Great animals leave there', 'parent_id': 15}, 
    {'id': 5, 'comment_id': 4, 'started_by': 'David', 'comment': 'Orange is the best', 'parent_id': 1}
]

def test_get_all_comments():
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

    for respond in RESPOND_COMMENT_LIST:
        respond_event = {
            "body": json.dumps(respond)
        }
        out = respond_comment(respond_event, "")
        out["body"] = json.loads(out["body"])
        assert out["statusCode"] == 201
        assert out["body"]["comment_id"] > 0

    event1 = {
        "queryStringParameters": {
            "question": "Random question"
        }
    }

    out = get_all_comments(event1,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Question does not exists"
    assert "comments" not in out["body"].keys()

    event2 = {
        "queryStringParameters": {
            "question": "What do you want to learn today"
        }
    }

    out = get_all_comments(event2,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 404
    assert out["body"]["message"] == "No commments available for this discussion"
    assert "comments" not in out["body"].keys()

    event3 = {
        "queryStringParameters": {
            "question": ""
        }

    }

    out = get_all_comments(event3,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 400
    assert out["body"]["message"] == "Invalid question. Questions must have text"
    assert "comments" not in out["body"].keys()

    event4 = {
        "queryStringParameters": {
            "question": "What is your favorite animal"
        }
    }

    out = get_all_comments(event4,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "All messages retrieved"
    assert out["body"]["comments"] == QUESTION_1_RESULT

    event5 = {
        "queryStringParameters": {
            "question": "How old are you"
        }
    }

    out = get_all_comments(event5,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "All messages retrieved"
    assert out["body"]["comments"] == QUESTION_2_RESULT

    event6 = {
        "queryStringParameters": {
            "question": "What is your favorite color"
        }
    }

    out = get_all_comments(event6,"")
    out["body"] = json.loads(out["body"])
    assert out["statusCode"] == 201
    assert out["body"]["message"] == "All messages retrieved"
    assert out["body"]["comments"] == QUESTION_3_RESULT

    delete_db_info()

if __name__ == "__main__":
    test_get_all_comments()