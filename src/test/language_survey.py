from survey import AnonymousSurvey

# 설문을 정의하고 설문조사를 만듦니다.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# 설문을 표시하고 응답을 저장
language_survey.show_question()
print("Enter 'q' at any time to quit.")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# 설문 결과를 표시
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()