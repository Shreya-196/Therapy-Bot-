from rasa_sdk import Action,Tracker 
from rasa_sdk.events import SlotSet
from typing import Any,Text,Dict,List
from rasa_sdk.executor import CollectingDispatcher
import random 

class ActionBreathingExercise(Action):

    def name(self) -> Text:
        return "action_breathing_exercise"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Any, Any]]:

        user_mood = tracker.get_slot("mood") 
        breathing_exercise = ""

        if user_mood.lower() in ["stressed"]:
            breathing_exercise = """
            Box Breathing:
            1. Inhale slowly and deeply for 4 seconds.
            2. Hold your breath for 4 seconds.
            3. Exhale slowly for 4 seconds.
            4. Hold your breath for 4 seconds.
            Repeat this cycle for 5-10 minutes.
            """
        elif user_mood.lower() in ["sad", "depressed"]:
            breathing_exercise = """
            **Diaphragmatic Breathing:**
            1. Lie down or sit comfortably.
            2. Place one hand on your chest and the other on your belly.
            3. Inhale slowly and deeply through your nose, allowing your belly to rise.
            4. Exhale slowly through your mouth, allowing your belly to fall.
            5. Focus on the sensation of your breath.
            Repeat this for 5-10 minutes.
            """
        elif user_mood.lower() in ["anxious"]:
            breathing_exercise = """
            4-7-8 Breathing:
            1. Inhale slowly through your nose for 4 seconds.
            2. Hold your breath for 7 seconds.
            3. Exhale slowly through your mouth for 8 seconds.
            Repeat this cycle for 4-5 times.
            """
        else:
            breathing_exercise = """
            Simple Deep Breathing:
            1. Inhale slowly and deeply through your nose.
            2. Exhale slowly and completely through your mouth.
            3. Repeat this for a few minutes, focusing on the sensation of your breath.
            """

        dispatcher.utter_message(text=f"Here's a breathing exercise that might help: {breathing_exercise}")
        return []

class ActionGenerateStrengthsAffirmations(Action):
    def name(self) -> Text:
        return "action_generate_strengths_affirmations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Any, Any]]:
        user_strengths = tracker.get_slot("user_strengths")
        
        print(f"User strength: {user_strengths}")  # Debugging line to check the slot value
        
        if not user_strengths:
            dispatcher.utter_message(text="Please tell me about some of your strengths.")
            return []

        # Check the strength and generate affirmations based on it
        if user_strengths.lower() == "creative":
            affirmations = [
                "I am a wellspring of creative ideas.",
                "I can find innovative solutions to challenges.",
                "My creativity allows me to see the world in new and exciting ways.",
                "I make a difference to this world.",
                "I am not worthless!"
            ]
        elif user_strengths.lower() == "kind":
            affirmations = [
                "My kindness makes a positive impact on the world.",
                "I treat others with compassion and understanding.",
                "I am a source of warmth and support for those around me.",
                "I make a difference to this world.",
                "I am not worthless!"
            ]
        elif user_strengths.lower() == "resilient":
            affirmations = [
                "I can bounce back from setbacks with strength and determination.",
                "I am adaptable and can overcome challenges.",
                "I believe in myself and my ability to persevere.",
                "I make a difference to this world.",
                "I am not worthless!"
            ]
        elif user_strengths.lower() == "organized":
            affirmations = [
                "I am efficient and effective in my approach to tasks.",
                "I can plan and execute my goals with precision.",
                "I create order and structure in my life.",
                "I make a difference to this world.",
                "I am not worthless!"
            ]
        else:
            affirmations = [
                f"I am confident in my ability to {user_strengths}.",
                f"I am proud of my {user_strengths}.",
                f"I am capable of achieving great things because of my {user_strengths}.",
                f"I embrace and celebrate my {user_strengths}.",
                "I make a difference to this world.",
                "I am not worthless!"
            ]

        # Send each affirmation as a separate message
        for affirmation in affirmations:
            dispatcher.utter_message(text=affirmation)
        
        return []

class ActionTeachMeditation(Action):

    def name(self) -> Text:
        return "action_teach_meditation"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Any, Any]]:

        user_issue = tracker.get_slot("mood") 

        meditation_guidance = []

        if user_issue.lower() in ["depression", "sadness"]:
            meditation_guidance = [ """
            **Mindful Breathing for Depression:**
            1. Find a quiet place where you won't be disturbed.
            2. Sit comfortably with your back straight.
            3. Gently close your eyes.
            4. Bring your attention to your breath. Notice the sensation of the air as it enters and exits your body. 
            5. If your mind wanders, gently guide it back to your breath. 
            6. Continue for 5-10 minutes. 
            This meditation can help you become more aware of the present moment and reduce rumination on negative thoughts.
            """ ]

        elif user_issue.lower() in ["insomnia", "sleep"]:
            meditation_guidance = ["""
            **Relaxation Meditation for Insomnia:**
            1. Find a quiet, comfortable place to lie down.
            2. Close your eyes and take slow, deep breaths.
            3. Imagine a peaceful and relaxing scene, such as a beach or a forest.
            4. Focus on the sights, sounds, and sensations of this peaceful scene.
            5. If your mind wanders, gently guide it back to the relaxing scene.
            6. Continue for 10-15 minutes before sleep.
            This meditation can help calm your mind and body, making it easier to fall asleep.
            """]

        elif user_issue.lower() in ["anger", "frustration"]:
            meditation_guidance = ["""
            **Cooling Down Meditation for Anger:**
            1. When you feel anger arising, find a quiet place.
            2. Close your eyes and bring your attention to your breath. 
            3. Notice the physical sensations of anger in your body (e.g., tightness in the chest, clenched fists).
            4. Gently acknowledge these sensations without judgment.
            5. Imagine a cooling image, such as a calm lake or a winter snowfall.
            6. Allow the cooling image to soothe and calm your mind and body.
            This meditation can help you become more aware of your anger and develop healthier ways to cope with it.
            """]

        else:
            meditation_guidance = ["""
            **General Mindfulness Meditation:**
            1. Find a quiet place where you won't be disturbed.
            2. Sit comfortably with your back straight.
            3. Gently close your eyes.
            4. Bring your attention to your breath. Notice the sensation of the air as it enters and exits your body. 
            5. If your mind wanders, gently guide it back to your breath. 
            6. Continue for 5-10 minutes. 
            This meditation can help increase mindfulness and reduce stress.
            """]

        for step in meditation_guidance:
            dispatcher.utter_message(text=step)
        return []
    