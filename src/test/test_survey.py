from survey import AnonymousSurvey

def test_store_single_response():
    """Test storing a single response in the survey."""
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)
    survey.store_response("English")

    # Check that the response was stored correctly
    assert survey.responses == ["English"]
