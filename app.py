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
# MODERN SAAS THEME ENGINE: DUAL LIGHT & DARK MODE
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    /* =====================================================
       CSS DESIGN TOKENS (LIGHT DEFAULT & SAAS DARK MODE)
       ===================================================== */
    :root {
        /* Light Mode Tokens - Crisp, high-contrast, perfectly visible boxes */
        --app-bg: #f1f5f9;
        --app-bg-mesh: radial-gradient(at 10% 10%, #e2e8f0 0px, transparent 50%), radial-gradient(at 90% 90%, #e0f2fe 0px, transparent 50%);
        --app-card-bg: #ffffff;
        --app-card-border: #cbd5e1;
        --app-card-border-hover: #94a3b8;
        --app-card-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
        
        --app-text-title: #0f172a;
        --app-text-body: #1e293b;
        --app-text-muted: #475569;
        --app-text-subtle: #64748b;
        
        --input-bg: #ffffff;
        --input-border: #cbd5e1;
        --input-border-hover: #64748b;
        --input-text: #0f172a;
        --input-placeholder: #64748b;
        --input-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
        --input-focus-ring: rgba(37, 99, 235, 0.22);
        
        --stepper-bg: #f8fafc;
        --stepper-border: #cbd5e1;
        --stepper-text: #334155;
        --stepper-hover-bg: #e2e8f0;
        --stepper-group-bg: #f1f5f9;
        
        --btn-primary-bg: linear-gradient(135deg, #1e40af 0%, #2563eb 50%, #3b82f6 100%);
        --btn-primary-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
        --btn-primary-hover-shadow: 0 6px 20px rgba(37, 99, 235, 0.45);
        
        --btn-secondary-bg: #ffffff;
        --btn-secondary-border: #cbd5e1;
        --btn-secondary-text: #1e293b;
        --btn-secondary-hover-bg: #f8fafc;
        --btn-secondary-hover-border: #2563eb;
        --btn-secondary-hover-text: #1d4ed8;
        
        --range-tag-bg: #e0f2fe;
        --range-tag-border: #bae6fd;
        --range-tag-text: #0369a1;
        
        --notice-bg: #fffbeb;
        --notice-border: #fcd34d;
        --notice-accent: #f59e0b;
        --notice-text: #78350f;
        --notice-strong: #92400e;
        
        --sub-box-bg: #f8fafc;
        --sub-box-border: #cbd5e1;
        
        --metric-card-bg: #f8fafc;
        --metric-card-border: #cbd5e1;
        
        --table-th-bg: #f1f5f9;
        --table-th-text: #1e293b;
        --table-td-bg: #ffffff;
        --table-td-alt: #f8fafc;
        --table-border: #cbd5e1;
        
        --badge-approved-bg: #dcfce7;
        --badge-approved-border: #86efac;
        --badge-approved-text: #15803d;
        
        --badge-rejected-bg: #fee2e2;
        --badge-rejected-border: #fca5a5;
        --badge-rejected-text: #b91c1c;
        
        --badge-ready-bg: #e2e8f0;
        --badge-ready-border: #cbd5e1;
        --badge-ready-text: #334155;
    }

    /* Modern SaaS Dark Mode Palette */
    @media (prefers-color-scheme: dark) {
        :root {
            --app-bg: #090d16;
            --app-bg-mesh: radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.15) 0px, transparent 50%), radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.12) 0px, transparent 50%), radial-gradient(at 50% 100%, rgba(15, 23, 42, 0.5) 0px, transparent 60%);
            --app-card-bg: #0f172a;
            --app-card-border: #1e293b;
            --app-card-border-hover: #334155;
            --app-card-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.6), 0 2px 6px -2px rgba(0, 0, 0, 0.4);
            
            --app-text-title: #f8fafc;
            --app-text-body: #e2e8f0;
            --app-text-muted: #94a3b8;
            --app-text-subtle: #64748b;
            
            --input-bg: #090d16;
            --input-border: #1e293b;
            --input-border-hover: #3b82f6;
            --input-text: #f8fafc;
            --input-placeholder: #64748b;
            --input-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
            --input-focus-ring: rgba(59, 130, 246, 0.35);
            
            --stepper-bg: #141e33;
            --stepper-border: #22324e;
            --stepper-text: #cbd5e1;
            --stepper-hover-bg: #1e2d4a;
            --stepper-group-bg: #0b1120;
            
            --btn-primary-bg: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%);
            --btn-primary-shadow: 0 4px 16px rgba(37, 99, 235, 0.4);
            --btn-primary-hover-shadow: 0 6px 22px rgba(59, 130, 246, 0.55);
            
            --btn-secondary-bg: #131d31;
            --btn-secondary-border: #22324e;
            --btn-secondary-text: #93c5fd;
            --btn-secondary-hover-bg: #1a2742;
            --btn-secondary-hover-border: #3b82f6;
            --btn-secondary-hover-text: #bfdbfe;
            
            --range-tag-bg: #111d33;
            --range-tag-border: #1e355b;
            --range-tag-text: #93c5fd;
            
            --notice-bg: #1f1404;
            --notice-border: #78350f;
            --notice-accent: #f59e0b;
            --notice-text: #fef08a;
            --notice-strong: #fde047;
            
            --sub-box-bg: #0b1120;
            --sub-box-border: #1e293b;
            
            --metric-card-bg: #131d31;
            --metric-card-border: #1e293b;
            
            --table-th-bg: #0b1120;
            --table-th-text: #cbd5e1;
            --table-td-bg: #0f172a;
            --table-td-alt: #0b1120;
            --table-border: #1e293b;
            
            --badge-approved-bg: #052e16;
            --badge-approved-border: #15803d;
            --badge-approved-text: #86efac;
            
            --badge-rejected-bg: #450a0a;
            --badge-rejected-border: #991b1b;
            --badge-rejected-text: #fca5a5;
            
            --badge-ready-bg: #131d31;
            --badge-ready-border: #22324e;
            --badge-ready-text: #94a3b8;
        }
    }

    [data-theme="dark"] {
        --app-bg: #090d16 !important;
        --app-bg-mesh: radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.15) 0px, transparent 50%), radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.12) 0px, transparent 50%), radial-gradient(at 50% 100%, rgba(15, 23, 42, 0.5) 0px, transparent 60%) !important;
        --app-card-bg: #0f172a !important;
        --app-card-border: #1e293b !important;
        --app-card-border-hover: #334155 !important;
        --app-card-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.6), 0 2px 6px -2px rgba(0, 0, 0, 0.4) !important;
        
        --app-text-title: #f8fafc !important;
        --app-text-body: #e2e8f0 !important;
        --app-text-muted: #94a3b8 !important;
        --app-text-subtle: #64748b !important;
        
        --input-bg: #090d16 !important;
        --input-border: #1e293b !important;
        --input-border-hover: #3b82f6 !important;
        --input-text: #f8fafc !important;
        --input-placeholder: #64748b !important;
        --input-shadow: 0 1px 3px rgba(0, 0, 0, 0.4) !important;
        --input-focus-ring: rgba(59, 130, 246, 0.35) !important;
        
        --stepper-bg: #141e33 !important;
        --stepper-border: #22324e !important;
        --stepper-text: #cbd5e1 !important;
        --stepper-hover-bg: #1e2d4a !important;
        --stepper-group-bg: #0b1120 !important;
        
        --btn-primary-bg: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%) !important;
        --btn-primary-shadow: 0 4px 16px rgba(37, 99, 235, 0.4) !important;
        --btn-primary-hover-shadow: 0 6px 22px rgba(59, 130, 246, 0.55) !important;
        
        --btn-secondary-bg: #131d31 !important;
        --btn-secondary-border: #22324e !important;
        --btn-secondary-text: #93c5fd !important;
        --btn-secondary-hover-bg: #1a2742 !important;
        --btn-secondary-hover-border: #3b82f6 !important;
        --btn-secondary-hover-text: #bfdbfe !important;
        
        --range-tag-bg: #111d33 !important;
        --range-tag-border: #1e355b !important;
        --range-tag-text: #93c5fd !important;
        
        --notice-bg: #1f1404 !important;
        --notice-border: #78350f !important;
        --notice-accent: #f59e0b !important;
        --notice-text: #fef08a !important;
        --notice-strong: #fde047 !important;
        
        --sub-box-bg: #0b1120 !important;
        --sub-box-border: #1e293b !important;
        
        --metric-card-bg: #131d31 !important;
        --metric-card-border: #1e293b !important;
        
        --table-th-bg: #0b1120 !important;
        --table-th-text: #cbd5e1 !important;
        --table-td-bg: #0f172a !important;
        --table-td-alt: #0b1120 !important;
        --table-border: #1e293b !important;
        
        --badge-approved-bg: #052e16 !important;
        --badge-approved-border: #15803d !important;
        --badge-approved-text: #86efac !important;
        
        --badge-rejected-bg: #450a0a !important;
        --badge-rejected-border: #991b1b !important;
        --badge-rejected-text: #fca5a5 !important;
        
        --badge-ready-bg: #131d31 !important;
        --badge-ready-border: #22324e !important;
        --badge-ready-text: #94a3b8 !important;
    }

    /* Global Body Canvas with Mesh Background */
    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .stApp {
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: var(--app-bg) !important;
        background-image: var(--app-bg-mesh) !important;
        background-attachment: fixed !important;
        color: var(--app-text-body) !important;
        transition: background-color 0.25s ease, color 0.25s ease !important;
    }

    /* Streamlit Default Resets */
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

    /* Main Container Padding */
    .block-container {
        max-width: 1450px !important;
        padding-top: 0.6rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
        margin: 0 auto !important;
    }

    /* =====================================================
       APP BRANDING & HEADER
       ===================================================== */
    .top-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.45rem;
    }
    .app-brand-container {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .app-logo-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        background: var(--btn-secondary-bg);
        border: 1.5px solid var(--btn-secondary-border);
        border-radius: 12px;
        box-shadow: 0 3px 10px rgba(37, 99, 235, 0.12);
        font-size: 1.35rem;
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
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.05 !important;
        color: var(--app-text-title) !important;
        -webkit-text-fill-color: initial !important;
    }
    .app-brand-subtitle {
        font-size: 0.76rem;
        font-weight: 600;
        color: var(--app-text-muted) !important;
        letter-spacing: 0.01em;
        margin: 0 !important;
        margin-top: 2px !important;
        padding: 0 !important;
        line-height: 1.1 !important;
    }

    /* =====================================================
       IMPORTANT NOTICE BANNER
       ===================================================== */
    .highlighted-notice-bar {
        background: var(--notice-bg);
        border: 1.5px solid var(--notice-border);
        border-left: 5px solid var(--notice-accent);
        border-radius: 10px;
        padding: 0.65rem 1.1rem;
        font-size: 0.78rem;
        color: var(--notice-text) !important;
        line-height: 1.45;
        margin-bottom: 0.95rem;
        display: flex;
        align-items: center;
        gap: 0.85rem;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.08);
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
        padding: 0.24rem 0.65rem;
        border-radius: 6px;
        white-space: nowrap;
        box-shadow: 0 1px 3px rgba(180, 83, 9, 0.25);
        flex-shrink: 0;
    }
    .notice-text-content {
        flex: 1;
        font-weight: 500;
        color: var(--notice-text) !important;
    }
    .notice-text-content strong {
        color: var(--notice-strong) !important;
        font-weight: 700;
    }

    /* =====================================================
       MAIN CARDS / CONTAINERS (CLEARLY VISIBLE BOXES)
       ===================================================== */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--app-card-bg) !important;
        border: 1.5px solid var(--app-card-border) !important;
        border-radius: 14px !important;
        box-shadow: var(--app-card-shadow) !important;
        padding: 1.15rem 1.25rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    }

    /* Section Headlines */
    .section-headline {
        font-size: 0.88rem;
        font-weight: 800;
        color: var(--app-text-title) !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 0;
        margin-bottom: 0.85rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .section-headline.loan-info {
        margin-top: 1.05rem;
        padding-top: 0.85rem;
        border-top: 1px dashed var(--app-card-border);
    }

    /* Field Labels & Range Indicators */
    .field-label-row {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        margin-bottom: 3px !important;
        width: 100% !important;
    }

    .field-label-text {
        color: var(--app-text-title) !important;
        -webkit-text-fill-color: var(--app-text-title) !important;
        font-size: 0.79rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        line-height: 1.2;
        margin-bottom: 0px !important;
        display: inline-block;
    }

    /* Modern SaaS Micro-Alert beside entering value */
    .saas-micro-alert {
        display: inline-flex !important;
        align-items: center !important;
        gap: 3px !important;
        font-size: 0.67rem !important;
        font-weight: 800 !important;
        padding: 1.5px 6px !important;
        border-radius: 5px !important;
        background: #fef2f2 !important;
        color: #dc2626 !important;
        border: 1px solid #fca5a5 !important;
        box-shadow: 0 1px 3px rgba(220, 38, 38, 0.12) !important;
        line-height: 1.15 !important;
        white-space: nowrap !important;
        animation: saasAlertPop 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
    }

    @keyframes saasAlertPop {
        0% { transform: scale(0.92); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }

    @media (prefers-color-scheme: dark) {
        .saas-micro-alert {
            background: #450a0a !important;
            color: #fca5a5 !important;
            border: 1px solid #991b1b !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4) !important;
        }
    }
    [data-theme="dark"] .saas-micro-alert {
        background: #450a0a !important;
        color: #fca5a5 !important;
        border: 1px solid #991b1b !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4) !important;
    }

    .field-range-below {
        font-size: 0.68rem;
        font-weight: 600;
        color: var(--app-text-muted) !important;
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
        background: var(--range-tag-bg);
        color: var(--range-tag-text);
        border: 1px solid var(--range-tag-border);
        font-weight: 700;
        padding: 0.03rem 0.35rem;
        border-radius: 4px;
        font-size: 0.60rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        flex-shrink: 0;
    }
    .field-range-below .range-badge-tag.error-tag {
        background: #fee2e2 !important;
        color: #b91c1c !important;
        border: 1px solid #fca5a5 !important;
        font-weight: 800 !important;
    }
    .field-range-below .range-error-text {
        color: #dc2626 !important;
        font-weight: 700 !important;
    }

    @media (prefers-color-scheme: dark) {
        .field-range-below .range-badge-tag.error-tag {
            background: #450a0a !important;
            color: #fca5a5 !important;
            border: 1px solid #991b1b !important;
        }
        .field-range-below .range-error-text {
            color: #f87171 !important;
        }
    }
    [data-theme="dark"] .field-range-below .range-badge-tag.error-tag {
        background: #450a0a !important;
        color: #fca5a5 !important;
        border: 1px solid #991b1b !important;
    }
    [data-theme="dark"] .field-range-below .range-error-text {
        color: #f87171 !important;
    }

    /* Tighten widget spacing without breaking layout or causing overlaps */
    div[data-testid="element-container"]:has(.field-label-text),
    div[data-testid="element-container"]:has(.field-label-row) {
        margin-bottom: 2px !important;
        padding-bottom: 0px !important;
    }
    div[data-testid="element-container"]:has(div[data-testid="stNumberInput"]),
    div[data-testid="element-container"]:has(div[data-testid="stTextInput"]),
    div[data-testid="element-container"]:has(div[data-testid="stSelectbox"]) {
        margin-top: 0px !important;
        margin-bottom: 2px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }
    div[data-testid="element-container"]:has(.field-range-below) {
        margin-top: 2px !important;
        margin-bottom: 0.35rem !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    /* Completely hide any internal/collapsed Streamlit widget labels to prevent overlapping */
    label[data-testid="stWidgetLabel"],
    div[data-testid="stWidgetLabel"],
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stTextInput"] label {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
        min-height: 0px !important;
        max-height: 0px !important;
        width: 0px !important;
        min-width: 0px !important;
        max-width: 0px !important;
        margin: 0px !important;
        padding: 0px !important;
        position: absolute !important;
        pointer-events: none !important;
        clip: rect(0, 0, 0, 0) !important;
        opacity: 0 !important;
        overflow: hidden !important;
    }

    /* =====================================================
       INPUTS & CONTROLS (NUMBER INPUTS)
       ===================================================== */
    div[data-testid="stNumberInput"],
    div[data-testid="stTextInput"] {
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
    }

    div[data-testid="stNumberInputContainer"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"],
    div[data-testid="stTextInput"] div[data-baseweb="input"] {
        background: var(--input-bg) !important;
        background-color: var(--input-bg) !important;
        border: 1.5px solid var(--input-border) !important;
        border-radius: 8px !important;
        min-height: 40px !important;
        height: 40px !important;
        color: var(--input-text) !important;
        -webkit-text-fill-color: var(--input-text) !important;
        box-shadow: var(--input-shadow) !important;
        transition: all 0.15s ease-in-out !important;
        overflow: hidden !important;
    }

    div[data-testid="stNumberInputContainer"]:hover,
    div[data-testid="stNumberInput"] div[data-baseweb="input"]:hover,
    div[data-testid="stTextInput"] div[data-baseweb="input"]:hover {
        border-color: var(--input-border-hover) !important;
    }

    div[data-testid="stNumberInputContainer"]:focus-within,
    div[data-testid="stNumberInput"] div[data-baseweb="input"]:focus-within,
    div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px var(--input-focus-ring) !important;
    }

    input,
    input[type="number"],
    input[type="text"],
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        color: var(--input-text) !important;
        -webkit-text-fill-color: var(--input-text) !important;
        font-weight: 600 !important;
        padding: 4px 10px !important;
        border: none !important;
        background: transparent !important;
    }

    input::placeholder,
    input::-webkit-input-placeholder {
        color: var(--input-placeholder) !important;
        -webkit-text-fill-color: var(--input-placeholder) !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        opacity: 1 !important;
    }

    /* STEPPER (+ / -) CONTROLS */
    div[data-testid="stNumberInputContainer"] [role="group"],
    div[data-testid="stNumberInput"] [role="group"],
    div[data-testid="stNumberInputStepDown"],
    div[data-testid="stNumberInputStepUp"] {
        background: var(--stepper-group-bg) !important;
        background-color: var(--stepper-group-bg) !important;
        border-left: 1.5px solid var(--input-border) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 4px !important;
        gap: 3px !important;
        height: 100% !important;
    }

    button[data-testid="stNumberInputStepDown"],
    button[data-testid="stNumberInputStepUp"],
    div[data-testid="stNumberInputStepDown"] button,
    div[data-testid="stNumberInputStepUp"] button,
    div[data-testid="stNumberInputContainer"] button {
        background: var(--stepper-bg) !important;
        background-color: var(--stepper-bg) !important;
        border: 1px solid var(--stepper-border) !important;
        color: var(--stepper-text) !important;
        -webkit-text-fill-color: var(--stepper-text) !important;
        border-radius: 4px !important;
        margin: 0 !important;
        padding: 0 !important;
        height: 22px !important;
        width: 22px !important;
        min-height: 22px !important;
        min-width: 22px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }

    button[data-testid="stNumberInputStepDown"]:hover,
    button[data-testid="stNumberInputStepUp"]:hover,
    div[data-testid="stNumberInputContainer"] button:hover {
        background: var(--stepper-hover-bg) !important;
        border-color: var(--input-border-hover) !important;
        color: var(--input-text) !important;
    }

    /* =====================================================
       SELECTBOX & BULLETPROOF CRISP SEPARATE BOXES
       (Gender, Marital Status, Employment Status,
        Education Level, Loan Purpose, Property Area, Employer Category)
       ===================================================== */
    div[data-testid="stSelectbox"] {
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
        width: 100% !important;
        background: transparent !important;
        border: none !important;
    }

    div[data-testid="stSelectbox"] > div {
        background: transparent !important;
        border: none !important;
        width: 100% !important;
    }

    /* Main outer box container for selectbox - identical background (#ffffff in light, #090d16 in dark) & border as Age / Loan Term */
    div[data-testid="stSelectbox"] [data-baseweb="select"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"],
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[role="combobox"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div[role="combobox"],
    div[data-testid="stSelectbox"] [aria-haspopup="listbox"] {
        background: var(--input-bg) !important;
        background-color: var(--input-bg) !important;
        border: 1.5px solid var(--input-border) !important;
        border-radius: 8px !important;
        min-height: 40px !important;
        height: 40px !important;
        color: var(--input-text) !important;
        -webkit-text-fill-color: var(--input-text) !important;
        box-shadow: var(--input-shadow) !important;
        transition: all 0.15s ease-in-out !important;
        box-sizing: border-box !important;
        cursor: pointer !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        overflow: hidden !important;
        outline: none !important;
    }

    /* Prevent double borders and transparent inner layers on nested child divs */
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[role="combobox"] {
        background: var(--input-bg) !important;
        background-color: var(--input-bg) !important;
        border: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"]:hover,
    div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover,
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[role="combobox"]:hover,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div[role="combobox"]:hover {
        border-color: var(--input-border-hover) !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"]:focus,
    div[data-testid="stSelectbox"] [data-baseweb="select"]:focus-visible,
    div[data-testid="stSelectbox"] [data-baseweb="select"]:focus-within,
    div[data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within,
    div[data-testid="stSelectbox"] [data-baseweb="select"][aria-expanded="true"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"][aria-expanded="true"],
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[aria-expanded="true"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div[aria-expanded="true"],
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[role="combobox"]:focus-within,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div[role="combobox"]:focus-within {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px var(--input-focus-ring) !important;
        outline: none !important;
    }

    /* Inner value container */
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div > div:first-child,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div:first-child,
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[role="combobox"] > div:first-child {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        flex: 1 !important;
        overflow: hidden !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Typography inside Selectbox */
    div[data-testid="stSelectbox"] [data-baseweb="select"] span,
    div[data-testid="stSelectbox"] [role="combobox"] span,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: var(--input-text) !important;
        -webkit-text-fill-color: var(--input-text) !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

    div[data-testid="stSelectbox"] [data-testid="stSelectboxPlaceholder"],
    div[data-testid="stSelectbox"] [data-baseweb="placeholder"] {
        color: var(--input-placeholder) !important;
        -webkit-text-fill-color: var(--input-placeholder) !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        white-space: nowrap !important;
    }

    /* Guaranteed Dropdown Chevron Symbol Styling (Clean target on icon container and SVG only) */
    div[data-testid="stSelectbox"] [data-baseweb="icon"],
    div[data-baseweb="select"] [data-baseweb="icon"] {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 18px !important;
        height: 18px !important;
        min-width: 18px !important;
        min-height: 18px !important;
        flex-shrink: 0 !important;
        pointer-events: none !important;
        background: transparent !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="icon"] svg,
    div[data-baseweb="select"] svg,
    div[data-testid="stSelectbox"] svg {
        width: 16px !important;
        height: 16px !important;
        min-width: 16px !important;
        min-height: 16px !important;
        display: block !important;
        fill: var(--app-text-muted) !important;
        stroke: var(--app-text-muted) !important;
        color: var(--app-text-muted) !important;
        opacity: 0.9 !important;
        visibility: visible !important;
        transition: transform 0.15s ease, fill 0.15s ease !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover svg,
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover svg {
        fill: var(--input-text) !important;
        stroke: var(--input-text) !important;
        color: var(--input-text) !important;
        opacity: 1 !important;
    }

    /* Dropdown Options Popup Menu */
    body > div[data-baseweb="popover"],
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    div[data-testid="stSelectboxVirtualDropdown"],
    ul[role="listbox"] {
        background-color: var(--app-card-bg) !important;
        background: var(--app-card-bg) !important;
        border: 1.5px solid var(--app-card-border) !important;
        border-radius: 10px !important;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35) !important;
        padding: 6px !important;
        z-index: 999999 !important;
    }

    li[role="option"],
    div[role="option"] {
        background-color: transparent !important;
        background: transparent !important;
        color: var(--input-text) !important;
        -webkit-text-fill-color: var(--input-text) !important;
        font-weight: 600 !important;
        font-size: 0.84rem !important;
        border-radius: 6px !important;
        padding: 8px 12px !important;
        margin: 2px 0 !important;
        cursor: pointer !important;
        transition: all 0.12s ease !important;
    }
    li[role="option"]:hover,
    li[role="option"][aria-selected="true"],
    div[role="option"]:hover,
    div[role="option"][aria-selected="true"] {
        background-color: var(--btn-secondary-bg) !important;
        background: var(--btn-secondary-bg) !important;
        color: var(--btn-secondary-hover-text) !important;
        -webkit-text-fill-color: var(--btn-secondary-hover-text) !important;
        font-weight: 700 !important;
    }

    div[data-testid="stInputInstructions"],
    div[data-testid="stInputInstructions"] > span {
        display: none !important;
    }

    /* =====================================================
       BUTTONS (PRIMARY PREDICT & SECONDARY CLEAR ALL)
       ===================================================== */
    div.stButton > button[kind="primary"],
    button[data-testid="baseButton-primary"],
    button[data-testid="stBaseButton-primary"] {
        background: var(--btn-primary-bg) !important;
        background-color: #2563eb !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        height: 44px !important;
        min-height: 44px !important;
        font-size: 0.94rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.01em !important;
        box-shadow: var(--btn-primary-shadow) !important;
        transition: all 0.18s ease-in-out !important;
        margin-top: 0.75rem !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stButton > button[kind="primary"]:hover,
    button[data-testid="baseButton-primary"]:hover {
        box-shadow: var(--btn-primary-hover-shadow) !important;
        transform: translateY(-1.5px) !important;
        filter: brightness(1.08) !important;
    }

    button[data-testid="baseButton-secondary"],
    button[data-testid="stBaseButton-secondary"],
    button[kind="secondary"],
    .clear-btn-wrap button,
    .clear-btn-wrap div.stButton > button,
    div[data-testid="stButton"] > button:not([kind="primary"]) {
        background: var(--btn-secondary-bg) !important;
        background-color: var(--btn-secondary-bg) !important;
        color: var(--btn-secondary-text) !important;
        -webkit-text-fill-color: var(--btn-secondary-text) !important;
        border: 1.5px solid var(--btn-secondary-border) !important;
        border-radius: 8px !important;
        height: 38px !important;
        min-height: 38px !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        padding: 0 1.15rem !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
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
        background: var(--btn-secondary-hover-bg) !important;
        border-color: var(--btn-secondary-hover-border) !important;
        color: var(--btn-secondary-hover-text) !important;
        -webkit-text-fill-color: var(--btn-secondary-hover-text) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.18) !important;
        transform: translateY(-1px) !important;
    }

    /* =====================================================
       RESULT PANEL & METRICS (SHARP, HIGH CONTRAST BOXES)
       ===================================================== */
    .result-header-box {
        background: var(--metric-card-bg);
        border: 1.5px solid var(--metric-card-border);
        border-radius: 10px;
        padding: 0.8rem 1.05rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
        margin-bottom: 0.75rem;
    }
    .result-title-text {
        font-size: 0.94rem;
        font-weight: 800;
        color: var(--app-text-title);
        display: flex;
        align-items: center;
        gap: 0.4rem;
        margin: 0;
    }

    .badge-status {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.28rem 0.75rem;
        border-radius: 20px;
        font-size: 0.74rem;
        font-weight: 800;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }
    .badge-status.approved {
        background: var(--badge-approved-bg);
        color: var(--badge-approved-text);
        border: 1.5px solid var(--badge-approved-border);
    }
    .badge-status.rejected {
        background: var(--badge-rejected-bg);
        color: var(--badge-rejected-text);
        border: 1.5px solid var(--badge-rejected-border);
    }
    .badge-status.ready {
        background: var(--badge-ready-bg);
        color: var(--badge-ready-text);
        border: 1.5px solid var(--badge-ready-border);
    }

    .prob-metric-card {
        background: var(--metric-card-bg);
        border: 1.5px solid var(--metric-card-border);
        border-radius: 12px;
        padding: 1.25rem 1rem;
        text-align: center;
        margin-bottom: 0.75rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }
    .prob-metric-number {
        font-size: 2.6rem;
        font-weight: 800;
        line-height: 1;
        letter-spacing: -0.03em;
    }
    .prob-metric-number.approved {
        color: #10b981;
    }
    .prob-metric-number.rejected {
        color: #ef4444;
    }
    .prob-metric-label {
        font-size: 0.74rem;
        font-weight: 700;
        color: var(--app-text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.5rem;
    }

    .prob-track {
        width: 100%;
        height: 9px;
        background: var(--app-bg);
        border-radius: 999px;
        overflow: hidden;
        margin-top: 0.75rem;
        border: 1px solid var(--metric-card-border);
    }
    .prob-fill {
        height: 100%;
        border-radius: 999px;
        transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .prob-fill.approved {
        background: linear-gradient(90deg, #34d399 0%, #059669 100%);
    }
    .prob-fill.rejected {
        background: linear-gradient(90deg, #f87171 0%, #dc2626 100%);
    }

    .mini-metrics-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }
    .mini-metric-box {
        background: var(--metric-card-bg);
        border: 1.5px solid var(--metric-card-border);
        border-radius: 10px;
        padding: 0.8rem 0.9rem;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
    }
    .mini-metric-tag {
        font-size: 0.68rem;
        font-weight: 800;
        color: var(--app-text-muted);
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .mini-metric-value {
        font-size: 1rem;
        font-weight: 800;
        margin-top: 0.25rem;
        color: var(--app-text-title);
    }

    .risk-pill {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 5px;
        font-size: 0.76rem;
        font-weight: 800;
    }
    .risk-low { 
        background: var(--badge-approved-bg); 
        color: var(--badge-approved-text); 
        border: 1px solid var(--badge-approved-border); 
    }
    .risk-moderate { 
        background: #fef3c7; 
        color: #b45309; 
        border: 1px solid #fcd34d; 
    }
    .risk-high { 
        background: var(--badge-rejected-bg); 
        color: var(--badge-rejected-text); 
        border: 1px solid var(--badge-rejected-border); 
    }

    @media (prefers-color-scheme: dark) {
        .risk-moderate {
            background: #382006;
            color: #fde047;
            border: 1px solid #78350f;
        }
    }
    [data-theme="dark"] .risk-moderate {
        background: #382006 !important;
        color: #fde047 !important;
        border: 1px solid #78350f !important;
    }

    .summary-note-card {
        background: var(--sub-box-bg);
        border: 1.5px solid var(--sub-box-border);
        border-radius: 10px;
        padding: 0.85rem 1rem;
        font-size: 0.76rem;
        color: var(--app-text-muted);
        line-height: 1.45;
        margin-bottom: 0.75rem;
    }
    .summary-note-card strong {
        color: var(--app-text-title);
    }

    .empty-state-card {
        background: var(--sub-box-bg);
        border: 1.5px dashed var(--app-card-border);
        border-radius: 10px;
        text-align: center;
        padding: 2rem 1.2rem;
        color: var(--app-text-muted);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.75rem;
    }
    .empty-icon {
        font-size: 2.5rem;
        margin-bottom: 0.65rem;
    }

    /* Expander styling */
    div[data-testid="stExpander"] {
        border: 1.5px solid var(--app-card-border) !important;
        border-radius: 10px !important;
        background: var(--app-card-bg) !important;
        margin-top: 0.75rem !important;
    }
    div[data-testid="stExpander"] summary {
        font-size: 0.78rem !important;
        font-weight: 700 !important;
        color: var(--app-text-title) !important;
        padding: 0.5rem 0.75rem !important;
    }

    /* Responsive Table */
    .table-responsive-box {
        overflow-x: auto;
        border-radius: 8px;
        border: 1.5px solid var(--table-border);
        margin-top: 0.4rem;
        -webkit-overflow-scrolling: touch;
    }
    .adaptive-custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.76rem;
        text-align: left;
    }
    .adaptive-custom-table th {
        background: var(--table-th-bg);
        color: var(--table-th-text);
        font-weight: 800;
        padding: 0.5rem 0.75rem;
        border-bottom: 1.5px solid var(--table-border);
        border-right: 1px solid var(--table-border);
    }
    .adaptive-custom-table td {
        background: var(--table-td-bg);
        color: var(--app-text-body);
        padding: 0.5rem 0.75rem;
        border-bottom: 1px solid var(--table-border);
        border-right: 1px solid var(--table-border);
        font-weight: 600;
    }
    .adaptive-custom-table tr:nth-child(even) td {
        background: var(--table-td-alt);
    }

    /* =====================================================
       MOBILE RESPONSIVENESS
       ===================================================== */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.4rem !important;
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
            padding-bottom: 1.75rem !important;
        }
        .top-header-row {
            flex-direction: column;
            align-items: stretch;
            gap: 0.55rem;
            margin-bottom: 0.55rem;
        }
        .app-brand-container {
            gap: 0.6rem;
        }
        .app-logo-badge {
            width: 38px;
            height: 38px;
            font-size: 1.2rem;
        }
        .app-brand-title {
            font-size: 1.3rem !important;
        }
        .app-brand-subtitle {
            font-size: 0.72rem !important;
        }
        .highlighted-notice-bar {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.4rem;
            padding: 0.6rem 0.85rem;
            font-size: 0.74rem;
            margin-bottom: 0.75rem;
        }
        .clear-btn-wrap {
            width: 100%;
        }
        .clear-btn-wrap button,
        .clear-btn-wrap div.stButton > button,
        button[data-testid="baseButton-secondary"],
        button[data-testid="stBaseButton-secondary"] {
            width: 100% !important;
            height: 40px !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            padding: 0.95rem 0.85rem !important;
            border-radius: 12px !important;
            margin-bottom: 0.75rem !important;
        }
        div.stButton > button[kind="primary"],
        button[data-testid="baseButton-primary"],
        button[data-testid="stBaseButton-primary"] {
            width: 100% !important;
            height: 46px !important;
            font-size: 0.95rem !important;
            margin-top: 0.55rem !important;
        }
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stTextInput"] div[data-baseweb="input"],
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
        div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
            min-height: 42px !important;
            height: 42px !important;
        }
        .field-label-text {
            font-size: 0.80rem !important;
            margin-bottom: 3px !important;
        }
        .field-range-below {
            font-size: 0.68rem !important;
            margin-top: -2px !important;
            margin-bottom: 0.4rem !important;
        }
        .section-headline {
            font-size: 0.84rem !important;
            margin-bottom: 0.75rem !important;
        }
        .prob-metric-card {
            padding: 1rem 0.85rem !important;
            margin-bottom: 0.65rem !important;
        }
        .prob-metric-number {
            font-size: 2.25rem !important;
        }
        .mini-metrics-row {
            gap: 0.55rem !important;
            margin-bottom: 0.65rem !important;
        }
        .mini-metric-box {
            padding: 0.65rem 0.75rem !important;
        }
        .mini-metric-value {
            font-size: 0.94rem !important;
        }
        .summary-note-card {
            padding: 0.75rem 0.85rem !important;
            font-size: 0.74rem !important;
            margin-bottom: 0.65rem !important;
        }
    }

    @media (max-width: 480px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        .app-brand-title {
            font-size: 1.2rem !important;
        }
        .app-brand-subtitle {
            font-size: 0.68rem !important;
        }
        .prob-metric-number {
            font-size: 2rem !important;
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
# HEADER & IMPORTANT NOTICE
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
# HELPER FUNCTIONS FOR FORM HEADERS & SAAS ALERTS
# =========================================================

def render_field_header(label_text, is_invalid=False, alert_msg=""):
    alert_html = f'<span class="saas-micro-alert">⚠️ {alert_msg}</span>' if (is_invalid and alert_msg) else ""
    st.markdown(
        f"""
        <div class="field-label-row">
            <span class="field-label-text">{label_text}</span>
            {alert_html}
        </div>
        """,
        unsafe_allow_html=True
    )

def render_range_footer(range_text, is_invalid=False, error_text=""):
    if is_invalid and error_text:
        st.markdown(
            f'<div class="field-range-below"><span class="range-badge-tag error-tag">⚠️ Invalid</span> <span class="range-error-text">{error_text}</span></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="field-range-below"><span class="range-badge-tag">Range</span> {range_text}</div>',
            unsafe_allow_html=True
        )

def render_options_footer(options_text):
    st.markdown(
        f'<div class="field-range-below"><span class="range-badge-tag">Options</span> {options_text}</div>',
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
            curr_val = st.session_state.get("applicant_income")
            is_inv = curr_val is not None and curr_val < 0
            render_field_header("Applicant Income (₹)", is_inv, "Must be ≥ 0")
            applicant_income = st.number_input(
                "Applicant Income (₹)",
                value=None,
                step=500.0,
                placeholder="Enter income",
                key="applicant_income",
                label_visibility="collapsed"
            )
            render_range_footer("≥ ₹0", is_inv, "Must be ≥ ₹0")

        with r1c2:
            curr_val = st.session_state.get("coapplicant_income")
            is_inv = curr_val is not None and curr_val < 0
            render_field_header("Coapplicant Income (₹)", is_inv, "Must be ≥ 0")
            coapplicant_income = st.number_input(
                "Coapplicant Income (₹)",
                value=None,
                step=500.0,
                placeholder="Enter income",
                key="coapplicant_income",
                label_visibility="collapsed"
            )
            render_range_footer("≥ ₹0 (0 if none)", is_inv, "Must be ≥ ₹0")

        with r1c3:
            curr_val = st.session_state.get("dti_ratio")
            is_inv = curr_val is not None and (curr_val < 0.0 or curr_val > 1.0)
            render_field_header("DTI Ratio (Debt-to-Income)", is_inv, "0.00–1.00 Only")
            dti_ratio = st.number_input(
                "DTI Ratio (Debt-to-Income)",
                value=None,
                step=0.01,
                format="%.2f",
                placeholder="Enter DTI ratio",
                key="dti_ratio",
                label_visibility="collapsed"
            )
            render_range_footer("0.00 – 1.00 &bull; E.g. 0.30", is_inv, "Allowed: 0.00 – 1.00")

        # Row 2: Age (In Years) | Credit Score | Savings
        r2c1, r2c2, r2c3 = st.columns(3)
        with r2c1:
            curr_val = st.session_state.get("age")
            is_inv = curr_val is not None and (curr_val < 21 or curr_val > 59)
            render_field_header("Age (In Years)", is_inv, "21–59 Yrs Only")
            age = st.number_input(
                "Age (In Years)",
                value=None,
                step=1,
                placeholder="Enter age",
                key="age",
                label_visibility="collapsed"
            )
            render_range_footer("21 – 59 Years", is_inv, "Allowed: 21 – 59 Years")

        with r2c2:
            curr_val = st.session_state.get("credit_score")
            is_inv = curr_val is not None and (curr_val < 550.0 or curr_val > 799.0)
            render_field_header("Credit Score", is_inv, "550–799 Only")
            credit_score = st.number_input(
                "Credit Score",
                value=None,
                step=1.0,
                placeholder="Enter credit score",
                key="credit_score",
                label_visibility="collapsed"
            )
            render_range_footer("550 – 799", is_inv, "Allowed: 550 – 799")

        with r2c3:
            curr_val = st.session_state.get("savings")
            is_inv = curr_val is not None and curr_val < 0
            render_field_header("Savings (₹)", is_inv, "Must be ≥ 0")
            savings = st.number_input(
                "Savings (₹)",
                value=None,
                step=500.0,
                placeholder="Enter savings",
                key="savings",
                label_visibility="collapsed"
            )
            render_range_footer("≥ ₹0", is_inv, "Must be ≥ ₹0")

        # Row 3: Dependents | Existing Loans | Collateral Value
        r3c1, r3c2, r3c3 = st.columns(3)
        with r3c1:
            curr_val = st.session_state.get("dependents")
            is_inv = curr_val is not None and (curr_val < 0 or curr_val > 3)
            render_field_header("Dependents", is_inv, "0–3 Only")
            dependents = st.number_input(
                "Dependents",
                value=None,
                step=1,
                placeholder="Enter dependents",
                key="dependents",
                label_visibility="collapsed"
            )
            render_range_footer("0 – 3 Dependents", is_inv, "Allowed: 0 – 3")

        with r3c2:
            curr_val = st.session_state.get("existing_loans")
            is_inv = curr_val is not None and (curr_val < 0 or curr_val > 4)
            render_field_header("Existing Loans", is_inv, "0–4 Only")
            existing_loans = st.number_input(
                "Existing Loans",
                value=None,
                step=1,
                placeholder="Enter number of loans",
                key="existing_loans",
                label_visibility="collapsed"
            )
            render_range_footer("0 – 4 Active Loans", is_inv, "Allowed: 0 – 4")

        with r3c3:
            curr_val = st.session_state.get("collateral_value")
            is_inv = curr_val is not None and curr_val < 0
            render_field_header("Collateral Value (₹)", is_inv, "Must be ≥ 0")
            collateral_value = st.number_input(
                "Collateral Value (₹)",
                value=None,
                step=500.0,
                placeholder="Enter collateral value",
                key="collateral_value",
                label_visibility="collapsed"
            )
            render_range_footer("≥ ₹0", is_inv, "Must be ≥ ₹0")

        # Row 4: Loan Amount | Loan Term | Gender
        r4c1, r4c2, r4c3 = st.columns(3)
        with r4c1:
            curr_val = st.session_state.get("loan_amount")
            is_inv = curr_val is not None and curr_val < 0
            render_field_header("Loan Amount (₹)", is_inv, "Must be ≥ 0")
            loan_amount = st.number_input(
                "Loan Amount (₹)",
                value=None,
                step=500.0,
                placeholder="Enter loan amount",
                key="loan_amount",
                label_visibility="collapsed"
            )
            render_range_footer("≥ ₹0", is_inv, "Must be ≥ ₹0")

        with r4c2:
            curr_val = st.session_state.get("loan_term")
            is_inv = curr_val is not None and (curr_val < 12 or curr_val > 84 or curr_val % 12 != 0)
            render_field_header("Loan Term (Months)", is_inv, "12–84 (Steps of 12)")
            loan_term = st.number_input(
                "Loan Term (Months)",
                value=None,
                step=12,
                placeholder="Enter loan term",
                key="loan_term",
                label_visibility="collapsed"
            )
            render_range_footer("12 – 84 Months (Steps of 12)", is_inv, "Allowed: 12, 24, 36... 84")

        with r4c3:
            render_field_header("Gender")
            gender = st.selectbox(
                "Gender",
                ["Female", "Male"],
                index=None,
                placeholder="Select gender",
                key="gender",
                label_visibility="collapsed"
            )
            render_options_footer("Female / Male")

        # Row 5: Marital Status | Employment Status | Education Level
        r5c1, r5c2, r5c3 = st.columns(3)
        with r5c1:
            render_field_header("Marital Status")
            marital_status = st.selectbox(
                "Marital Status",
                ["Married", "Single"],
                index=None,
                placeholder="Select marital status",
                key="marital_status",
                label_visibility="collapsed"
            )
            render_options_footer("Married / Single")

        with r5c2:
            render_field_header("Employment Status")
            employment_status = st.selectbox(
                "Employment Status",
                ["Contract", "Salaried", "Self-employed", "Unemployed"],
                index=None,
                placeholder="Select employment status",
                key="employment_status",
                label_visibility="collapsed"
            )
            render_options_footer("Contract / Salaried / Self-emp. / Unemp.")

        with r5c3:
            render_field_header("Education Level")
            education_level = st.selectbox(
                "Education Level",
                ["Graduate", "Not Graduate"],
                index=None,
                placeholder="Select education level",
                key="education_level",
                label_visibility="collapsed"
            )
            render_options_footer("Graduate / Not Graduate")

        # Section: Loan Information
        st.markdown(
            '<div class="section-headline loan-info">💼 Loan Information</div>',
            unsafe_allow_html=True
        )

        lr1, lr2, lr3 = st.columns(3)
        with lr1:
            render_field_header("Loan Purpose")
            loan_purpose = st.selectbox(
                "Loan Purpose",
                ["Business", "Car", "Education", "Home", "Personal"],
                index=None,
                placeholder="Select loan purpose",
                key="loan_purpose",
                label_visibility="collapsed"
            )
            render_options_footer("Business / Car / Education / Home / Personal")

        with lr2:
            render_field_header("Property Area")
            property_area = st.selectbox(
                "Property Area",
                ["Rural", "Semiurban", "Urban"],
                index=None,
                placeholder="Select property area",
                key="property_area",
                label_visibility="collapsed"
            )
            render_options_footer("Rural / Semiurban / Urban")

        with lr3:
            render_field_header("Employer Category")
            employer_category = st.selectbox(
                "Employer Category",
                ["Government", "MNC", "Private", "Unemployed"],
                index=None,
                placeholder="Select employer category",
                key="employer_category",
                label_visibility="collapsed"
            )
            render_options_footer("Government / MNC / Private / Unemployed")

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
            # Idle / Ready State
            st.markdown(
                """
                <div class="result-header-box">
                    <div class="result-title-text">📊 Prediction Result</div>
                    <span class="badge-status ready">● Ready</span>
                </div>
                <div class="empty-state-card">
                    <div class="empty-icon">🏛️</div>
                    <div style="font-weight: 800; color: var(--app-text-title); font-size: 0.98rem; margin-bottom: 0.35rem;">Ready for Prediction</div>
                    <div style="font-size: 0.78rem; color: var(--app-text-muted); line-height: 1.45;">Enter the applicant details on the left and click predict to calculate the ML loan assessment.</div>
                </div>
                <div class="mini-metrics-row">
                    <div class="mini-metric-box">
                        <div class="mini-metric-tag">Prediction</div>
                        <div class="mini-metric-value" style="color: var(--app-text-subtle);">—</div>
                    </div>
                    <div class="mini-metric-box">
                        <div class="mini-metric-tag">Risk Level</div>
                        <div class="mini-metric-value" style="color: var(--app-text-subtle);">—</div>
                    </div>
                </div>
                <div class="summary-note-card" style="text-align: center; color: var(--app-text-subtle); font-size: 0.74rem;">
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

            out_of_range = []
            if applicant_income is not None and applicant_income < 0:
                out_of_range.append("Applicant Income (≥ ₹0)")
            if coapplicant_income is not None and coapplicant_income < 0:
                out_of_range.append("Coapplicant Income (≥ ₹0)")
            if dti_ratio is not None and (dti_ratio < 0.0 or dti_ratio > 1.0):
                out_of_range.append("DTI Ratio (0.00 – 1.00)")
            if age is not None and (age < 21 or age > 59):
                out_of_range.append("Age (21 – 59 Years)")
            if credit_score is not None and (credit_score < 550.0 or credit_score > 799.0):
                out_of_range.append("Credit Score (550 – 799)")
            if savings is not None and savings < 0:
                out_of_range.append("Savings (≥ ₹0)")
            if dependents is not None and (dependents < 0 or dependents > 3):
                out_of_range.append("Dependents (0 – 3)")
            if existing_loans is not None and (existing_loans < 0 or existing_loans > 4):
                out_of_range.append("Existing Loans (0 – 4)")
            if collateral_value is not None and collateral_value < 0:
                out_of_range.append("Collateral Value (≥ ₹0)")
            if loan_amount is not None and loan_amount <= 0:
                out_of_range.append("Loan Amount (Must be > 0)")
            if loan_term is not None and (loan_term < 12 or loan_term > 84 or loan_term % 12 != 0):
                out_of_range.append("Loan Term (12 – 84 in steps of 12)")

            if missing or out_of_range:
                missing_pills = "".join([f'<span style="display:inline-block; background:var(--notice-bg); color:var(--notice-text); border:1.5px solid var(--notice-border); border-radius:4px; padding:2px 8px; font-size:0.72rem; font-weight:700; margin:2px 4px 2px 0;">{field}</span>' for field in missing])
                range_pills = "".join([f'<span style="display:inline-block; background:#fee2e2; color:#b91c1c; border:1.5px solid #fca5a5; border-radius:4px; padding:2px 8px; font-size:0.72rem; font-weight:700; margin:2px 4px 2px 0;">{field}</span>' for field in out_of_range])
                
                notice_items = ""
                if missing:
                    notice_items += f"""
                    <div style="color: var(--notice-text); font-size: 0.78rem; line-height: 1.45; font-weight: 600; margin-bottom: 0.35rem;">
                        Missing <strong>{len(missing)} required field(s)</strong>:
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:4px; margin-bottom: 0.55rem;">
                        {missing_pills}
                    </div>
                    """
                if out_of_range:
                    notice_items += f"""
                    <div style="color: #dc2626; font-size: 0.78rem; line-height: 1.45; font-weight: 700; margin-bottom: 0.35rem;">
                        Values out of allowed range (<strong>{len(out_of_range)}</strong>):
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:4px; margin-bottom: 0.35rem;">
                        {range_pills}
                    </div>
                    """

                st.markdown(
                    f"""
                    <div class="result-header-box">
                        <div class="result-title-text">📊 Prediction Result</div>
                        <span class="badge-status rejected">⚠️ Attention Needed</span>
                    </div>
                    <div style="background: var(--notice-bg); border: 1.5px solid var(--notice-border); border-left: 5px solid var(--notice-accent); border-radius: 10px; padding: 0.9rem 1.05rem; margin-bottom: 0.75rem; box-shadow: 0 2px 6px rgba(245, 158, 11, 0.08);">
                        <div style="color: var(--notice-strong); font-weight: 800; font-size: 0.9rem; display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.4rem;">
                            <span>⚠️</span> Form Validation Check
                        </div>
                        {notice_items}
                    </div>
                    <div class="mini-metrics-row">
                        <div class="mini-metric-box">
                            <div class="mini-metric-tag">Status</div>
                            <div class="mini-metric-value" style="color: #d97706; font-size: 0.92rem;">INCOMPLETE</div>
                        </div>
                        <div class="mini-metric-box">
                            <div class="mini-metric-tag">Total Issues</div>
                            <div class="mini-metric-value" style="color: #ef4444; font-size: 0.92rem;">{len(missing) + len(out_of_range)} Issues</div>
                        </div>
                    </div>
                    <div class="summary-note-card" style="text-align: center; font-weight: 600;">
                        Correct the highlighted fields on the left and click Predict again.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Run ML Pipeline
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
                                <div class="mini-metric-value" style="color: #10b981;">APPROVED</div>
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
                                <div class="mini-metric-value" style="color: #ef4444;">NOT APPROVED</div>
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

                # Collapsed Expander for Submitted Information
                with st.expander("👁 View Submitted Information", expanded=False):
                    st.markdown(
                        f"""
                        <div class="table-responsive-box">
                            <table class="adaptive-custom-table">
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
