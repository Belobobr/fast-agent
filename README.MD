
https://docs.databricks.com/aws/en/generative-ai/guide/gen-ai-challenges


# Building production-level quality
Unpredictable performance: LLMs can produce inconsistent or unexpected results. A prompt that works one day might fail the next if the model or context changes.
Response accuracy and safety: Developers must ensure responses are both correct and safe. Incorrect outputs (hallucinations) or harmful and offensive content can damage user trust, brand reputation, or even violate regulations.
Defining “high quality”: Domain experts often need to contribute their specialized knowledge to evaluate outputs and refine prompt logic. This collaboration requires tooling that nontechnical stakeholders can use.


# Production-quality deliverables
Easy to collaborate with subject matter experts (SMEs) to collect input to inform the definition of quality.

Agent Evaluation provides built-in UIs to allow subject matter experts to label evaluation/training data and provide feedback on gen AI app outputs.
Monitoring UIs help analyze SME interactions and transform valuable feedback into structured evaluation data for ongoing improvement.
You can take advantage of Mosaic AI's evaluation and monitoring features whether you deploy your app on Databricks or elsewhere.
Accurate, fast, quality measurement in development and production, for gen AI apps deployed both on and outside of Databricks.

With Agent Evaluation:
Evaluation sets are used to define and measure the standard of quality.
AI judges measure quality and identify the root causes of quality issues.
Agent monitoring to automatically assess the quality of production deployments using LLM judges.
Monitoring UI to identify and debug quality issues during production.
Rapid development tools that reduce development time
Agent Evaluation
Synthetic evaluation set generation provides high-quality evaluation data to test and evaluate gen AI app quality before engaging SMEs.
Evaluation functionality facilitates quickly assessing quality using the LLM judges and evaluation datasets.
Agent Framework: Deploy your gen AI app's code & config, logged as MLflow models, to production-ready serving APIs hosted on model serving using one line of code.
AI Playground: Sandboxed UI to interact with a deployed app.

# Practical advice

https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns#practical-advice


# GeanAI developer workflow
https://docs.databricks.com/aws/en/generative-ai/tutorials/ai-cookbook/genai-developer-workflow

## Gather requirements
https://docs.databricks.com/aws/en/generative-ai/tutorials/ai-cookbook/genai-developer-workflow#-gather-requirements

### Is the use case a good fit for gen AI?

### User experience

Define how users will interact with the gen AI app and what kind of responses are expected.

🟢 [P0] Typical request: What will a typical user request look like? Gather examples from stakeholders.
🟢 [P0] Expected responses: What type of responses should the system generate (for example, short answers, long-form explanations, creative narratives)?

### Data
Determine the nature, source(s), and quality of the data that will be used in the gen AI app.

🟢 [P0] Data sources: What data sources are available?
For each source, determine:
Is the data structured or unstructured?
What is the source format (for example, PDF, HTML, JSON, XML)?
Where does the data reside?
How much data is available?
How should the data be accessed?


### Performance constraints
Capture performance and resource requirements for the gen AI application.

Latency

🟢 [P0] Time-to-first token: What's the maximum acceptable delay before delivering the first token of output?
Note: Latency is typically measured using p50 (median) and p95 (95th percentile) to capture both average and worst-case performance.
🟢 [P0] Time-to-completion: What's the acceptable (time-to-completion) response time for users?
🟢 [P0] Streaming latency: If responses are streamed, is a higher overall latency acceptable?


### Evaluation
Establish how the gen AI app will be assessed and improved over time.

🟢 [P0] Business KPIs: Which business goal or KPI should the application impact? Define your baseline values and targets.
🟢 [P0] Stakeholder feedback: Who will provide initial and ongoing feedback on application performance and outputs? Identify specific user groups or domain experts.
🟢 [P0] Measuring quality: What metrics (for example, accuracy, relevance, safety, human scores) will be used to assess the quality of generated outputs?
How will these metrics be computed during development (for example, against synthetic data, manually-curated datasets)?
How will quality be measured in production (for example, logging and analyzing responses to real user queries)?
What is your overall tolerance for error? (for example, accept a certain percentage of minor factual inaccuracies, or require near-100% correctness for critical use cases.)
The aim is to build towards an evaluation set from actual user queries, synthetic data, or a combination of both. This set provides a consistent way to assess performance as the system evolves.


### Deployment
Understand how the gen AI solution will be integrated, deployed, monitored, and maintained.

