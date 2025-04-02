from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class AIProcessor:
    def __init__(self, models_dir='models'):
        self.models = {}
        self.models_dir = models_dir
        os.makedirs(models_dir, exist_ok=True)