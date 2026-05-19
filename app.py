"""World Holidays Explorer — A futuristic global holiday discovery tool."""
import streamlit as st
from datetime import date
import calendar
import holidays
import folium
from streamlit_folium import folium_static
import pandas as pd
import json

from styles import get_css, PALETTE
from data import (
    COUNTRIES, COORDS, get_flag,
    get_holidays_for_month, get_holidays_for_year,
    build_calendar_html,
)

# ── Page Config ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Vancanza — World Holidays Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(get_css(), unsafe_allow_html=True)

# ── Sidebar Controls ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌍 Vancanza")
    st.markdown("*Global Holiday Intelligence*")
    st.markdown("---")

    selected_countries = st.multiselect(
        "🔍 Select Countries",
        list(COUNTRIES.keys()),
        default=["Morocco", "United States", "France", "Japan"],
        help="Pick one or more countries to explore their holidays",
    )

    col_y, col_m = st.columns(2)
    with col_y:
        year = st.selectbox(
            "📅 Year",
            list(range(2020, date.today().year + 3)),
            index=date.today().year - 2020,
        )
    with col_m:
        month = st.selectbox(
            "📆 Month",
            list(range(1, 13)),
            index=date.today().month - 1,
            format_func=lambda m: calendar.month_abbr[m],
        )

    st.markdown("---")
    view_mode = st.radio("📊 View Mode", ["Monthly", "Yearly Overview"], horizontal=True)
    show_comparison = st.checkbox("📈 Country Comparison", value=False)

    st.markdown("---")
    st.markdown("##### 🎨 Quick Presets")
    preset = st.selectbox("Load a preset", [
        "Custom", "G7 Nations", "BRICS", "Europe Top 5",
        "Middle East", "Southeast Asia", "Africa",
    ])
    PRESETS = {
        "G7 Nations": ["United States", "United Kingdom", "France", "Germany", "Japan", "Italy", "Canada"],
        "BRICS": ["Brazil", "Russia", "India", "China", "South Africa"],
        "Europe Top 5": ["France", "Germany", "Spain", "Italy", "United Kingdom"],
        "Middle East": ["Saudi Arabia", "United Arab Emirates", "Qatar", "Kuwait", "Bahrain", "Oman"],
        "Southeast Asia": ["Thailand", "Vietnam", "Indonesia", "Philippines", "Singapore", "Malaysia"],
        "Africa": ["Morocco", "South Africa", "Kenya", "Nigeria", "Egypt", "Ethiopia"],
    }
    if preset != "Custom" and preset in PRESETS:
        valid = [c for c in PRESETS[preset] if c in COUNTRIES]
        if valid:
            selected_countries = valid

    st.markdown("---")
    st.caption(f"📦 {len(COUNTRIES)} countries supported")
    st.caption(f"🔌 Powered by `holidays` library")

# ── Hero Header ──────────────────────────────────────────────────────
month_name = calendar.month_name[month]
st.markdown(f"""
<div class="hero-header">
    <div class="hero-title">🌍 Vancanza — World Holidays Explorer</div>
    <div class="hero-sub">Discover public holidays across {len(COUNTRIES)}+ countries • {month_name} {year}</div>
</div>
""", unsafe_allow_html=True)

# ── Compute Holiday Data ─────────────────────────────────────────────
all_holidays_data = {}
total_holidays = 0
for country in selected_countries:
    code = COUNTRIES.get(country)
    if not code:
        continue
    h_list = get_holidays_for_month(code, year, month)
    all_holidays_data[country] = {"code": code, "holidays": h_list, "count": len(h_list)}
    total_holidays += len(h_list)

# ── Stats Cards ──────────────────────────────────────────────────────
next_holiday = None
today = date.today()
for country, info in all_holidays_data.items():
    for d, name in info["holidays"]:
        if d >= today and (next_holiday is None or d < next_holiday[0]):
            next_holiday = (d, name, country)

next_str = f"{next_holiday[0].strftime('%b %d')} — {next_holiday[2]}" if next_holiday else "None this month"

