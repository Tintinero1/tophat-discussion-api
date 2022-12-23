
def validate_user(started_by):
    """ This function will ensure correctness 
    for usernames 

    Parameters
    ----------
    started_by: str, required
        username to be validated

    Returns
    ------
    started_by: str
        validated username
    """

    started_by = str(started_by)

    if len(started_by) > 45:
            started_by = started_by[:45]

    elif len(started_by) == 0:
            started_by = 'Anon'

    return started_by

def validate_question(question):
    """ This function will ensure correctness 
    for questions 

    Parameters
    ----------
    question: str, required
        question to be validated

    Returns
    ------
    question: str, if question was validated
        validated question
    False, if question is invalid
    """

    question = str(question)

    if len(question) > 500:
            question = question[:500]

    elif len(question) == 0:
            return False

    return question

def validate_comment_id(comment_id):
    """ This function will ensure correctness 
    for comment id 

    Parameters
    ----------
    comment_id: int, required
        question to be validated

    Returns
    ------
    comment_id: str, if comment id was validated
        validated comment id
    False, if comment id is invalid
    """

    try:
        comment_id = int(comment_id)
        
        if comment_id == 0:
            return False

        comment_id = str(comment_id)
    except ValueError as e:
        print(e)
        return False

    return comment_id

def validate_commment(comment):
    """ This function will ensure correctness 
    for comments or responses 

    Parameters
    ----------
    comment: str, required
        comment to be validated

    Returns
    ------
    comment: str, if comment was validated
        validated comment
    False, if comment is invalid
    """
    return validate_question(comment)