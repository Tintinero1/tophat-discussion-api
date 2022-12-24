import pytest
import logging
import requests
import json
from fake_useragent import UserAgent
from tests.integration.test_vars import API_GATEWAY_URL
ua = UserAgent()

logger = logging.getLogger(__name__)

def test_api_gateway_start_discussion():
    url_to_test = API_GATEWAY_URL + "/startdiscussion"
    logger.info(f"url: {url_to_test}")
    data = {
        "started_by": "Jason",
        "question": "Do you have pets?"
    }
    response = requests.post(url_to_test, headers={"User-Agent": ua.chrome}, json=data)
    logger.info(
        f"the response error code is {response.status_code}\n"
        f"the json of the response is {json.dumps(response.json(),    indent=2)}")
    print(response.json())
    assert response.status_code == 201
    assert "message" in response.json()
    assert "discussion_id" in response.json()
    assert response.json()["discussion_id"] > 0
    assert response.json()["message"] == "Created new discussion"

def test_api_gateway_respond_discussion():
    url_to_test = API_GATEWAY_URL + "/respondDiscussion"
    logger.info(f"url: {url_to_test}")
    data = {
        "question": "Do you have pets?",
        "started_by": "Clair",
        "comment": "I have 2 hamsters!"
    }
    response = requests.post(url_to_test, headers={"User-Agent": ua.chrome}, json=data)
    logger.info(
        f"the response error code is {response.status_code}\n"
        f"the json of the response is {json.dumps(response.json(),    indent=2)}")
    print(response.json())
    assert response.status_code == 201
    assert "message" in response.json()
    assert "comment_id" in response.json()
    assert response.json()["comment_id"] > 0
    assert response.json()["message"] == "Created new response"

def test_api_gateway_respond_comment():
    url_to_test = API_GATEWAY_URL + "/respondComment"
    logger.info(f"url: {url_to_test}")
    data = {
        "comment_id": "2",
        "started_by": "Ryan",
        "response": "That is awesome Clair"
    }
    response = requests.post(url_to_test, headers={"User-Agent": ua.chrome}, json=data)
    logger.info(
        f"the response error code is {response.status_code}\n"
        f"the json of the response is {json.dumps(response.json(),    indent=2)}")
    print(response.json())
    assert response.status_code == 201
    assert "message" in response.json()
    assert "comment_id" in response.json()
    assert response.json()["comment_id"] > 0
    assert response.json()["message"] == "Created new response"

def test_api_gateway_get_all_comments():
    url_to_test = API_GATEWAY_URL + "/allComments?question=Do%20you%20have%20pets?"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n"
        f"the json of the response is {json.dumps(response.json(),    indent=2)}")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "comments" in response.json()
    assert response.json()["message"] == "All messages retrieved"
    assert len(response.json()["message"]) > 0


if __name__ == "__main__":
    test_api_gateway_get_all_comments()