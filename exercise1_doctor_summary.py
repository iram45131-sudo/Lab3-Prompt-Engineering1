
def doctor_summary(patient_notes, patient_name):
    prompt = f"""
You are a medical documentation assistant.

Patient Name: {patient_name}
Consultation Notes: {patient_notes}

Create a summary with these sections:
1. Symptoms
2. Diagnosis
3. Recommendation

If information is missing, write "Not provided".
Do not invent medical information.
"""
    print(prompt)


patient_name = input("Enter patient name: ")
patient_notes = input("Enter consultation notes: ")

doctor_summary(patient_notes, patient_name)
