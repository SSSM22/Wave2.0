from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from res.image import scrape_website
from docx import Document
import shutil
import mimetypes
from django.http import FileResponse, Http404
import os

# Create your views here.
service = ChromeService(ChromeDriverManager().install())
def index(request):
    
    return render(request,'index.html')

def details(request):
 if request.method == 'POST':
    headers = {"cookie": "CONSENT=YES+cb.20230531-04-p0.en+FX+908"}
    link=request.POST['link']
    # link='https://internshala.com/internship/detail/work-from-home-php-development-internship-at-areeyarath-boonsoontornpat1718254017'
    if 'internshala' in link:
        response=requests.get(link,headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            about = soup.find('div',class_="internship_details")
            todo = about.find_all('div',class_="text-container")
            skills=about.find_all('div',class_="round_tabs_container")
            first_todo = todo[0] if todo else None
            first_skills = skills[0] if skills else None
            if first_todo:
                print("First div in todo:")
                first_todo=first_todo.get_text()
            if first_skills:
            
                first_skills=first_skills.get_text()
                print("First div in skills:",first_skills)
        text=generate_content(first_todo,first_skills)
        resume=update_resume(text)
        return resume

    if 'naukri' in link:
        ans=scrape_website(link)
        text=generate_content(ans)
        resume=update_resume(text)
        return resume

        

    else:
            response=requests.get(link,headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                generate_content(soup)

            return HttpResponse("yes")

def generate_content(job_des,skills=None):
    gemini_api_key = 'AIzaSyBzsemF33e6V-x2vz3pOtSKWwsvQ1h52v4'#'AIzaSyCqdMnGnigseAJH8bBSfuggxF-oqU5lrXQ'  # Replace with your actual API key
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}'

    if skills!=None:

        data = {
            "contents": [
                {
                    "parts": [
                        {
                         "text": f'make an objective for my resume with job description {job_des} and skills {skills}'
                        }
                    ]
                }
            ]
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes

            return(response.text)

        except requests.exceptions.RequestException as e:
            print("error")
            # return {'error': f'Request error: {str(e)}'}
    else:
        data = {
            "contents": [
                {
                    "parts": [
                        {
                         "text": f'make my resume with job description avaliable in html page along with skills required {job_des}'
                        }
                    ]
                }
            ]
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes

            return(response.text)

        except requests.exceptions.RequestException as e:
            print("error")
            # return {'error': f'Request error: {str(e)}'}





def update_resume(text):
#  if request.method == 'POST':
#         if form.is_valid():
            shutil.copy(r'res\sesume_template.docx', r'res\download.docx')
            f='nasum'
            l='moddin'
            m="mail.dom"
            p=167885
    
            # Fill the template
            document = Document('res\download.docx')
            for paragraph in document.paragraphs:
                if 'object.ive' in paragraph.text:
                    paragraph.text=paragraph.text.replace('object.ive',text)
                if 'first_name' in paragraph.text:
                    paragraph.text = paragraph.text.replace('first_name', f)
                if 'last_name' in paragraph.text:
                    paragraph.text = paragraph.text.replace('last_name', l)
                if 'email' in paragraph.text:
                    paragraph.text = paragraph.text.replace('contact', m)
                if 'phone_number' in paragraph.text:
                    paragraph.text = paragraph.text.replace('phone_number', str(p))
                if 'education' in paragraph.text:
                    paragraph.text = paragraph.text.replace('education', resume.education)
                if 'experience' in paragraph.text:
                    paragraph.text = paragraph.text.replace('experience', resume.experience)
                if 'skills' in paragraph.text:
                    paragraph.text = paragraph.text.replace('skills', resume.skills)
            # Save the filled document
            document.save('res\download.docx')
            file_path = os.path.join('res/','download.docx')
            if os.path.exists(file_path):
                response = FileResponse(open(file_path, 'rb'))
                return response
            

