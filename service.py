import numpy as np
import bentoml
from typing import List


@bentoml.service(name="iris_classifier")
class IrisService:

    model = bentoml.sklearn.load_model("iris_clf:latest")

    @bentoml.api
    def predict(self, input_data: List[List[float]]) -> List[int]:
        """
        Example input:
        [[5.1, 3.5, 1.4, 0.2]]
        """
        data = np.array(input_data)
        preds = self.model.predict(data)
        return preds.tolist()
