# EVALUATION

# install
```bash
pip install --upgrade "mlflow>=3.1"
```

## 1. Option run mlflow
```python
import mlflow

# Creates local mlruns directory for experiments
mlflow.set_experiment("my-genai-experiment")
```

## 2. Option run local server
```bash
mlflow server --host 0.0.0.0 --port 5001
```


```python
import mlflow

# Connect to remote MLflow server
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("my-genai-experiment")
```

```bash
curl -X POST https://litellm.ml.wktodev.net/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-Rxx5LwjUXxhDSkdcgZYsaA" \
-d '{
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}'
```


# MODELS LOGGING
How LoggedModel Works for Versioning
A LoggedModel in MLflow is not just for traditional machine learning models; it's adapted to be the core of GenAI application versioning. Each distinct state of your application that you want to evaluate, deploy, or refer back to can be captured as a new version of a LoggedModel.

Key Characteristics:

Central Versioned Entity: Represents a specific version of your GenAI application or a significant, independently versionable component.
Captures Application State: A LoggedModel version records a particular configuration of code, parameters, and other dependencies.
Flexible Code Management:
Metadata Hub (Primary): Most commonly, LoggedModel links to externally managed code (e.g., via a Git commit hash), acting as a metadata record for that code version along with its associated configurations and MLflow entities (evaluations, traces).
Packaged Artifacts (Optional): For specific deployment needs (like Databricks Model Serving), LoggedModel can also bundle the application code and dependencies directly.
Lifecycle Tracking: The history of LoggedModel versions allows you to track the application's evolution, compare performance, and manage its lifecycle from development to production.