🟡 [P1] Integration: How should the gen AI solution integrate with existing systems and workflows?
Identify integration points (for example, Slack, CRM, BI tools) and required data connectors.
Determine how requests and responses will flow between the gen AI app and downstream systems (for example, REST APIs, webhooks).
🟡 [P1] Deployment: What are the requirements for deploying, scaling, and versioning the application? This article covers how the end-to-end lifecycle can be handled on Databricks using MLflow, Unity Catalog, Agent Framework, Agent Evaluation, and Model Serving.
🟡 [P1] Production monitoring & observability: How will you monitor the application once it's in production?
Logging & traces: Capture full execution traces.
Quality metrics: Continuously evaluate key metrics (such as correctness, latency, relevance) on live traffic.
Alerts & dashboards: Set up alerts for critical issues.
Feedback loop: Incorporate user feedback in production (thumbs up or down) to catch issues early and drive iterative improvements.


### Example


| Area            | Considerations                                                                                                   | Requirements                                                                                                                                                                                                                      |
|-----------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User experience | - Interaction modality<br>- Typical user query examples<br>- Expected response format and style<br>- Handling ambiguous or irrelevant queries | - Chat interface integrated with Slack<br>- Example queries: "How do I reduce cluster startup time?" "What kind of support plan do I have?"<br>- Clear, technical responses with code snippets and links to relevant documentation<br>- Provide contextual suggestions and escalate to support engineers when needed |
| Agent logic     | - Query understanding and classification<br>- Multistep planning and decision-making<br>- Autonomous tool-selection and execution<br>- State and context management across interactions<br>- Error handling and fallback mechanisms | - LLM-powered planning with deterministic fallbacks<br>- Integrate with a set of pre-defined tools (such as docs retrieval or Salesforce retrieval tool)<br>- Maintain conversation state for coherent multi-turn interactions and robust error recovery |
| Data            | - Number and type of data sources<br>- Data format and location<br>- Data size and update frequency<br>- Data quality and consistency | - Four data sources<br>- Company documentation (HTML, PDF)<br>- Resolved support tickets (JSON)<br>- Community forum posts (Delta table)<br>- Salesforce connector<br>- Data stored in Unity Catalog and updated weekly<br>- Total data size: 5GB<br>- Consistent data structure and quality maintained by dedicated docs and support teams |
| Performance     | - Maximum acceptable latency<br>- Cost constraints<br>- Expected usage and concurrency | - Maximum latency requirement<br>- Cost constraints<br>- Expected peak load                                                                                                                |
| Evaluation      | - Evaluation dataset availability<br>- Quality metrics<br>- User feedback collection | - Subject matter experts from each product area help review outputs and adjust incorrect answers to create the evaluation dataset<br>- Business KPIs: Increase in support ticket resolution rate, decrease in user time spent per support ticket<br>- Quality metrics: LLM-judged answer correctness and relevance, LLM judges retrieval precision, user upvote or downvote<br>- Feedback collection: Slack will be instrumented to provide a thumbs up/down |
| Security        | - Sensitive data handling<br>- Access control requirements | - No sensitive customer data should be in the retrieval source<br>- User authentication through Databricks Community SSO                                                                   |
| Deployment      | - Integration with existing systems<br>- Deployment and versioning | - Integration with support ticket system<br>- Agent deployed as a Databricks Model Serving endpoint    


# BUILD
In this stage, you transform your solution design into a working gen AI application. Rather than perfecting everything upfront, start small with a minimal proof-of-concept (POC) that can be tested quickly. This lets you deploy to a pre-production environment as soon as possible, gather representative queries from actual users or SMEs, and refine based on real-world feedback.

Flowchart showing prepare, build, deploy steps.

The build process follows these key steps:

a. Prepare data & tools: Ensure the required data is accessible, parsed, and ready for retrieval. Implement or register the Unity Catalog functions and connections (for example, retrieval APIs or external API calls) your agent will need. b. Build agent: Orchestrate the core logic, starting with a simple POC approach. c. Quality check: Validate essential functionality before exposing the app to more users. d. Deploy pre-production agent: Make the POC available to test users and subject matter experts for initial feedback. e. Collect user feedback: Use real-world usage to identify improvement areas, additional data or tools needed, and potential refinements for the next iteration.

## b. Build agent
After your data and tools are in place, you can build the agent that responds to incoming requests such as user queries. To create an initial prototype agent, use either Python or AI playground. Follow these steps:

## c. Quality check
Before you expose the agent to a broader pre-production audience, run an offline "good enough" quality check to catch any major issues before deploying it to an endpoint. At this stage, you typically won't have a large, robust evaluation dataset, but you can still do a quick pass to ensure the agent behaves as intended on a handful of sample queries.


#### 1. Test interactively in a notebook
manual inspection: Manually call your agent with representative requests. Pay attention to whether it retrieves the right data, calls tools correctly, and follows the desired format.
Inspect MLflow traces: If you've enabled MLflow Tracing, review the step-by-step telemetry. Confirm that the agent picks the appropriate tool(s), handles errors gracefully, and does not generate unexpected intermediate requests or results.
Check latency: Note how long each request takes to run. If response times or token usage are too high, you may need to prune steps or simplify logic before going further.


