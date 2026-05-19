"""Holiday descriptions, fun facts, and smart matching."""

# Comprehensive holiday knowledge base
# Keys are normalized lowercase holiday name fragments for fuzzy matching
HOLIDAY_DB = {
    # ── NEW YEAR ─────────────────────────────────────────────────────
    "new year": {
        "desc": "The celebration marking the first day of the year in the Gregorian calendar. Observed worldwide with fireworks, gatherings, and traditions symbolizing fresh starts.",
        "facts": [
            "The Times Square ball drop in NYC has been a tradition since 1907.",
            "In Spain, people eat 12 grapes at midnight — one for each chime of the clock.",
            "In Denmark, people smash old plates on friends' doorsteps to bring good luck.",
            "In Colombia, to invite travel blessings, some carry an empty suitcase around the block.",
            "In Brazil, people wear white for peace and jump over seven waves in the ocean, making a wish each time.",
            "New Year's Day is the most celebrated holiday globally, with ~90% of the world getting the day off.",
        ],
    },
    "chinese new year": {
        "desc": "The most important festival in Chinese culture, marking the start of the lunisolar calendar year. Celebrations last 15 days and involve family reunions, feasts, and dragon dances.",
        "facts": [
            "Each year is associated with one of 12 zodiac animals.",
            "Red envelopes (hongbao) with money are given to children for good luck.",
            "Over 3 billion trips are made during the Chinese New Year travel rush — the largest human migration.",
            "Fireworks were invented in China and are central to the celebration.",
        ],
    },
    "lunar new year": {
        "desc": "A major festival celebrated across East and Southeast Asia, marking the beginning of the lunar calendar year with family gatherings and cultural traditions.",
        "facts": [
            "Vietnam calls it Tết, Korea calls it Seollal, and each country has unique customs.",
            "Special foods are prepared — dumplings in China, rice cakes in Korea, bánh chưng in Vietnam.",
            "The celebration is over 3,500 years old.",
        ],
    },
    # ── CHRISTMAS ────────────────────────────────────────────────────
    "christmas": {
        "desc": "A Christian holiday celebrating the birth of Jesus Christ, widely observed on December 25th. It has evolved into a global cultural celebration with gift-giving, decorations, and family traditions.",
        "facts": [
            "Christmas was not widely celebrated in America until the 19th century.",
            "About 30 countries around the world do not mark Christmas as a public holiday at all.",
            "Santa Claus is based on St. Nicholas, a 4th-century Greek bishop known for generosity.",
            "In Catalonia, Spain, a hollow 'Christmas Log' (Tió de Nadal) is kept warm and 'fed' before 'pooping' presents.",
            "In Venezuela, it is a tradition in Caracas to roller skate to early morning Christmas mass.",
            "In Japan, Christmas is celebrated as a romantic occasion featuring a tradition of eating KFC.",
        ],
    },
    "christmas day": {
        "desc": "The principal feast day celebrating the Nativity of Jesus Christ, observed by billions worldwide with religious services, gift exchanges, and festive meals.",
        "facts": [
            "December 25 was chosen to coincide with existing Roman winter solstice festivals.",
            "The first Christmas card was created in London in 1843.",
            "Japan celebrates Christmas with KFC — a tradition since a 1974 marketing campaign.",
        ],
    },
    "christmas eve": {
        "desc": "The evening before Christmas Day, observed with church services, family gatherings, and in many cultures, the main gift-giving celebration.",
        "facts": [
            "In many European countries, presents are exchanged on Christmas Eve rather than Christmas Day.",
            "NORAD has tracked Santa's journey on Christmas Eve since 1955.",
            "In Norway, many people hide their brooms on Christmas Eve to prevent witches and evil spirits from stealing them for a joyride.",
        ],
    },
    # ── EASTER ───────────────────────────────────────────────────────
    "easter": {
        "desc": "The most important Christian holiday, celebrating the resurrection of Jesus Christ from the dead. The date varies each year, determined by the lunar calendar.",
        "facts": [
            "Easter eggs symbolize new life and the empty tomb of Jesus.",
            "The Easter Bunny tradition originated among German Lutherans in the 1600s.",
            "Americans buy over 16 billion jellybeans for Easter each year.",
            "The White House Easter Egg Roll has been held since 1878.",
        ],
    },
    "good friday": {
        "desc": "A Christian holiday commemorating the crucifixion of Jesus Christ and his death at Calvary. It is observed with solemn church services, fasting, and prayer.",
        "facts": [
            "It's called 'Good' Friday possibly from 'God's Friday' or because the crucifixion is seen as 'good' for humanity.",
            "In the Philippines, some devotees are actually nailed to crosses in reenactments.",
            "Hot cross buns are traditionally eaten on Good Friday in Britain.",
        ],
    },
    "easter monday": {
        "desc": "The day after Easter Sunday, observed as a public holiday in many countries. Traditions include egg rolling, picnics, and continued Easter celebrations.",
        "facts": [
            "In Poland, Easter Monday is called Śmigus-Dyngus — people splash each other with water.",
            "In Australia, the Easter Bilby replaces the Easter Bunny to raise awareness of native wildlife.",
        ],
    },
    # ── INDEPENDENCE DAYS ────────────────────────────────────────────
    "independence day": {
        "desc": "A national holiday commemorating the date a country declared or gained its independence, typically from a colonial power. Celebrated with patriotic displays, parades, and fireworks.",
        "facts": [
            "The US Independence Day on July 4th was not widely celebrated until after the War of 1812.",
            "India's independence at midnight on August 15, 1947 was chosen by astrologers as an auspicious time.",
            "Over 60 countries celebrate independence from the British Empire alone.",
        ],
    },
    "independence": {
        "desc": "A national day marking the country's sovereignty and freedom, celebrated with patriotic ceremonies, cultural events, and public festivities.",
        "facts": [
            "Independence celebrations often feature military parades, flag ceremonies, and cultural performances.",
            "Many countries gained independence in waves — Latin America in the 1800s, Africa and Asia in the 1900s.",
        ],
    },
    # ── LABOR / WORKERS ──────────────────────────────────────────────
    "labor day": {
        "desc": "A holiday honoring the labor movement and the contributions of workers to society. Celebrated on different dates worldwide — May 1st in most countries, first Monday of September in the US and Canada.",
        "facts": [
            "International Workers' Day (May 1) was inspired by the 1886 Haymarket affair in Chicago.",
            "The first US Labor Day was celebrated on September 5, 1882 in New York City.",
            "Over 80 countries celebrate Labor Day on May 1st.",
        ],
    },
    "labour day": {
        "desc": "A public holiday celebrating the achievements of workers and the labor movement, marked by parades, speeches, and community events.",
        "facts": [
            "Canada's Labour Day has been a statutory holiday since 1894.",
            "In Australia, the date varies by state — from March to October.",
        ],
    },
    "workers": {
        "desc": "A holiday dedicated to recognizing the contributions of working people to the economy and society.",
        "facts": [
            "The eight-hour workday movement began in the 1810s and was central to labor rights advocacy.",
        ],
    },
    "may day": {
        "desc": "Celebrated on May 1st, it marks both the ancient spring festival and the modern International Workers' Day. Traditions include maypole dancing and labor rights marches.",
        "facts": [
            "Maypole dancing dates back to medieval Germanic traditions celebrating spring.",
            "The distress call 'Mayday' is unrelated — it comes from the French 'm'aider' (help me).",
        ],
    },
    # ── THANKSGIVING ─────────────────────────────────────────────────
    "thanksgiving": {
        "desc": "A harvest festival giving thanks for the year's blessings. In the US, it commemorates the 1621 feast between Pilgrims and Wampanoag people. In Canada, it celebrates the harvest season.",
        "facts": [
            "The first Macy's Thanksgiving Day Parade was held in 1924.",
            "Americans consume about 46 million turkeys on Thanksgiving.",
            "President Lincoln declared Thanksgiving a national holiday in 1863 during the Civil War.",
            "Canadian Thanksgiving falls on the second Monday of October.",
        ],
    },
    # ── VALENTINE'S DAY ──────────────────────────────────────────────
    "valentine": {
        "desc": "A celebration of romantic love observed on February 14th, named after Saint Valentine, a Christian martyr. People exchange cards, flowers, chocolates, and gifts.",
        "facts": [
            "About 150 million Valentine's cards are exchanged annually worldwide.",
            "The oldest known valentine was written in 1415 by Charles, Duke of Orléans, from prison.",
            "In Finland, Valentine's Day is called 'Friend's Day' (Ystävänpäivä).",
        ],
    },
    # ── RAMADAN / EID ────────────────────────────────────────────────
    "ramadan": {
        "desc": "The ninth month of the Islamic calendar, observed by Muslims worldwide as a month of fasting (sawm), prayer, reflection, and community. It commemorates the first revelation of the Quran to Prophet Muhammad.",
        "facts": [
            "Muslims fast from dawn to sunset — no food, drink, or smoking during daylight hours.",
            "The exact dates shift 11 days earlier each Gregorian year due to the lunar calendar.",
            "Iftar (the evening meal breaking the fast) is often a community event.",
        ],
    },
    "eid al-fitr": {
        "desc": "The 'Festival of Breaking the Fast,' marking the end of Ramadan. It's one of the two major Islamic holidays, celebrated with prayers, feasts, charity, and family gatherings.",
        "facts": [
            "Giving to charity (Zakat al-Fitr) before the Eid prayer is obligatory for Muslims.",
            "Children often receive gifts of money or new clothes.",
            "Celebrations typically last three days.",
        ],
    },
    "eid al-adha": {
        "desc": "The 'Festival of Sacrifice,' the holiest Islamic holiday commemorating Prophet Ibrahim's willingness to sacrifice his son in obedience to God. Celebrated with prayers and sharing of meat with family and those in need.",
        "facts": [
            "It falls on the 10th day of Dhul Hijjah, the last month of the Islamic calendar.",
            "About 100 million animals are ritually sacrificed worldwide during Eid al-Adha.",
            "The meat is divided into three parts: family, friends, and the poor.",
        ],
    },
    "eid": {
        "desc": "An Islamic festival and celebration. The two major Eids — Eid al-Fitr and Eid al-Adha — are the most significant holidays in the Muslim calendar.",
        "facts": [
            "'Eid Mubarak' (Blessed Eid) is the traditional greeting.",
            "Special Eid prayers are performed in congregation, often in open grounds.",
        ],
    },
    # ── DIWALI ───────────────────────────────────────────────────────
    "diwali": {
        "desc": "The Hindu 'Festival of Lights,' celebrating the victory of light over darkness and good over evil. Observed with oil lamps (diyas), fireworks, family feasts, and rangoli art.",
        "facts": [
            "Diwali is celebrated by Hindus, Jains, Sikhs, and some Buddhists.",
            "It's associated with Lakshmi, the goddess of wealth and prosperity.",
            "The festival lasts five days, each with its own significance.",
            "More fireworks are set off during Diwali than any other celebration worldwide.",
        ],
    },
    # ── NATIONAL DAYS ────────────────────────────────────────────────
    "national day": {
        "desc": "A designated day celebrating a nation's identity, often marking independence, unification, or a founding event. Observed with ceremonies, parades, and cultural events.",
        "facts": [
            "France's national day (Bastille Day, July 14) commemorates the storming of the Bastille in 1789.",
            "China's National Day (October 1) marks the founding of the People's Republic in 1949.",
        ],
    },
    "republic day": {
        "desc": "A holiday marking the date a country adopted its republican constitution or form of government. Celebrated with military parades and patriotic ceremonies.",
        "facts": [
            "India's Republic Day (January 26) features one of the world's most spectacular parades in New Delhi.",
            "Turkey's Republic Day (October 29) marks the declaration of the Republic in 1923.",
        ],
    },
    "revolution day": {
        "desc": "Commemorates a major revolutionary event that shaped the nation's history and political identity, often involving the overthrow of a monarchy or colonial power.",
        "facts": [
            "Many nations celebrate their revolutions as defining moments of national consciousness.",
        ],
    },
    "constitution day": {
        "desc": "A holiday commemorating the adoption or ratification of a nation's constitution, celebrating the rule of law and democratic governance.",
        "facts": [
            "Norway's Constitution Day (May 17) is one of the most enthusiastically celebrated national days in the world.",
        ],
    },
    # ── REMEMBRANCE / VETERANS ───────────────────────────────────────
    "remembrance": {
        "desc": "A day of solemn reflection honoring military personnel who died in service. Often observed with two minutes of silence, poppy wearing, and ceremonies at war memorials.",
        "facts": [
            "The red poppy symbol comes from the WWI poem 'In Flanders Fields' by John McCrae.",
            "The two-minute silence tradition began on Armistice Day, November 11, 1919.",
        ],
    },
    "veterans day": {
        "desc": "A US federal holiday honoring all who have served in the armed forces. Originally 'Armistice Day,' marking the end of World War I on November 11, 1918.",
        "facts": [
            "Veterans Day was renamed from Armistice Day in 1954 to honor all veterans, not just WWI.",
            "It coincides with Remembrance Day in Commonwealth countries.",
        ],
    },
    "memorial day": {
        "desc": "A US federal holiday for mourning military personnel who died while serving. It also marks the unofficial start of summer.",
        "facts": [
            "The National Moment of Remembrance asks Americans to pause at 3:00 PM local time.",
            "Memorial Day was originally called Decoration Day, from the tradition of decorating graves.",
        ],
    },
    "anzac day": {
        "desc": "A national day of remembrance in Australia and New Zealand commemorating the members of the Australian and New Zealand Army Corps (ANZAC) who served in all wars.",
        "facts": [
            "The Dawn Service tradition reflects the time of the original Gallipoli landing in 1915.",
            "ANZAC biscuits were sent by wives to soldiers as they kept well during transit.",
        ],
    },
    # ── CULTURAL / REGIONAL ──────────────────────────────────────────
    "bastille day": {
        "desc": "France's national day celebrating the storming of the Bastille prison on July 14, 1789, a pivotal event in the French Revolution symbolizing the rise of the people against tyranny.",
        "facts": [
            "The Bastille only held 7 prisoners when it was stormed.",
            "The military parade on the Champs-Élysées is the oldest and largest regular military parade in Europe.",
            "The French call it 'la Fête nationale' — not 'Bastille Day.'",
        ],
    },
    "canada day": {
        "desc": "Canada's national holiday celebrating the anniversary of Confederation on July 1, 1867, when three colonies united into a single country called Canada.",
        "facts": [
            "It was originally called 'Dominion Day' until 1982.",
            "Ottawa's Parliament Hill hosts the country's largest Canada Day celebration.",
        ],
    },
    "australia day": {
        "desc": "Australia's official national day, held on January 26, marking the anniversary of the 1788 arrival of the First Fleet at Port Jackson, New South Wales.",
        "facts": [
            "The day is controversial — many Indigenous Australians call it 'Invasion Day.'",
            "Citizenship ceremonies are a major feature, with thousands becoming citizens on this day.",
        ],
    },
    "victoria day": {
        "desc": "A Canadian federal holiday celebrated on the last Monday before May 25, in honour of Queen Victoria's birthday. It also marks the unofficial start of summer in Canada.",
        "facts": [
            "Informally known as 'May Two-Four' — both for the date and the Canadian slang for a case of 24 beers.",
        ],
    },
    "king's birthday": {
        "desc": "A public holiday celebrating the birthday of the reigning monarch. The date may not correspond to the actual birthday but is set by the government.",
        "facts": [
            "In the UK, the King's official birthday is celebrated in June regardless of his actual birthdate.",
            "The tradition of an official birthday separate from the actual one dates back to King George II in 1748.",
        ],
    },
    "queen's birthday": {
        "desc": "A public holiday celebrating the birthday of the reigning queen. In many Commonwealth nations, it's observed on a convenient date rather than the actual birthday.",
        "facts": [
            "Queen Elizabeth II's actual birthday was April 21, but it was officially celebrated in June.",
        ],
    },
    # ── SPRING FESTIVALS ─────────────────────────────────────────────
    "holi": {
        "desc": "The Hindu 'Festival of Colors' celebrating the victory of good over evil and the arrival of spring. Participants throw colored powder and water at each other in joyous celebration.",
        "facts": [
            "Holi celebrates the legend of Prahlada and Holika from Hindu mythology.",
            "The colors were originally made from natural sources like turmeric, neem, and flowers.",
            "The night before Holi, bonfires are lit in a ritual called Holika Dahan.",
        ],
    },
    "nowruz": {
        "desc": "The Persian New Year marking the spring equinox, celebrated for over 3,000 years across Central Asia, the Middle East, and diaspora communities worldwide.",
        "facts": [
            "The Haft-sin table features seven symbolic items starting with the letter 'S' in Farsi.",
            "Nowruz is recognized by the UN as International Day of Nowruz.",
            "Celebrations last 13 days, ending with Sizdah Bedar — a picnic day outdoors.",
        ],
    },
    # ── HARVEST / SEASONAL ───────────────────────────────────────────
    "mid-autumn": {
        "desc": "A harvest festival celebrated in East Asian cultures during the full moon of the 8th lunar month. Families gather to admire the moon, eat mooncakes, and carry lanterns.",
        "facts": [
            "Mooncakes traditionally contain lotus seed paste and salted egg yolks.",
            "The festival is associated with the legend of Chang'e, who lives on the moon.",
        ],
    },
    "harvest": {
        "desc": "A traditional celebration giving thanks for the annual harvest. Harvest festivals are found in virtually every culture worldwide.",
        "facts": [
            "Harvest festivals predate organized religion, dating back to ancient agricultural societies.",
        ],
    },
    # ── HALLOWEEN / ALL SAINTS ───────────────────────────────────────
    "halloween": {
        "desc": "Observed on October 31st, Halloween originated from the ancient Celtic festival of Samhain. Modern celebrations include costumes, trick-or-treating, carved pumpkins, and haunted attractions.",
        "facts": [
            "Americans spend about $10 billion on Halloween annually.",
            "The tradition of carving pumpkins originated from an Irish myth about 'Stingy Jack.'",
            "The word 'Halloween' comes from 'All Hallows' Eve.'",
        ],
    },
    "all saints": {
        "desc": "A Christian solemnity honoring all saints, known and unknown. Observed on November 1st in Western Christianity, it's a time to remember those who have attained heaven.",
        "facts": [
            "In Mexico, it overlaps with Día de los Muertos (Day of the Dead) celebrations.",
            "In many European countries, it's a day to visit and decorate graves of loved ones.",
        ],
    },
    "day of the dead": {
        "desc": "A Mexican tradition honoring deceased loved ones with colorful altars (ofrendas), marigold flowers, sugar skulls, and the favorite foods of the departed.",
        "facts": [
            "UNESCO recognizes Día de los Muertos as an Intangible Cultural Heritage of Humanity.",
            "The celebration blends pre-Columbian Aztec rituals with Catholic traditions.",
        ],
    },
    # ── MIDSUMMER ────────────────────────────────────────────────────
    "midsummer": {
        "desc": "A celebration of the summer solstice, particularly popular in Scandinavian countries. Features include maypole dancing, flower wreaths, and outdoor feasts.",
        "facts": [
            "In Sweden, Midsummer is considered bigger than Christmas by many Swedes.",
            "Traditional belief holds that picking seven different flowers and placing them under your pillow on Midsummer's Eve will make you dream of your future spouse.",
        ],
    },
    # ── EMANCIPATION / FREEDOM ───────────────────────────────────────
    "emancipation": {
        "desc": "A holiday commemorating the freeing of enslaved people, marking a pivotal moment in the fight for human rights and dignity.",
        "facts": [
            "Different countries and regions celebrate emancipation on different dates, reflecting when abolition took effect locally.",
        ],
    },
    "juneteenth": {
        "desc": "A US federal holiday commemorating June 19, 1865, when enslaved people in Galveston, Texas, learned of their freedom — 2.5 years after the Emancipation Proclamation.",
        "facts": [
            "Juneteenth became a federal holiday in 2021, making it the newest US federal holiday.",
            "Traditional celebrations include barbecues, parades, and readings of the Emancipation Proclamation.",
            "The red food and drink at Juneteenth celebrations symbolize the resilience of enslaved people.",
        ],
    },
    # ── MOTHER'S / FATHER'S DAY ──────────────────────────────────────
    "mother": {
        "desc": "A celebration honoring mothers and motherhood, observed on various dates around the world. The modern holiday was established in the US in 1914.",
        "facts": [
            "Anna Jarvis, who campaigned for Mother's Day, later opposed its commercialization.",
            "Mother's Day is the busiest day of the year for restaurants in the US.",
            "In the UK, 'Mothering Sunday' has been observed since the 16th century.",
        ],
    },
    "father": {
        "desc": "A celebration honoring fathers and fatherhood, complementing Mother's Day. First celebrated in the US in 1910.",
        "facts": [
            "Father's Day is the busiest day for collect phone calls in the US.",
            "In Germany, Father's Day (Vatertag) involves men pulling wagons filled with beer on hikes.",
        ],
    },
    # ── MARTIN LUTHER KING JR ────────────────────────────────────────
    "martin luther king": {
        "desc": "A US federal holiday honoring Dr. Martin Luther King Jr., the civil rights leader who advocated for nonviolent resistance against racial discrimination. Observed on the third Monday of January.",
        "facts": [
            "MLK's 'I Have a Dream' speech is considered one of the greatest speeches in history.",
            "It's the only US federal holiday designated as a national day of service.",
            "King was 35 when he received the Nobel Peace Prize — the youngest at that time.",
        ],
    },
    # ── MISCELLANEOUS ────────────────────────────────────────────────
    "boxing day": {
        "desc": "A holiday observed on December 26 in many Commonwealth nations. Originally a day for giving gifts to servants and tradespeople, it's now associated with shopping sales and sporting events.",
        "facts": [
            "The name may come from the 'Christmas box' — a clay pot containing coins, broken open on this day.",
            "In some countries, Boxing Day is one of the biggest shopping days of the year.",
        ],
    },
    "summer bank holiday": {
        "desc": "A public holiday in the United Kingdom, traditionally marking the end of the summer season. It usually falls on the last Monday of August (except in Scotland, where it is earlier).",
        "facts": [
            "Bank holidays were introduced by the Bank Holidays Act of 1871, spearheaded by Sir John Lubbock.",
            "It is often celebrated with short trips, DIY home improvements, and the famous Notting Hill Carnival in London.",
        ],
    },
    "bank holiday": {
        "desc": "A public holiday in the United Kingdom, some Commonwealth countries, and Ireland. Originally days when banks were officially closed, they are now general public holidays.",
        "facts": [
            "The term 'bank holiday' is used universally in the UK to refer to all public holidays.",
        ],
    },
    "st. patrick": {
        "desc": "An Irish cultural and religious holiday celebrating St. Patrick, the foremost patron saint of Ireland. Famous worldwide for green attire, parades, and shamrocks.",
        "facts": [
            "St. Patrick was actually born in Roman Britain, not Ireland.",
            "The original color associated with St. Patrick was blue, not green.",
            "Chicago dyes its river green every St. Patrick's Day — a tradition since 1962.",
        ],
    },
    "ascension": {
        "desc": "A Christian holiday commemorating Jesus Christ's ascension to heaven 40 days after his resurrection on Easter. It always falls on a Thursday.",
        "facts": [
            "Ascension Day is a public holiday in many European countries.",
            "In some traditions, it marks the beginning of a 10-day period of prayer leading to Pentecost.",
        ],
    },
    "pentecost": {
        "desc": "A Christian holiday celebrating the descent of the Holy Spirit upon the Apostles, 50 days after Easter. Considered the 'birthday of the Church.'",
        "facts": [
            "Pentecost comes from the Greek 'pentekostos' meaning 'fiftieth.'",
            "In Italy, rose petals are dropped from church ceilings to symbolize the Holy Spirit.",
        ],
    },
    "whit monday": {
        "desc": "The day after Whitsunday (Pentecost), observed as a public holiday in many European countries with traditional outdoor festivals and processions.",
        "facts": [
            "'Whitsun' may refer to the white garments worn by the newly baptized at Pentecost.",
        ],
    },
    "assumption": {
        "desc": "A Christian feast day commemorating the belief that the Virgin Mary was taken up body and soul into heavenly glory at the end of her earthly life.",
        "facts": [
            "August 15 is a public holiday in many Catholic countries worldwide.",
            "The doctrine was formally defined by Pope Pius XII in 1950.",
        ],
    },
    "epiphany": {
        "desc": "A Christian feast day celebrating the revelation of God incarnate as Jesus Christ. In Western Christianity, it commemorates the visit of the Magi (Three Wise Men).",
        "facts": [
            "In Spain, the Three Kings (Reyes Magos) bring gifts to children on January 6 — not Santa Claus.",
            "King cake, eaten during Epiphany, contains a hidden figurine — whoever finds it hosts the next party.",
        ],
    },
    "carnival": {
        "desc": "A festive season occurring before Lent, featuring parades, masquerades, music, and dancing. Most famous in Rio de Janeiro, Venice, and New Orleans (Mardi Gras).",
        "facts": [
            "Rio's Carnival parade is the world's largest, with 2 million people per day on the streets.",
            "The word 'carnival' may come from Latin 'carne vale' meaning 'farewell to meat.'",
        ],
    },
    "youth day": {
        "desc": "A holiday dedicated to celebrating young people and their role in society. Many countries observe it on different dates with cultural events and educational activities.",
        "facts": [
            "The UN's International Youth Day is August 12.",
            "South Africa's Youth Day (June 16) commemorates the 1976 Soweto uprising.",
        ],
    },
    "children's day": {
        "desc": "A day recognizing children worldwide, promoting their welfare, and celebrating childhood. Dates vary by country.",
        "facts": [
            "Universal Children's Day is November 20, the date the UN adopted the Declaration of the Rights of the Child.",
            "In Japan, Children's Day (May 5) features carp-shaped koinobori streamers.",
        ],
    },
    "women's day": {
        "desc": "International Women's Day (March 8) celebrates women's achievements and advocates for gender equality worldwide.",
        "facts": [
            "The first National Women's Day was observed in the US on February 28, 1909.",
            "In Russia, March 8 is an official public holiday and men give flowers to women.",
        ],
    },
    "human rights": {
        "desc": "A day commemorating the adoption of the Universal Declaration of Human Rights by the UN General Assembly on December 10, 1948.",
        "facts": [
            "The UDHR has been translated into over 500 languages — the most translated document in the world.",
        ],
    },
    "unity day": {
        "desc": "A national holiday celebrating the unity and togetherness of a nation's people, often marking a historical event that brought the country together.",
        "facts": [
            "Germany's Unity Day (October 3) marks reunification in 1990.",
        ],
    },
    "throne day": {
        "desc": "A national holiday celebrating the anniversary of a monarch's accession to the throne, marked with ceremonies, parades, and public festivities.",
        "facts": [
            "Morocco's Throne Day (July 30) is one of the country's most important national celebrations.",
        ],
    },
    "green march": {
        "desc": "Commemorates Morocco's Green March of November 6, 1975, when 350,000 Moroccans marched into Western Sahara to assert Morocco's claim to the territory.",
        "facts": [
            "The march was called 'Green' in reference to the color of Islam.",
            "It was one of the largest peaceful marches in history.",
        ],
    },
    "manifesto of independence": {
        "desc": "Commemorates Morocco's Manifesto of Independence, signed on January 11, 1944, demanding independence from France and Spain.",
        "facts": [
            "The manifesto was signed by 66 Moroccan nationalists.",
        ],
    },
    "melon day": {
        "desc": "A national holiday in Turkmenistan dedicated to the muskmelon, celebrated on the second Sunday of August.",
        "facts": [
            "Turkmenistan is famous for producing nearly 400 varieties of muskmelon.",
            "The holiday was established in 1994 by the country's first president.",
        ],
    },
    "night of the radishes": {
        "desc": "An annual event in Oaxaca, Mexico (Noche de Rábanos) on December 23rd where locals carve elaborate scenes out of giant radishes.",
        "facts": [
            "The radishes used are specially grown for the event and can weigh up to 3 kg (6.6 lbs).",
            "The tradition started in 1897 to attract customers to the Christmas market.",
        ],
    },
}


def _normalize(text):
    """Lowercase and strip for matching."""
    return text.lower().strip()


def get_holiday_info(holiday_name, country_name=""):
    """
    Look up holiday description and fun facts.
    Uses fuzzy substring matching against the knowledge base.
    Returns (description, [facts]) or (generic_desc, []) if not found.
    """
    name_lower = _normalize(holiday_name)

    # Try exact key match first, then substring match
    best_match = None
    best_len = 0
    for key, info in HOLIDAY_DB.items():
        if key in name_lower or name_lower in key:
            if len(key) > best_len:
                best_match = info
                best_len = len(key)

    if best_match:
        return best_match["desc"], best_match["facts"]

    # Generate a sensible generic description
    generic = f"A public holiday observed in {country_name}." if country_name else f"A public holiday."
    generic_facts = [
        "Public holidays give workers a day off and often carry deep cultural or historical significance.",
        "Many holidays have evolved over centuries, blending religious, cultural, and civic traditions.",
    ]
    return generic, generic_facts
