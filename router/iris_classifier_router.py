from fastapi import APIRouter
from starlette.responses import JSONResponse

from iris.iris_classifier import IrisClassifier
from iris.models import Iris


router = APIRouter()


@router.post('/classify_iris')
def extract_name(iris_features: Iris):
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify_iris(iris_features))
