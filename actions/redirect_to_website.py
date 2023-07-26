# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict

import datetime as dt
import webbrowser

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_show_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         url = 'https://amazon.com'

#         webbrowser.open_new(url)

#         dispatcher.utter_message(text=f"{dt.datetime.now()}")

#         return []

    
import requests
from rasa_sdk.events import SlotSet

class RedirecttoUserShopPage(Action):

    def name(self) -> Text:
        return "action_redirect_to_userShopPage"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot('email')
        # api_token = <YOUR_API_TOKEN>
        url = "https://dummy.restapiexample.com/api/v1/employees/1"
        # payload = {"q": city, "appid": api_token, "units": "metric", "lang": "en"}
        
        response = requests.get(url)
        if response.ok:
           response_data = response.json()
           employee_name = response_data["data"]["employee_name"]
           msg = f"Redirecting you to the Shop Page: {employee_name}, {email}"

        else: 
           msg = f"Shop not found with provided email address:"

        dispatcher.utter_message(msg )
        return [SlotSet("email", None)]


class RedirecttoOrderPage(Action):

    def name(self) -> Text:
        return "action_redirect_to_orderPage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
            url = 'https://lowes.com'
            webbrowser.open_new(url)
            dispatcher.utter_message(text=f"{dt.datetime.now()}")

            return []
    
class RedirecttoFAQ(Action):

    def name(self) -> Text:
        return "action_redirect_to_FAQ"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
            url = 'https://amazon.com'
            webbrowser.open_new(url)
            dispatcher.utter_message(text=f"{dt.datetime.now()}")

            return []
    
class RedirecttoReward(Action):

    def name(self) -> Text:
        return "action_redirect_to_Reward"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
            url = 'https://etsy.com'
            webbrowser.open_new(url)
            dispatcher.utter_message(text=f"{dt.datetime.now()}")

            return []