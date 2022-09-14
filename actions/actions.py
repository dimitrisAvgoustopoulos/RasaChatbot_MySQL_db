# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from email import charset
from email.policy import strict
from encodings import utf_8
from html import entities
from typing import Any, Text, Dict, List
from matplotlib.font_manager import json_dump

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import mysql.connector
from mysql.connector import Error
import json







class Action_SQL_Query(Action):


    def name(self) -> Text:
        return "sql_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        



        # SeminarSlotValue=tracker.get_slot("seminar")
        # SpeechSlotValue=tracker.get_slot("speech")
        # TheatreSlotValue=tracker.get_slot("theatre")
        # PaintingSlotValue=tracker.get_slot("painting")
        # LocationSlotValue=tracker.get_slot("location")

        # latEntitType= tracker.latest_message['intents'].get('name')

        latEntitType= tracker.latest_message['entities'][0]['entity']
        latEntitValue= tracker.latest_message['entities'][0]['value']

        sqltypevar=""
        sqlcityvar=""
        sqlQuery=""



        if (latEntitType=="Seminar"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Σεμινάριο'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)

        elif (latEntitType=="Speech"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Ομιλία'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)

        elif (latEntitType=="Theatre"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Θέατρο'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)

        elif (latEntitType=="Painting"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Ζωγραφική'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)

        elif (latEntitType=="Concert"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Συναυλία'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)

        elif (latEntitType=="Festival"):

                dispatcher.utter_message("Κατηγορία: {}".format(latEntitType))
                sqltypevar='Φεστιβάλ'
                sqlQuery="SELECT * FROM events WHERE type='%s'" % (sqltypevar)


        elif (latEntitValue=="Αθήνα" or latEntitValue=="αθήνα"):

                dispatcher.utter_message("Κeyword Τοποθεσίας: {}".format(latEntitValue))
                sqlcityvar='Αθήνα' 
                sqlQuery="SELECT * FROM events WHERE city='%s'" % (sqlcityvar)

        elif (latEntitValue=="Θεσσαλονίκη" or latEntitValue=="θεσσαλονίκη" ):

                dispatcher.utter_message("Location Τοποθεσίας: {}".format(latEntitValue))
                sqlcityvar='Θεσσαλονίκη'
                sqlQuery="SELECT * FROM events WHERE city='%s'" % (sqlcityvar)

        elif (latEntitValue=="Πάτρα" or latEntitValue=="πάτρα"):

                dispatcher.utter_message("Location Τοποθεσίας: {}".format(latEntitValue))
                sqlcityvar='Πάτρα'
                sqlQuery="SELECT * FROM events WHERE city='%s'" % (sqlcityvar)

        #year
        
        if (latEntitValue=="2022"):
             sqlQuery="SELECT * FROM events WHERE day LIKE '%%%s%%' "%(latEntitValue)

        elif(latEntitValue=="2023"):
             sqlQuery="SELECT * FROM events WHERE day LIKE '%%%s%%' "%(latEntitValue)

        #SQL
 

        connection = mysql.connector.connect(host='mysql-ptuxiakh.alwaysdata.net', port='3306', database='ptuxiakh_events', user='ptuxiakh', password='1531998aA@', charset='utf8')
        cursor = connection.cursor() 
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Συνολικός αριθμός αποτελεσμάτων: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("Βρήκα την εκδήλωση: "+(row[1])+", τύπος "+(row[6])+" στις "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" στις"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+", στην "+(row[4])+" στην τοποθεσία "+(row[5])) 


            else:
                dispatcher.utter_message("Error while connecting to MySQL", e) 
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()

        return[]# AllSlotsReset if i get values from slots

class Action_SQL_Multiple_Query(Action):


    def name(self) -> Text:
        return "sql_multiple_query1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:




        #for athens events
        SeA_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="1",entity_role="SeminarInAthens"), None)
        SeA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="1",entity_role="SeminarInAthens"),None)
        
        SpA_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="2",entity_role="SpeechInAthens"), None)
        SpA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="2",entity_role="SpeechInAthens"), None)

        ThA_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="3",entity_role="TheatreInAthens"), None)
        ThA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="3",entity_role="TheatreInAthens"), None)
        
        PaA_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="4",entity_role="PaintingInAthens"), None)
        PaA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="4",entity_role="PaintingInAthens"), None)
        
        CoA_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="5",entity_role="ConcertInAthens"), None)
        CoA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="5",entity_role="ConcertInAthens"), None)
        
        FeA_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="6",entity_role="FestivalInAthens"), None)
        FeA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="6",entity_role="FestivalInAthens"), None)
        
        
        #for thessaloniki events
        SeTh_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="7",entity_role="SeminarInThessaloniki"), None)
        SeTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="7",entity_role="SeminarInThessaloniki"), None)
        
        SpTh_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="8",entity_role="SpeechInThessaloniki"), None)
        SpTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="8",entity_role="SpeechInThessaloniki"), None)

        ThTh_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="9",entity_role="TheatreInThessaloniki"), None)
        ThTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="9",entity_role="TheatreInThessaloniki"), None)

        PaTh_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="10",entity_role="PaintingInThessaloniki"), None)
        PaTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="10",entity_role="PaintingInThessaloniki"), None)

        CoTh_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="11",entity_role="ConcertInThessaloniki"), None)
        CoTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="11",entity_role="ConcertInThessaloniki"), None)

        FeTh_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="12",entity_role="FestivalInThessaloniki"), None)
        FeTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="12",entity_role="FestivalInThessaloniki"), None)

        #for patras events
        SePa_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="13",entity_role="SeminarInPatras"), None)
        SePa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="13",entity_role="SeminarInPatras"), None)
        
        SpPa_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="14",entity_role="SpeechInPatras"), None)
        SpPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="14",entity_role="SpeechInPatras"), None)

        ThPa_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="15",entity_role="TheatreInPatras"), None)
        ThPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="15",entity_role="TheatreInPatras"), None)

        PaPa_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="16",entity_role="PaintingInPatras"), None)
        PaPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="16",entity_role="PaintingInPatras"), None)

        CoPa_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="17",entity_role="ConcertInPatras"), None)
        CoPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="17",entity_role="ConcertInPatras"), None)

        FePa_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="18",entity_role="FestivalInPatras"), None)
        FePa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="18",entity_role="FestivalInPatras"), None)
       

        sqlQuery=""
        
        #ATHENS
        if (( SeA_type=="σεμινάρια" or SeA_type=="σεμινάριο") and (SeA_location=="Αθήνα" or SeA_location=="αθήνα")):
       
                dispatcher.utter_message("keywords: {},{}".format( SeA_type,SeA_location))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( SpA_type=="ομιλίες" or SpA_type=="ομιλία") and (SpA_location=="Αθήνα" or SpA_location=="αθήνα")):
       
                dispatcher.utter_message("keywords: {},{}".format( SpA_type,SpA_location))
                sqltypevar="Ομιλία"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)
        
        elif  (( ThA_type=="θέατρο" or ThA_type=="θεατρική παράσταση" or ThA_type=="θεατρικές παραστάσεις") and (ThA_location=="Αθήνα" or ThA_location=="αθήνα")):

                dispatcher.utter_message("keywords: {},{}".format( ThA_type,ThA_location))
                sqltypevar="Θέατρο"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( PaA_type=="ζωγραφική" or PaA_type=="έκθεση ζωγραφικής" or PaA_type=="εκθέσεις ζωγραφικής") and  (PaA_location=="Αθήνα" or PaA_location=="αθήνα")):
       
                dispatcher.utter_message("keywords: {},{}".format( PaA_type,PaA_location))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar) 

        elif  (( CoA_type=="συναυλίες" or CoA_type=="συναυλία") and  (CoA_location=="Αθήνα" or CoA_location=="αθήνα")):
       
                dispatcher.utter_message("keywords: {},{}".format( CoA_type,CoA_location))
                sqltypevar="Συναυλία"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( FeA_type=="φεστιβάλ") and  (FeA_location=="Αθήνα" or FeA_location=="αθήνα")):
       
                dispatcher.utter_message("keywords: {},{}".format( FeA_type,FeA_location))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Αθήνα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)  


        #THESSALONIKI
        if (( SeTh_type=="σεμινάρια" or SeTh_type=="σεμινάριο") and (SeTh_location=="Θεσσαλονίκη" or SeTh_location=="θεσσαλονίκη")):
       
                dispatcher.utter_message("keywords: {},{}".format( SeTh_type,SeTh_location))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( SpTh_type=="ομιλίες" or SpTh_type=="ομιλία") and (SpTh_location=="Θεσσαλονίκη" or SpTh_location=="θεσσαλονίκη")):
       
                dispatcher.utter_message("keywords: {},{}".format( SpTh_type,SpTh_location))
                sqltypevar="Ομιλία"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)
        
        elif  (( ThTh_type=="θέατρο" or ThTh_type=="θεατρική παράσταση" or ThTh_type=="θεατρικές παραστάσεις") and (ThTh_location=="Θεσσαλονίκη" or ThTh_location=="θεσσαλονίκη")):

                dispatcher.utter_message("keywords: {},{}".format( ThTh_type,ThTh_location))
                sqltypevar="Θέατρο"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( PaTh_type=="ζωγραφική" or PaTh_type=="έκθεση ζωγραφικής" or PaTh_type=="εκθέσεις ζωγραφικής") and  (PaTh_location=="Θεσσαλονίκη" or PaTh_location=="θεσσαλονίκη")):
       
                dispatcher.utter_message("keywords: {},{}".format( PaTh_type,PaTh_location))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( CoTh_type=="συναυλίες" or CoTh_type=="συναυλία") and  (CoTh_location=="Θεσσαλονίκη" or CoTh_location=="θεσσαλονίκη")):
       
                dispatcher.utter_message("keywords: {},{}".format( CoTh_type,CoTh_location))
                sqltypevar="Συναυλία"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( FeTh_type=="φεστιβάλ") and  (FeTh_location=="Θεσσαλονίκη" or FeTh_location=="θεσσαλονίκη")):
       
                dispatcher.utter_message("keywords: {},{}".format( FeTh_type,FeTh_location))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Θεσσαλονίκη"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)   

        #PATRAS
        if (( SePa_type=="σεμινάρια" or SePa_type=="σεμινάριο") and (SePa_location=="Πάτρα" or SePa_location=="πάτρα")):
       
                dispatcher.utter_message("keywords: {},{}".format( SePa_type,SePa_location))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( SpPa_type=="ομιλίες" or SpPa_type=="ομιλία") and (SpPa_location=="Πάτρα" or SpPa_location=="πάτρα")):
       
                dispatcher.utter_message("keywords: {},{}".format( SpPa_type,SpPa_location))
                sqltypevar="Ομιλία"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)
        
        elif  (( ThPa_type=="θέατρο" or ThPa_type=="θεατρική παράσταση" or ThPa_type=="θεατρικές παραστάσεις") and (ThPa_location=="Πάτρα" or ThPa_location=="πάτρα")):

                dispatcher.utter_message("keywords: {},{}".format( ThPa_type,ThPa_location))
                sqltypevar="Θέατρο"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( PaPa_type=="ζωγραφική" or PaPa_type=="έκθεση ζωγραφικής" or PaPa_type=="εκθέσεις ζωγραφικής") and  (PaPa_location=="Πάτρα" or PaPa_location=="πάτρα")):
       
                dispatcher.utter_message("keywords: {},{}".format( PaPa_type,PaPa_location))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( CoPa_type=="συναυλίες" or CoPa_type=="συναυλία") and  (CoPa_location=="Πάτρα" or CoPa_location=="πάτρα")):
       
                dispatcher.utter_message("keywords: {},{}".format( CoPa_type,CoPa_location))
                sqltypevar="Συναυλία"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)

        elif  (( FePa_type=="φεστιβάλ") and  (FePa_location=="Πάτρα" or FePa_location=="πάτρα")):
       
                dispatcher.utter_message("keywords: {},{}".format( FePa_type,FePa_location))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Πάτρα"
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)
                


        #SQL


        connection = mysql.connector.connect(host='mysql-ptuxiakh.alwaysdata.net', port='3306', database='ptuxiakh_events', user='ptuxiakh', password='1531998aA@', charset='utf8')
        cursor = connection.cursor()
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Συνολικός αριθμός αποτελεσμάτων: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("Βρήκα την εκδήλωση: "+(row[1])+", τύπος "+(row[6])+" στις "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" στις"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+", στην "+(row[4])+" στην τοποθεσία "+(row[5])) 


            else:
                dispatcher.utter_message("Error while connecting to MySQL", e) 
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
        return[]



