from bs4 import BeautifulSoup
import pandas as pd
import os

data = []
for file in os.listdir("data_hospital"):
    try:
        with open(f"data_hospital/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Extracting doctor name
        name_tag = soup.find("h2", attrs={"data-qa-id": "doctor_name"})
        name = name_tag.get_text().strip() if name_tag else ""

        # Extracting specialty
        specialty_tag = soup.find("div", class_="u-grey_3-text").find("span") if soup.find("div", class_="u-grey_3-text") else ""
        specialty = specialty_tag.get_text().strip() if specialty_tag else ""

        # Extracting experience
        experience_tag = soup.find("div", attrs={"data-qa-id": "doctor_experience"})
        experience = experience_tag.get_text().strip().split("years")[0].strip() if experience_tag else ""

        # Extracting locality
        locality_tag = soup.find("span", attrs={"data-qa-id": "practice_locality"})
        locality = locality_tag.get_text().strip() if locality_tag else ""

        # Extracting city
        city_tag = soup.find("span", attrs={"data-qa-id": "practice_city"})
        city = city_tag.get_text().strip() if city_tag else ""

        # Extracting clinic
        clinic_tag = soup.find("span", attrs={"data-qa-id": "doctor_clinic_name"})
        clinic = clinic_tag.get_text().strip() if clinic_tag else ""

        # Extracting fee
        fee_tag = soup.find("span", attrs={"data-qa-id": "consultation_fee"})
        fee = fee_tag.get_text().strip() if fee_tag else ""

        # Extracting recommendation percentage
        recommendation_tag = soup.find("span", attrs={"data-qa-id": "doctor_recommendation"})
        recommendation = recommendation_tag.get_text().strip() if recommendation_tag else ""

        # Extracting rating percentage
        rating_tag = soup.find("span", attrs={"data-qa-id": "doctor_recommendation"})
        rating = rating_tag.get_text().strip() if rating_tag else ""

        # Extracting patient stories
        stories_tag = soup.find("span", attrs={"data-qa-id": "total_feedback"})
        stories = stories_tag.get_text().strip().split("Patient")[0].strip() if stories_tag else ""

        # Extracting link
        link_tag = soup.find("a", href=True)
        link = f"https://www.practo.com{link_tag['href']}" if link_tag and link_tag.get("href") else ""

        data.append({
            "Doctor Name": name,
            "Specialty": specialty,
            "Experience": experience,
            "Locality": locality,
            "City": city,
            "Clinic Name": clinic,
            "Consultation Fee": fee,
            "Rating": rating,
            "Patient Stories": stories,
            "Profile Link": link
        })

    except Exception as e:
        print(e)

df= pd.DataFrame(data=data)
df.to_csv("hospital_data.csv")
