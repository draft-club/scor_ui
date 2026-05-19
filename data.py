"""Data helpers: country lists, coordinates, holiday fetching."""
import holidays
from datetime import date, datetime
import calendar

# Build full country list from holidays library + common names
_HOLIDAYS_SUPPORTED = holidays.list_supported_countries()

# Map of common country names -> ISO codes (comprehensive)
COUNTRY_NAMES = {
    "Afghanistan": "AF", "Albania": "AL", "Algeria": "DZ", "American Samoa": "AS",
    "Andorra": "AD", "Angola": "AO", "Argentina": "AR", "Armenia": "AM",
    "Aruba": "AW", "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ",
    "Bahamas": "BS", "Bahrain": "BH", "Bangladesh": "BD", "Barbados": "BB",
    "Belarus": "BY", "Belgium": "BE", "Belize": "BZ", "Benin": "BJ",
    "Bolivia": "BO", "Bosnia and Herzegovina": "BA", "Botswana": "BW", "Brazil": "BR",
    "Brunei": "BN", "Bulgaria": "BG", "Burkina Faso": "BF", "Burundi": "BI",
    "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA", "Chad": "TD",
    "Chile": "CL", "China": "CN", "Colombia": "CO", "Costa Rica": "CR",
    "Croatia": "HR", "Cuba": "CU", "Curacao": "CW", "Cyprus": "CY",
    "Czech Republic": "CZ", "Denmark": "DK", "Djibouti": "DJ",
    "Dominican Republic": "DO", "Ecuador": "EC", "Egypt": "EG",
    "El Salvador": "SV", "Estonia": "EE", "Eswatini": "SZ", "Ethiopia": "ET",
    "Finland": "FI", "France": "FR", "Gabon": "GA", "Georgia": "GE",
    "Germany": "DE", "Ghana": "GH", "Greece": "GR", "Guam": "GU",
    "Guatemala": "GT", "Guernsey": "GG", "Honduras": "HN", "Hong Kong": "HK",
    "Hungary": "HU", "Iceland": "IS", "India": "IN", "Indonesia": "ID",
    "Iran": "IR", "Iraq": "IQ", "Ireland": "IE", "Isle of Man": "IM",
    "Israel": "IL", "Italy": "IT", "Jamaica": "JM", "Japan": "JP",
    "Jersey": "JE", "Jordan": "JO", "Kazakhstan": "KZ", "Kenya": "KE",
    "Kuwait": "KW", "Kyrgyzstan": "KG", "Laos": "LA", "Latvia": "LV",
    "Lesotho": "LS", "Liechtenstein": "LI", "Lithuania": "LT", "Luxembourg": "LU",
    "Madagascar": "MG", "Malawi": "MW", "Malaysia": "MY", "Maldives": "MV",
    "Malta": "MT", "Marshall Islands": "MH", "Mexico": "MX", "Moldova": "MD",
    "Monaco": "MC", "Montenegro": "ME", "Morocco": "MA", "Mozambique": "MZ",
    "Namibia": "NA", "Netherlands": "NL", "New Zealand": "NZ", "Nicaragua": "NI",
    "Nigeria": "NG", "North Macedonia": "MK", "Norway": "NO", "Oman": "OM",
    "Pakistan": "PK", "Palau": "PW", "Panama": "PA", "Papua New Guinea": "PG",
    "Paraguay": "PY", "Peru": "PE", "Philippines": "PH", "Poland": "PL",
    "Portugal": "PT", "Puerto Rico": "PR", "Qatar": "QA", "Romania": "RO",
    "Russia": "RU", "Rwanda": "RW", "Saudi Arabia": "SA", "Senegal": "SN",
    "Serbia": "RS", "Seychelles": "SC", "Singapore": "SG", "Slovakia": "SK",
    "Slovenia": "SI", "South Africa": "ZA", "South Korea": "KR", "Spain": "ES",
    "Sri Lanka": "LK", "Sweden": "SE", "Switzerland": "CH", "Taiwan": "TW",
    "Tanzania": "TZ", "Thailand": "TH", "Timor-Leste": "TL", "Tonga": "TO",
    "Trinidad and Tobago": "TT", "Tunisia": "TN", "Turkey": "TR",
    "Uganda": "UG", "Ukraine": "UA", "United Arab Emirates": "AE",
    "United Kingdom": "GB", "United States": "US", "Uruguay": "UY",
    "Uzbekistan": "UZ", "Vanuatu": "VU", "Vatican City": "VA",
    "Venezuela": "VE", "Vietnam": "VN", "Zambia": "ZM", "Zimbabwe": "ZW",
}

