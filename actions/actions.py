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
from rasa_sdk.events import SlotSet, AllSlotsReset
import mysql.connector
from mysql.connector import Error
import json
from datetime import datetime





class ActionSelect_Seminar_Events(Action):


    def name(self) -> Text:
        return "sql_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        SeminarSlotValue=tracker.get_slot("seminar")
        SpeechSlotValue=tracker.get_slot("speech")
        TheatreSlotValue=tracker.get_slot("theatre")
        PaintingSlotValue=tracker.get_slot("painting")
        LocationSlotValue=tracker.get_slot("location")
      
      
        sqltypevar=""
        sqlcityvar=""
        
        if SeminarSlotValue=="σεμινάρια" or SeminarSlotValue=="σεμινάριο":

                dispatcher.utter_message("keyword: {}".format(SeminarSlotValue))
                sqltypevar='Σεμινάριο'

        elif SpeechSlotValue=="ομιλίες" or SpeechSlotValue=="ομιλία":

                dispatcher.utter_message("keyword: {}".format(SpeechSlotValue))
                sqltypevar='Ομιλία'
            
        elif TheatreSlotValue=="θέατρο" or TheatreSlotValue=="θεατρικές παραστάσεις" or TheatreSlotValue=="θεατρική παράσταση":

                dispatcher.utter_message("keyword: {}".format(TheatreSlotValue))
                sqltypevar='Θεατρική Παράσταση'
        
        elif PaintingSlotValue=="ζωγραφική" or  PaintingSlotValue=="έκθεση ζωγραφικής" or PaintingSlotValue=="εκθέσεις ζωγραφικής":

                dispatcher.utter_message("keyword: {}".format(PaintingSlotValue))
                sqltypevar='Έκθεση ζωγραφικής'

        elif LocationSlotValue=="Αθήνα":

                dispatcher.utter_message("keyword: {}".format(LocationSlotValue))
                sqlcityvar='Αθήνα' 

        elif LocationSlotValue=="Θεσσαλονίκη":

                dispatcher.utter_message("keyword: {}".format(LocationSlotValue))
                sqlcityvar='Θεσσαλονίκη'



        connection = mysql.connector.connect(host='mysql-ptuxiakh.alwaysdata.net', port='3306', database='ptuxiakh_events', user='ptuxiakh', password='1531998aA@', charset='utf8')
           
        try:
            
            if connection.is_connected():
                sql_select_Query = "SELECT * FROM events WHERE type='%s' OR city='%s'" % (sqltypevar, sqlcityvar)
                cursor = connection.cursor()  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Συνολικός αριθμός αποτελεσμάτων: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("Βρήκα την εκδήλωση: "+(row[1])+", τύπος "+(row[6])+" στις "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" στις"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+" στην "+(row[4])+" στην τοποθεσία, "+(row[5])) 

                
            else:
                dispatcher.utter_message("Error while connecting to MySQL", e) 
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()

        return[AllSlotsReset()]
        
