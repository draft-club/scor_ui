"""Clean minimal white CSS with toggle chips and layout support."""

def get_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
.stApp { background: #ffffff; color: #1a1a2e; font-family: 'Inter', sans-serif; }
.stApp > header { background: #fff !important; }
[data-testid="stSidebar"] { background: #fafafa !important; border-right: 1px solid #e5e7eb !important; }
.page-title { font-size: 1.3rem; font-weight: 600; color: #1a1a2e; margin: 0 0 2px 0; }
.page-sub { font-size: 0.82rem; color: #6b7280; margin-bottom: 14px; }

/* Calendar table */
table.hcal { width: 100%; border-collapse: separate; border-spacing: 2px; font-family: 'Inter', sans-serif; }
table.hcal th { background: #f9fafb; color: #6b7280; padding: 7px 4px; font-size: 0.7rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; border-radius: 4px; }
table.hcal td { background: #fff; border: 1px solid #e5e7eb; padding: 5px 3px; text-align: center; border-radius: 5px; vertical-align: top; color: #1a1a2e; font-size: 0.8rem; }
table.hcal td:hover { background: #f9fafb; }
table.hcal td.empty { background: transparent; border-color: transparent; }
table.hcal td.holiday { background: #d1fae5; border-color: #059669; color: #059669; font-weight: 600; }
table.hcal td.today { background: #dbeafe; border-color: #2563eb; }
.h-name { font-size: 0.52rem; color: #059669; display: block; margin-top: 1px; line-height: 1.1; max-width: 70px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

/* Holiday list rows */
.h-row { display: flex; align-items: center; gap: 12px; padding: 9px 12px; border-bottom: 1px solid #f3f4f6; }
.h-row:hover { background: #f9fafb; }
.h-date-chip { background: #f3f4f6; color: #1a1a2e; padding: 3px 10px; border-radius: 5px; font-size: 0.76rem; font-weight: 500; min-width: 64px; text-align: center; }
.h-name-text { color: #1a1a2e; font-size: 0.85rem; font-weight: 500; }
.h-country-text { color: #6b7280; font-size: 0.72rem; }
.section-label { font-size: 0.92rem; font-weight: 600; color: #1a1a2e; margin: 18px 0 8px 0; padding-bottom: 5px; border-bottom: 1px solid #e5e7eb; }

/* Toggle chip grid */
.toggle-grid { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 14px 0; }
.toggle-chip { display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 500; background: #f3f4f6; color: #6b7280; border: 1px solid #e5e7eb; transition: all 0.2s ease; }
.toggle-chip.active { background: #d1fae5; color: #059669; border-color: #059669; }
.chip-count { background: rgba(0,0,0,0.06); padding: 1px 7px; border-radius: 10px; font-size: 0.7rem; font-weight: 600; }
.toggle-chip.active .chip-count { background: rgba(5,150,105,0.15); color: #059669; }

/* Stat cards row */
.stats-row { display: flex; gap: 10px; margin-top: 10px; }
.stat-card { flex: 1; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px 10px; text-align: center; }
.stat-number { font-size: 1.3rem; font-weight: 600; color: #1a1a2e; }
.stat-label { font-size: 0.68rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

/* Map section */
.map-section { margin: 8px 0 0 0; }

/* Expander styling */
div[data-testid="stExpander"] { border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 8px; }
div[data-testid="stExpander"] summary { font-size: 0.88rem; font-weight: 500; }

/* Download button */
.stDownloadButton > button { background: #fff !important; color: #1a1a2e !important; border: 1px solid #e5e7eb !important; border-radius: 6px !important; font-size: 0.8rem !important; }
.stDownloadButton > button:hover { background: #f9fafb !important; }

/* Holiday detail cards */
.holiday-detail-desc { font-size: 0.88rem; color: #374151; line-height: 1.6; padding: 10px 14px; background: #f9fafb; border-left: 3px solid #059669; border-radius: 0 6px 6px 0; margin-bottom: 10px; }
.fun-facts-title { font-size: 0.82rem; font-weight: 600; color: #d97706; margin: 8px 0 4px 0; }
.fun-fact-item { font-size: 0.82rem; color: #4b5563; padding: 3px 0 3px 8px; line-height: 1.5; }
</style>
"""