st.markdown(f"""
<div class="stat-grid">
    <div class="stat-card">
        <div class="stat-icon">🌐</div>
        <div class="stat-value">{len(selected_countries)}</div>
        <div class="stat-label">Countries Selected</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🎉</div>
        <div class="stat-value">{total_holidays}</div>
        <div class="stat-label">Holidays Found</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">📅</div>
        <div class="stat-value">{month_name[:3]} {year}</div>
        <div class="stat-label">Current Period</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">⏭️</div>
        <div class="stat-value" style="font-size:1rem">{next_str}</div>
        <div class="stat-label">Next Holiday</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Main Content: Map + Calendar ─────────────────────────────────────
col_map, col_cal = st.columns([3, 2])

with col_map:
    st.markdown('<div class="glass-panel"><h3><span class="icon">🗺️</span> Interactive World Map</h3>', unsafe_allow_html=True)

    if not selected_countries:
        st.info("Select countries from the sidebar to see them on the map.")
    else:
        m = folium.Map(
            location=[20, 10],
            zoom_start=2,
            tiles="CartoDB dark_matter",
            attr="Vancanza",
        )

        for country, info in all_holidays_data.items():
            code = info["code"]
            coords = COORDS.get(code)
            if not coords:
                continue
            count = info["count"]
            h_list = info["holidays"]
            radius = 7 + count * 3
            flag = get_flag(code)

            # Build popup HTML
            popup_html = f"""
            <div style="font-family:Inter,sans-serif;min-width:200px;background:#0f2035;
                        color:#e0f7fa;padding:14px;border-radius:10px;border:1px solid rgba(0,131,143,0.3)">
                <div style="font-size:16px;font-weight:700;margin-bottom:8px;
                            color:#00e5ff">{flag} {country}</div>
                <div style="font-size:12px;color:#b0bec5;margin-bottom:6px">
                    {month_name} {year} • {count} holiday{'s' if count != 1 else ''}
                </div>
            """
            if h_list:
                for d, name in h_list[:8]:
                    popup_html += f"""
                    <div style="display:flex;gap:8px;align-items:center;margin:4px 0;
                                padding:4px 8px;background:rgba(0,200,83,0.1);border-radius:6px;
                                border-left:2px solid #00c853">
                        <span style="font-size:11px;color:#00c853;font-weight:600;
                                     white-space:nowrap">{d.strftime('%b %d')}</span>
                        <span style="font-size:11px;color:#e0f7fa">{name}</span>
                    </div>"""
                if count > 8:
                    popup_html += f'<div style="font-size:11px;color:#607d8b;margin-top:4px">...and {count-8} more</div>'
            else:
                popup_html += '<div style="font-size:12px;color:#607d8b">No holidays this month</div>'
            popup_html += "</div>"

            # Color based on holiday count
            if count == 0:
                fill_color = "#455a64"
            elif count <= 2:
                fill_color = "#00838f"
            elif count <= 5:
                fill_color = "#00c853"
            else:
                fill_color = "#00e5ff"

            folium.CircleMarker(
                location=coords,
                radius=radius,
                color=PALETTE["accent"],
                weight=2,
                fill=True,
                fill_color=fill_color,
                fill_opacity=0.75,
                popup=folium.Popup(popup_html, max_width=320),
                tooltip=f"{flag} {country}: {count} holidays",
            ).add_to(m)

            # Add a subtle pulsing ring for countries with many holidays
            if count >= 3:
                folium.CircleMarker(
                    location=coords,
                    radius=radius + 8,
                    color=fill_color,
                    weight=1,
                    fill=False,
                    opacity=0.3,
                ).add_to(m)

        folium_static(m, width=700, height=480)
    st.markdown('</div>', unsafe_allow_html=True)

with col_cal:
    st.markdown('<div class="glass-panel"><h3><span class="icon">📅</span> Holiday Calendar</h3>', unsafe_allow_html=True)

    if not selected_countries:
        st.write("No country selected.")
    else:
        # Aggregate holidays for calendar
        aggregated = {}
        for country, info in all_holidays_data.items():
            for d, name in info["holidays"]:
                aggregated.setdefault(d.day, []).append(f"{country}: {name}")

        cal_html = build_calendar_html(year, month, aggregated, today)
        st.markdown(cal_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Country badges
    st.markdown('<div class="glass-panel"><h3><span class="icon">🏷️</span> Selected Countries</h3>', unsafe_allow_html=True)
    badges_html = ""
    for country, info in all_holidays_data.items():
        flag = get_flag(info["code"])
        badges_html += f'<span class="country-badge">{flag} {country} <span class="count-badge">{info["count"]}</span></span>'
    st.markdown(badges_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Tabs: Details, Comparison, Export ────────────────────────────────
st.markdown("---")
tabs = st.tabs(["📋 Holiday Details", "📊 Comparison", "📥 Export Data"])

with tabs[0]:
    if not selected_countries:
        st.info("Select countries to see holiday details.")
    else:
        for country, info in all_holidays_data.items():
            flag = get_flag(info["code"])
            with st.expander(f"{flag} {country} — {info['count']} holidays in {month_name} {year}", expanded=len(selected_countries) <= 3):
                if info["holidays"]:
                    html_items = ""
                    for d, name in info["holidays"]:
                        day_name = d.strftime("%A")
                        html_items += f"""
                        <div class="h-list-item">
                            <div class="h-date">{d.strftime('%b %d')}<br><span style="font-size:0.65rem;opacity:0.7">{day_name}</span></div>
                            <div class="h-info">
                                <div class="name">{name}</div>
                                <div class="country">{flag} {country}</div>
                            </div>
                        </div>"""
                    st.markdown(html_items, unsafe_allow_html=True)
                else:
                    st.markdown(f"*No public holidays in {month_name} {year}*")

with tabs[1]:
    if show_comparison and len(selected_countries) >= 2:
        st.markdown("#### 📊 Holiday Count Comparison")

        if view_mode == "Monthly":
            comp_data = {country: info["count"] for country, info in all_holidays_data.items()}
            df = pd.DataFrame({"Country": list(comp_data.keys()), "Holidays": list(comp_data.values())})
            df = df.sort_values("Holidays", ascending=True)
            st.bar_chart(df.set_index("Country"))
        else:
            # Yearly overview
            yearly = {}
            for country in selected_countries:
                code = COUNTRIES.get(country)
                if code:
                    y_holidays = get_holidays_for_year(code, year)
                    monthly_counts = [0] * 12
                    for d, name in y_holidays:
                        monthly_counts[d.month - 1] += 1
                    yearly[country] = monthly_counts

            if yearly:
                months = [calendar.month_abbr[i] for i in range(1, 13)]
                df_yearly = pd.DataFrame(yearly, index=months)
                st.line_chart(df_yearly)

                # Summary table
                summary = []
                for country, counts in yearly.items():
                    summary.append({
                        "Country": f"{get_flag(COUNTRIES[country])} {country}",
                        "Total Holidays": sum(counts),
                        "Busiest Month": calendar.month_name[counts.index(max(counts)) + 1],
                        "Max in Month": max(counts),
                    })
                st.dataframe(pd.DataFrame(summary), use_container_width=True, hide_index=True)
    elif not show_comparison:
        st.info("Enable **Country Comparison** in the sidebar to see charts.")
    else:
        st.info("Select at least 2 countries for comparison.")

with tabs[2]:
    if selected_countries:
        # Build export data
        export_rows = []
        for country, info in all_holidays_data.items():
            for d, name in info["holidays"]:
                export_rows.append({
                    "Country": country,
                    "ISO Code": info["code"],
                    "Date": d.isoformat(),
                    "Day": d.strftime("%A"),
                    "Holiday Name": name,
                })

        if export_rows:
            df_export = pd.DataFrame(export_rows)
            st.dataframe(df_export, use_container_width=True, hide_index=True)

            csv = df_export.to_csv(index=False)
            st.download_button(
                "📥 Download as CSV",
                csv,
                f"holidays_{month_name}_{year}.csv",
                "text/csv",
            )

            json_str = df_export.to_json(orient="records", indent=2)
            st.download_button(
                "📥 Download as JSON",
                json_str,
                f"holidays_{month_name}_{year}.json",
                "application/json",
            )
        else:
            st.info("No holidays found for the selected criteria.")
    else:
        st.info("Select countries to export holiday data.")

# ── Footer ───────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(f"""
<div style="text-align:center;padding:20px;color:{PALETTE['text_dim']};font-size:0.8rem">
    🌍 <b style="color:{PALETTE['teal_light']}">Vancanza</b> — World Holidays Explorer •
    Powered by <code>holidays</code> library •
    {len(COUNTRIES)} countries • {year}
</div>
""", unsafe_allow_html=True)
