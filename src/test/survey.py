class AnonymousSurvey:
    """A class to represent an anonymous survey."""
    
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        """ display the survey question """
        print(self.question)
    
    def store_response(self, new_response):
        """ store a response to the survey """
        self.responses.append(new_response)

    def show_results(self):
        """ show all the responses that have been given """
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
