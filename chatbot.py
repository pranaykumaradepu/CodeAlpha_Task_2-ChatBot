import json
import re
import random_responses


# to load json file
def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)


# To store json file
responses_data = load_json("responses.json")


def get_responses(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # to check all the responses
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # to check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # the amount of required words should match the required score
        if required_score == len(required_words):
            # to check each word the user entered
            for word in split_message:
                # to add the word which is in the response, add to the score
                if word in response['user_input']:
                    response_score += 1

        # to add score to list
        score_list.append(response_score)

    # to Find the best response and return it if they are not all zero
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # to check if input is empty
    if best_response != 0:
        return responses_data[response_index]["bot_response"]

    return random_responses.random_string()


bot = True
while bot:
    user_input = input("You: ")
    print("Bot:", get_responses(user_input))
    if user_input in ["see you", "goodbye", "bye", "exit"]:
        bot = False
