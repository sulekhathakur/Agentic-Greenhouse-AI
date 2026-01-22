import streamlit as st
import pandas as pd
from agent.llm import get_llm

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Agentic AI – Greenhouse Emissions Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Utility: Clean LLM Output (CRITICAL)
# --------------------------------------------------
def clean_llm_output(text: str) -> str:
    if not text:
        return ""
    return (
        text.replace("```", "")
        .replace("```text", "")
        .replace("```markdown", "")
        .strip()
    )

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("greenhouse.csv")

df = load_data()

# --------------------------------------------------
# Global Styles (Research-Grade UI)
# --------------------------------------------------
st.markdown(
    """
    <style>
        html, body {
            background-color: #0b0f14;
            color: #e5e7eb;
            font-family: 'IBM Plex Sans', system-ui;
        }

        h1, h2, h3 {
            font-weight: 600;
            letter-spacing: -0.02em;
        }

        .pill {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 13px;
            margin-right: 8px;
        }

        .pill-green { background: #0f766e; color: #ccfbf1; }
        .pill-blue { background: #1e3a8a; color: #dbeafe; }
        .pill-amber { background: #78350f; color: #fde68a; }

        .output-box {
            background: #020617;
            border-left: 4px solid #22c55e;
            padding: 20px;
            border-radius: 8px;
            font-size: 15px;
            line-height: 1.65;
        }

        footer {
            text-align: center;
            color: #9ca3af;
            font-size: 14px;
            margin-top: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.markdown("### 🌍 Agent Control Panel")

    st.markdown(
        """
        **System Type**  
        Agentic AI (Goal-Driven)

        **Core Stack**  
        • LangChain  
        • LangGraph  
        • Groq LLM  
        • Streamlit  

        **Dataset**  
        Greenhouse Gas Emissions
        """
    )

    st.divider()

    st.markdown("**Agent Capabilities**")
    st.checkbox("Autonomous Planning", True, disabled=True)
    st.checkbox("Tool-Based Reasoning", True, disabled=True)
    st.checkbox("Data-Driven Analysis", True, disabled=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 style="color:#22c55e;">Agentic AI — Greenhouse Emissions Intelligence</h1>
    <p style="color:#9ca3af; max-width: 70%;">
        A research-oriented autonomous analysis system that interprets policy-scale
        climate objectives and generates data-backed environmental insights.
    </p>

    <div style="margin-top:12px;">
        <span class="pill pill-green">Agentic Reasoning</span>
        <span class="pill pill-blue">Autonomous Planning</span>
        <span class="pill pill-amber">Data-Driven Intelligence</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Metrics
# --------------------------------------------------
c1, c2, c3 = st.columns(3)
c1.metric("Dataset Size", f"{df.shape[0]} rows")
c2.metric("Reasoning Mode", "Autonomous")
c3.metric("Application Type", "Research Prototype")

# --------------------------------------------------
# Main Layout
# --------------------------------------------------
left, right = st.columns([2.2, 1])

with left:
    st.markdown("## Define Analysis Objective")

    st.markdown(
        """
        Provide a **clear analytical objective**.  
        The agent will interpret intent, plan analysis steps,
        examine the dataset, and generate structured insights.
        """
    )

    user_goal = st.text_area(
        label="",
        placeholder=(
            "Example:\n"
            "Identify the top greenhouse gas contributors across sectors "
            "and propose cost-feasible mitigation strategies backed by data trends."
        ),
        height=160
    )

    run_agent = st.button("Execute Agent Analysis", use_container_width=True)

with right:
    st.markdown("## Agent Workflow")

    st.markdown(
        """
        **1. Goal Interpretation**  
        Converts intent into analytical objectives  

        **2. Autonomous Planning**  
        Determines analysis pathway  

        **3. Dataset Examination**  
        Identifies patterns & contributors  

        **4. Insight Generation**  
        Produces structured recommendations  
        """
    )

# --------------------------------------------------
# Agent Execution
# --------------------------------------------------
if run_agent:
    if not user_goal.strip():
        st.warning("Please provide an analysis objective.")
    else:
        with st.spinner("Agent reasoning and analysis in progress..."):
            llm = get_llm()

            prompt = f"""
            You are an autonomous climate data analysis agent.

            Objective:
            {user_goal}

            Dataset Columns:
            {list(df.columns)}

            Sample Data:
            {df.head(8).to_string()}

            Produce:
            - Key findings
            - Observed emission patterns
            - Actionable, realistic recommendations

            Style:
            Formal, research-oriented, no code, no markdown formatting.
            """

            response = llm.invoke(prompt)
            final_output = clean_llm_output(response.content)

        st.success("Analysis complete")

        st.markdown("## Research Insights")
        st.markdown(f"<div class='output-box'>{final_output}</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.markdown(
    """
    <footer>
        Built by <strong>Sulekha Thakur</strong><br/>
        Agentic AI • Climate Intelligence • Research Prototype
    </footer>
    """,
    unsafe_allow_html=True
)
