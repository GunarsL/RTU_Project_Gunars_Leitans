##Import Selenium library
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
##Import Pandas library
import pandas as pd
##Import Tkinter library
import tkinter as tk
from tkinter import *
#Import Datetime library
from datetime import datetime
#Import OS library
import os

excel_filename = ""
job_position = ""
job_location = ""
salary = 0

def get_user_input():
    root = tk.Tk()
    root.title("JobSearch: Automated vacancy search program")
    root.geometry("420x220")

    # tiek definēta funkcija, kura kalpo kā mainīgo iegūšanas funkcijas un vienlaikus tkinter vides aizvēršana
    def submit_on_click():
        global excel_filename, job_position, job_location, salary
        excel_filename = excel_filename_entry.get()
        job_position = job_position_entry.get()
        job_location = job_location_entry.get()
        salary = salary_slider_entry.get()
        root.destroy()

    # tiek definēti lietotāja ievades lauki ar paskaidrojumiem, kā arī neliela stila izmaiņa
    file_name_label = tk.Label(font=("Roboto", 10, "bold"), text="Ievadiet excel(.xlsx) faila nosaukumu:")
    excel_filename_entry = tk.Entry()

    file_name_label.pack()
    excel_filename_entry.pack()


    job_position_label = tk.Label(font=("Roboto", 10, "bold"), text="Ievadiet darba profesiju vai amatu:")
    job_position_entry = tk.Entry()

    job_position_label.pack()
    job_position_entry.pack()

    job_location_label = tk.Label(font=("Roboto", 10, "bold"), text="Ievadiet pilsētu, novadu vai valsti:")
    job_location_entry = tk.Entry()

    job_location_label.pack()
    job_location_entry.pack()

    salary_label = tk.Label(font=("Roboto", 10, "bold"), text="Norādiet minimālo algu:")
    salary_slider_entry = tk.Scale(root, from_=0, to=10000, orient=tk.HORIZONTAL, resolution=100, length=300)

    salary_label.pack()
    salary_slider_entry.pack()

    # funkcija tiek izsaukta, kad lietotājs nospiež pogu Meklēt, tādējādi saglabājot savu ievadīto informāciju vēlākai apstrādei
    submit_button = tk.Button(root, text="Meklēt", command=submit_on_click)
    submit_button.pack()
    
    root.mainloop()

# tiek izsaukta funkcija lietotāja ievades datiem izmantojot tkinter vidi
get_user_input()

service = Service()
option = webdriver.ChromeOptions()
# rodas sertifikātu error, kad tiek atvērta mājaslapa. lai nodrošinātu, ka programma strādā kā paredzēta, tiek ieviesta šī rinda
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=option)

# tiek pievienota mājaslapa, kuras URL saitē tiek ievietota lietotāja sniegtā informācija
driver.get(f"https://www.visidarbi.lv/darba-sludinajumi/kas:{job_position}/kur:{job_location}?salary_from={salary}#results")

# šie atslēgas vārdi tiek izmantoti izceltajās jeb reklamētajās vakancēs, kas var atkārtoties vai arī nebūt saistītam ar meklēto
filtered_words = ["PREMIUM", "PREMIUM DUAL"]

# HTML koda elementa atrašanās vieta, no kuras pēc tam tiek meklēta visa informācija par vakancēm
vacancys = driver.find_elements(By.XPATH, "//*[contains(@class, 'big-item')]")

# programmas darba veikšanas laika mainīgais
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

details_info_list = []

for vacancy_items in vacancys:
    # atrod vakanču amata nosaukumu
    title_location = vacancy_items.find_element(By.TAG_NAME, "h3")
    vacancy_title = title_location.text

    # tiek veikta pārbaude priekš vārdiem no saraksta, lai atbrīvotos no reklāmu vai īpaši izceltajām vakancēm
    if any(word.upper() in vacancy_title.upper() for word in filtered_words):
            continue

    # atrod vakanču pieejamo informācijas tagu 
    details_location = vacancy_items.find_elements(By.TAG_NAME, "li")

    # atrod vakanču klasi, kas satur vakances saiti un iegūst tā vērtību
    vacancy_link = vacancy_items.find_element(By.CLASS_NAME, "image").get_attribute("href")

    vacancy_info = []

    # pievieno vakances amatu
    vacancy_info.append(vacancy_title)

    # pievieno vakances pieejamo informāciju
    for vacancy_details in details_location:
            vacancy_info.append(vacancy_details.text)

    # pievieno vakances saiti
    vacancy_info.append(vacancy_link)

    # pievieno sarakstam programmas darba veikšanas laiku
    vacancy_info.append(current_timestamp)

    # pievieno ārējam, vispārējam sarakstam, visu nepieciešamo informāciju
    details_info_list.append(vacancy_info)


# excel faila path
excel_filename_path = f"./{excel_filename}.xlsx"

if os.path.isfile(excel_filename_path):
    # nolasa esošo excel failu
    existing_df = pd.read_excel(excel_filename_path)

    # pievieno mainīgajam jauno informāciju no saraksta
    new_data_df = pd.DataFrame(details_info_list)

    # apvieno esošo failu ar jauno informāciju
    existing_df = pd.concat([existing_df, new_data_df], ignore_index=True)

    # iebūvētā openpyxl bibliotēka pandas veic saglabāšanu
    writer = pd.ExcelWriter(excel_filename_path, engine='openpyxl') 
    existing_df.to_excel(writer, index=False)
    writer.close()

else:
    # excel faila izveide, ja programma tiek palaista pirmo reizi
    df = pd.DataFrame(details_info_list)
    df.to_excel(excel_filename_path, index=False)

driver.quit()