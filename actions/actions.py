# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from email import charset
from email.policy import strict
from encodings import utf_8
from typing import Any, Text, Dict, List
from matplotlib.font_manager import json_dump

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
from mysql.connector import Error
import json
from datetime import datetime




class ActionSelect_Seminar_Events(Action):


    def name(self) -> Text:
        return "select_seminar_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE type='Σεμινάριο'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
               dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
        return[]
        

class ActionSelect_Speach_Events(Action):


    def name(self) -> Text:
        return "select_speach_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE type='Ομιλία'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
                dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
            return[]    

class ActionSelect_Theatre_Events(Action):


    def name(self) -> Text:
        return "select_theatre_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE type='Θεατρική Παράσταση'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
                dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
            return[]            


class ActionSelect_Painting_Events(Action):


    def name(self) -> Text:
        return "select_painting_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE type='Έκθεση ζωγραφικής'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
                dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
            return[]    

class ActionSelect_Athens_Events(Action):


    def name(self) -> Text:
        return "select_athens_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE city='Αθήνα'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
                dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
            return[]    

class ActionSelect_Thessaloniki_Events(Action):


    def name(self) -> Text:
        return "select_thessaloniki_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='rasadatabase',
                                                user='root',
                                                password='', charset='utf8')
            

            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE city='Θεσσαλονίκη'"
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Total number of results: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("I found the event: "+(row[1])+", type "+(row[6])+" at "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" on"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" o'clock in "+(row[4])+" at the location, "+(row[5])) 
            else :
                dispatcher.utter_message("Error while connecting to MySQL", e)
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
            return[]                                               
