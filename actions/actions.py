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
from datetime import datetime
import os






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



        #SQL
 

        connection = mysql.connector.connect(host=os.environ['secret1'], port=os.environ['secret2'], database=os.environ['secret3'], user=os.environ['secret4'], password=os.environ['secret5'], charset='utf8')
           
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery
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
        return "sql_multiple_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        import config

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
       

        sqltypevar=""
        sqlcityvar=""
        sqlQuery=""
        
        #athens
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


        #thessaloniki
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

        #patras
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


        connection = mysql.connector.connect(host=os.environ['secret1'], port=os.environ['secret2'], database=os.environ['secret3'], user=os.environ['secret4'], password=os.environ['secret5'], charset='utf8')
           
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery
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

        import config
        sqlQuery="SELECT * FROM events"


        #SQL
        connection = mysql.connector.connect(host=os.environ['secret1'], port=os.environ['secret2'], database=os.environ['secret3'], user=os.environ['secret4'], password=os.environ['secret5'], charset='utf8')
           
        try:
            
            if connection.is_connected():
                sql_select_Query = sqlQuery
                cursor = connection.cursor()  
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