class Action_SQL_Multiple_Query(Action):


    def name(self) -> Text:
        return "sql_multiple_query2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:




        #for athens events
        SeA_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="1",entity_role="SeminarInAthens"), None)
        SeA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="1",entity_role="SeminarInAthens"),None)
        SeA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        SpA_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="2",entity_role="SpeechInAthens"), None)
        SpA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="2",entity_role="SpeechInAthens"), None)
        SpA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        ThA_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="3",entity_role="TheatreInAthens"), None)
        ThA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="3",entity_role="TheatreInAthens"), None)
        ThA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        PaA_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="4",entity_role="PaintingInAthens"), None)
        PaA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="4",entity_role="PaintingInAthens"), None)
        PaA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        CoA_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="5",entity_role="ConcertInAthens"), None)
        CoA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="5",entity_role="ConcertInAthens"), None)
        CoA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        FeA_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="6",entity_role="FestivalInAthens"), None)
        FeA_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="6",entity_role="FestivalInAthens"), None)
        FeA_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)
        
        
        #for thessaloniki events
        SeTh_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="7",entity_role="SeminarInThessaloniki"), None)
        SeTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="7",entity_role="SeminarInThessaloniki"), None)
        SeTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        SpTh_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="8",entity_role="SpeechInThessaloniki"), None)
        SpTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="8",entity_role="SpeechInThessaloniki"), None)
        SpTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        ThTh_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="9",entity_role="TheatreInThessaloniki"), None)
        ThTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="9",entity_role="TheatreInThessaloniki"), None)
        ThTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        PaTh_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="10",entity_role="PaintingInThessaloniki"), None)
        PaTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="10",entity_role="PaintingInThessaloniki"), None)
        PaTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        CoTh_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="11",entity_role="ConcertInThessaloniki"), None)
        CoTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="11",entity_role="ConcertInThessaloniki"), None)
        CoTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        FeTh_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="12",entity_role="FestivalInThessaloniki"), None)
        FeTh_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="12",entity_role="FestivalInThessaloniki"), None)
        FeTh_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        #for patras events
        SePa_type= next(tracker.get_latest_entity_values(entity_type="Seminar",entity_group="13",entity_role="SeminarInPatras"), None)
        SePa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="13",entity_role="SeminarInPatras"), None)
        SePa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        SpPa_type= next(tracker.get_latest_entity_values(entity_type="Speech",entity_group="14",entity_role="SpeechInPatras"), None)
        SpPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="14",entity_role="SpeechInPatras"), None)
        SpPa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        ThPa_type= next(tracker.get_latest_entity_values(entity_type="Theatre",entity_group="15",entity_role="TheatreInPatras"), None)
        ThPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="15",entity_role="TheatreInPatras"), None)
        ThPa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        PaPa_type= next(tracker.get_latest_entity_values(entity_type="Painting",entity_group="16",entity_role="PaintingInPatras"), None)
        PaPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="16",entity_role="PaintingInPatras"), None)
        PaPa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        CoPa_type= next(tracker.get_latest_entity_values(entity_type="Concert",entity_group="17",entity_role="ConcertInPatras"), None)
        CoPa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="17",entity_role="ConcertInPatras"), None)
        CoPa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        FePa_type= next(tracker.get_latest_entity_values(entity_type="Festival",entity_group="18",entity_role="FestivalInPatras"), None)
        FePa_location= next(tracker.get_latest_entity_values(entity_type="Location", entity_group="18",entity_role="FestivalInPatras"), None)
        FePa_Year=next(tracker.get_latest_entity_values(entity_type="Year", entity_group="0",entity_role="EventYear"),None)

        sqlQuery=""
        
        #ATHENS
        #search with year
        if (( SeA_type=="σεμινάρια" or SeA_type=="σεμινάριο") and (SeA_location=="Αθήνα" or SeA_location=="αθήνα") and (SeA_Year=="2022" or SeA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SeA_type,SeA_location,SeA_Year))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Αθήνα"
                sqlyear=SeA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif ((SpA_type=="ομιλίες" or SpA_type=="ομιλία") and (SpA_location=="Αθήνα" or SpA_location=="αθήνα") and (SpA_Year=="2022" or SpA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SpA_type,SpA_location,SpA_Year))
                sqltypevar="Ομιλία"
                sqlcityvar="Αθήνα"
                sqlyear=SpA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
        
        elif (( ThA_type=="θέατρο" or ThA_type=="θεατρική παράσταση" or ThA_type=="θεατρικές παραστάσεις") and (ThA_location=="Αθήνα" or ThA_location=="αθήνα") and (ThA_Year=="2022" or ThA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( ThA_type,ThA_location,ThA_Year))
                sqltypevar="Θέατρο"
                sqlcityvar="Αθήνα"
                sqlyear=ThA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
        
        elif (( PaA_type=="ζωγραφική" or PaA_type=="έκθεση ζωγραφικής" or PaA_type=="εκθέσεις ζωγραφικής") and  (PaA_location=="Αθήνα" or PaA_location=="αθήνα") and (PaA_Year=="2022" or PaA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( PaA_type,PaA_location,PaA_Year))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Αθήνα"
                sqlyear=PaA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
        
        elif (( CoA_type=="συναυλίες" or CoA_type=="συναυλία") and  (CoA_location=="Αθήνα" or CoA_location=="αθήνα") and (CoA_Year=="2022" or CoA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( CoA_type,CoA_location,CoA_Year))
                sqltypevar="Συναυλία"
                sqlcityvar="Αθήνα"
                sqlyear=CoA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
        
        elif (( FeA_type=="φεστιβάλ") and  (FeA_location=="Αθήνα" or FeA_location=="αθήνα") and (FeA_Year=="2022" or FeA_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( FeA_type,FeA_location,FeA_Year))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Αθήνα"
                sqlyear=FeA_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        #THESSALONIKI
        #search with year
        if (( SeTh_type=="σεμινάρια" or SeTh_type=="σεμινάριο") and (SeTh_location=="Θεσσαλονίκη" or SeTh_location=="θεσσαλονίκη") and (SeTh_Year=="2022" or SeTh_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SeTh_type,SeTh_location,SeTh_Year))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=SeTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( SpTh_type=="ομιλίες" or SpTh_type=="ομιλία") and (SpTh_location=="Θεσσαλονίκη" or SpTh_location=="θεσσαλονίκη") and (SpTh_Year=="2022" or SpTh_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SpTh_type,SpTh_location,SpTh_Year))
                sqltypevar="Ομιλία"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=SpTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
        
        elif  (( ThTh_type=="θέατρο" or ThTh_type=="θεατρική παράσταση" or ThTh_type=="θεατρικές παραστάσεις") and (ThTh_location=="Θεσσαλονίκη" or ThTh_location=="θεσσαλονίκη") and (ThTh_Year=="2022" or ThTh_Year=="2023")):

                dispatcher.utter_message("keywords: {},{},{}".format( ThTh_type,ThTh_location,ThTh_Year))
                sqltypevar="Θέατρο"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=ThTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( PaTh_type=="ζωγραφική" or PaTh_type=="έκθεση ζωγραφικής" or PaTh_type=="εκθέσεις ζωγραφικής") and  (PaTh_location=="Θεσσαλονίκη" or PaTh_location=="θεσσαλονίκη") and (PaTh_Year=="2022" or PaTh_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( PaTh_type,PaTh_location,PaTh_Year))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=PaTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( CoTh_type=="συναυλίες" or CoTh_type=="συναυλία") and  (CoTh_location=="Θεσσαλονίκη" or CoTh_location=="θεσσαλονίκη") and (CoTh_Year=="2022" or CoTh_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( CoTh_type,CoTh_location,CoTh_Year))
                sqltypevar="Συναυλία"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=CoTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( FeTh_type=="φεστιβάλ") and  (FeTh_location=="Θεσσαλονίκη" or FeTh_location=="θεσσαλονίκη") and (FeTh_Year=="2022" or FeTh_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( FeTh_type,FeTh_location,FeTh_Year))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Θεσσαλονίκη"
                sqlyear=FeTh_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        #PATRAS
        #search with year
        if (( SePa_type=="σεμινάρια" or SePa_type=="σεμινάριο") and (SePa_location=="Πάτρα" or SePa_location=="πάτρα") and (SePa_Year=="2022" or SePa_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SePa_type,SePa_location,SePa_Year))
                sqltypevar="Σεμινάριο"
                sqlcityvar="Πάτρα"
                sqlyear=SePa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( SpPa_type=="ομιλίες" or SpPa_type=="ομιλία") and (SpPa_location=="Πάτρα" or SpPa_location=="πάτρα") and (SpPa_Year=="2022" or SpPa_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( SpPa_type,SpPa_location,SpPa_Year))
                sqltypevar="Ομιλία"
                sqlcityvar="Πάτρα"
                sqlyear=SpPa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s'" % (sqltypevar, sqlcityvar)
        
        elif  (( ThPa_type=="θέατρο" or ThPa_type=="θεατρική παράσταση" or ThPa_type=="θεατρικές παραστάσεις") and (ThPa_location=="Πάτρα" or ThPa_location=="πάτρα") and (ThPa_Year=="2022" or ThPa_Year=="2023")):

                dispatcher.utter_message("keywords: {},{},{}".format( ThPa_type,ThPa_location,ThPa_Year))
                sqltypevar="Θέατρο"
                sqlcityvar="Πάτρα"
                sqlyear=ThPa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( PaPa_type=="ζωγραφική" or PaPa_type=="έκθεση ζωγραφικής" or PaPa_type=="εκθέσεις ζωγραφικής") and  (PaPa_location=="Πάτρα" or PaPa_location=="πάτρα") and (PaPa_Year=="2022" or PaPa_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( PaPa_type,PaPa_location,PaPa_Year))
                sqltypevar="Ζωγραφική"
                sqlcityvar="Πάτρα"
                sqlyear=PaPa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( CoPa_type=="συναυλίες" or CoPa_type=="συναυλία") and  (CoPa_location=="Πάτρα" or CoPa_location=="πάτρα") and (CoPa_Year=="2022" or CoPa_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( CoPa_type,CoPa_location,CoPa_Year))
                sqltypevar="Συναυλία"
                sqlcityvar="Πάτρα"
                sqlyear=CoPa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)

        elif  (( FePa_type=="φεστιβάλ") and  (FePa_location=="Πάτρα" or FePa_location=="πάτρα") and (FePa_Year=="2022" or FePa_Year=="2023")):
       
                dispatcher.utter_message("keywords: {},{},{}".format( FePa_type,FePa_location,FePa_Year))
                sqltypevar="Φεστιβάλ"
                sqlcityvar="Πάτρα"
                sqlyear=FePa_Year
                sqlQuery="SELECT * FROM events WHERE type='%s' AND city='%s' AND day LIKE '%%%s%%'" % (sqltypevar, sqlcityvar,sqlyear)
                


        #SQL


        connection = mysql.connector.connect(host='mysql-ptuxiakh.alwaysdata.net', port='3306', database='ptuxiakh_events', user='ptuxiakh', password='1531998aA@', charset='utf8')
        cursor = connection.cursor()
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Συνολικός αριθμός αποτελεσμάτων: "+json.dumps(cursor.rowcount))

                for row in records:
                    date=(row[2])
                    time=(row[3])
                    
                    dispatcher.utter_message("Βρήκα την εκδήλωση: "+(row[1])+", τύπος "+(row[6])+" στις "
                    +json.dumps(date, indent=4, sort_keys=True, default=str)+" στις"
                    +json.dumps(time, indent=4, sort_keys=True, default=str)+", στην "+(row[4])+" στην τοποθεσία "+(row[5])) 


            else:
                dispatcher.utter_message("Error while connecting to MySQL", e) 
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
        return[]


class Action_All_Dates(Action):


    def name(self) -> Text:
        return "eventDates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        sqlQuery="SELECt * FROM events"

            
        #SQL
        connection = mysql.connector.connect(host='mysql-ptuxiakh.alwaysdata.net', port='3306', database='ptuxiakh_events', user='ptuxiakh', password='1531998aA@', charset='utf8')
        cursor = connection.cursor()
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery  
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                dispatcher.utter_message("Συνολικός αριθμός αποτελεσμάτων: "+json.dumps(cursor.rowcount))

                for row in records:
                    date= (row[2])
                    time=(row[3])

                    dispatcher.utter_message("Στις "+json.dumps(date, indent=4, sort_keys=True, default=str)+", υπάρχει η εκδήλωση "+row[1]+" τύπου "+(row[6])
                    +" στην τοποθεσία, "+(row[4])+" "+(row[5])+" ώρα "+json.dumps(time, indent=4, sort_keys=True, default=str))
                    


            else:
                dispatcher.utter_message("Error while connecting to MySQL", e) 
        except Error as e:
                dispatcher.utter_message("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                    cursor.close()
                    connection.close()
        return[]
