"""constants.py"""

from typing import List, Dict, Text
import openai
from constants import GPT_3DOT5_TURBO, DEPLOYMENT_NAME


def construct_messages(query:Text):
    messages = [
        # {'role': 'system',
        #  'content': """You are an assistant who responds in the style of Dr Seuss."""},
        {'role': 'user',
         'content': query},
    ]
    return messages


def get_chat_completion(messages: List[Dict], model=GPT_3DOT5_TURBO,
                                 temperature=0, use_azure_openai=True):
    """

    :param messages:
        messages =  [
        {'role':'system',
         'content': CLASSIFY_SYSTEM_MESSAGE},
        {'role':'user',
         'content': f"{DELIMITER}{user_message}{DELIMITER}"},
    ]
    :param model:
    :param temperature:
    :return:
    """
    if use_azure_openai:
        deployment_name = DEPLOYMENT_NAME if use_azure_openai else None
        response = openai.ChatCompletion.create(
            model=model,
            engine=deployment_name,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
    else:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        #     print(str(response.choices[0].message))
        content = response.choices[0].message["content"]

        token_dict = {
            'prompt_tokens': response['usage']['prompt_tokens'],
            'completion_tokens': response['usage']['completion_tokens'],
            'total_tokens': response['usage']['total_tokens'],
        }
    return content
