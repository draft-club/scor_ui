"""HoliGlobe - World Holidays Explorer. Clean minimal UI."""
import streamlit as st
from datetime import date
import calendar
import holidays
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import urllib.parse

from styles import get_css
from data import (
    COUNTRIES, COORDS, get_flag,
    get_holidays_for_month, get_holidays_for_year,
    build_calendar_html,
)
from holiday_info import get_holiday_info

st.set_page_config(page_title="HoliGlobe", page_icon="🌍", layout="wide")
st.markdown(get_css(), unsafe_allow_html=True)

# ── Sidebar: ALL controls + toggles ─────────────────────────────────
with st.sidebar:
    st.markdown("**Explorer Controls**")
    st.caption("World Holidays Explorer")
    st.markdown("---")

    preset = st.selectbox("Quick presets", ["Custom", "G7", "BRICS", "Europe", "Middle East", "Southeast Asia", "Africa"])
    PRESETS = {
        "G7": ["United States", "United Kingdom", "France", "Germany", "Japan", "Italy", "Canada"],
        "BRICS": ["Brazil", "Russia", "India", "China", "South Africa"],
        "Europe": ["France", "Germany", "Spain", "Italy", "United Kingdom"],
        "Middle East": ["Saudi Arabia", "United Arab Emirates", "Qatar", "Kuwait", "Bahrain", "Oman"],
        "Southeast Asia": ["Thailand", "Vietnam", "Indonesia", "Philippines", "Singapore", "Malaysia"],
        "Africa": ["Morocco", "South Africa", "Kenya", "Nigeria", "Egypt", "Ethiopia"],
    }

    if preset == "Custom":
        selected_countries = st.multiselect(
            "Countries",
            list(COUNTRIES.keys()),
            default=["Morocco", "United States", "France", "Japan"],
        )
    else:
        selected_countries = [c for c in PRESETS.get(preset, []) if c in COUNTRIES]

    col_y, col_m = st.columns(2)
    with col_y:
        year = st.selectbox("Year", list(range(2020, date.today().year + 3)), index=date.today().year - 2020)
    with col_m:
        month = st.selectbox("Month", list(range(1, 13)), index=date.today().month - 1, format_func=lambda m: calendar.month_abbr[m])

    # ── Quick toggles (in sidebar, under controls) ───────────────────
    st.markdown("---")
    st.markdown('<div class="section-label" style="border:none;margin-top:4px;">Selected</div>', unsafe_allow_html=True)

# ── Compute holidays ────────────────────────────────────────────────
month_name = calendar.month_name[month]
today = date.today()
all_data = {}
total = 0
for country in selected_countries:
    code = COUNTRIES.get(country)
    if not code:
        continue
    h = get_holidays_for_month(code, year, month)
    all_data[country] = {"code": code, "holidays": h, "count": len(h)}
    total += len(h)