# Filter to only holidays-supported countries
COUNTRIES = {k: v for k, v in sorted(COUNTRY_NAMES.items()) if v in _HOLIDAYS_SUPPORTED}

# Capital city coordinates for map markers
COORDS = {
    "AF":(34.52,69.17),"AL":(41.33,19.82),"DZ":(36.75,3.04),"AD":(42.51,1.52),
    "AO":(-8.84,13.23),"AR":(-34.60,-58.38),"AM":(40.18,44.51),"AU":(-35.28,149.13),
    "AT":(48.21,16.37),"AZ":(40.41,49.87),"BS":(25.05,-77.35),"BH":(26.23,50.59),
    "BD":(23.81,90.41),"BB":(13.10,-59.61),"BY":(53.90,27.57),"BE":(50.85,4.35),
    "BZ":(17.25,-88.77),"BO":(-16.50,-68.15),"BA":(43.86,18.41),"BW":(-24.65,25.91),
    "BR":(-15.79,-47.88),"BG":(42.70,23.32),"CA":(45.42,-75.70),"CL":(-33.45,-70.67),
    "CN":(39.90,116.41),"CO":(4.71,-74.07),"CR":(9.93,-84.08),"HR":(45.81,15.98),
    "CU":(23.11,-82.37),"CY":(35.17,33.36),"CZ":(50.08,14.44),"DK":(55.68,12.57),
    "DJ":(11.59,43.15),"DO":(18.47,-69.90),"EC":(-0.18,-78.47),"EG":(30.04,31.24),
    "SV":(13.69,-89.19),"EE":(59.44,24.75),"ET":(9.02,38.75),"FI":(60.17,24.94),
    "FR":(48.86,2.35),"GE":(41.72,44.79),"DE":(52.52,13.41),"GH":(5.60,-0.19),
    "GR":(37.98,23.73),"GT":(14.63,-90.51),"HN":(14.07,-87.19),"HK":(22.32,114.17),
    "HU":(47.50,19.04),"IS":(64.15,-21.94),"IN":(28.61,77.21),"ID":(-6.21,106.85),
    "IR":(35.69,51.39),"IQ":(33.31,44.37),"IE":(53.35,-6.26),"IL":(31.77,35.23),
    "IT":(41.90,12.50),"JM":(18.00,-76.79),"JP":(35.68,139.65),"JO":(31.96,35.95),
    "KZ":(51.17,71.45),"KE":(-1.29,36.82),"KW":(29.38,47.99),"LV":(56.95,24.11),
    "LI":(47.14,9.52),"LT":(54.69,25.28),"LU":(49.61,6.13),"MY":(3.14,101.69),
    "MT":(35.90,14.51),"MX":(19.43,-99.13),"MD":(47.01,28.86),"MC":(43.73,7.42),
    "ME":(42.43,19.26),"MA":(34.02,-6.84),"MZ":(-25.97,32.57),"NA":(-22.56,17.08),
    "NL":(52.37,4.90),"NZ":(-41.29,174.78),"NI":(12.11,-86.24),"NG":(9.06,7.49),
    "MK":(42.00,21.43),"NO":(59.91,10.75),"OM":(23.59,58.54),"PK":(33.69,73.04),
    "PA":(8.98,-79.52),"PY":(-25.26,-57.58),"PE":(-12.05,-77.04),"PH":(14.60,120.98),
    "PL":(52.23,21.01),"PT":(38.72,-9.14),"PR":(18.47,-66.11),"QA":(25.29,51.53),
    "RO":(44.43,26.10),"RU":(55.76,37.62),"SA":(24.69,46.72),"RS":(44.79,20.47),
    "SG":(1.35,103.82),"SK":(48.15,17.11),"SI":(46.06,14.51),"ZA":(-25.75,28.19),
    "KR":(37.57,126.98),"ES":(40.42,-3.70),"LK":(6.93,79.85),"SE":(59.33,18.07),
    "CH":(46.95,7.45),"TW":(25.03,121.57),"TZ":(-6.79,39.28),"TH":(13.76,100.50),
    "TN":(36.81,10.18),"TR":(39.93,32.85),"UA":(50.45,30.52),"AE":(24.45,54.65),
    "GB":(51.51,-0.13),"US":(38.91,-77.04),"UY":(-34.88,-56.16),"UZ":(41.30,69.28),
    "VE":(10.48,-66.90),"VN":(21.03,105.85),"ZM":(-15.39,28.32),"ZW":(-17.83,31.05),
    "SZ":(-26.31,31.13),"CW":(12.17,-68.98),"AW":(12.51,-70.03),"SC":(-4.62,55.45),
    "RW":(-1.94,29.87),"SN":(14.72,-17.47),"BN":(4.93,114.95),"KH":(11.56,104.92),
    "GA":(0.39,9.45),"GG":(49.45,-2.54),"JE":(49.21,-2.13),"IM":(54.15,-4.48),
    "KG":(42.87,74.59),"LA":(17.97,102.63),"LS":(-29.31,27.48),"MG":(-18.88,47.51),
    "MW":(-13.96,33.79),"MV":(4.18,73.51),"TO":(-21.21,-175.20),"TL":(-8.56,125.57),
    "TT":(10.66,-61.51),"UG":(0.35,32.58),"VA":(41.90,12.45),"VU":(-17.73,168.32),
    "TD":(12.13,15.05),"CM":(3.87,11.52),"BJ":(6.37,2.43),"BF":(12.37,-1.52),
    "BI":(-3.38,29.36),"PG":(-6.31,147.15),"MH":(7.10,171.38),"PW":(7.50,134.62),
    "GU":(13.47,144.75),"AS":(-14.28,-170.70),
}