#### 2. Vibe check
This can be done either in a notebook or in AI Playground.
Coherence & correctness: Does the agent's output make sense for the queries you tested? Are there glaring inaccuracies or missing details?
Edge cases: If you tried a few off-the-beaten-path queries, did the agent still respond logically or at least fail gracefully (for example, politely declining to answer rather than producing nonsensical output)?
Prompt adherence: If you provided high-level instructions such as desired tone or formatting, is the agent following these?


#### 3. Assess "good enough" quality
If you are limited on test queries at this point, consider generating synthetic data. See Create an evaluation set.
Address major issues: If you discover major flaws (for example, the agent repeatedly calls invalid tools or outputs nonsense), fix these issues before exposing them to a wider audience. See Common quality issues and how to fix them.
Decide on viability: If the agent meets a basic bar of usability and correctness for a small set of queries, you can proceed. If not, refine the prompts, fix tool or data issues, and retest.

If everything looks viable for a limited rollout, you're ready to deploy the agent to pre-production. A thorough evaluation process will happen in later phases, especially after you have more real data, SME feedback, and a structured evaluation set. For now, focus on ensuring your agent reliably demonstrates its core functionality.


## d. Deploy pre-production agent
After your agent meets a baseline quality threshold, the next step is to host it in a pre-production environment so you can understand how users query the app and collect their feedback to guide development. This environment can be your development environment during the POC phase. The main requirement is that the environment is accessible to select internal testers or domain experts.

### 1. Deploy the agent
Log and register agent: First, log the agent as an MLflow model and register it in Unity Catalog.
Deploy using Agent Framework: Use Agent Framework to take the registered agent and deploy it as a Model Serving endpoint.
### 2. Inference tables
Agent Framework automatically stores requests, responses and traces along with metadata in an inference table in Unity Catalog for each serving endpoint.
### 3. Secure and configure
Access control: Restrict endpoint access to your test group (SMEs, power users). This ensures controlled usage and avoids unexpected data exposure.
Authentication: Confirm that any required secrets, API tokens, or database connections are properly configured.


## e. Collect user feedback
After you've deployed your agent to a pre-production environment, the next step is to collect feedback from real users and SMEs to uncover gaps, spot inaccuracies, and refine your agent further.

Use the Review App

When you deploy your agent with Agent Framework, a simple chat-style Review App is created. It provides a user-friendly interface where testers can pose questions and immediately rate the agent's responses.
All requests, responses, and user feedback (thumbs up/down, written comments) are automatically logged to an inference table, making it easy to analyze later.
Use the Monitoring UI to inspect logs

Track upvotes/downvotes or textual feedback in the Monitoring UI to see which responses testers found particularly helpful (or unhelpful).
Engage domain experts

Encourage SMEs to run through typical and unusual scenarios. Domain knowledge helps surface subtle errors such as policy misinterpretations or missing data.
Keep a backlog of issues, from minor prompt tweaks to larger data pipeline refactors. Decide which fixes to prioritize before moving on.
Curate new evaluation data

Convert notable or problematic interactions into test cases. Over time, these form the basis of a more robust evaluation dataset.
If possible, add correct or expected answers to these cases. This helps measure quality in subsequent evaluation cycles.
Iterate based on feedback

Apply quick fixes like small prompt changes or new guardrails to address immediate pain points.
For more complex issues, such as requiring advanced multi-step logic or new data sources, gather enough evidence before investing in major architectural changes.
By leveraging feedback from the Review App, inference table logs, and SME insights, this pre-production phase helps surface key gaps and refine your agent iteratively. The real-world interactions gathered in this step create the foundation for building a structured evaluation set, allowing you to transition from ad-hoc improvements to a more systematic approach to quality measurement. After recurring issues are addressed and performance stabilizes, you'll be well-prepared for a production deployment with robust evaluation in place.


# 2. Evaluate & iterate

After your gen AI app has been tested in a pre-production environment, the next step is to systematically measure, diagnose, and refine its quality. This "evaluate and iterate" phase transforms raw feedback and logs into a structured evaluation set, allowing you to repeatedly test improvements and ensure your app meets the required standards for accuracy, relevance, and safety.

This phase includes the following steps:

Gather real queries from logs: Convert high-value or problematic interactions from your inference tables into test cases.
Add expert labels: Where possible, attach ground truths or style and policy guidelines to these cases so you can measure correctness, groundedness, and other quality dimensions more objectively.
Leverage Agent Evaluation: Use built-in LLM judges or custom checks to quantify app quality.
Iterate: Improve quality by refining your agent's logic, data pipelines, or prompts. Re-run the evaluation to confirm whether you've resolved key issues.

