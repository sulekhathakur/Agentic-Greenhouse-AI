from typing import TypedDict
import pandas as pd

class AgentState(TypedDict, total=False):
    user_goal: str
    refined_goal: str
    plan: str
    dataframe: pd.DataFrame
    analysis_result: str
    insights: str
