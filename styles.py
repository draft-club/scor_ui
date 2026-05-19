"""CSS styles for the World Holidays Explorer app - SCOR-inspired deep teal palette."""

PALETTE = {
    "bg_dark": "#0a1628",
    "bg_card": "#0f2035",
    "bg_card_hover": "#132a42",
    "teal": "#00838f",
    "teal_light": "#26c6da",
    "teal_glow": "rgba(0, 131, 143, 0.3)",
    "accent": "#00e5ff",
    "green": "#00c853",
    "white": "#e0f7fa",
    "text": "#b0bec5",
    "text_dim": "#607d8b",
    "border": "rgba(0, 131, 143, 0.2)",
    "gradient_start": "#00838f",
    "gradient_end": "#006064",
    "holiday_bg": "rgba(0, 200, 83, 0.15)",
    "today_bg": "rgba(0, 229, 255, 0.15)",
}

def get_css():
    P = PALETTE
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* === GLOBAL === */
.stApp {{
    background: linear-gradient(135deg, {P['bg_dark']} 0%, #0d1f33 50%, {P['bg_dark']} 100%);
    color: {P['white']};
    font-family: 'Inter', sans-serif;
}}
.stApp > header {{ background: transparent !important; }}
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {P['bg_card']} 0%, {P['bg_dark']} 100%) !important;
    border-right: 1px solid {P['border']} !important;
}}
[data-testid="stSidebar"] * {{ color: {P['white']} !important; }}
[data-testid="stSidebar"] .stSelectbox > div > div,
[data-testid="stSidebar"] .stMultiSelect > div > div {{
    background: {P['bg_dark']} !important;
    border: 1px solid {P['border']} !important;
    color: {P['white']} !important;
}}

/* === HERO HEADER === */
.hero-header {{
    background: linear-gradient(135deg, {P['gradient_start']}, {P['gradient_end']});
    border-radius: 16px;
    padding: 30px 40px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 32px {P['teal_glow']};
    border: 1px solid {P['border']};
}}
.hero-header::before {{
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(0,229,255,0.1) 0%, transparent 70%);
    border-radius: 50%;
}}
.hero-title {{
    font-size: 2.2rem;
    font-weight: 800;
    color: #fff;
    margin: 0;
    letter-spacing: -0.5px;
}}
.hero-sub {{
    font-size: 1rem;
    color: rgba(255,255,255,0.7);
    margin-top: 6px;
    font-weight: 300;
}}

/* === STAT CARDS === */
.stat-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 24px;
}}
.stat-card {{
    background: {P['bg_card']};
    border: 1px solid {P['border']};
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}}
.stat-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px {P['teal_glow']};
    border-color: {P['teal']};
}}
.stat-card::after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, {P['teal']}, {P['accent']});
    opacity: 0;
    transition: opacity 0.3s ease;
}}
.stat-card:hover::after {{ opacity: 1; }}
.stat-icon {{ font-size: 1.8rem; margin-bottom: 6px; }}
.stat-value {{
    font-size: 1.8rem;
    font-weight: 800;
    color: {P['accent']};
    font-family: 'JetBrains Mono', monospace;
}}
.stat-label {{
    font-size: 0.8rem;
    color: {P['text']};
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}}

/* === GLASS PANELS === */
.glass-panel {{
    background: {P['bg_card']};
    border: 1px solid {P['border']};
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}}
.glass-panel h3 {{
    color: {P['white']};
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.glass-panel h3 .icon {{ font-size: 1.3rem; }}

/* === CALENDAR === */
table.hcal {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 4px;
    font-family: 'Inter', sans-serif;
}}
table.hcal th {{
    background: linear-gradient(135deg, {P['teal']}, {P['gradient_end']});
    color: #fff;
    padding: 10px 6px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 8px;
}}
table.hcal td {{
    background: {P['bg_dark']};
    border: 1px solid {P['border']};
    padding: 8px 4px;
    text-align: center;
    border-radius: 8px;
    vertical-align: top;
    min-height: 50px;
    transition: all 0.2s ease;
    color: {P['text']};
    font-size: 0.85rem;
}}
table.hcal td:hover {{
    border-color: {P['teal']};
    background: {P['bg_card_hover']};
}}
table.hcal td.empty {{ background: transparent; border-color: transparent; }}
table.hcal td.holiday {{
    background: {P['holiday_bg']};
    border-color: {P['green']};
    color: {P['green']};
    font-weight: 700;
}}
table.hcal td.today {{
    background: {P['today_bg']};
    border-color: {P['accent']};
    box-shadow: 0 0 12px rgba(0,229,255,0.2);
}}
.h-name {{
    font-size: 0.6rem;
    color: {P['green']};
    display: block;
    margin-top: 2px;
    line-height: 1.2;
    max-width: 80px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}}

/* === HOLIDAY LIST === */
.h-list-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 16px;
    border-left: 3px solid {P['teal']};
    background: {P['bg_dark']};
    border-radius: 0 10px 10px 0;
    margin-bottom: 8px;
    transition: all 0.2s ease;
}}
.h-list-item:hover {{
    background: {P['bg_card_hover']};
    border-left-color: {P['accent']};
    transform: translateX(4px);
}}
.h-date {{
    background: linear-gradient(135deg, {P['teal']}, {P['gradient_end']});
    color: #fff;
    padding: 6px 10px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
    min-width: 70px;
    text-align: center;
}}
.h-info {{ flex: 1; }}
.h-info .name {{
    color: {P['white']};
    font-weight: 600;
    font-size: 0.9rem;
}}
.h-info .country {{
    color: {P['text_dim']};
    font-size: 0.75rem;
    margin-top: 2px;
}}

/* === BADGES === */
.country-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: {P['bg_dark']};
    border: 1px solid {P['border']};
    border-radius: 20px;
    padding: 5px 12px;
    margin: 3px;
    font-size: 0.8rem;
    color: {P['white']};
    transition: all 0.2s ease;
}}
.country-badge:hover {{
    border-color: {P['teal']};
    box-shadow: 0 0 12px {P['teal_glow']};
}}
.count-badge {{
    background: {P['teal']};
    color: #fff;
    border-radius: 10px;
    padding: 1px 7px;
    font-size: 0.7rem;
    font-weight: 700;
}}

/* === SCROLLBAR === */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: {P['bg_dark']}; }}
::-webkit-scrollbar-thumb {{
    background: {P['teal']};
    border-radius: 3px;
}}

/* === STREAMLIT OVERRIDES === */
.stTabs [data-baseweb="tab-list"] {{
    gap: 4px;
    background: {P['bg_dark']};
    border-radius: 12px;
    padding: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    background: transparent;
    color: {P['text']};
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: 500;
}}
.stTabs [aria-selected="true"] {{
    background: {P['teal']} !important;
    color: #fff !important;
}}
div[data-testid="stExpander"] {{
    background: {P['bg_card']};
    border: 1px solid {P['border']};
    border-radius: 12px;
}}
.stDownloadButton > button {{
    background: linear-gradient(135deg, {P['teal']}, {P['gradient_end']}) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 8px 20px !important;
    transition: all 0.3s ease !important;
}}
.stDownloadButton > button:hover {{
    box-shadow: 0 4px 16px {P['teal_glow']} !important;
    transform: translateY(-1px) !important;
}}

/* === RESPONSIVE === */
@media (max-width: 768px) {{
    .stat-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .hero-title {{ font-size: 1.5rem; }}
}}
</style>
"""
