import random


def get_response(message):
    """ Returns random response according to message received """

    # payload = requests.get(
    #     f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={message}&date={current_date}')
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
     }

    # Return the matching response to the user
    if message == 'fat':
        bot_response = random.choice(jokes['fat'])

    elif message == 'stupid':
        bot_response = random.choice(jokes['stupid'])

    elif message == 'dumb':
        bot_response = random.choice(jokes['dumb'])

    elif message in ['hi', 'hey', 'hello']:
        bot_response = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        bot_response = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return bot_response

