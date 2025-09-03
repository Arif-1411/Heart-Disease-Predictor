from django.contrib import admin
from .models import PredictionRecord

@admin.register(PredictionRecord)
class PredictionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'sex', 'cp', 'chol', 'thalach', 'result', 'timestamp')
    list_filter = ('result', 'sex', 'cp', 'thal')
    search_fields = ('result',)
    ordering = ('-timestamp',)
