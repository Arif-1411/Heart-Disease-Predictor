from django.db import models

class PredictionRecord(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField(verbose_name="Chest Pain Type")
    trestbps = models.IntegerField(verbose_name="Resting Blood Pressure")
    chol = models.IntegerField(verbose_name="Cholesterol")
    fbs = models.IntegerField(verbose_name="Fasting Blood Sugar > 120 mg/dl")
    restecg = models.IntegerField(verbose_name="Resting ECG Result")
    thalach = models.IntegerField(verbose_name="Max Heart Rate Achieved")
    exang = models.IntegerField(verbose_name="Exercise Induced Angina")
    oldpeak = models.FloatField(verbose_name="ST Depression")
    slope = models.IntegerField(verbose_name="Slope of ST Segment")
    ca = models.IntegerField(verbose_name="Number of Major Vessels Colored")
    thal = models.IntegerField(verbose_name="Thalassemia Type")

    result = models.CharField(max_length=50)  # "Heart Disease" or "No Heart Disease"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