# Render toggle chips inside the sidebar (needs all_data computed first)
with st.sidebar:
    if selected_countries:
        toggle_html = '<div class="toggle-grid">'
        for country in selected_countries:
            info = all_data.get(country, {})
            count = info.get("count", 0)
            code = info.get("code", "")
            flag = get_flag(code) if code else ""
            badge_class = "toggle-chip active" if count > 0 else "toggle-chip"
            toggle_html += f'<div class="{badge_class}">{flag} {country}<span class="chip-count">{count}</span></div>'
        toggle_html += '</div>'
        st.markdown(toggle_html, unsafe_allow_html=True)
    else:
        st.caption("No countries selected")

    # Quick stats
    st.markdown(f'''
        <div class="stats-row">
            <div class="stat-card">
                <div class="stat-number">{len(selected_countries)}</div>
                <div class="stat-label">Countries</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{total}</div>
                <div class="stat-label">Holidays</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{month_name[:3]}</div>
                <div class="stat-label">{year}</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# ── Title ────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">🌍 HoliGlobe</div>', unsafe_allow_html=True)
st.markdown(f'<div class="page-sub">{len(selected_countries)} countries selected &middot; {month_name} {year} &middot; {total} holidays found</div>', unsafe_allow_html=True)

# ── TOP ROW: Map (center) + Calendar (RHS) — same level ─────────────
col_map, col_calendar = st.columns([3, 2])

with col_map:
    if not selected_countries:
        st.info("Select countries from the sidebar.")
    else:
        m = folium.Map(location=[20, 10], zoom_start=2, tiles="CartoDB positron")

        for country, info in all_data.items():
            code = info["code"]
            coords = COORDS.get(code)
            if not coords:
                continue
            count = info["count"]
            h_list = info["holidays"]
            radius = 6 + count * 2

            popup_lines = [f"<b>{country}</b> — {month_name} {year}<br>{count} holiday{'s' if count != 1 else ''}<br>"]
            for d, name in h_list[:10]:
                popup_lines.append(f"<span style='font-size:12px'>{d.strftime('%b %d')}: {name}</span><br>")
            if count > 10:
                popup_lines.append(f"<i>...and {count - 10} more</i>")
            popup_html = "".join(popup_lines)

            fill = "#059669" if count else "#9ca3af"
            folium.CircleMarker(
                location=coords, radius=radius,
                color="#2563eb", weight=1, fill=True,
                fill_color=fill, fill_opacity=0.7,
                popup=folium.Popup(popup_html, max_width=280),
                tooltip=f"{country}: {count} holidays",
            ).add_to(m)

        folium_static(m, width=None, height=440)

with col_calendar:
    st.markdown(f'<div class="section-label">Calendar — {month_name} {year}</div>', unsafe_allow_html=True)
    aggregated = {}
    for country, info in all_data.items():
        for d, name in info["holidays"]:
            aggregated.setdefault(d.day, []).append(f"{country}: {name}")
    cal_html = build_calendar_html(year, month, aggregated, today)
    st.markdown(cal_html, unsafe_allow_html=True)

# ── BELOW: Collapsible details ──────────────────────────────────────
st.markdown("---")

# Holiday list with clickable details
with st.expander("📋 Holiday List — Descriptions & Fun Facts", expanded=False):
    all_items = []
    for country, info in all_data.items():
        for d, name in info["holidays"]:
            all_items.append((d, name, country))
    all_items.sort()

    if all_items:
        for i, (d, name, country) in enumerate(all_items):
            desc, facts = get_holiday_info(name, country)
            # Pick up to 2 random fun facts to keep it fresh
            shown_facts = random.sample(facts, min(2, len(facts)))

            with st.expander(f"📅 {d.strftime('%b %d')} — **{name}** ({country})"):
                WIKI_COUNTRIES = {"Japan", "China", "Spain", "Germany", "United Kingdom", "United States", "France", "Morocco", "Romania", "India", "Ireland", "Canada"}
                if country in WIKI_COUNTRIES:
                    query = urllib.parse.quote(f"{name} {country} holiday")
                    wiki_url = f"https://en.wikipedia.org/wiki/Special:Search?search={query}"
                    st.markdown(f'##### <a href="{wiki_url}" target="_blank" style="color: #2563eb; text-decoration: none;">{name} ↗</a>', unsafe_allow_html=True)
                
                st.markdown(f'<div class="holiday-detail-desc">{desc}</div>', unsafe_allow_html=True)
                if shown_facts:
                    st.markdown('<div class="fun-facts-title">💡 Fun Facts</div>', unsafe_allow_html=True)
                    for fact in shown_facts:
                        st.markdown(f'<div class="fun-fact-item">• {fact}</div>', unsafe_allow_html=True)
                st.caption(f"📍 {country} · {d.strftime('%A, %B %d, %Y')}")
    else:
        st.write("No holidays found for this period.")

# Country details with holiday descriptions
with st.expander("🌍 Country Details", expanded=False):
    for country, info in all_data.items():
        st.markdown(f"### {get_flag(info['code'])} {country} — {info['count']} holidays")
        if info["holidays"]:
            for d, name in info["holidays"]:
                desc, facts = get_holiday_info(name, country)
                with st.expander(f"{d.strftime('%A, %B %d')} — {name}"):
                    WIKI_COUNTRIES = {"Japan", "China", "Spain", "Germany", "United Kingdom", "United States", "France", "Morocco", "Romania", "India", "Ireland", "Canada"}
                    if country in WIKI_COUNTRIES:
                        query = urllib.parse.quote(f"{name} {country} holiday")
                        wiki_url = f"https://en.wikipedia.org/wiki/Special:Search?search={query}"
                        st.markdown(f'**<a href="{wiki_url}" target="_blank" style="color: #2563eb; text-decoration: none;">{name} ↗</a>**', unsafe_allow_html=True)
                    
                    st.write(desc)
                    if facts:
                        st.markdown("**💡 Did you know?**")
                        for fact in facts[:2]:
                            st.markdown(f"- {fact}")
        else:
            st.write("No holidays this month.")
        st.markdown("---")

# Yearly overview
with st.expander("📊 Yearly Overview", expanded=False):
    if len(selected_countries) >= 2:
        yearly = {}
        for country in selected_countries:
            code = COUNTRIES.get(country)
            if code:
                yh = get_holidays_for_year(code, year)
                counts = [0] * 12
                for d, name in yh:
                    counts[d.month - 1] += 1
                yearly[country] = counts
        if yearly:
            months = [calendar.month_abbr[i] for i in range(1, 13)]
            df = pd.DataFrame(yearly, index=months)
            st.line_chart(df)

            summary = []
            for country, counts in yearly.items():
                summary.append({
                    "Country": country,
                    "Total": sum(counts),
                    "Busiest month": calendar.month_name[counts.index(max(counts)) + 1],
                })
            st.dataframe(pd.DataFrame(summary), use_container_width=True, hide_index=True)
    else:
        st.write("Select at least 2 countries to compare.")

# Export
with st.expander("💾 Export Data", expanded=False):
    rows = []
    for country, info in all_data.items():
        for d, name in info["holidays"]:
            desc, _ = get_holiday_info(name, country)
            rows.append({
                "Country": country,
                "Date": d.isoformat(),
                "Day": d.strftime("%A"),
                "Holiday": name,
                "Description": desc,
            })
    if rows:
        df_exp = pd.DataFrame(rows)
        st.dataframe(df_exp, use_container_width=True, hide_index=True)
        st.download_button("Download CSV", df_exp.to_csv(index=False), f"holidays_{month_name}_{year}.csv", "text/csv")
    else:
        st.write("No data to export.")
