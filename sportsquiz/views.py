from django.shortcuts import render
import requests
from django.http import JsonResponse
from sportsquiz.models import SportsQuizCategory, SportQuestionModel
import random

# Create your views here.


# Saving General Knowledge Quiz Questions in Model From API
def general_knowledge_api(request):
    try:
        url = "https://quiz26.p.rapidapi.com/questions"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "quiz26.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad responses (4xx or 5xx)
        gk_quiz_data = response.json()
        
        quiz_category = SportsQuizCategory.objects.get(title='General Knowledge Quiz')

        for question_data in gk_quiz_data:

            # Check if the question already exists in the database
            existing_question = SportQuestionModel.objects.filter(question = question_data['question']).first()
            if existing_question is None:

                # Save the answer in question_answer variable from options
                if question_data['answer'] == 'A':
                    question_answer = question_data['A']
                elif question_data['answer'] == 'B':
                    question_answer = question_data['B']
                elif question_data['answer'] == 'C':
                    question_answer = question_data['C']
                else:
                    question_answer = question_data['D']

                # If the question does not exist, create a new instance
                SportQuestionModel.objects.create(
                    question = question_data['question'],
                    option1 = question_data['A'],
                    option2 = question_data['B'],
                    option3 = question_data['C'],
                    option4 = question_data['D'],
                    answer = question_answer,
                    category = quiz_category,
                )
        response_data = {'message': 'All the General Knowledge Questions and Answers Saved Successfully in the Model SportQuestionModel'}
        return JsonResponse(response_data, safe=False)

    except Exception as e:
        # Handle exceptions, log the error, and return an appropriate response
        error_message = f"An error occurred in fetching the api: {str(e)}"
        response_data = {'error': error_message}
        return JsonResponse(response_data, status=500, safe=False)

# Saving All Sports Quiz Easy Questions in Model From API
def all_sports_easy_api(request):
    try:
        url = "https://opentdb.com/api.php?amount=20&category=21&difficulty=easy&type=multiple"
        response = requests.get(url)
        data = response.json()
        all_sports_data = data['results']

        quiz_category = SportsQuizCategory.objects.get(title='All Sports Quiz')

        for question_data in all_sports_data:
            existing_question = SportQuestionModel.objects.filter(question = question_data['question']).first()
            if existing_question is None:
                options = list(question_data['incorrect_answers'])
                options.append(question_data['correct_answer'])

                # Shuffle the options randomly
                random.shuffle(options)

                # Save the shuffled options to option1, option2, option3, and option4
                option1, option2, option3, option4 = options

                # If the question does not exist, create a new instance
                # Now you can use option1, option2, option3, option4 to save to your model
                SportQuestionModel.objects.create(
                    question=question_data['question'],
                    option1 = option1,
                    option2 = option2,
                    option3 = option3,
                    option4 = option4,
                    answer = question_data['correct_answer'],
                    category = quiz_category,
                )
        response_data = {'message': 'All Sports Quiz Questions and Answers Saved Successfully in the Model SportQuestionModel'}
        return JsonResponse(response_data)
    except Exception as e:
        # Handle exceptions, log the error, and return an appropriate response
        error_message = f"An error occurred in fetching the api: {str(e)}"
        response_data = {'error': error_message}
        return JsonResponse(response_data, status=500, safe=False)

# Saving All Sports Quiz Medium Questions in Model From API
def all_sports_medium_api(request):
    try:
        url = "https://opentdb.com/api.php?amount=100000&category=21&difficulty=medium&type=multiple"
        response = requests.get(url)
        data = response.json()
        all_sports_data = data['results']

        quiz_category = SportsQuizCategory.objects.get(title='All Sports Quiz')
        print(quiz_category)

        for question_data in all_sports_data:
            existing_question = SportQuestionModel.objects.filter(question = question_data['question']).first()
            if existing_question is None:
                options = list(question_data['incorrect_answers'])
                options.append(question_data['correct_answer'])

                # Shuffle the options randomly
                random.shuffle(options)

                # Save the shuffled options to option1, option2, option3, and option4
                option1, option2, option3, option4 = options

                # If the question does not exist, create a new instance
                # Now you can use option1, option2, option3, option4 to save to your model
                SportQuestionModel.objects.create(
                    question = question_data['question'],
                    option1 = option1,
                    option2 = option2,
                    option3 = option3,
                    option4 = option4,
                    answer = question_data['correct_answer'],
                    category = quiz_category,
                )
        response_data = {'message': 'All Sports Quiz Questions and Answers Saved Successfully in the Model SportQuestionModel'}
        return JsonResponse(response_data)
    except Exception as e:
        # Handle exceptions, log the error, and return an appropriate response
        error_message = f"An error occurred in fetching the api: {str(e)}"
        response_data = {'error': error_message}
        return JsonResponse(response_data, status=500, safe=False)

# Saving All Sports Quiz Hard Questions in Model From API
def all_sports_hard_api(request):
    try:
        url = "https://opentdb.com/api.php?amount=20&category=21&difficulty=hard&type=multiple"
        response = requests.get(url)
        data = response.json()
        all_sports_data = data['results']

        quiz_category = SportsQuizCategory.objects.get(title='All Sports Quiz')
        print(quiz_category)

        for question_data in all_sports_data:
            existing_question = SportQuestionModel.objects.filter(question = question_data['question']).first()
            if existing_question is None:
                options = list(question_data['incorrect_answers'])
                options.append(question_data['correct_answer'])

                # Shuffle the options randomly
                random.shuffle(options)

                # Save the shuffled options to option1, option2, option3, and option4
                option1, option2, option3, option4 = options

                # If the question does not exist, create a new instance
                # Now you can use option1, option2, option3, option4 to save to your model
                SportQuestionModel.objects.create(
                    question = question_data['question'],
                    option1 = option1,
                    option2 = option2,
                    option3 = option3,
                    option4 = option4,
                    answer = question_data['correct_answer'],
                    category = quiz_category,
                )
        response_data = {'message': 'All Sports Quiz Questions and Answers Saved Successfully in the Model SportQuestionModel'}
        return JsonResponse(response_data)
    except Exception as e:
        # Handle exceptions, log the error, and return an appropriate response
        error_message = f"An error occurred in fetching the api: {str(e)}"
        response_data = {'error': error_message}
        return JsonResponse(response_data, status=500, safe=False)
    
def all_sports_api(request):
    url = "https://opentdb.com/api.php?amount=20&category=21&difficulty=hard&type=multiple"
    response = requests.get(url)
    data = response.json()
    quiz_questions_list = SportQuestionModel.objects.filter(category=5).all()

    # Get the count of the queryset
    questions_count = quiz_questions_list.count()
    print(questions_count)
    return JsonResponse(data)
