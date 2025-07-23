from django.shortcuts import render
from .forms import HeartForm
from .models import PredictionRecord
import numpy as np
import pickle
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'predictor_collection', 'model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), 'predictor_collection', 'scaler.pkl')

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    return model, scaler

model, scaler = load_model()

def predict_heart(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            input_data = np.array([
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal'],
            ]).reshape(1, -1)

            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

            # Save prediction
            PredictionRecord.objects.create(
                age=form.cleaned_data['age'],
                sex=form.cleaned_data['sex'],
                cp=form.cleaned_data['cp'],
                trestbps=form.cleaned_data['trestbps'],
                chol=form.cleaned_data['chol'],
                fbs=form.cleaned_data['fbs'],
                restecg=form.cleaned_data['restecg'],
                thalach=form.cleaned_data['thalach'],
                exang=form.cleaned_data['exang'],
                oldpeak=form.cleaned_data['oldpeak'],
                slope=form.cleaned_data['slope'],
                ca=form.cleaned_data['ca'],
                thal=form.cleaned_data['thal'],
                result=result
            )

            return render(request, 'predictor/result.html', {'result': result})
    else:
        form = HeartForm()

    return render(request, 'predictor/form.html', {'form': form})
