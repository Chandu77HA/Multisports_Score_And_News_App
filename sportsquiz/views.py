from django.shortcuts import render
import requests
from django.http import JsonResponse
from sportsquiz.models import SportsQuizCategory, SportQuestionModel
import random

# Create your views here.

def sports_quiz_home(request):
    get_sports_quiz = SportsQuizCategory.objects.all().order_by('id')
    context = {
        'sports_data' : get_sports_quiz,
    }
    return render(request,'sportsquiz/sports_quiz_home.html', context)


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

'''
def all_sports_quiz(request):
    if request.method == 'POST':
        print(request.method)
        return render(request, 'sportsquiz/quiz_results.html')
    else:
        category_title = 'All Sports Quiz'  # Change this to the title of the category you want to filter
        all_questions_queryset = SportQuestionModel.objects.filter(category__title=category_title).all()
        questions_queryset = random.sample(list(all_questions_queryset), 5)
        all_sports_quiz_data = {
            'questions_queryset': questions_queryset,
            'category': category_title,
        }
        return render(request, 'sportsquiz/sports_quiz.html', all_sports_quiz_data)
'''

def sports_quiz(request, category_title):
    if request.method == 'POST':
        print(request.POST)
        correct = 0
        incorrect = 0
        total = 0
        score = 0
        selected_answers = {}
        for key, value in request.POST.items():
            # print(key, value)
            if key.startswith('Question_'):
                total = total + 1
                question_id = int(key.split('_')[1])
                get_answer = SportQuestionModel.objects.get(pk=question_id).answer
                if value == get_answer:
                    correct = correct + 1
                    score = score + 1
                else:
                    incorrect = incorrect + 1
                    score = score - 0.25
                selected_answers[question_id] = value
        if score > 0:
            quiz_percentage = (score/total) * 100
        else:
            quiz_percentage = 0
        quiz_result = {
            'category_title':category_title,
            'total':total,
            'selected_answers': selected_answers,
            'correct': correct,
            'incorrect': incorrect,
            'score': score,
            'quiz_percentage':quiz_percentage,
        }
        return render(request, 'sportsquiz/quiz_results.html', quiz_result)
    else:
        questions_queryset = SportQuestionModel.objects.filter(category__title=category_title)[:10]
        # all_questions_queryset = SportQuestionModel.objects.filter(category__title=category_title).all()
        # questions_queryset = random.sample(list(all_questions_queryset), 10)
        all_sports_quiz_data = {
            'questions_queryset': questions_queryset,
            'category': category_title,
        }
        return render(request, 'sportsquiz/sports_quiz.html', all_sports_quiz_data)
