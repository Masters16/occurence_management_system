import base64
import datetime
import json
import uuid

import requests
from django.contrib.auth.models import User, Group
import random

import config

from jinja2 import Environment, FileSystemLoader


def generate_exam_id():
    current_time = datetime.datetime.now()
    random_num = random.randrange(0, 100)
    header = "EXAM"

    return f"EXAM-{random_num}-{current_time}"


def generate_o_report(report_type, template_id, payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(station_name=payload['station_name'],
                              station_id=payload['station_id'],
                              the_police=payload['the_police'],
                              document_number=payload['document_number'],
                              document_date=payload['document_date'],
                              records=payload['records']
                              )

    with open(filename, mode="w", encoding="utf-8") as new_card:
        new_card.write(content)

    html = open("id.html", "r").read()
    encoded_html = base64.b64encode(html.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer af11ffcd3c4b1212dada2d2b',
        'Content-Type': 'application/json'
    }

    data = {
        "page": {
            "pdf": {
                "printBackground": True
            },
            "setContent": {
                "html": encoded_html
            }
        }
    }

    url = 'https://api.doppio.sh/v1/render/pdf/direct'

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        pdf_content = response.content

        doc_id = uuid.uuid4()
        filename = f"static/reports/{report_type}-reports/{payload['the_police']}-report-{current_date}-{doc_id}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename, 'id': doc_id}
    else:
        return "Error:", response.status_code


def generate_u_report(report_type, template_id, payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(station_name=payload['station_name'],
                              station_id=payload['station_id'],
                              police_id=payload['police_id'],
                              document_number=payload['document_number'],
                              document_date=payload['document_date'],
                              users=payload['users']
                              )

    with open(filename, mode="w", encoding="utf-8") as new_card:
        new_card.write(content)

    html = open("id.html", "r").read()
    encoded_html = base64.b64encode(html.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer af11ffcd3c4b1212dada2d2b',
        'Content-Type': 'application/json'
    }

    data = {
        "page": {
            "pdf": {
                "printBackground": True
            },
            "setContent": {
                "html": encoded_html
            }
        }
    }

    url = 'https://api.doppio.sh/v1/render/pdf/direct'

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        pdf_content = response.content

        doc_id = uuid.uuid4()
        filename = f"static/reports/{report_type}-reports/{payload['police_id']}-report-{current_date}-{doc_id}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename, 'id': doc_id}
    else:
        return "Error:", response.status_code
