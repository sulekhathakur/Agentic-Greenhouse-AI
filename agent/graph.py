from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.llm import get_llm
from agent.tools import load_data, basic_analysis

# -------------------------
# Node 1: Goal Interpreter
# -------------------------
def goal_interpreter_node(state: AgentState):
    llm = get_llm()  # ✅ created here
    prompt = f"""
    You are an intelligent AI agent.

    User Goal:
    {state['user_goal']}

    Convert this into a clear, analytical objective.
    """
    refined_goal = llm.invoke(prompt).content
    return {"refined_goal": refined_goal}

# -------------------------
# Node 2: Planner
# -------------------------
def planner_node(state: AgentState):
    llm = get_llm()
    prompt = f"""
    Analytical Objective:
    {state['refined_goal']}

    Create a concise, step-by-step analysis plan.
    """
    plan = llm.invoke(prompt).content
    return {"plan": plan}

# -------------------------
# Node 3: Data Analysis
# -------------------------
def analysis_node(state: AgentState):
    df = load_data()
    analysis = basic_analysis(df)
    return {
        "dataframe": df,
        "analysis_result": analysis
    }

# -------------------------
# Node 4: Insight Generator
# -------------------------
def insight_node(state: AgentState):
    llm = get_llm()
    prompt = f"""
    Objective:
    {state['refined_goal']}

    Plan:
    {state['plan']}

    Data Analysis:
    {state['analysis_result']}

    Generate:
    - Key insights
    - Observed emission patterns
    - Actionable recommendations
    """
    insights = llm.invoke(prompt).content
    return {"insights": insights}

# -------------------------
# Build LangGraph
# -------------------------
def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("goal_interpreter", goal_interpreter_node)
    graph.add_node("planner", planner_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("insights", insight_node)

    graph.set_entry_point("goal_interpreter")
    graph.add_edge("goal_interpreter", "planner")
    graph.add_edge("planner", "analysis")
    graph.add_edge("analysis", "insights")
    graph.add_edge("insights", END)

    return graph.compile()
