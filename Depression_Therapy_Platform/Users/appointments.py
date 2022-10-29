from pprint import pprint
from urllib import request, response
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE='client_secret_PsyCura.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# snippet to create a new calendar
"""
request_body = {
    'summary': 'Calendar_Name',
}

response = service.calendars().insert(body=request_body).execute()
pprint(response)
"""

# snippet to print all existing calendars
"""
response = service.calendarList().list().execute()
pprint(response)
"""

calendar_id = '5lnu2uakgegiudqs7taniti1bs@group.calendar.google.com'

# snippet to create a new event
colors = service.colors().get().execute()
pprint(colors)

event_request_body = {
    'start': {
        'dateTime': convert_to_RFC_datetime(2022, 11, 1, 15, 0),
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': convert_to_RFC_datetime(2022, 11, 1, 16, 0),
        'timeZone': 'Asia/Kolkata',
    },
    'summary': 'Testing',
    'description': 'This is a test event',
    'colorId': 1,
    'attendees': [
        {
            'email': 'pratikjalan11@gmail.com',
            'displayName': 'Pratik Jalan',
            'organizer': True,
            'self': True,
            'resource': False,
            'optional': False,
            'responseStatus': 'accepted',
        },
        {
            'email': 'pratikjallan.201cs142@nitk.edu.in',
            'displayName': 'Pratik Jallan NITK',
            'organizer': False,
            'self': False,
            'resource': False,
            'optional': False,
            'responseStatus': 'accepted',
        }
    ],

}

# response = service.events().insert(calendarId=calendar_id, body=event_request_body).execute()
# pprint(response)

# get schedules events in the future
response = service.events().list(calendarId=calendar_id, timeMin=convert_to_RFC_datetime(2022, 10, 1, 0, 0), timeMax=convert_to_RFC_datetime(2022, 11, 30, 23, 59), singleEvents=True, orderBy='startTime').execute()
# get date and time of the events
for event in response['items']:
    print(event['start']['dateTime'], event['summary'])

# get attendees email
attendees = response['items'][0]['attendees']
for attendee in attendees:
    print(attendee['email'])
