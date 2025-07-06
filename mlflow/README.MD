# The goal here is to prototype work with mlflow

At its core, MLflow organizes all GenAI application data within Experiments. Think of an experiment as a project folder that contains every trace, evaluation run, app version, prompt, and quality assessment from throughout your app's lifecycle.

1. Data model

Experiment: Container for a single application's data
Observability data
Traces: App execution logs
Assessments: Quality measurements attached to a trace
Evaluation data
Evaluation Datasets: Inputs for quality evaluation
Evaluation Runs: Results of quality evaluation
Human labeling data
Labeling Sessions: Queues of traces for human labeling
Labeling Schemas: Structured questions to ask labelers
Application versioning data
Logged Models: App version snapshots
Prompts: LLM prompt templates

2. MLflow provides SDKs for interacting with your app's data to evaluate and improve quality:

_mlflow.genai.scorers._*: Functions that analyze a trace's quality, creating feedback assessments
mlflow.genai.evaluate(): SDK for evaluating an app's version using evaluation datasets and scorers to identify and improve quality issues
mlflow.genai.add_scheduled_scorer(): SDK for running scorers on production traces to monitor quality


3. MLflow provides UIs for managing and using your app's data:

Review App: Web UI for collecting domain expert assessments
MLflow Experiment UI: UIs for viewing and interacting with traces, evaluation results, labeling sessions, app versions, and prompts.


# Testing

Why Traditional Testing Fails for GenAI
🚫 Fixed Test Cases Don't Work
Traditional software testing relies on predetermined inputs and expected outputs. GenAI apps face:

Infinite input variations: Users can phrase requests in unlimited ways
Context-dependent correctness: The "right" answer depends on conversation history
Evolving expectations: What users consider helpful changes over time
🚫 Code Coverage Isn't Meaningful
In traditional software, code coverage indicates test completeness. For GenAI:

Prompt changes affect behavior: Modifying a prompt template changes outputs without touching code
Model updates impact quality: Upgrading to a new model version can break working features
External dependencies matter: Changes in knowledge cutoffs or training data affect responses
🚫 Binary Pass/Fail Doesn't Apply
Traditional tests either pass or fail. GenAI quality exists on a spectrum:

Partial correctness: Responses can be mostly right with minor issues
Subjective quality: Different users may prefer different response styles
Trade-off decisions: A "worse" response might be acceptable if it's 10x faster


### The Compounding Effect
These challenges don't exist in isolation—they compound:

Free-form inputs + Evolving patterns = You can't predict what users will ask tomorrow
Free-form outputs + Domain expertise = You need specialists to evaluate ever-changing responses
Quality trade-offs + All of the above = Every optimization requires re-evaluating across multiple dimensions