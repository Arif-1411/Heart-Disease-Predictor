from django import forms

class HeartForm(forms.Form):
    SEX_CHOICES = [(1, 'Male'), (0, 'Female')]
    CP_CHOICES = [
        (0, 'Typical Angina'),
        (1, 'Atypical Angina'),
        (2, 'Non-anginal Pain'),
        (3, 'Asymptomatic'),
    ]
    FBS_CHOICES = [(1, 'Yes'), (0, 'No')]
    RESTECG_CHOICES = [
        (0, 'Normal'),
        (1, 'ST-T wave abnormality'),
        (2, 'Left Ventricular Hypertrophy'),
    ]
    EXANG_CHOICES = [(1, 'Yes'), (0, 'No')]
    SLOPE_CHOICES = [
        (0, 'Upsloping'),
        (1, 'Flat'),
        (2, 'Downsloping'),
    ]
    THAL_CHOICES = [
        (1, 'Normal'),
        (2, 'Fixed Defect'),
        (3, 'Reversible Defect'),
    ]

    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(choices=SEX_CHOICES, label='Sex')
    cp = forms.ChoiceField(choices=CP_CHOICES, label='Chest Pain Type')
    trestbps = forms.IntegerField(label='Resting BP')
    chol = forms.IntegerField(label='Cholesterol')
    fbs = forms.ChoiceField(choices=FBS_CHOICES, label='Fasting Blood Sugar > 120 mg/dl')
    restecg = forms.ChoiceField(choices=RESTECG_CHOICES, label='Resting ECG')
    thalach = forms.IntegerField(label='Max Heart Rate Achieved')
    exang = forms.ChoiceField(choices=EXANG_CHOICES, label='Exercise Induced Angina')
    oldpeak = forms.FloatField(label='Oldpeak')
    slope = forms.ChoiceField(choices=SLOPE_CHOICES, label='Slope')
    ca = forms.IntegerField(label='Ca (number of vessels, 0–3)')
    thal = forms.ChoiceField(choices=THAL_CHOICES, label='Thal')
