# AGENT

# class Agent:
#     def __init__(self, name: str, model: str, task: str, prompts: list = None, messages: list = None):
#         self.name = name
#         self.model = model
#         self.task = task
#         self.prompts = prompts or []
#         self.messages = messages or []

#     def run(self, question: str):
#         # Simulate running the agent with the provided question
#         response = f"Response from {self.name} using {self.model} for question: {question}"
#         return response


# AGENT EVALUATION (SHOULD BE IN THE NOTEBOOK, DURING CI E.T.C)
# should be available in notebooks, ci, e.t.c

# def run_agent_evaluation():
#     # 

#     source_code_version = get_source_code_version()

#     agent_flow = get_agent_flow()

#     evaluation_dataset = get_agent_evaluation_dataset() 
#     # Should be stored outside code base and be evailable to update from traces, subject matter experts e.t.c

#     evaluation_results = evaluate_agent_flow(
#         agent_flow=agent_flow,
#         evaluation_dataset=evaluation_dataset,
#     )

#     # log evaluation results from local notebook
#     log_evaluation_results(
#         evaluation_results=evaluation_results,
#         agent_flow=agent_flow,
#     )

# BASIC WORKFLOW
# 1. checkout source code version
# 2. get agent flow
# 3. get evaluation dataset
# 4. evaluate agent flow with evaluation dataset
# 5. log evaluation results
# 6. IMPROVE AGENT FLOW
# 7. evaluate again
# 8. log evaluation results again


# BASIC IDEAS:
# 1. agent workflow (iteration on agent)

## CODE
from typing import List


class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def execute(self, *args, **kwargs):
        # Simulate tool execution
        return f"Executed {self.name} with args: {args}, kwargs: {kwargs}"

class Agent:
    def __init__(
            self, 
            name: str, 
            model: str, 
            system_prompt: list = [],
            tools: list[Tool] = []
        ):
        self.name = name
        self.model = model
        self.system_prompt = system_prompt
        self.tools = tools

    def run(self, messages: List[str]):
        # Simulate running the agent with the provided question
        response = f"Response from {self.name} using {self.model} for question: {messages}"
        return response
    
## EVALUATION
def get_dataset():
    # Simulate fetching a dataset for evaluation

    # load dataset from s3 or any predefined source
    return [
        
    ]

### Looks like traces - first class citizens in the agent workflow (it's easier to check it then logs)
### TRACES - are used for debugging purposes....

# 2. agent serving workflow (iteration on agent serving)

## TRACES, let's store traces somewhere, so we can use them for evaluation, training, e.t.c

def log_trace(trace: str):
    # Simulate logging a trace
    return f"Trace logged: {trace}"

# 3. agent integration to chat workflow

## USER FEEDBACK, associated with traces, models, prompts e.t.c

def log_feed_back():
    # Simulate logging user feedback
    return "Feedback logged successfully"