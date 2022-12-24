import json
from respond_comment import respond_comment
from discussion.start_discussion import start_discussion
from discussion.respond_discussion import respond_discussion
from tests.mock.mock_respond_comment import RESPOND_COMMENT_LIST
from tests.mock.mock_start_discussion import DISCUSSION_LIST
from tests.mock.mock_respond_discussion import RESPOND_DISCUSSION_LIST

def populate_db():

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


if __name__ == "__main__":
    populate_db()