Note that these capabilities work even if your gen AI app runs outside Databricks. By instrumenting your code with MLflow Tracing, you can capture traces from any environment and unify them in the Databricks Data Intelligence Platform for consistent evaluation and monitoring. As you continue to incorporate new queries, feedback, and SME insights, your evaluation dataset becomes a living resource that underpins a continuous improvement cycle, ensuring your gen AI app stays robust, reliable, and aligned with business goals.


## a. Evaluate agent
After your agent is running in a pre-production environment, the next step is to systematically measure its performance beyond ad-hoc vibe checks. Mosaic AI Agent Evaluation enables you to create evaluation sets, run quality checks with built-in or custom LLM judges, and iterate quickly on problem areas.

Offline and online evals
When evaluating gen AI applications, there are two primary approaches: offline evaluation and online evaluation. This phase of the development cycle focuses on offline evaluation, which refers to systematic assessment outside of live user interactions. Online evaluation is covered later when discussing monitoring your agent in production.

Teams often rely too heavily on "vibe testing" for too long in the developer workflow, informally trying a handful of queries and subjectively judging if responses seem reasonable. While this provides a starting point, it lacks the rigor and coverage needed to build production-quality applications.

In contrast, a proper offline evaluation process does the following:

Establishes a quality baseline before wider deployment, creating clear metrics to target for improvement.
Identifies specific weaknesses that require attention, moving beyond the limitation of testing only expected use cases.
Detects quality regressions as you refine your app by automatically comparing performance across versions.
Provides quantitative metrics to demonstrate improvement to stakeholders.
Helps discover edge cases and potential failure modes before users do.
Reduces risk of deploying an underperforming agent to production.
Investing time in offline evaluation pays significant dividends in the long run, helping you drive towards delivering consistently high-quality responses.


### Create an evaluation set
An evaluation set serves as the foundation for measuring your gen AI app's performance. Similar to a test suite in traditional software development, this collection of representative queries and expected responses becomes your quality benchmark and regression testing dataset.


You can build an evaluation set through several complementary approaches:

1. Transform inference table logs into evaluation examples

The most valuable evaluation data comes directly from real usage. Your pre-production deployment has generated inference table logs containing requests, agent responses, tool calls, and retrieved context.

Converting these logs into an evaluation set provides several advantages:

Real-world coverage: Unpredictable user behaviors you might not have anticipated are included.
Problem-focused: You can filter specifically for negative feedback or slow responses.
Representative distribution: The actual frequency of different query types is captured.


2. Generate synthetic evaluation data

If you don't have a curated set of user queries, you can auto-generate a synthetic evaluation dataset. This "starter set" of queries helps you quickly assess whether the agent:

Returns coherent, accurate answers.
Responds in the right format.
Respects structure, tonality, and policy guidelines.
Correctly retrieves context (for RAG).
Synthetic data typically isn't perfect. Think of it as a temporary stepping stone. You'll also want to:

Have SMEs or domain experts review and prune any irrelevant or repetitive queries.
Replace or augment it later with real-world usage logs.


3. Manually curate queries

If you prefer not to rely on synthetic data, or don't have inference logs yet, identify 10 to 15 real or representative queries and create an evaluation set from these. Representative queries might come from user interviews or developer brainstorming. Even a short, curated list can expose glaring flaws in your agent's responses.


These approaches are not mutually exclusive but complementary. An effective evaluation set evolves over time and typically combines examples from multiple sources, including the following:

Start with manually curated examples to test core functionality.
Optionally add synthetic data to broaden coverage before you have real user data.
Gradually incorporate real-world logs as they become available.
Continually refresh with new examples that reflect changing usage patterns.


##### Best practices for evaluation queries
When crafting your evaluation set, deliberately include diverse query types such as the following:

Both expected and unexpected usage patterns (such as very long or short requests).
Potential misuse attempts or prompt injection attacks (such as attempts to reveal the system prompt).
Complex queries requiring multiple reasoning steps or tool calls.
Edge cases with minimal or ambiguous information (such as misspellings or vague queries).
Examples representing different user skill levels and backgrounds.
Queries that test for potential biases in responses (such as "compare Company A vs Company B").
Remember that your evaluation set should grow and evolve alongside your application. As you uncover new failure modes or user behaviors, add representative examples to ensure your agent continues to improve in those areas.


##### Add evaluation criteria

Use expected facts (recommended)
Use expected response (alternative)

The guidelines LLM judge interprets these natural language instructions and assesses whether the response complies with them. This works particularly well for subjective quality dimensions like tone, formatting, and adherence to organizational policies.





