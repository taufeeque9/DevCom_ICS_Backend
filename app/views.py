from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from wsgiref.util import FileWrapper
import datetime
import string

# Create your views here.


class IcsView(generics.ListAPIView):

    def get(self, request, format=None):

        slot = self.request.GET.get('slot')
        time_table = {
            "1A": ['MO', '083000'],
            "2A": ['MO', '093000'],
            "3A": ['MO', '103500'],
            "4A": ['MO', '113500'],
            "8A": ['MO', '140000'],
            "9A": ['MO', '153000'],
            "12A": ['MO', '170500'],
            "13A": ['MO', '183500'],

            "4B": ['TU', '083000'],
            "1B": ['TU', '093000'],
            "2B": ['TU', '103500'],
            "3B": ['TU', '113500'],
            "10A": ['TU', '140000'],
            "11A": ['TU', '153000'],
            "14A": ['TU', '170500'],
            "15A": ['TU', '183500'],

            "7A": ['WE', '083000'],
            "5A": ['WE', '093000'],
            "6A": ['WE', '110500'],
            "X1": ['WE', '140000'],
            "X2": ['WE', '150000'],
            "X3": ['WE', '160000'],
            "XC": ['WE', '170500'],
            "XD": ['WE', '183500'],

            "3C": ['TH', '083000'],
            "4C": ['TH', '093000'],
            "1C": ['TH', '103500'],
            "2C": ['TH', '113500'],
            "8B": ['TH', '140000'],
            "9B": ['TH', '153000'],
            "12B": ['TH', '170500'],
            "13B": ['TH', '183500'],

            "7B": ['FR', '083000'],
            "5B": ['FR', '093000'],
            "6B": ['FR', '110500'],
            "10B": ['FR', '140000'],
            "11B": ['FR', '153000'],
            "14B": ['FR', '170500'],
            "15B": ['FR', '183500']
        }

        date_today = str(datetime.date.today())
        print(date_today.replace('-', ''))
        day = time_table[slot]
        dstart = "DTSTART:" + date_today.replace('-', '') + "T" + day[1]

        # RRULE:FREQ=WEEKLY;BYDAY=SU,MO;INTERVAL=1
        rrule = "RRULE:FREQ=WEEKLY;BYDAY=" + day[0] + ";INTERVAL=1"

        f = open("/home/rahul/Desktop/test/project/app/demofile2.ics", "w")
        f.write("BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\n{}\n".format(dstart))
        f.write("{}\nDESCRIPTION: {}\nSEQUENCE:0\nSTATUS:CONFIRMED\nSUMMARY: {}\nTRANSP:OPAQUE\nEND:VEVENT".format(rrule, slot, slot))
        f.write("\nEND:VCALENDAR")
        f.close()

        filename = 'demofile2.ics'
        fileformat = self.request.GET.get('fileformat')
        if fileformat == 'raw':
            zip_file = open('/home/rahul/Desktop/test/project/app/demofile2.ics', 'rb')
            response = HttpResponse(FileWrapper(zip_file), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="%s"' % 'demofile2.ics'
            return response
