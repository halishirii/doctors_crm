import pandas as pd
from pathlib import Path
DATA_FILE=(Path(__file__).parent.parent / 
    "data"/ "doctors_crm.xlsx")
def load_doctors():
    return pd.read_excel(DATA_FILE, sheet_name="doctors")
def save_doctors(df):
    with pd.ExcelWriter(
        DATA_FILE, engine="openpyxl",mode="a",
        if_sheet_exists="replace"
    ) as writer:
        df.to_excel(writer, sheet_name="doctors", index=False)
        
def add_doctor(name, "specialty": "",
    medical_code:"",
    city:"",
    clinic_address:"",
    source:"",
    nobat_url:"",
    axon_url:""):
    new_doctor={
    "name":name,
    "specialty": "",
    "medical_code":"",
    "city":"",
    "clinic_address":"",
    "source":"",
    "nobat_url":"",
    "axon_url":""}
    df= load_doctors()
    if name in df['name'].values:
        return("پزشک در لیست وجود دارد")
    else:
        new_row= pd.DataFrame([new_doctor])
        df= pd.concat([df, new_row], ignore_index= True)
        save_doctors(df)
    
def delete_doctor(medical_code):
    df= load_doctors()

    if medical_code not in df['medical_code'].values:
        return "پزشکی با این کد نظام پیدا نشد"
    df = df[df["medical_code"] != medical_code ]
    save_doctors(df)

def find_doctors(name= None, specialty= None, city= None ,medical_code= None):
    """
    جستجوی پزشکان بر اساس معیارهای داده، تمامی پارامترها اختیاری هسند و درصورت وارد نکردم هیچ پارامتری، تمامی پزشکان نمایش داده می شوند
    """