import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CreditWise AI • Smart Loan Approval Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PREMIUM HIGH-CONTRAST LIGHT FINTECH UI (CLEAN LIGHT INPUTS)
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    /* Global Page Styling & Theme Variables Override */
    :root,
    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .stApp,
    [data-theme="dark"],
    [data-theme="light"],
    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    div[data-baseweb="select"],
    div[data-baseweb="input"] {
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #f3f6fb !important;
        color: #0f172a !important;
        --background-color: #f3f6fb !important;
        --secondary-background-color: #eef4fc !important;
        --text-color: #0f172a !important;
        --primary-color: #2563eb !important;
    }

    /* Streamlit Defaults */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 1.5rem !important;
    }
    [data-testid="stToolbar"] {
        display: none !important;
    }
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* Block Container */
    .block-container {
        max-width: 1450px !important;
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
        margin: 0 auto !important;
    }

    /* =====================================================
       STYLISH APP HEADER & BRANDING
       ===================================================== */
    .top-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.35rem;
    }
    .app-brand-container {
        display: flex;
        align-items: center;
        gap: 0.65rem;
    }
    .app-logo-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1.5px solid #bfdbfe;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(37, 99, 235, 0.12);
        font-size: 1.3rem;
        flex-shrink: 0;
    }
    .app-brand-text-col {
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin: 0 !important;
        padding: 0 !important;
    }
    .app-brand-title {
        font-size: 1.45rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0b1f3a 0%, #1e40af 50%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.05 !important;
    }
    .app-brand-subtitle {
        font-size: 0.75rem;
        font-weight: 600;
        color: #486581;
        letter-spacing: 0.01em;
        margin: 0 !important;
        margin-top: 1px !important;
        padding: 0 !important;
        line-height: 1.1 !important;
    }

    /* =====================================================
       HIGHLIGHTED IMPORTANT NOTICE SECTION
       ===================================================== */
    .highlighted-notice-bar {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 45%, #fff7ed 100%);
        border: 1.5px solid #fcd34d;
        border-left: 5px solid #f59e0b;
        border-radius: 10px;
        padding: 0.6rem 1rem;
        font-size: 0.77rem;
        color: #78350f;
        line-height: 1.42;
        margin-bottom: 0.85rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        box-shadow: 0 3px 10px rgba(245, 158, 11, 0.12), 0 1px 2px rgba(245, 158, 11, 0.06);
    }
    .notice-badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        background: #f59e0b;
        color: #ffffff;
        -webkit-text-fill-color: #ffffff;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        padding: 0.22rem 0.6rem;
        border-radius: 6px;
        white-space: nowrap;
        box-shadow: 0 1px 3px rgba(180, 83, 9, 0.25);
        flex-shrink: 0;
    }
    .notice-text-content {
        flex: 1;
        font-weight: 500;
    }
    .notice-text-content strong {
        color: #92400e;
        font-weight: 700;
    }

    /* Cards / Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #dbe4f0 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05), 0 2px 4px -2px rgba(15, 23, 42, 0.03) !important;
        padding: 1rem 1.15rem !important;
    }

    /* Form Section Header */
    .section-headline {
        font-size: 0.85rem;
        font-weight: 700;
        color: #0f294d;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        margin-top: 0;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.35rem;
    }
    .section-headline.loan-info {
        margin-top: 0.95rem;
        padding-top: 0.75rem;
        border-top: 1px dashed #e2e8f0;
    }

    /* Field Label Text (Directly Above Input Box - Very Close) */
    .field-label-text {
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        line-height: 1.2;
        margin-bottom: 2px !important;
        display: block;
    }

    /* Field Range Indicator (Directly Below Input Box - Right Corner & Hugging Box Closely) */
    .field-range-below {
        font-size: 0.67rem;
        font-weight: 600;
        color: #475569;
        margin-top: -6px !important;
        margin-bottom: 0.35rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-end !important;
        text-align: right !important;
        gap: 0.25rem;
        line-height: 1.1;
        width: 100% !important;
    }
    .field-range-below .range-badge-tag {
        background: #e0ecfb;
        color: #1e3a8a;
        border: 1px solid #bfdbfe;
        font-weight: 700;
        padding: 0.03rem 0.32rem;
        border-radius: 4px;
        font-size: 0.60rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        flex-shrink: 0;
    }

    /* Tighten Streamlit element containers between label, input and range */
    div[data-testid="element-container"]:has(.field-label-text) {
        margin-bottom: -12px !important;
        padding-bottom: 0px !important;
    }
    div[data-testid="element-container"]:has(div[data-testid="stNumberInput"]),
    div[data-testid="element-container"]:has(div[data-testid="stTextInput"]),
    div[data-testid="element-container"]:has(div[data-testid="stSelectbox"]) {
        margin-top: 0px !important;
        margin-bottom: -8px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }
    div[data-testid="element-container"]:has(.field-range-below) {
        margin-top: -4px !important;
        margin-bottom: 0.15rem !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    /* Widget Spacing & Outer Resets */
    div[data-testid="stNumberInput"],
    div[data-testid="stTextInput"],
    div[data-testid="stSelectbox"] {
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
        height: auto !important;
        min-height: auto !important;
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
    }

    /* =====================================================
       COMPREHENSIVE LIGHT FINTECH SELECTBOX & INPUT STYLING
       (CLEAN WHITE BOXES, LIGHT STEPPERS, CRISP CHEVRONS)
       ===================================================== */
    /* 1. All BaseWeb & Streamlit input controls */
    div[data-testid="stNumberInputContainer"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"],
    div[data-testid="stNumberInputContainer"] > div,
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stTextInputContainer"] > div {
        background: #ffffff !important;
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        min-height: 40px !important;
        height: 40px !important;
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.15s ease-in-out !important;
        overflow: hidden !important;
    }

    /* 2. Selectbox Root & Outer Wrapper */
    div[data-testid="stSelectbox"],
    div[data-testid="stSelectbox"] > div {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 3. The Selectbox Input Box (Visible Control) - Pristine White Box with Clean Border */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: #ffffff !important;
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        min-height: 40px !important;
        height: 40px !important;
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
        padding-left: 12px !important;
        padding-right: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        cursor: pointer !important;
        transition: all 0.15s ease-in-out !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover {
        border-color: #94a3b8 !important;
        background-color: #ffffff !important;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.06) !important;
    }

    /* 4. Selectbox Inner elements transparency (preventing black backgrounds inside) */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div > div,
    div[data-testid="stSelectbox"] [data-baseweb="icon"],
    div[data-testid="stSelectbox"] [role="button"] {
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }

    /* 5. Typography and Values inside Selectboxes & Inputs */
    input,
    input[type="number"],
    input[type="text"],
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input,
    div[data-testid="stSelectbox"] input,
    div[data-testid="stSelectbox"] span,
    div[data-testid="stSelectbox"] p,
    div[data-testid="stSelectbox"] div {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        font-size: 0.84rem !important;
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
        font-weight: 600 !important;
    }

    input {
        padding: 4px 8px !important;
        border: none !important;
        background: transparent !important;
    }

    /* 6. Placeholders */
    input::placeholder,
    input::-webkit-input-placeholder,
    input::-moz-placeholder,
    input:-ms-input-placeholder,
    div[data-testid="stNumberInput"] input::placeholder,
    div[data-testid="stTextInput"] input::placeholder,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div[aria-hidden="true"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] span:empty,
    div[data-testid="stSelectbox"] [data-testid="stSelectboxPlaceholder"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] [data-baseweb="placeholder"] {
        color: #64748b !important;
        -webkit-text-fill-color: #64748b !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        opacity: 1 !important;
    }

    /* 7. Dropdown Arrow - Clean Downward Chevron (Opposite of ^) */
    div[data-testid="stSelectbox"] svg,
    div[data-baseweb="select"] svg,
    div[data-testid="stSelectbox"] [data-baseweb="icon"] svg {
        fill: #475569 !important;
        color: #475569 !important;
        width: 16px !important;
        height: 16px !important;
        min-width: 16px !important;
        min-height: 16px !important;
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        display: block !important;
    }
    div[data-testid="stSelectbox"] svg path,
    div[data-baseweb="select"] svg path,
    div[data-testid="stSelectbox"] [data-baseweb="icon"] svg path {
        fill: #475569 !important;
        color: #475569 !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover svg {
        fill: #0f294d !important;
        color: #0f294d !important;
    }

    /* 8. STEPPER (+ / -) BUTTONS - PERFECTLY CENTERED, EQUALLY FITTED & BALANCED */
    div[data-testid="stNumberInputContainer"] div[data-baseweb="input"] > div:last-child,
    div[data-testid="stNumberInput"] div[data-baseweb="input"] > div:last-child,
    div[data-testid="stNumberInputContainer"] [role="group"],
    div[data-testid="stNumberInput"] [role="group"] {
        background: #f8fafc !important;
        background-color: #f8fafc !important;
        border-left: 1px solid #e2e8f0 !important;
        border-top: none !important;
        border-bottom: none !important;
        border-right: none !important;
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 6px !important;
        gap: 4px !important;
        height: 100% !important;
        min-height: 100% !important;
        margin: 0 !important;
        box-sizing: border-box !important;
    }

    div[data-testid="stNumberInputStepDown"],
    div[data-testid="stNumberInputStepUp"] {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        height: auto !important;
        width: auto !important;
    }

    button[data-testid="stNumberInputStepDown"],
    button[data-testid="stNumberInputStepUp"],
    div[data-testid="stNumberInputStepDown"] button,
    div[data-testid="stNumberInputStepUp"] button,
    div[data-testid="stNumberInputContainer"] button,
    div[data-testid="stNumberInput"] button,
    div[data-testid="stNumberInputContainer"] [role="group"] button,
    div[data-testid="stNumberInput"] [role="group"] button,
    div[data-testid="stNumberInputContainer"] div[data-baseweb="input"] button {
        background: #ffffff !important;
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        color: #334155 !important;
        -webkit-text-fill-color: #334155 !important;
        border-radius: 4px !important;
        margin: 0 !important;
        padding: 0 !important;
        height: 22px !important;
        width: 22px !important;
        min-height: 22px !important;
        min-width: 22px !important;
        max-height: 22px !important;
        max-width: 22px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        align-self: center !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
        box-sizing: border-box !important;
    }

    button[data-testid="stNumberInputStepDown"]:hover,
    button[data-testid="stNumberInputStepUp"]:hover,
    div[data-testid="stNumberInputContainer"] button:hover,
    div[data-testid="stNumberInput"] button:hover,
    div[data-testid="stNumberInputStepDown"] button:hover,
    div[data-testid="stNumberInputStepUp"] button:hover {
        background: #f1f5f9 !important;
        background-color: #f1f5f9 !important;
        border-color: #94a3b8 !important;
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
    }

    div[data-testid="stNumberInput"] button svg,
    div[data-testid="stNumberInputContainer"] button svg,
    div[data-testid="stNumberInputStepDown"] svg,
    div[data-testid="stNumberInputStepUp"] svg,
    button[data-testid="stNumberInputStepDown"] svg,
    button[data-testid="stNumberInputStepUp"] svg {
        fill: #334155 !important;
        color: #334155 !important;
        width: 9px !important;
        height: 9px !important;
        min-width: 9px !important;
        min-height: 9px !important;
        max-width: 9px !important;
        max-height: 9px !important;
        display: block !important;
        margin: auto !important;
    }

    /* 9. Focus State across all widgets */
    div[data-testid="stNumberInputContainer"]:focus-within,
    div[data-testid="stNumberInput"] div[data-baseweb="input"]:focus-within,
    div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within,
    div[data-testid="stSelectbox"]:focus-within [data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div[aria-expanded="true"] {
        background-color: #ffffff !important;
        background: #ffffff !important;
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }

    /* Inner nested container resets */
    div[data-testid="stNumberInputContainer"] div[data-baseweb="base-input"],
    div[data-testid="stNumberInputContainer"] div[data-baseweb="input"],
    div[data-testid="stNumberInput"] div[data-baseweb="base-input"],
    div[data-testid="stTextInput"] div[data-baseweb="base-input"] {
        border: none !important;
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }

    /* Streamlit input instruction / tooltip styling */
    div[data-testid="stInputInstructions"],
    div[data-testid="stInputInstructions"] > span {
        display: none !important;
    }

    /* Streamlit Alert, Warning, Notification High-Contrast Light Styling */
    div[data-testid="stAlert"],
    .stAlert,
    div[data-testid="stNotification"],
    div[data-baseweb="notification"] {
        background-color: #fffbeb !important;
        background: #fffbeb !important;
        border: 1.5px solid #fcd34d !important;
        border-left: 5px solid #f59e0b !important;
        border-radius: 8px !important;
        color: #78350f !important;
        -webkit-text-fill-color: #78350f !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        padding: 0.6rem 0.85rem !important;
        margin: 0.5rem 0 !important;
    }
    div[data-testid="stAlert"] *,
    .stAlert *,
    div[data-testid="stNotification"] *,
    div[data-baseweb="notification"] * {
        color: #78350f !important;
        -webkit-text-fill-color: #78350f !important;
    }
    div[data-testid="stAlert"] svg {
        fill: #d97706 !important;
        color: #d97706 !important;
    }
    div[data-testid="stCaptionContainer"],
    .stCaption,
    small {
        color: #475569 !important;
        -webkit-text-fill-color: #475569 !important;
        font-size: 0.74rem !important;
        font-weight: 600 !important;
    }

    /* 10. Dropdown Popup Menu (Listbox when opened) - Pure White with Clear Options */
    body > div[data-baseweb="popover"],
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    div[data-testid="stSelectboxVirtualDropdown"],
    ul[role="listbox"] {
        background-color: #ffffff !important;
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.12) !important;
        padding: 4px !important;
        z-index: 999999 !important;
    }

    /* 11. Individual Dropdown Options */
    li[role="option"],
    div[role="option"] {
        background-color: #ffffff !important;
        background: #ffffff !important;
        color: #0f294d !important;
        -webkit-text-fill-color: #0f294d !important;
        font-weight: 600 !important;
        font-size: 0.83rem !important;
        border-radius: 6px !important;
        padding: 8px 12px !important;
        margin: 2px 0 !important;
        cursor: pointer !important;
        transition: all 0.12s ease !important;
    }
    li[role="option"]:hover,
    li[role="option"]:focus,
    li[role="option"][aria-selected="true"],
    div[role="option"]:hover,
    div[role="option"][aria-selected="true"] {
        background-color: #eef4fc !important;
        background: #eef4fc !important;
        color: #1d4ed8 !important;
        -webkit-text-fill-color: #1d4ed8 !important;
        font-weight: 700 !important;
    }

    /* =====================================================
       PREDICT BUTTON (PRIMARY ACTION)
       ===================================================== */
    div.stButton > button[kind="primary"],
    button[data-testid="baseButton-primary"],
    button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%) !important;
        background-color: #2563eb !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        height: 44px !important;
        min-height: 44px !important;
        font-size: 0.92rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.01em !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.28) !important;
        transition: all 0.15s ease-in-out !important;
        margin-top: 0.65rem !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stButton > button[kind="primary"]:hover,
    button[data-testid="baseButton-primary"]:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.38) !important;
        transform: translateY(-1px) !important;
    }

    /* =====================================================
       CLEAR ALL BUTTON - COHESIVE ICE-BLUE WITH HOVER EFFECT
       ===================================================== */
    button[data-testid="baseButton-secondary"],
    button[data-testid="stBaseButton-secondary"],
    button[kind="secondary"],
    .clear-btn-wrap button,
    .clear-btn-wrap div.stButton > button,
    div[data-testid="stButton"] > button:not([kind="primary"]) {
        background: #eef4fc !important;
        background-color: #eef4fc !important;
        color: #1e3a8a !important;
        -webkit-text-fill-color: #1e3a8a !important;
        border: 1.5px solid #c8ddf7 !important;
        border-radius: 8px !important;
        height: 38px !important;
        min-height: 38px !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        padding: 0 1.15rem !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.18s ease-in-out !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    button[data-testid="baseButton-secondary"]:hover,
    button[data-testid="stBaseButton-secondary"]:hover,
    button[kind="secondary"]:hover,
    .clear-btn-wrap button:hover,
    div[data-testid="stButton"] > button:not([kind="primary"]):hover {
        background: #dbeafe !important;
        background-color: #dbeafe !important;
        color: #1d4ed8 !important;
        -webkit-text-fill-color: #1d4ed8 !important;
        border-color: #93c5fd !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.15) !important;
        transform: translateY(-1px) !important;
    }

    /* Result Panel Styling (Right Column - Distinct Separated Boxes) */
    .result-container-card {
        display: flex;
        flex-direction: column;
        gap: 0.65rem;
    }
    .result-header-box {
        background: #ffffff;
        border: 1.5px solid #dbe4f0;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 5px rgba(15, 23, 42, 0.03);
        margin-bottom: 0.65rem;
    }
    .result-title-text {
        font-size: 0.92rem;
        font-weight: 800;
        color: #0f294d;
        display: flex;
        align-items: center;
        gap: 0.4rem;
        margin: 0;
    }

    .badge-status {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.25rem 0.65rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.02em;
    }
    .badge-status.approved {
        background: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
    }
    .badge-status.rejected {
        background: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fca5a5;
    }
    .badge-status.ready {
        background: #eef4fc;
        color: #1e3a8a;
        border: 1px solid #c8ddf7;
    }

    /* Gauge / Probability Card (Separated Box) */
    .prob-metric-card {
        background: #ffffff;
        border: 1.5px solid #dbe4f0;
        border-radius: 10px;
        padding: 1.15rem 1rem;
        text-align: center;
        margin-bottom: 0.65rem;
        box-shadow: 0 2px 5px rgba(15, 23, 42, 0.03);
    }
    .prob-metric-number {
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1;
        letter-spacing: -0.03em;
    }
    .prob-metric-number.approved {
        color: #059669;
    }
    .prob-metric-number.rejected {
        color: #dc2626;
    }
    .prob-metric-label {
        font-size: 0.72rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.45rem;
    }

    /* Modern Progress Track */
    .prob-track {
        width: 100%;
        height: 8px;
        background: #e2e8f0;
        border-radius: 999px;
        overflow: hidden;
        margin-top: 0.65rem;
    }
    .prob-fill {
        height: 100%;
        border-radius: 999px;
        transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .prob-fill.approved {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
    }
    .prob-fill.rejected {
        background: linear-gradient(90deg, #f87171 0%, #dc2626 100%);
    }

    /* 2-Column Mini Metrics in Right Panel (Separated Boxes) */
    .mini-metrics-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.65rem;
        margin-bottom: 0.65rem;
    }
    .mini-metric-box {
        background: #ffffff;
        border: 1.5px solid #dbe4f0;
        border-radius: 10px;
        padding: 0.75rem 0.85rem;
        box-shadow: 0 2px 5px rgba(15, 23, 42, 0.03);
    }
    .mini-metric-tag {
        font-size: 0.65rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }
    .mini-metric-value {
        font-size: 0.98rem;
        font-weight: 800;
        margin-top: 0.2rem;
    }

    .risk-pill {
        display: inline-block;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 800;
    }
    .risk-low { background: #dcfce7; color: #15803d; }
    .risk-moderate { background: #fef3c7; color: #b45309; }
    .risk-high { background: #fee2e2; color: #b91c1c; }

    /* Summary Note Card (Separated Box) */
    .summary-note-card {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.75rem 0.95rem;
        font-size: 0.74rem;
        color: #334e68;
        line-height: 1.4;
        margin-bottom: 0.65rem;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
    }

    /* Empty state (Separated Box) */
    .empty-state-card {
        background: #f8fafc;
        border: 1.5px dashed #cbd5e1;
        border-radius: 10px;
        text-align: center;
        padding: 1.8rem 1rem;
        color: #64748b;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.65rem;
    }
    .empty-icon {
        font-size: 2.4rem;
        margin-bottom: 0.6rem;
    }

    /* Expander styling */
    div[data-testid="stExpander"] {
        border: 1.5px solid #dbe4f0 !important;
        border-radius: 10px !important;
        background: #ffffff !important;
        margin-top: 0.65rem !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02) !important;
    }
    div[data-testid="stExpander"] summary {
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        color: #1e293b !important;
        padding: 0.4rem 0.6rem !important;
    }

    /* Light Theme Submitted Info Table */
    .table-responsive-box {
        overflow-x: auto;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        margin-top: 0.35rem;
        -webkit-overflow-scrolling: touch;
    }
    .light-custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.75rem;
        text-align: left;
    }
    .light-custom-table th {
        background: #f1f5f9;
        color: #334155;
        font-weight: 700;
        padding: 0.45rem 0.65rem;
        border-bottom: 1px solid #cbd5e1;
        border-right: 1px solid #e2e8f0;
    }
    .light-custom-table td {
        background: #ffffff;
        color: #0f172a;
        padding: 0.45rem 0.65rem;
        border-bottom: 1px solid #f1f5f9;
        border-right: 1px solid #f1f5f9;
        font-weight: 600;
    }
    .light-custom-table tr:nth-child(even) td {
        background: #f8fafc;
    }

    /* =====================================================
       COMPREHENSIVE MOBILE RESPONSIVENESS (<768px & <480px)
       ===================================================== */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.4rem !important;
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
            padding-bottom: 1.5rem !important;
        }
        .top-header-row {
            flex-direction: column;
            align-items: stretch;
            gap: 0.6rem;
            margin-bottom: 0.6rem;
        }
        .app-brand-container {
            gap: 0.55rem;
        }
        .app-logo-badge {
            width: 36px;
            height: 36px;
            font-size: 1.15rem;
        }
        .app-brand-title {
            font-size: 1.25rem;
        }
        .app-brand-subtitle {
            font-size: 0.7rem;
        }
        .highlighted-notice-bar {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.4rem;
            padding: 0.55rem 0.75rem;
            font-size: 0.73rem;
        }
        .clear-btn-wrap {
            width: 100%;
        }
        .clear-btn-wrap button,
        .clear-btn-wrap div.stButton > button,
        button[data-testid="baseButton-secondary"] {
            width: 100% !important;
            height: 40px !important;
        }
        div.stButton > button[kind="primary"] {
            width: 100% !important;
            height: 44px !important;
            font-size: 0.95rem !important;
        }
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stTextInput"] div[data-baseweb="input"],
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
            min-height: 42px !important;
            height: 42px !important;
        }
    }

    @media (max-width: 480px) {
        .app-brand-title {
            font-size: 1.1rem;
        }
        .prob-metric-number {
            font-size: 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL & ARTIFACTS
# =========================================================

@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    ohe = joblib.load("encoder.pkl")
    education_encoder = joblib.load("education_encoder.pkl")
    return model, scaler, ohe, education_encoder


try:
    model, scaler, ohe, education_encoder = load_artifacts()
except Exception as e:
    st.error(f"Error loading model artifacts: {e}")
    st.stop()


# =========================================================
# CLEAR ALL CALLBACK
# =========================================================

def clear_all():
    st.session_state["applicant_income"] = None
    st.session_state["coapplicant_income"] = None
    st.session_state["dti_ratio"] = None
    st.session_state["age"] = None
    st.session_state["credit_score"] = None
    st.session_state["savings"] = None
    st.session_state["dependents"] = None
    st.session_state["existing_loans"] = None
    st.session_state["collateral_value"] = None
    st.session_state["loan_amount"] = None
    st.session_state["loan_term"] = None
    st.session_state["gender"] = None
    st.session_state["marital_status"] = None
    st.session_state["employment_status"] = None
    st.session_state["education_level"] = None
    st.session_state["loan_purpose"] = None
    st.session_state["property_area"] = None
    st.session_state["employer_category"] = None


# =========================================================
# HEADER & UPDATED IMPORTANT NOTICE
# =========================================================

head_col1, head_col2 = st.columns([5.8, 1.4], vertical_alignment="center")

with head_col1:
    st.markdown(
        """
        <div class="top-header-row">
            <div class="app-brand-container">
                <div class="app-logo-badge">🏦</div>
                <div class="app-brand-text-col">
                    <h1 class="app-brand-title">CreditWise AI</h1>
                    <div class="app-brand-subtitle">Data-Driven Loan Approval Prediction</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with head_col2:
    st.markdown('<div class="clear-btn-wrap">', unsafe_allow_html=True)
    st.button(
        "↻ Clear All",
        key="clear_button",
        on_click=clear_all,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlighted-notice-bar">
        <span class="notice-badge-pill">⚠️ IMPORTANT NOTICE</span>
        <div class="notice-text-content">
            This is a <strong>machine-learning estimate</strong> based on historical data. It is for educational purposes only and <strong>does not guarantee</strong> actual loan approval or rejection. Final decisions are made by the relevant financial institution.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MAIN 2-COLUMN DASHBOARD (INPUT LEFT, RESULT BESIDE ON RIGHT)
# =========================================================

form_col, result_col = st.columns([1.95, 1.05], gap="medium")


# =========================================================
# LEFT COLUMN: COMPACT FORM GRID
# =========================================================

with form_col:
    with st.container(border=True):
        st.markdown(
            '<div class="section-headline">👤 Applicant & Financial Information</div>',
            unsafe_allow_html=True
        )

        # Row 1: Applicant Income | Coapplicant Income | DTI Ratio
        r1c1, r1c2, r1c3 = st.columns(3)
        with r1c1:
            st.markdown(
                '<div class="field-label-text">Applicant Income (₹)</div>',
                unsafe_allow_html=True
            )
            applicant_income = st.number_input(
                "Applicant Income (₹)",
                min_value=0.0,
                value=None,
                step=500.0,
                placeholder="Enter income",
                key="applicant_income",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> ≥ ₹0</div>',
                unsafe_allow_html=True
            )
        with r1c2:
            st.markdown(
                '<div class="field-label-text">Coapplicant Income (₹)</div>',
                unsafe_allow_html=True
            )
            coapplicant_income = st.number_input(
                "Coapplicant Income (₹)",
                min_value=0.0,
                value=None,
                step=500.0,
                placeholder="Enter income",
                key="coapplicant_income",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> ≥ ₹0 (0 if none)</div>',
                unsafe_allow_html=True
            )
        with r1c3:
            st.markdown(
                '<div class="field-label-text">DTI Ratio (Debt-to-Income)</div>',
                unsafe_allow_html=True
            )
            dti_ratio = st.number_input(
                "DTI Ratio (Debt-to-Income)",
                min_value=0.00,
                max_value=1.00,
                value=None,
                step=0.01,
                format="%.2f",
                placeholder="Enter DTI ratio",
                key="dti_ratio",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 0.00 – 1.00 &bull; E.g., 30% → 0.30</div>',
                unsafe_allow_html=True
            )

        # Row 2: Age (In Years) | Credit Score | Savings
        r2c1, r2c2, r2c3 = st.columns(3)
        with r2c1:
            st.markdown(
                '<div class="field-label-text">Age (In Years)</div>',
                unsafe_allow_html=True
            )
            age = st.number_input(
                "Age (In Years)",
                min_value=21,
                max_value=59,
                value=None,
                step=1,
                placeholder="Enter age",
                key="age",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 21 – 59 Years</div>',
                unsafe_allow_html=True
            )
        with r2c2:
            st.markdown(
                '<div class="field-label-text">Credit Score</div>',
                unsafe_allow_html=True
            )
            credit_score = st.number_input(
                "Credit Score",
                min_value=550.0,
                max_value=799.0,
                value=None,
                step=1.0,
                placeholder="Enter credit score",
                key="credit_score",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 550 – 799</div>',
                unsafe_allow_html=True
            )
        with r2c3:
            st.markdown(
                '<div class="field-label-text">Savings (₹)</div>',
                unsafe_allow_html=True
            )
            savings = st.number_input(
                "Savings (₹)",
                min_value=0.0,
                value=None,
                step=500.0,
                placeholder="Enter savings",
                key="savings",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> ≥ ₹0</div>',
                unsafe_allow_html=True
            )

        # Row 3: Dependents | Existing Loans | Collateral Value
        r3c1, r3c2, r3c3 = st.columns(3)
        with r3c1:
            st.markdown(
                '<div class="field-label-text">Dependents</div>',
                unsafe_allow_html=True
            )
            dependents = st.number_input(
                "Dependents",
                min_value=0,
                max_value=3,
                value=None,
                step=1,
                placeholder="Enter dependents",
                key="dependents",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 0 – 3 Dependents</div>',
                unsafe_allow_html=True
            )
        with r3c2:
            st.markdown(
                '<div class="field-label-text">Existing Loans</div>',
                unsafe_allow_html=True
            )
            existing_loans = st.number_input(
                "Existing Loans",
                min_value=0,
                max_value=4,
                value=None,
                step=1,
                placeholder="Enter number of loans",
                key="existing_loans",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 0 – 4 Active Loans</div>',
                unsafe_allow_html=True
            )
        with r3c3:
            st.markdown(
                '<div class="field-label-text">Collateral Value (₹)</div>',
                unsafe_allow_html=True
            )
            collateral_value = st.number_input(
                "Collateral Value (₹)",
                min_value=0.0,
                value=None,
                step=500.0,
                placeholder="Enter collateral value",
                key="collateral_value",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> ≥ ₹0</div>',
                unsafe_allow_html=True
            )

        # Row 4: Loan Amount | Loan Term | Gender
        r4c1, r4c2, r4c3 = st.columns(3)
        with r4c1:
            st.markdown(
                '<div class="field-label-text">Loan Amount (₹)</div>',
                unsafe_allow_html=True
            )
            loan_amount = st.number_input(
                "Loan Amount (₹)",
                min_value=0.0,
                value=None,
                step=500.0,
                placeholder="Enter loan amount",
                key="loan_amount",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> ≥ ₹0</div>',
                unsafe_allow_html=True
            )
        with r4c2:
            st.markdown(
                '<div class="field-label-text">Loan Term (Months)</div>',
                unsafe_allow_html=True
            )
            loan_term = st.number_input(
                "Loan Term (Months)",
                min_value=12,
                max_value=84,
                value=None,
                step=12,
                placeholder="Enter loan term",
                key="loan_term",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Range</span> 12 – 84 Months (Steps of 12)</div>',
                unsafe_allow_html=True
            )
        with r4c3:
            st.markdown(
                '<div class="field-label-text">Gender</div>',
                unsafe_allow_html=True
            )
            gender = st.selectbox(
                "Gender",
                ["Female", "Male"],
                index=None,
                placeholder="Select gender",
                key="gender",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Female / Male</div>',
                unsafe_allow_html=True
            )

        # Row 5: Marital Status | Employment Status | Education Level
        r5c1, r5c2, r5c3 = st.columns(3)
        with r5c1:
            st.markdown(
                '<div class="field-label-text">Marital Status</div>',
                unsafe_allow_html=True
            )
            marital_status = st.selectbox(
                "Marital Status",
                ["Married", "Single"],
                index=None,
                placeholder="Select marital status",
                key="marital_status",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Married / Single</div>',
                unsafe_allow_html=True
            )
        with r5c2:
            st.markdown(
                '<div class="field-label-text">Employment Status</div>',
                unsafe_allow_html=True
            )
            employment_status = st.selectbox(
                "Employment Status",
                ["Contract", "Salaried", "Self-employed", "Unemployed"],
                index=None,
                placeholder="Select employment status",
                key="employment_status",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Contract / Salaried / Self-emp. / Unemp.</div>',
                unsafe_allow_html=True
            )
        with r5c3:
            st.markdown(
                '<div class="field-label-text">Education Level</div>',
                unsafe_allow_html=True
            )
            education_level = st.selectbox(
                "Education Level",
                ["Graduate", "Not Graduate"],
                index=None,
                placeholder="Select education level",
                key="education_level",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Graduate / Not Graduate</div>',
                unsafe_allow_html=True
            )

        # Section: Loan Information
        st.markdown(
            '<div class="section-headline loan-info">💼 Loan Information</div>',
            unsafe_allow_html=True
        )

        lr1, lr2, lr3 = st.columns(3)
        with lr1:
            st.markdown(
                '<div class="field-label-text">Loan Purpose</div>',
                unsafe_allow_html=True
            )
            loan_purpose = st.selectbox(
                "Loan Purpose",
                ["Business", "Car", "Education", "Home", "Personal"],
                index=None,
                placeholder="Select loan purpose",
                key="loan_purpose",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Business / Car / Education / Home / Personal</div>',
                unsafe_allow_html=True
            )
        with lr2:
            st.markdown(
                '<div class="field-label-text">Property Area</div>',
                unsafe_allow_html=True
            )
            property_area = st.selectbox(
                "Property Area",
                ["Rural", "Semiurban", "Urban"],
                index=None,
                placeholder="Select property area",
                key="property_area",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Rural / Semiurban / Urban</div>',
                unsafe_allow_html=True
            )
        with lr3:
            st.markdown(
                '<div class="field-label-text">Employer Category</div>',
                unsafe_allow_html=True
            )
            employer_category = st.selectbox(
                "Employer Category",
                ["Government", "MNC", "Private", "Unemployed"],
                index=None,
                placeholder="Select employer category",
                key="employer_category",
                label_visibility="collapsed"
            )
            st.markdown(
                '<div class="field-range-below"><span class="range-badge-tag">Options</span> Government / MNC / Private / Unemployed</div>',
                unsafe_allow_html=True
            )

        # Primary Action Button
        predict_button = st.button(
            "✨ Predict Loan Approval",
            type="primary",
            use_container_width=True
        )


# =========================================================
# RIGHT COLUMN: PREDICTION RESULT CARD (BESIDE FORM)
# =========================================================

with result_col:
    with st.container(border=True):
        if not predict_button:
            # Idle / Ready State (Separated Boxes)
            st.markdown(
                """
                <div class="result-header-box">
                    <div class="result-title-text">📊 Prediction Result</div>
                    <span class="badge-status ready">● Ready</span>
                </div>
                <div class="empty-state-card">
                    <div class="empty-icon">🏛️</div>
                    <div style="font-weight: 700; color: #0f294d; font-size: 0.95rem; margin-bottom: 0.25rem;">Ready for Prediction</div>
                    <div style="font-size: 0.78rem; color: #486581; line-height: 1.4;">Enter the applicant details on the left and click predict to calculate the ML loan assessment.</div>
                </div>
                <div class="mini-metrics-row">
                    <div class="mini-metric-box">
                        <div class="mini-metric-tag">Prediction</div>
                        <div class="mini-metric-value" style="color: #94a3b8;">—</div>
                    </div>
                    <div class="mini-metric-box">
                        <div class="mini-metric-tag">Risk Level</div>
                        <div class="mini-metric-value" style="color: #94a3b8;">—</div>
                    </div>
                </div>
                <div class="summary-note-card" style="text-align: center; color: #64748b; font-size: 0.72rem;">
                    No prediction calculated yet. Fill form and click predict.
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Validation Check
            missing = []
            if applicant_income is None: missing.append("Applicant Income")
            if coapplicant_income is None: missing.append("Coapplicant Income")
            if dti_ratio is None: missing.append("DTI Ratio")
            if age is None: missing.append("Age")
            if credit_score is None: missing.append("Credit Score")
            if savings is None: missing.append("Savings")
            if dependents is None: missing.append("Dependents")
            if existing_loans is None: missing.append("Existing Loans")
            if collateral_value is None: missing.append("Collateral Value")
            if loan_amount is None: missing.append("Loan Amount")
            if loan_term is None: missing.append("Loan Term")
            if gender is None: missing.append("Gender")
            if marital_status is None: missing.append("Marital Status")
            if employment_status is None: missing.append("Employment Status")
            if education_level is None: missing.append("Education Level")
            if loan_purpose is None: missing.append("Loan Purpose")
            if property_area is None: missing.append("Property Area")
            if employer_category is None: missing.append("Employer Category")

            if missing:
                missing_pills = "".join([f'<span style="display:inline-block; background:#fef3c7; color:#92400e; border:1px solid #fde68a; border-radius:4px; padding:2px 7px; font-size:0.7rem; font-weight:700; margin:2px 3px 2px 0;">{field}</span>' for field in missing])
                st.markdown(
                    f"""
                    <div class="result-header-box">
                        <div class="result-title-text">📊 Prediction Result</div>
                        <span class="badge-status" style="background:#fee2e2; color:#b91c1c; border: 1px solid #fca5a5;">⚠️ Incomplete</span>
                    </div>
                    <div style="background: #fffbeb; border: 1.5px solid #fcd34d; border-left: 5px solid #f59e0b; border-radius: 9px; padding: 0.85rem 1rem; margin-bottom: 0.65rem; box-shadow: 0 2px 6px rgba(245, 158, 11, 0.08);">
                        <div style="color: #92400e; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.35rem;">
                            <span>⚠️</span> Please complete all required fields.
                        </div>
                        <div style="color: #78350f; font-size: 0.76rem; line-height: 1.45; font-weight: 600; margin-bottom: 0.5rem;">
                            Please enter or select values for the remaining <strong>{len(missing)} field(s)</strong> on the left:
                        </div>
                        <div style="display:flex; flex-wrap:wrap; gap:3px;">
                            {missing_pills}
                        </div>
                    </div>
                    <div class="mini-metrics-row">
                        <div class="mini-metric-box">
                            <div class="mini-metric-tag">Status</div>
                            <div class="mini-metric-value" style="color: #d97706; font-size: 0.88rem;">INCOMPLETE</div>
                        </div>
                        <div class="mini-metric-box">
                            <div class="mini-metric-tag">Missing Fields</div>
                            <div class="mini-metric-value" style="color: #dc2626; font-size: 0.88rem;">{len(missing)} Remaining</div>
                        </div>
                    </div>
                    <div class="summary-note-card" style="text-align: center; color: #475569; font-weight: 600;">
                        Provide all required inputs on the left and click Predict again.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Run exact ML Pipeline
                input_df = pd.DataFrame({
                    "Applicant_Income": [applicant_income],
                    "Coapplicant_Income": [coapplicant_income],
                    "Employment_Status": [employment_status],
                    "Age": [age],
                    "Marital_Status": [marital_status],
                    "Dependents": [dependents],
                    "Credit_Score": [credit_score],
                    "Existing_Loans": [existing_loans],
                    "DTI_Ratio": [dti_ratio],
                    "Savings": [savings],
                    "Collateral_Value": [collateral_value],
                    "Loan_Amount": [loan_amount],
                    "Loan_Term": [loan_term],
                    "Loan_Purpose": [loan_purpose],
                    "Property_Area": [property_area],
                    "Education_Level": [education_level],
                    "Gender": [gender],
                    "Employer_Category": [employer_category]
                })

                # Education Level Encoding
                input_df["Education_Level"] = education_encoder.transform(
                    input_df["Education_Level"]
                )

                # Categorical One-Hot Encoding
                categorical_columns = [
                    "Employment_Status",
                    "Marital_Status",
                    "Loan_Purpose",
                    "Property_Area",
                    "Gender",
                    "Employer_Category"
                ]

                encoded = ohe.transform(input_df[categorical_columns])
                encoded_df = pd.DataFrame(
                    encoded,
                    columns=ohe.get_feature_names_out(categorical_columns),
                    index=input_df.index
                )

                input_df = pd.concat(
                    [input_df.drop(columns=categorical_columns), encoded_df],
                    axis=1
                )

                # Feature Engineering
                input_df["DTI_Ratio_sq"] = input_df["DTI_Ratio"] ** 2
                input_df["Credit_Score_sq"] = input_df["Credit_Score"] ** 2

                # Exact Training Feature Order
                if hasattr(scaler, "feature_names_in_"):
                    expected_features = list(scaler.feature_names_in_)
                    missing_features = [
                        f for f in expected_features if f not in input_df.columns
                    ]

                    if missing_features:
                        st.error("Model input mismatch detected.")
                        st.caption("Missing: " + ", ".join(missing_features))
                        st.stop()

                    input_df = input_df[expected_features]

                # Scaling
                input_scaled = scaler.transform(input_df)

                # Prediction
                prediction = model.predict(input_scaled)[0]
                probabilities = model.predict_proba(input_scaled)[0]

                if prediction == 1:
                    approval_index = list(model.classes_).index(1)
                    approval_prob = probabilities[approval_index] * 100

                    if approval_prob >= 80:
                        risk_label = "LOW"
                        risk_class = "risk-low"
                    elif approval_prob >= 60:
                        risk_label = "MODERATE"
                        risk_class = "risk-moderate"
                    else:
                        risk_label = "HIGHER"
                        risk_class = "risk-high"

                    st.markdown(
                        f"""
                        <div class="result-header-box">
                            <div class="result-title-text">📊 Prediction Result</div>
                            <span class="badge-status approved">✓ APPROVED</span>
                        </div>
                        <div class="prob-metric-card">
                            <div class="prob-metric-number approved">{approval_prob:.2f}%</div>
                            <div class="prob-metric-label">Estimated Approval Probability</div>
                            <div class="prob-track">
                                <div class="prob-fill approved" style="width: {min(100.0, max(5.0, approval_prob))}%;"></div>
                            </div>
                        </div>
                        <div class="mini-metrics-row">
                            <div class="mini-metric-box">
                                <div class="mini-metric-tag">Prediction</div>
                                <div class="mini-metric-value" style="color: #059669;">APPROVED</div>
                            </div>
                            <div class="mini-metric-box">
                                <div class="mini-metric-tag">Risk Level</div>
                                <div class="mini-metric-value"><span class="risk-pill {risk_class}">{risk_label}</span></div>
                            </div>
                        </div>
                        <div class="summary-note-card">
                            The model predicts a <strong>favorable approval outcome</strong> based on submitted financial parameters and creditworthiness.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    rejection_index = list(model.classes_).index(0)
                    rejection_prob = probabilities[rejection_index] * 100

                    if rejection_prob >= 80:
                        risk_label = "HIGH"
                        risk_class = "risk-high"
                    elif rejection_prob >= 60:
                        risk_label = "MODERATE"
                        risk_class = "risk-moderate"
                    else:
                        risk_label = "LOWER"
                        risk_class = "risk-low"

                    st.markdown(
                        f"""
                        <div class="result-header-box">
                            <div class="result-title-text">📊 Prediction Result</div>
                            <span class="badge-status rejected">✕ NOT APPROVED</span>
                        </div>
                        <div class="prob-metric-card">
                            <div class="prob-metric-number rejected">{rejection_prob:.2f}%</div>
                            <div class="prob-metric-label">Estimated Non-Approval Probability</div>
                            <div class="prob-track">
                                <div class="prob-fill rejected" style="width: {min(100.0, max(5.0, rejection_prob))}%;"></div>
                            </div>
                        </div>
                        <div class="mini-metrics-row">
                            <div class="mini-metric-box">
                                <div class="mini-metric-tag">Prediction</div>
                                <div class="mini-metric-value" style="color: #dc2626;">NOT APPROVED</div>
                            </div>
                            <div class="mini-metric-box">
                                <div class="mini-metric-tag">Risk Level</div>
                                <div class="mini-metric-value"><span class="risk-pill {risk_class}">{risk_label}</span></div>
                            </div>
                        </div>
                        <div class="summary-note-card">
                            The model estimates a <strong>higher risk profile</strong> based on debt ratio, credit score, or collateral coverage.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # Collapsed Expander for Submitted Information (Light, High-Contrast Table)
                with st.expander("👁 View Submitted Information", expanded=False):
                    st.markdown(
                        f"""
                        <div class="table-responsive-box">
                            <table class="light-custom-table">
                                <thead>
                                    <tr>
                                        <th>Field</th>
                                        <th>Submitted Value</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr><td>Applicant Income</td><td>₹{applicant_income:,.2f}</td></tr>
                                    <tr><td>Coapplicant Income</td><td>₹{coapplicant_income:,.2f}</td></tr>
                                    <tr><td>DTI Ratio</td><td>{dti_ratio * 100:.1f}% ({dti_ratio:.2f})</td></tr>
                                    <tr><td>Age</td><td>{age} Years</td></tr>
                                    <tr><td>Credit Score</td><td>{credit_score:.0f}</td></tr>
                                    <tr><td>Savings</td><td>₹{savings:,.2f}</td></tr>
                                    <tr><td>Dependents</td><td>{dependents}</td></tr>
                                    <tr><td>Existing Loans</td><td>{existing_loans}</td></tr>
                                    <tr><td>Collateral Value</td><td>₹{collateral_value:,.2f}</td></tr>
                                    <tr><td>Loan Amount</td><td>₹{loan_amount:,.2f}</td></tr>
                                    <tr><td>Loan Term</td><td>{loan_term} Months</td></tr>
                                    <tr><td>Gender</td><td>{gender}</td></tr>
                                    <tr><td>Marital Status</td><td>{marital_status}</td></tr>
                                    <tr><td>Employment Status</td><td>{employment_status}</td></tr>
                                    <tr><td>Education Level</td><td>{education_level}</td></tr>
                                    <tr><td>Loan Purpose</td><td>{loan_purpose}</td></tr>
                                    <tr><td>Property Area</td><td>{property_area}</td></tr>
                                    <tr><td>Employer Category</td><td>{employer_category}</td></tr>
                                </tbody>
                            </table>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
