import pandas as pd
def doctorin():
    doctors=  pd.DataFrame(columns=[
        'medical_code',
        'name',
        'specialty',
        'clinic_address',
        'city',
        'source',
        'nobat_url',
        'axon_url'])
    interactions = pd.DataFrame(columns=[
        'medical_code',
        'date',
        'type',
        'note',
        'mood_score',
        'next_action'
    ])
    with pd.ExcelWriter("doctors_crm.xlsx") as writer:
        doctors.to_excel(writer, sheet_name='doctors', index= False)
        interactions.to_excel(writer, sheet_name='interactions', index= False)
        
def search_doctor(file, name= None, code=None):
    df= pd.read_excel(file, sheet_name='doctors')
    if name:
        return
        df[df['name'].str.contains(name, na=False)]
    if code:
        return df[df['medical_code']==code]
    return df

        
if __name__ == "__main__":
    doctorin()