# Country flag emojis
def get_flag(code):
    try:
        return ''.join(chr(0x1F1E6 + ord(c) - ord('A')) for c in code.upper())
    except Exception:
        return "🏳️"

def get_holidays_for_month(country_code, year, month):
    """Get holidays for a specific country/year/month."""
    try:
        cal = holidays.country_holidays(country_code, years=year)
    except Exception:
        return []
    items = []
    for d, name in cal.items():
        if isinstance(d, date) and d.year == year and d.month == month:
            items.append((d, name))
    items.sort()
    return items

def get_holidays_for_year(country_code, year):
    """Get all holidays for a country in a given year."""
    try:
        cal = holidays.country_holidays(country_code, years=year)
    except Exception:
        return []
    items = [(d, name) for d, name in cal.items() if isinstance(d, date)]
    items.sort()
    return items

def build_calendar_html(year, month, aggregated_holidays, today=None):
    """Build an HTML calendar table with holiday highlights."""
    cal_data = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    html = f'<table class="hcal"><thead><tr>'
    for wd in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        html += f"<th>{wd}</th>"
    html += '</tr></thead><tbody>'
    for week in cal_data:
        html += '<tr>'
        for day in week:
            if day == 0:
                html += '<td class="empty"></td>'
            else:
                classes = []
                if day in aggregated_holidays:
                    classes.append("holiday")
                if today and today.year == year and today.month == month and today.day == day:
                    classes.append("today")
                cls = f' class="{" ".join(classes)}"' if classes else ""
                content = f"<b>{day}</b>"
                if day in aggregated_holidays:
                    # Show first holiday name abbreviated
                    first = aggregated_holidays[day][0].split(":")[1].strip() if ":" in aggregated_holidays[day][0] else aggregated_holidays[day][0]
                    content += f'<span class="h-name" title="{first}">{first}</span>'
                html += f"<td{cls}>{content}</td>"
        html += '</tr>'
    html += '</tbody></table>'
    return html
