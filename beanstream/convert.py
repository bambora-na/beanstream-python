# -*- coding: utf-8 -*-
types = {
    'B': 'Bambora',
    'TD': 'TD',
    'FD': 'First Data',
    'UK': 'UK',
    'G': 'Global Payments',
    'V': 'Vital',
    'EL': 'Elavon',
    'E': 'Elavon',
    'EFT': 'EFT',
    'E/A': 'EBP/ACH',
    'PT': 'Paymentech',
    'IOP': 'INTERAC Online',
    'EMV': 'Europay, Mastercard, Visa',
    'DJN': 'Desjardins',
}

import csv
import json

messages = {}

def is_approved(message):
    message_up = message.upper()
    if (
        'approved'.upper() in message_up or
        'approval'.upper() in message_up and
        not 'duplicate'.upper() in message_up
    ):
        return True
    return False

def make_line(line):
    return str(line[0]), {
        "type": types[line[1].upper()],
        "approved": is_approved(line[3]),
        "cardholder_message": line[2],
        "merchant_message": line[3],
    }

for line in csv.reader(open('messages.csv')):
    if '-' in line[0]:
        from_id, to_id = line[0].split('-')
        from_id, to_id = int(from_id), int(to_id)
        for id in range(from_id, to_id+1):
            id2, value = make_line(line)
            messages[id2] = value
    else:
        id2, value = make_line(line)
        messages[id2] = value

print(json.dumps(messages, indent=2))
