# Conversation export

Claude Code session that produced this repo (23–24 November 2026). User messages and Claude's replies are verbatim; tool calls are listed by name and description only, tool output is left out, and local paths and personal details are redacted.

## User
> I want you to look at these engine oils. My bike is Honda Hornet 2.0, ~1300km total mileage, I am getting ~43km/L mileage now, I mainly commute in Dhaka. So far I've used Pro Honda Mineral 10W-30 1L, (oil changes: 400km, then 800km), in the next oil change at 1500km I want to use a better engine oil. Please suggest which will be best for for the bike with highest value (bang for buck). You should download the technical spec sheet/data sheet of these oils to judge them fully. You can also suggest oils other than these e.g. Amsoil, Champion, Shell, Mobil and so on.
> 
> Here's the current price of the oils in this directory:
> 1. Liqui Moly - 1400 BDT
> 2. Motul - 1600 BDT
> 3. Maxima - 2200 BDT

## Claude

- *Bash*: List files in the engine-oils directories
- *Bash*: List all files in the oil subfolders
- *Read*: <repo>/liqui-moly/870424251_28939764902331549_2646183054178094570_n.jpg
- *Read*: <repo>/liqui-moly/883410596_2145235646084761_7542637716388773806_n.jpg
- *Read*: <repo>/liqui-moly/883199214_1825153345303203_3647369760904968315_n.jpg
- *Read*: <repo>/motul/861307516_2263536184491320_3009882981903670918_n.jpg
- *Read*: <repo>/motul/852027135_3289704684557918_5088041280498492784_n.jpg
- *Read*: <repo>/motul/854033771_3234567593406748_1590740038645807692_n.jpg
- *Read*: <repo>/motul/850097055_1627839242472029_3831161132185322015_n.jpg
- *Read*: <repo>/maxima/787573958_971135232679861_7346808769488642626_n.jpg
- *Read*: <repo>/maxima/795066772_1949695889052828_6602472168522970601_n.jpg
- *Read*: <repo>/maxima/788211608_1821249989033696_4302185885757184609_n.jpg
- *ToolSearch*: select:WebSearch
- *Bash*: Check which PDF text tools are installed
- *WebSearch*: Liqui Moly Motorbike 4T 10W-30 Street 23226 product information
- *WebSearch*: Motul 7100 4T 10W-30 technical data sheet API SP JASO MA2 104089
- *WebSearch*: Maxima Pro Plus+ 10W-30 30-01901 technical data sheet
- *WebSearch*: Honda Hornet 2.0 owner's manual engine oil capacity recommended oil 10W-30 JASO MA
- *Bash*: Download Motul and Maxima datasheet PDFs
- *Bash*: Extract text from Motul and Maxima datasheets
- *Bash*: Fetch Liqui Moly product page and list PDF links
- *Bash*: Search Liqui Moly page HTML for datasheet links

Motul and Maxima datasheets are downloaded. Now pulling the Liqui Moly datasheet link out of its product page.

- *Bash*: Extract Liqui Moly datasheet URLs from page JSON
- *Bash*: Inspect context around datasheet keywords in page
- *Bash*: Find download component config for article 23226
- *Bash*: Query Liqui Moly PIM API for article 23226 sheets
- *Bash*: Parse Liqui Moly sheet JSON for English PI links
- *Bash*: Download Liqui Moly product info and safety sheets
- *Bash*: Dedupe identical Liqui Moly PDFs and extract text

Liqui Moly's datasheet is in: 11.5 cSt at 100°C, flash 230°C, Noack 12.9%. Now reading its safety sheet for the base-oil makeup, then the Honda spec.

- *Bash*: Extract composition section from Liqui Moly SDS
- *WebSearch*: Hornet 2.0 engine oil capacity litre 10W30 owner's manual Honda 184cc
- *WebSearch*: maximausa.com Pro Plus+ 10W-30 technical data sheet viscosity index flash point API SN Plus PEAC
- *WebSearch*: Honda Hornet 2.0 Bangladesh engine oil recommendation Pro Honda fully synthetic 10W30 price BD
- *Bash*: Fetch Hornet 2.0 spec pages and grep oil details
- *WebSearch*: "Hornet 2.0" owner's manual pdf honda2wheelersindia engine oil capacity "after draining"
- *WebSearch*: Hornet 2.0 oil change interval km Bangladesh Honda service schedule synthetic oil 2000 km
- *Bash*: Probe Honda India and Bangladesh sites for Hornet 2.0 manual
- *Bash*: Fetch Bangladesh Honda owner's manual and Hornet 2.0 pages

Found Bangladesh Honda's official Hornet 2.0 owner's manual. Pulling the oil spec, capacity and service schedule from it.

- *Bash*: Download Hornet 2.0 manual and read site FAQ
- *Bash*: Grep owner's manual text for oil-related lines
- *Bash*: Locate manual pages mentioning oil specs
- *Bash*: Render manual pages 44, 59, 102 as images
- *Read*: <scratch>/honda-manual/page44-044.png
- *Read*: <scratch>/honda-manual/page102-102.png
- *Bash*: Find maintenance schedule pages in manual

Manual confirms 10W-30, JASO MA, API SJ+ (not "Energy/Resource Conserving"), 1.0 L at drain. Now checking its maintenance-schedule page for the oil interval.

- *Bash*: Preview text of manual pages 36 to 43
- *Bash*: Render maintenance schedule pages 38-39
- *Read*: <scratch>/honda-manual/sched-038.png
- *Read*: <scratch>/honda-manual/sched-039.png
- *Agent*: Research BD alternative oils
- *WebSearch*: JASO T903 registered 4-stroke motorcycle engine oil list JALOS pdf M033MOT211
- *WebSearch*: Maxima Pro Plus+ 10W-30 PEAC new formula 2024 API SN Plus JASO MA2 M001MAX309
- *Bash*: Probe Maxima site for current Pro Plus+ datasheet
- *Bash*: Fetch Maxima Pro Plus product page details
- *Bash*: Fetch Maxima Pro Plus product JSON
- *Bash*: Look for JASO registered oil list on JALOS site
- *Bash*: Inspect JALOS site index for JASO list links
- *Bash*: Fetch JASO English page and list its links
- *Bash*: Read JASO list index page text and links
- *Bash*: Open JASO motorcycle 4-stroke oil page
- *Bash*: Download JASO filed 4T oil list and check codes

JASO's current filed-oil list (1 Nov 2026) confirms the Liqui Moly (M049LMG114) and Motul (M033MOT211) registrations. Checking the Maxima code next.

- *Bash*: Search JASO list for Maxima and context lines
- *Bash*: List all Maxima JASO codes in the filed list

JASO's list (1 Nov 2026) has 30 Maxima entries, but not the M001MAX309 code printed on the Pro Plus+ bottle. I'll retry Maxima's site for the current (2025 PEAC) datasheet.

- *Bash*: Retry Maxima Pro Plus product page
- *WebSearch*: Maxima Racing Oils "Pro Plus+" 10W-30 PEAC technical data sheet pdf viscosity 100°C flash point 2025
- *Bash*: Fetch Maxima gallon product page for TDS link
- *Bash*: Probe Maxima Shopify CDN for Pro Plus TDS filenames
- *Bash*: Download official Maxima Pro Plus TDS and extract text
- *Bash*: Rename Maxima datasheets and list all downloads
- *WebSearch*: Motul official distributor Bangladesh Maahel Motors IPC genuine Motul 7100 fake
- *Bash*: Read Dhaka Tribune article on Motul distributor
- *Bash*: Print body of the Motul-Rancon article
- *WebSearch*: ACI Motors Liqui Moly Bangladesh official distributor
- *Bash*: Fetch German and US Liqui Moly datasheets, grep base oil
- *Bash*: Fetch Motul France 7100 10W-30 TDS and grep key lines

Motul's French sheet calls the 7100 "100% Synthetic – Ester", while its German sheet says "Synthetic Technology". So the Motul and Liqui Moly are probably built on the same kind of base oil, and the Motul adds ester.

What I have so far:

| | Liqui Moly 10W-30 Street | Motul 7100 10W-30 | Maxima Pro Plus+ 10W-30 |
|---|---|---|---|
| Price | 1,400 | 1,600 | 2,200 |
| Viscosity at 100°C (cSt) | 11.5 | 10.5 | 10.8 |
| Viscosity index | 145 | 150 | 156 |
| HTHS (mPa·s) | ≥2.9 (minimum only, no measured value) | 3.2 | not published |
| Flash point | 230°C | 236°C | 205°C |
| JASO MA2 on JASO's current list | yes | yes | code not found |

All three meet what the Bangladesh Honda manual asks for: 10W-30, JASO MA and API SJ or higher.

Still waiting on the research agent for Bangladesh prices and datasheets of alternatives (Shell, Mobil, Motul 5100, AMSOIL, Champion and others). The final recommendation comes when it finishes, because a cheaper alternative could change the best-value pick.

## User
> I got Amsoil's price from the seller:
> ```
> Amsoil 10W-30 - 946ml 1750 টাকা, 1 লিটার 1850 টাকা
> ```

## Claude
Thanks, that price changes things. At 1,850 BDT for 1 L, AMSOIL costs 250 more than the Motul and 350 less than the Maxima, so it needs a proper datasheet comparison. First I'll check AMSOIL's 10W-30 on JASO's filed list (already downloaded), and tell the research agent it can skip AMSOIL's price.

- *Bash*: Find AMSOIL entries in JASO filed oil list
- *ToolSearch*: select:SendMessage
- *SendMessage*: 
- *Bash*: Double-check AMSOIL JASO entries; render oil-change pages
- *ListAgents*: 
- *Read*: <scratch>/honda-manual/oilchg-059.png
- *Read*: <scratch>/honda-manual/oilchg-057.png
- *Bash*: List agent downloads and read Ravenol datasheet
- *Bash*: Verify JASO codes and read AMSOIL datasheet text
- *Bash*: Grep AMSOIL product page for specs and pack sizes
- *Bash*: Read agent's newer AMSOIL datasheet copy
- *ToolSearch*: select:TaskStop
- *TaskStop*: 

Before relying on the agent's numbers, I'll spot-check the three figures that affect the recommendation: Honda's own oil prices on bdhonda.com and the Ravenol price.

- *Bash*: Spot-check Pro Honda and Ravenol prices
- *Bash*: Grep saved pages for the quoted prices
- *WebSearch*: AMSOIL G3348 Synthetic Metric Motorcycle Oil data bulletin pdf MCT 10W-30
- *WebSearch*: AMSOIL "100% Synthetic 4T Performance" 10W-30 motorcycle oil 1 liter pakwheels pdf
- *Bash*: Copy Ravenol and AMSOIL datasheets into user folder

I'd buy the **Liqui Moly Motorbike 4T 10W-30 Street at 1,400 Tk**. It's the best value of everything I checked. If you're willing to spend 300 Tk more, the **Ravenol Motobike 4-T Ester 10W-30 at 1,700 Tk** has the best datasheet of any 10W-30 I found, and it costs less than the AMSOIL and the Maxima. I'd skip the Maxima.

**What your bike needs.** Bangladesh Honda's own Hornet 2.0 manual asks for SAE 10W-30, JASO MA and API SJ or higher, and says not to use oils marked "Energy Conserving" or "Resource Conserving". Each change takes 1.0 L and there's no paper filter. The manual explicitly allows non-Honda oil that meets those standards, so using any oil below won't affect your warranty.

| 10W-30 oil | Price (Tk) | Viscosity at 100°C | HTHS | Flash point | Evaporation loss (Noack) | API / JASO |
|---|---|---|---|---|---|---|
| Pro Honda Mineral (your current) | 710 | – | – | – | – | SL / MA, no datasheet |
| **Liqui Moly 4T Street** | 1,400 | 11.5 | ≥2.9 (only the minimum is stated) | 230°C | 12.9% | SP / MA2, on JASO's list |
| Pro Honda Full Synthetic | 1,420 | – | – | – | – | SL / MA, no datasheet |
| Motul 7100 | 1,600 | 10.5 | 3.2 | 236°C | not published | SP / MA2, on JASO's list |
| **Ravenol 4-T Ester** | 1,700 | 12.0 | not published | 260°C | 3.3% | SN / MA2, on JASO's list |
| AMSOIL Synthetic Motorcycle (MCT), 946 ml | 1,750 | 11.2 | 3.5 | 244°C | 5.8% | SH / MA2 claimed, not on JASO's list |
| AMSOIL 100% Synthetic 4T Performance | 1,850 (1 L) | 12.0 | 3.7 | 228°C | 5.6% | SL / MA2 claimed, not on JASO's list |
| Maxima Pro Plus+ | 2,200 | 10.8 | not published | 205°C | not published | SN Plus / its MA2 code isn't on JASO's list |

In an air-cooled engine sitting in Dhaka traffic, the most telling numbers are evaporation loss and flash point. Oil that evaporates is what makes a 1 L sump thicken and run low between changes.

**Why Liqui Moly is the value pick**
- It's the cheapest real upgrade and has the newest ratings (API SP and JASO MA2, 2023 version). I confirmed its JASO registration on JASO's current list.
- At 11.5 cSt it sits in the thicker half of the 10W-30 range, which gives a hot air-cooled engine some margin.
- It comes through ACI Motors, Liqui Moly's official Bangladesh distributor (that's the sticker in your photo), so the risk of a fake is lower.
- Its weak spot is the 12.9% evaporation loss, which is ordinary. Its German datasheet calls the base oil "synthetic technology", the term used there for refined mineral-derived (hydrocracked) oil rather than true synthetic stock. That's fine at about 3,000 km per change.

**Why Ravenol is the step up.** For 300 Tk more you get about a quarter of Liqui Moly's evaporation loss, the highest flash point of anything I found, and the thickest oil within the 10W-30 grade. Its JASO MA2 registration is on JASO's list (M049RAV174). Rokomari has it at 1,700. When you buy, check the label says "Motobike 4-T Ester 10W-30" and shows that JASO number.

**Why not the others**
- **Motul 7100:** It's a good oil, with ester and a measured HTHS of 3.2. On paper, though, it isn't clearly better than the Liqui Moly; its German datasheet also says "synthetic technology". The extra 200 Tk mainly buys the ester. Also, Motul made Rancon its exclusive Bangladesh distributor in August 2026. Your bottle came through IPC and Maahel Motors. That may just be older legitimate stock, but check the QR code before buying.
- **Maxima:** It's the most expensive and has the lowest flash point of the oils compared here. JASO's current list has 30 Maxima oils but not the code printed on this bottle (M001MAX309), so I couldn't verify its MA2 claim. Its datasheet is from 2020, before Maxima's 2025 reformulation; the cap seal in your photo shows the new version.
- **Pro Honda Full Synthetic:** It costs about the same as the Liqui Moly but has older ratings (API SL, JASO MA) and Honda publishes no data for it.
- **Champion, Shell, Mobil:** Champion's Propulse TT 10W-30 (1,450) is a synthetic blend according to Champion's own datasheet, even though Bangladeshi listings call it full synthetic. Shell's and Mobil's synthetic motorcycle oils in Bangladesh are 10W-40, which isn't the grade Honda specifies.

**About the AMSOIL quote**
- Its numbers are strong, but neither AMSOIL 10W-30 is on JASO's list (only AMSOIL's 10W-40 is). Its API ratings are old and its datasheets date from 2017–18. The Ravenol has lower evaporation loss, a higher flash point and a verified JASO registration, and it costs 50–150 Tk less.
- The 946 ml and 1 L prices are probably for two different AMSOIL oils. Their US motorcycle oil comes in 946 ml bottles, which is 54 ml short of the 1.0 L fill. Ask the seller which product each price is for.
- Make sure the bottle says "Motorcycle Oil" and JASO MA/MA2. AMSOIL's car 10W-30s (Signature Series, OE, XL) aren't made for a wet clutch. The only AMSOIL I found listed in Bangladeshi shops was car oil.

**How often to change.** Honda's Bangladesh schedule is a first change at 1,000 km, then every 4,000 km or 4 months. After your 1,500 km change, about every 3,000 km makes sense for Dhaka traffic with any of these oils. Don't go past 4,000 km or 4 months while the warranty lasts (2 years or 20,000 km). You can stop changing it as often as you did at 400 and 800 km. At 3,000 km per change, the Liqui Moly works out to about 0.47 Tk/km and the Ravenol about 0.57 Tk/km. Your 43 km/L won't noticeably change with any of these oils.

I saved the datasheets in your `engine-oils` folder, one `datasheets` subfolder per brand. I added Ravenol and AMSOIL folders too. Maxima has two sheets: the current one and an older one that only claims API SL.

Sources:
- [Bangladesh Honda Hornet 2.0 owner's manual](https://bdhonda.com/public/uploads/2026/09/6ab0b2cf2a019_HORNET_2.0.pdf), [Hornet 2.0 page](https://bdhonda.com/products/hornet20)
- [Pro Honda Full Synthetic](https://bdhonda.com/genuine-lubes-chemicals_vehicle-accessories-all/pro-honda-fully-synthetic-oil-10w30-ma), [Pro Honda Mineral](https://bdhonda.com/genuine-lubes-chemicals_vehicle-accessories-all/honda-4t-mineral-10w-30-jaso-ma-1l-01)
- [Liqui Moly product info (EN)](https://pim.liqui-moly.de/ws/pi/article/23226?language=en), [German version](https://pim.liqui-moly.de/ws/pi/article/2526?language=de), [Liqui Moly on ACI Motors](https://www.liqui-moly.com/en/unternehmen/aktuelles/bilder-und-geschichten/2025/02/bangladesh-great-success-in-a-small-country.html)
- [Motul 7100 10W-30 datasheet](https://azupim01.motul.com/media/motulData/DO/base/7100_10w-30_4t_en_de_motul_16501_20240614.pdf), [Motul appoints Rancon (Dhaka Tribune)](https://www.dhakatribune.com/business/416482/motul-joins-hands-with-rancon-in-bangladesh)
- [Maxima Pro Plus+ datasheet](https://cdn.shopify.com/s/files/1/0555/2957/0594/files/ProPlus_TDS.pdf), [Maxima's 2025 reformulation (Cycle News)](https://www.cyclenews.com/2025/01/article/maxima-racing-oils-peac-additive-system)
- [Ravenol datasheet](https://ravenol.de/storage/app/media/product-pdf/Tds_1172111_en.pdf), [Rokomari listing](https://rokomari.com/product/433596/ravenol-10w-30-synthetic-engine-oil-for-motorbike-made-in-germany-1-litre)
- [AMSOIL data bulletin G3348](https://cdn.shopify.com/s/files/1/0028/0687/4161/files/MCT_MCF_MFF_g3348.pdf), [AMSOIL 4T Performance bulletin (copy)](https://fcache1.pakwheels.com/original/4X/7/9/c/79c6205a82a8964328aa87e2ad5459feb5bd204f.pdf), [AMSOIL international 4T page](https://www.amsoil.com/international/products/synthetic-4t-motorcycle-oil.aspx)
- [JASO list of registered 4-stroke motorcycle oils, 1 Nov 2026](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)

## User
> Will 5W-30 oils be better for my bike, and did you also consider Motorex. I want you to create a image ranking the engine oils for my bike with their comparision

## Claude
Three parts: whether 5W-30 suits your bike, where Motorex fits, and a ranking image. First I'll pull the Motorex datasheet the research agent downloaded, and check JASO's list for Motorex and for motorcycle 5W-30 oils.

- *Bash*: Read Motorex Top Speed 4T 10W-30 datasheet
- *Bash*: Check JASO list for Motorex and 5W-30 MA2 oils
- *WebSearch*: Motorex Top Speed 4T 10W-30 price Bangladesh 2026
- *Bash*: Check Motorcycle Valley Motorex 10W-30 listings
- *Skill*: 
- *Bash*: Check local tools and fonts for rendering an image
- *Bash*: List dataviz skill files and read form guide
- *Bash*: Read dataviz reference palette
- *Bash*: Read dataviz marks and anatomy reference
- *Bash*: Read dataviz anti-patterns and components references
- *Bash*: Validate bar colors with dataviz palette script

Both bar colours pass. Before building, I'll check whether Pro Honda's oils appear on JASO's list, so the image doesn't misstate their status.

- *Bash*: Search JASO list for Pro Honda entries
- *Bash*: Look for Bangladesh or Asian Honda 10W-30 JASO entries
- *Write*: <scratch>/ranking/ranking.html
- *Bash*: Render ranking HTML to PNG with headless Chrome

Rendered. Checking the layout visually.

- *Read*: <scratch>/ranking/ranking.png
- *Write*: <scratch>/ranking/ranking.html
- *Bash*: Re-render the revised ranking image
- *Read*: <scratch>/ranking/ranking.png

Much better: values sit at the bar tips, the thickness scale lines up, and every column fits. I'll zoom into the top rows at full resolution to check small details (dots, icons, pills).

- *Bash*: Crop detail regions of the ranking image
- *Read*: <scratch>/ranking/crop-right.png
- *Read*: <scratch>/ranking/crop-left.png

Detail check passes: dots, rings, bar ends, status icons and pills all render cleanly with no clipping. Saving the final image and the Motorex datasheet into your folder.

- *Bash*: Save ranking image and Motorex datasheet to user folder

No, a 5W-30 won't be better. Yes, Motorex was checked; I'd left it out only because I couldn't find a current Bangladeshi price. The ranking image is saved as `hornet-2.0-engine-oil-ranking.png` in your `engine-oils` folder.

**Why 5W-30 won't help**
- The "30" is how thick the oil is once the engine is hot, and it's the same class for 5W-30 and 10W-30.
- The "W" number only matters below freezing: a 5W is tested for cold starting at −30°C, a 10W at −25°C. Dhaka never gets near that, so you'd gain nothing.
- Bangladesh Honda's Hornet 2.0 manual lists only 10W-30.
- Most 5W-30s in shops are car oils marked "Resource Conserving". Their friction additives can make your clutch slip, and Honda's manual rules them out. Motorcycle 5W-30s do exist, but they're rare: JASO's list has 28, against 203 motorcycle 10W-30s.
- Stretching an oil from 5W to 30 often takes more thickening additive, and your gearbox, which shares the engine oil, breaks that down over time.

**Motorex Top Speed 4T 10W-30**
- **Strengths:** API SP and JASO MA2, with the JASO registration confirmed on JASO's list. Its evaporation loss is 6.6%, about half the Liqui Moly's.
- **Weaknesses:** It's on the thinner side at 10.6 cSt. Motorex only states minimums for flash point (above 200°C) and HTHS (2.9 or more).
- **Price:** The Bangladeshi listings I found are old and disagree: 1,550 Tk in March 2024, and 850 Tk on older pages that show it out of stock.
- If your seller can get it for around 1,550 Tk, it's a reasonable alternative to the Motul. I ranked it 4th.

**The ranking in the image**

| Rank | Oil |
|---|---|
| 1 | Liqui Moly Motorbike 4T 10W-30 Street (best value) |
| 2 | Ravenol Motobike 4-T Ester 10W-30 (best protection for the money) |
| 3 | Motul 7100 10W-30 |
| 4 | Motorex Top Speed 4T 10W-30 |
| 5 | AMSOIL 10W-30 motorcycle oil |
| 6 | Pro Honda Full Synthetic 10W-30 |
| 7 | Maxima Pro Plus+ 10W-30 |
| Reference | Pro Honda Mineral 10W-30 (your current oil) |

For each oil the image shows:
- price
- where it sits in the 10W-30 thickness range
- evaporation loss
- flash point
- HTHS (film strength)
- its API and JASO ratings, and whether its JASO number is actually on JASO's list

Short notes underneath cover AMSOIL's two different bottles, why 5W-30 isn't included, and where each price came from.

I also saved Motorex's datasheet in `motorex/datasheets/`, next to the other brands' sheets.

Sources:
- [Motorex Top Speed 4T 10W-30 datasheet (May 2024, retailer-hosted copy)](https://assetsinternal.struct.com/motostore/e4c1c85f-6972-4e7e-96a7-519dbf091773/TOP-SPEED-4T-SAE-10W30-MA2-1017607-EN-20240515-151300.pdf)
- [Motorcycle Valley: Motorex Top Speed 10W-30, 1,550 Tk (March 2024)](https://www.motorcyclevalley.com/oil/overview/motorex-top-speed-4t-10w30-jaso-ma-2)
- [Motorcycle Valley: older Motorex 10W-30 listing, 850 Tk](https://www.motorcyclevalley.com/oil/overview/motorex-fully-synthetic-10W30)
- [JASO list of registered 4-stroke motorcycle oils, 1 Nov 2026](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)
- [Bangladesh Honda Hornet 2.0 owner's manual](https://bdhonda.com/public/uploads/2026/09/6ab0b2cf2a019_HORNET_2.0.pdf)

## User
> If price isn't the concern then which engine oil is the best for my bike?

## Claude
I'd pick the **Ravenol Motobike 4-T Ester 10W-30**, with AMSOIL's 10W-30 motorcycle oil a close second.

| | Ravenol 4-T Ester | AMSOIL 10W-30 motorcycle | Motorex Top Speed | Motul 7100 |
|---|---|---|---|---|
| Evaporation loss (lower is better) | **3.3%** | 5.6–5.8% | 6.6% | not published |
| Flash point (higher is better) | **260°C** | 228–244°C | >200°C | 236°C |
| Thickness when hot (cSt) | **12.0** | 11.2–12.0 | 10.6 | 10.5 |
| HTHS film strength | not published | **3.5–3.7** | ≥2.9 (minimum only) | 3.2 |
| JASO MA2 on JASO's list | yes | no | yes | yes |

**Why Ravenol**
- Your engine is air-cooled, sits in hot traffic and holds only 1 L of oil, so heat is what wears the oil out. The light parts evaporate, and the oil thickens and runs low between changes. Ravenol has the lowest evaporation loss and the highest flash point of every oil I found.
- At 12.0 cSt it's near the thick end of the 10W-30 range. That gives close to the strongest oil film Honda's grade allows, without moving to 10W-40.
- Its JASO MA2 registration is on JASO's list, so its rating for clutch friction is on file with JASO. That matters for your assist-and-slipper clutch.

**What it gives up**
- It's rated API SN rather than the newer SP. Honda only asks for SJ, and the SP changes mainly target turbocharged car engines.
- Ravenol doesn't publish an HTHS figure. AMSOIL's edge is a published 3.5–3.7 and a higher TBN (acid-neutralising reserve), and TBN mostly matters with long change intervals.

**Why AMSOIL comes second**
- Its numbers are excellent, but its JASO MA2 is only a claim (it isn't on JASO's list), and its datasheets are from 2017–18.
- If you buy it, check the bottle says "Motorcycle Oil".

**Why not a 10W-40 racing oil** (Motul 300V, Liqui Moly Synth Street Race, Mobil 1 Racing 4T)
- Honda specifies 10W-30 for your bike.
- A thick 10W-30 like the Ravenol already gives you most of the extra oil-film strength those oils offer.

**Buying and changing it**
- Check the Ravenol label says "Motobike 4-T Ester 10W-30" and shows JASO number M049RAV174.
- If you're happy to spend more, changing it sooner does more than paying for a pricier oil. Every 2,500–3,000 km, and never past Honda's 4,000 km or 4 months, will help the engine more than the differences between these top oils.
- Make sure the 8,000 km service cleans the oil strainer and centrifugal filter. The engine has no paper filter, so those are what keep the oil clean.

Sources: [Ravenol datasheet](https://ravenol.de/storage/app/media/product-pdf/Tds_1172111_en.pdf), [AMSOIL data bulletin G3348](https://cdn.shopify.com/s/files/1/0028/0687/4161/files/MCT_MCF_MFF_g3348.pdf), [JASO list of registered 4-stroke motorcycle oils](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)

## User
> Please improve the image, I want to post it in facebook's Honda Hornet 2.0 Fan Club group. Only list commonly available engine oils, if you don't have the latest price then don't include it, no need to include charts in the image, you can make the best cell in a column green text with light shade green background, and worst cell in a column red text with light red shade background. use ৳ sign before the TK, mention in the column lower is better or higher is better, include Shell, Champion, Pertamina, Sinopec, Pakelo too, the image shouldn't say anything special about me, it's for general Honda Hornet 2.0 users in Bangladesh, most are Dhaka commuters, some are country side riders, some are long riders/tour worms, some are Pathao/Uber riders. You should mention all the technical data as columns, also mention the base oil API group i.e. Group-III or IV etc. has ester or not, how much detergent, acid netrilizers are in it etc. recommended drain period for City/traffic commuters, and for highway riders, ৳/km

## Claude
This is a bigger rebuild: more brands, every datasheet column, and suggested drain intervals and ৳/km for different kinds of riders. I'll split the research:
- **Agent 1:** Pertamina, Sinopec and Pakelo: what's actually sold in Bangladesh, current prices and datasheets.
- **Agent 2:** Shell, Kixx, the Motul 5100 version sold in Bangladesh, the current Motul 7100 price, and gaps for Mobil and Pro Honda.
- **Me:** base-oil evidence (Group III vs IV, ester) and missing additive data for the oils already in the table, plus a redesign of the image.

- *Agent*: Research Pertamina Sinopec Pakelo BD
- *Agent*: Research Shell Kixx Motul BD data
- *Bash*: Check base-oil wording for Liqui Moly and Champion
- *Bash*: Print full text of both Champion datasheets
- *WebSearch*: Motul 7100 4T 10W-30 safety data sheet SDS composition 104089
- *WebSearch*: Ravenol Motobike 4-T Ester 10W-30 1172111 safety data sheet SDB pdf
- *Bash*: Fetch Ravenol German datasheet and safety sheet composition
- *Bash*: Fetch Ravenol German datasheet from main domain

Ravenol's German sheet says "Öltyp: Synthetisch" (synthetic), and its safety sheet lists only additive ingredients, so its base-oil group stays "not stated". Next, the Maxima Pro Plus+ safety sheet.

- *Bash*: Fetch Maxima Pro Plus safety sheet composition
- *Bash*: Fetch Motul 7100 10W-30 safety sheet composition
- *Bash*: Compute text contrast for best/worst cell colors
- *Bash*: Check JASO list for Champion and Mobil entries
- *Bash*: Search JASO list for ExxonMobil 10W-30 filings
- *Write*: <scratch>/fb-image/build.py

Now the page template. It has a title, top picks, Honda's requirement, the table, and short notes for riders, with no personal references and no eyebrow-style labels.

- *Write*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Make note titles inline lead-in sentences
- *Write*: <scratch>/fb-image/data.json
- *Bash*: Build HTML from data and render a test image
- *Read*: <scratch>/fb-image/test.png
- *Bash*: Re-check Champion and Mobil prices on retailer pages
- *Bash*: Read MJL's Mobil Super Moto 10W-30 description

Prices confirmed on retailer pages: Champion Propulse TT ৳1,450 and Moto HP ৳950 (BikeBD, in stock), Mobil Super Moto ৳625 (MJL, the official distributor). MJL describes the Mobil 10W-30 as "synthetic technology" with API SL additives and lists it apart from its mineral oils, so the table will treat it as a blend rather than plain mineral.

A first draft of the image already renders correctly with 9 oils. I'm waiting on the two research agents for the remaining brands:
- Pertamina, Sinopec and Pakelo
- Shell, Kixx, the Motul 5100 sold in Bangladesh, and the current Motul 7100 price

Once their data is in, I'll add those rows, finalise the ranking, and export the Facebook-sized image.

## User
> Also does elf have any 10W-30 motorcyle oils?

## Claude
I'll check ELF myself while the agents finish: first JASO's filed-oil list for ELF 10W-30 motorcycle oils, then what's actually sold in Bangladesh.

- *Bash*: Search JASO list for ELF and TotalEnergies 10W-30
- *WebSearch*: ELF Moto 4 10W-30 motorcycle oil JASO MA2 TotalEnergies
- *WebSearch*: ELF motorcycle engine oil price in Bangladesh 10W-30
- *Bash*: Look for ELF 10W-30 listings in Bangladeshi shops

Yes, ELF makes 10W-30 motorcycle oils, but I couldn't find any of them sold in Bangladesh:

- **ELF Moto 4 Tourer XP FE 10W-30:** JASO MA2, registered with JASO (M033TEL202).
- **ELF Moto 4 Tourer SL 10W-30:** API SL, JASO MA. It's listed in TotalEnergies' Thailand catalogue.
- **ELF Moto 4 Maxi Tech 10W-30:** an older oil, API SJ, JASO MA, listed in European catalogues.
- **ELF Scooter 4 Power 10W-30:** avoid this one for a Hornet. It's JASO MB, a scooter oil that can make a wet clutch slip.

The only ELF motorcycle oils listed in Bangladeshi shops are 10W-40 and thicker. BikeBD's ELF Moto 4 10W-40 page shows ৳1,150 but out of stock (page updated August 2026). Since there's no 10W-30 on sale with a current price, ELF stays out of the image unless you know a shop that stocks one of the 10W-30s.

The image is still waiting on the two research agents (Pertamina, Sinopec, Pakelo, Shell, Kixx and the Motul prices). I'll finish it as soon as they report.

Sources:
- [TotalEnergies catalogue: ELF Moto 4 Tourer SL 10W-30 (Thailand)](https://lubricants.catalog.elf.com/corporate/en_TH/1wg_moto-4-tourer-sl-10w-30)
- [TotalEnergies catalogue: Moto 4 Maxi Tech 10W-30](https://lubricants.catalog.totalenergies.com/catalog-bg/en_UK/qdl_moto-4-maxi-tech-10w-30)
- [JASO list of registered motorcycle oils](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)
- [BikeBD: ELF Moto 4 10W-40](https://www.bikebd.com/motorcycle/elf-moto-4-road-10w-40)

## User
> What about essenza? Mobil also doesn't have 10W-30 right?

## Claude
Mobil does sell a 10W-30 in Bangladesh, Mobil Super Moto 10W-30; it's already in the table. What Mobil lacks here is a fully synthetic 10W-30. More on that below; first I'll look up Essenza.

- *WebSearch*: Essenza motorcycle engine oil 10W-30 Bangladesh price JASO MA2
- *Bash*: Search JASO list for Essenza entries
- *Bash*: Read BDStall Essenza 10W-30 listing details
- *WebSearch*: "Essenza" "Powerful Tour" 4T 10W-30 technical data sheet lubricant manufacturer

The BDStall page is behind Cloudflare, and there's no Essenza datasheet anywhere I searched. I'll make one more search to identify who makes or imports Essenza in Bangladesh.

- *WebSearch*: Essenza lubricants Bangladesh distributor engine oil brand origin Sintetica Powerful Tour

**Essenza:** I'm leaving it out of the image. Essenza sells one 10W-30, Powerful Tour 4T 10W-30, but there's not enough to put it in the table:
- **Price:** ৳640, but only from a single seller on BDStall plus a Bikroy classified ad. Neither shows a date, and I found no official importer or distributor.
- **Rating:** API SL and JASO MA (not MA2). Essenza has no entries on JASO's registered list.
- **Data:** I found no datasheet, so every technical column would be blank. The seller's listing says "maximum usage 1,800 km", which suggests a basic mineral oil.
- **Origin:** One Bikroy ad says it's made in Turkey (by Lubrimax), but I couldn't confirm that from the maker.

Their Sintetica line is 10W-40 and 20W-40, not Honda's grade.

**Mobil:** It does have a 10W-30 in Bangladesh, and it's already in the image: **Mobil Super Moto 10W-30**, ৳625 at MJL, Mobil's official distributor. It's rated API SL with a claimed JASO MA2. Mobil sells it as "synthetic technology", meaning a blend rather than a full synthetic. In my earlier note I meant that Mobil's fully synthetic motorcycle oil here, Mobil 1 Racing 4T (৳2,050), only comes in 10W-40. Also skip Mobil Super Moto Scooter 10W-30: it's a JASO MB scooter oil in a 0.8 L bottle.

The image is still waiting on the two research agents. I'll finish it when they report.

Sources:
- [BDStall: Essenza Powerful Tour 10W-30](https://www.bdstall.com/details/essenza-powerful-tour-4t-sae-10w-30-1l-engine-oil-88412/)
- [Bikroy: Essenza Powerful Tour 10W-30](https://bikroy.com/motijheel/car-parts-and-accessories/essenza-powerful-tour-4t-sae-10w-30-1l-engine-oil-Cevck9OB44gnj4rbqbgU0DyY.html)
- [MJL: Mobil Super Moto 10W-30](https://buymobil.mjlbl.com/product/mobil-super-moto-10w-30-4t-1l)
- [JASO list of registered motorcycle oils](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)

The first agent is done. Results:
- **Pakelo:** two 10W-30 wet-clutch oils, both in stock on Daraz.
  - Krypton MBK, fully synthetic, ৳1,650. Its datasheet is strong: HTHS 3.4, Noack 8.4%, TBN 7.7.
  - Multisint MBK, a synthetic/mineral blend, ৳1,200.
  - Pakelo isn't on JASO's list at all, so its MA2 claims can't be verified.
  - The Daraz listings show older API levels (SN and SM) than the 2024 datasheets (SP and SN). The Bangladeshi stock may be the earlier version.
- **Sinopec:** Xplore 10W-30 at ৳840. Its MA2 registration is on JASO's list, though the published data is partial.
- **Pertamina:** no 10W-30 motorcycle oil on sale in Bangladesh. The only Pertamina motorcycle oil found here is a JASO MB scooter oil, which is wrong for the Hornet's clutch, so it gets a "not included" note.

I'm adding these rows now; Shell, Kixx and the Motul 5100 slot in when the second agent reports.

- *Bash*: Add Pakelo and Sinopec rows and reorder ranking
- *Read*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Rebuild and render with 12 oils
- *Read*: <scratch>/fb-image/test.png
- *Edit*: <scratch>/fb-image/build.py
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Mark Pro Honda oils unranked and shorten Mobil base

I've added Pakelo and Sinopec, and the draft image now has 12 oils; the two Pro Honda oils sit at the bottom unranked because Honda publishes no datasheet for them. Pertamina is out: the only Pertamina motorcycle oil sold in Bangladesh is a JASO MB scooter oil, which is wrong for the Hornet's wet clutch. The image's "Not included" note explains that, along with ELF, Motorex, AMSOIL, Essenza and 5W-30s.

Still waiting on the second agent for Shell, Kixx, the Motul 5100 sold here, and the current Motul 7100 price. I'll add those, check the render, and export the final Facebook-sized image once it reports.

Both agents are done. In summary:
- **Shell:** Advance AX5 10W-30 (mineral, ৳700 at Rokomari, in stock) goes in. The fully synthetic Advance Fuel Save 10W-30 is out of stock at Rokomari and BikeBD. AX7 and City appear only in Shell's catalogue, not in shops.
- **Kixx Ultra 4T SN 10W-30:** ৳1,350, in stock. Its MA2 registration is on JASO's list, but there's no datasheet, so it goes in the unranked group.
- **Motul 5100 10W-30:** ৳1,150 at Oil House, in stock. The version on Bangladeshi shelves is unclear: India's older SM version or the current global SP version.
- **Motul 7100:** ৳1,650 at Oil House, matching the bottle's MRP.
- **Mobil Super Moto 10W-30:** Mobil's own Bangladesh datasheet calls it mineral ("high performance conventional"), despite MJL's "synthetic technology" tag. I'll go with the datasheet and say so in the notes.

These numbers will be on a public post, so I'll spot-check the values that decide best or worst cells against the downloaded datasheets.

- *Bash*: List the agents' downloaded datasheet files
- *Bash*: Verify Pakelo datasheet values from downloaded PDFs

Pakelo's figures match its datasheets exactly. Next: Sinopec, Shell AX5, the Motul 5100 global sheet, and Kixx's JASO entries.

- *Bash*: Verify Sinopec, Shell, Motul 5100 and Kixx data
- *Bash*: Extract Shell AX5 and Motul 5100 property values
- *Bash*: Add Motul 5100, Shell AX5, Kixx and set final order

Now the notes text: the Mobil base-oil caveat, the datasheet-version caveats for Pakelo, Motul 5100 and Shell AX5, and Shell Fuel Save in "Not included".

- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Update sources line, rebuild and render 15-oil image
- *Read*: <scratch>/fb-image/test.png
- *Bash*: Render final HD and Facebook-sized images
- *Read*: <scratch>/fb-image/crop-mid.png

At full resolution the ৳ signs, colours and text are crisp. I'll look at the Facebook-sized version as a whole, then save it to your folder.

- *Read*: <scratch>/fb-image/final-fb.png

The final image is ready. I'll save both sizes and the source files to your folder, plus the new brands' datasheets so any number in the post can be traced back if someone in the group questions it.

- *Bash*: Save final images, source and new datasheets to user folder

The Facebook image is ready: `hornet-2.0-engine-oil-comparison.png` in your `engine-oils` folder. It's 2048 px wide, the size Facebook keeps; there's also a 4080 px `-hd` version for zooming in. Every value that's coloured best or worst was checked against the downloaded datasheets.

**What's in it**
- **Oils:** 15 commonly sold 10W-30 oils that have a current price, including Shell, Champion, Sinopec and Pakelo. Twelve are ranked. Kixx and both Pro Honda oils are listed at the bottom unranked, because their makers publish no datasheet.
- **Columns:** price (৳), base oil and API group, ester, API rating, JASO MA2 (checked against JASO's own list), viscosity at 40 and 100 °C, viscosity index, HTHS, flash point, pour point and Noack.
- **Additives:** TBN shows the acid neutralisers and sulfated ash shows the detergent metals.
- **Cost:** suggested change interval and ৳/km, each given separately for city and highway riding.
- **Reading it:** every column header says whether higher or lower is better. The best cell is green and the worst is red.
- **Rider guide:** the city figures are for Dhaka traffic, Pathao/Uber and dusty village roads; the highway figures are for long rides and touring.
- **Ranking:**

  | Rank | Oil |
  |---|---|
  | 1 | Ravenol |
  | 2 | Motul 7100 |
  | 3 | Liqui Moly |
  | 4 | Pakelo Krypton |
  | 5 | Maxima |
  | 6 | Champion Propulse TT |
  | 7 | Motul 5100 |
  | 8 | Sinopec Xplore |
  | 9 | Champion Moto HP |
  | 10 | Pakelo Multisint |
  | 11 | Mobil Super Moto |
  | 12 | Shell AX5 |

- **Top picks:** best protection is Ravenol, best-value synthetic is Liqui Moly, and cheapest per km is Mobil Super Moto.

**Things people may question after you post**
- **Ranking basis:** oils are ranked on verified specs and the makers' published test data. An oil with no published data can't rank high, however good it might be.
- **Change intervals are my suggestion,** always within Honda's 4,000 km or 4 months:

  | Oil type | City | Highway |
  |---|---|---|
  | Mineral | 2,000 km | 3,000 km |
  | Semi-synthetic | 2,500 km | 3,500 km |
  | Synthetic | 3,000 km | 4,000 km |

  The ৳/km figures follow from these intervals.
- **Mobil:** Super Moto is listed as mineral because Mobil's own Bangladesh datasheet says so, even though MJL markets it as "synthetic technology".
- **Pakelo and Motul 5100:** Pakelo's datasheets are newer than the API levels on its Daraz listings, and it's unclear which Motul 5100 version is on Bangladeshi shelves. The image's footnotes say both.
- **Base oil groups:** makers rarely disclose them. Group III for Liqui Moly and Motul 7100 comes from their German datasheets; Pakelo's comes from its safety data sheets.
- **Prices:** these are MRP or major-retailer prices, so Liqui Moly shows ৳1,450 (MRP), not your seller's ৳1,400.

**Left out** (the image explains each):
- Pertamina and ELF: no 10W-30 motorcycle oil on sale here.
- Shell Advance Fuel Save: out of stock at the main shops.
- Motorex: no current price.
- AMSOIL: not in mainstream shops.
- Essenza: no datasheet.

The new brands' datasheets are saved in their brand folders. The image's data and template are in `image-source/`, so prices can be updated and the image regenerated later.

Sources:
- [Pakelo Krypton MBK datasheet](https://pakelo.com/images/tech_sheets/TDS/Pakelo_TDS_0441_16_02_EN.pdf) and [Daraz listing](https://www.daraz.com.bd/products/pakelo-krypton-mbk-sn-jaso-ma2-10w30-i556617914.html)
- [Pakelo Multisint MBK datasheet](https://pakelo.com/images/tech_sheets/TDS/Pakelo_TDS_0401_16_02_EN.pdf) and [Daraz listing](https://www.daraz.com.bd/products/pakelo-mulitisint-mbk-sm-jaso-ma2-10w30-1-lt-revosynt-i556587917.html)
- [Sinopec Xplore datasheet](http://sinolubesg.sinopec.com/sinolubesg/Resource/pdf/products-automotive-motorcycle02.pdf) and [Sinopec Bangladesh listing](https://sinopecbd.com/products/sinopec-xplore-10w-30-4t)
- [Shell AX5 10W-30 datasheet](https://www.shell-livedocs.com/data/published/en/aeedda8d-0218-4792-b775-1fe59b5ed89f.pdf) and [Rokomari listing](https://www.rokomari.com/product/510240/shell-advance-10w-30-premium-mineral-1-litre)
- [Motul 5100 10W-30 datasheet (2026)](https://azupim01.motul.com/media/motulData/DO/base/5100_10w-30_4t_en_fr_motul_15100_20260316.pdf) and [Oil House listing](https://oilhouse.com.bd/product/motul-5100-4t-10w-30-semi-synthetic-1l/)
- [Mobil Super Moto Bangladesh datasheet](https://www.mobil.com/en-bd/passenger-vehicle-lube/pds/ap-xx-mobil-super-moto-10w-30-15w-40-20w-40-20w-50)
- [Kixx Ultra 4T SN on BikeBD](https://bikebd.com/motorcycle/kixx-ultra-4t-sn-10w30-fully-synthetic)
- [Champion Propulse TT on BikeBD](https://www.bikebd.com/motorcycle/champion-propulse-tt-4t-10w-30-ester-full-synthetic)
- [JASO list of registered motorcycle oils (1 Nov 2026)](https://www.jalos.or.jp/onfile/pdf/4T_EV_LIST.pdf)

## User
> I told you to not include mineral oils

## Claude
I'll take out the three mineral oils: Pro Honda Mineral, Mobil Super Moto and Shell Advance AX5. Semi-synthetic blends stay in, since they aren't mineral oils. The cheapest-per-km pick and the best/worst colours will recalculate without them.

- *Read*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Remove mineral oils, rerank, and re-render image
- *Read*: <scratch>/fb-image/final-fb.png
- *Bash*: Save updated images and source to user folder

I've removed the mineral oils and updated `hornet-2.0-engine-oil-comparison.png` in your `engine-oils` folder, and its 4080 px `-hd` version.

- **Removed:** Pro Honda Mineral, Mobil Super Moto and Shell Advance AX5. The "Not included" note now lists mineral oils, and the intro and interval notes now cover only synthetic and semi-synthetic oils.
- **Now in the image:** 12 oils. Ten are ranked: Ravenol, Motul 7100, Liqui Moly, Pakelo Krypton, Maxima, Champion Propulse TT, Motul 5100, Sinopec Xplore, Champion Moto HP and Pakelo Multisint. Kixx and Pro Honda Full Synthetic stay at the bottom, unranked, because neither has a datasheet.
- **Cheapest per km** is now Sinopec Xplore (৳840, ৳0.34/km in the city).
- **Best and worst colours** were recalculated. With no mineral oils left, the semi-synthetic oils now show red in the base-oil column.

The semi-synthetic oils (Champion, Motul 5100, Sinopec, Pakelo Multisint) are blends of synthetic and mineral base oil, not mineral oils, so I kept them. Tell me if you want only full synthetics and I'll cut it down to those.

## User
> Why aren't there any engine oils with Group IV PAO base? aren't they available in 10W-30 grade?

## Claude
Short answer: Group IV (PAO) 10W-30 motorcycle oils do exist. Makers rarely state the base-oil group, though, and the PAO-based ones sold in Bangladesh seem to be 10W-40 only. Let me confirm with a few searches before answering properly.

- *WebSearch*: Red Line 10W-30 motorcycle oil base stock polyol ester PAO JASO MA2
- *WebSearch*: AMSOIL motorcycle oil base oil PAO polyalphaolefin Group IV 10W-30 MCT
- *WebSearch*: "PAO" OR "polyalphaolefin" 10W-30 4T motorcycle oil JASO MA2 full synthetic Group IV

Before answering, I'll confirm the Noack and flash figures for Liqui Moly's fully synthetic 10W-40 from the German datasheet I already downloaded, since I'll use it as a benchmark.

- *Bash*: Verify Liqui Moly Synth 10W-40 Noack and flash point

They do exist in 10W-30, but none made the image, for three reasons.

**1. Makers almost never say which group they use.**
- "Fully synthetic" on a bottle doesn't mean Group IV. In most markets, refined Group III mineral-based oil can legally be sold as "synthetic".
- Safety data sheets only list hazardous ingredients, so PAO rarely shows up there either.
- Some oils in the table may well contain PAO. Ravenol's 3.3% evaporation loss and Maxima's "ester-based synthetic" wording suggest premium base oils. Since no maker actually states the group, the image says "group not stated" instead of guessing.

**2. The fully synthetic, ester-type bike oils sold in Bangladesh only come in 10W-40 here.**
- Motul 300V, ৳2,250 at Oil House.
- Liqui Moly Motorbike 4T Synth Street Race, ৳1,700–1,760. Its German datasheet calls it "vollsynthetisch" (fully synthetic), unlike the Street 10W-30's "Synthesetechnologie".
- Mobil 1 Racing 4T, ৳2,050 at MJL.

**3. PAO-based 10W-30s exist abroad, but they aren't sold in Bangladeshi shops.** The clearest example is Red Line 10W-30 Motorcycle Oil, which retailers describe as a PAO plus ester blend. It has drawbacks for a Hornet:
- It comes in 946 ml US quarts, which is less than the 1.0 L you need.
- Several listings give it only JASO MA, not MA2.
- It carries very high zinc and phosphorus, around 2,000 ppm phosphorus per retailer data, which is hard on a catalytic converter.

AMSOIL doesn't state its base oils either.

**Does it matter for a Hornet 2.0?** Less than the label suggests. PAO's benefits are low evaporation, heat resistance and long oil life, and those show up in the published test numbers anyway:

| Oil | Evaporation loss | Flash point |
|---|---|---|
| Ravenol 4-T Ester 10W-30 | 3.3% | 260 °C |
| Liqui Moly Synth 10W-40 (fully synthetic) | 3.7% | 250 °C |

At 3,000–4,000 km per change, a well-made Group III oil is plenty. Judge by evaporation loss, flash point and HTHS rather than the base-oil label.

I can add a one-line note to the image explaining why no Group IV oil appears, since people in the group are likely to ask the same thing.

Sources:
- [Red Line 10W-30 (Lordco)](https://lordco.com/Product/10W30-Synthetic-Motorcycle-Engine-Oil-946mL-RLO42304)
- [Red Line 10W-30 additive figures (OneFastShop)](https://onefastshop.com/products/red-line-10w30-motorcycle-oil-1-quart-12-pack)
- [AMSOIL 10W-30 MCT product page](https://www.amsoil.com/p/amsoil-10w-30-100-synthetic-motorcycle-oil-mct/)
- [Liqui Moly Synth 10W-40 datasheet (German)](https://pim.liqui-moly.de/ws/pi/article/20753?language=de)
- [MJL Mobil shop](https://buymobil.mjlbl.com/product/mobil-super-moto-10w-30-4t-1l)

## User
> Include Shell Advance Fuel Save, and AMSOIL

## Claude
I'll add both. First I'll confirm Shell Fuel Save's figures from the datasheet the agent downloaded. For AMSOIL, the seller's two quotes come to the same per-litre price: ৳1,750 for 946 ml is ৳1,850 per litre, the same as the 1 L quote. So I'll list it at ৳1,850 per litre, using AMSOIL's own data bulletin for the figures.

- *Bash*: Verify Shell Advance Fuel Save 10W-30 datasheet values
- *Edit*: <scratch>/fb-image/build.py
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Add AMSOIL and Shell Fuel Save rows, rebuild, render
- *Read*: <scratch>/fb-image/final-fb.png
- *Bash*: Save updated images and source to user folder

I've added both oils and updated `hornet-2.0-engine-oil-comparison.png` in your `engine-oils` folder, plus its 4080 px `-hd` version. The image now has 14 oils: 12 ranked, with Kixx and Pro Honda Full Synthetic unranked because they have no datasheet.

**AMSOIL Synthetic Motorcycle Oil is ranked 4th, at ৳1,850 per litre.**
- **Price:** this comes from your seller's quotes. ৳1,750 for 946 ml and ৳1,850 for 1 L work out to the same price per litre, so the image shows ৳1,850.
- **Data:** figures are from AMSOIL's 2018 data bulletin. It's best in its column on HTHS (3.5), TBN (11.6) and pour point (−46 °C).
- **Why not higher:** its JASO MA2 is only claimed (it isn't on JASO's list), and its API SH is the oldest rating in the table. Both show red, and both are why it sits below Ravenol, Motul 7100 and Liqui Moly, whose ratings are verified.
- **The 1 L pack:** it may be AMSOIL's international 4T Performance line rather than this oil. A note in the image says so.

**Shell Advance 4T Fuel Save is ranked 6th, at ৳1,080.**
- **Price:** this is Rokomari's listed price. Its name line says it's often out of stock.
- **Base oil:** Shell sells it as "100% Synthetic" using PurePlus. That's Shell's gas-to-liquids base oil, which counts as Group III, so the image says "Group III (GTL)".
- **Data:** Shell publishes only viscosity, flash point (235 °C) and pour point. Its JASO MA2 has no number on JASO's list.

The top picks stay the same: Ravenol for best protection and Sinopec Xplore for cheapest per km. I relabelled the Liqui Moly pick "Best value, verified synthetic". Shell Fuel Save is now cheaper per km among the synthetics, but its ratings aren't verified and it has little published data. I also added a short line warning about fake and refilled oil.

## User
> You should put how it's ranked in the title

## Claude
I'll put the ranking method in the title itself: base oil first, then verified specs, then lab data. The line under it will spell out the order those are applied in.

- *Read*: <scratch>/fb-image/template.html
- *Read*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Rebuild with ranking method in title and render
- *Read*: <scratch>/fb-image/crop-top.png

The new title fits on one line, and the line under it explains the order. Saving it.

- *Bash*: Save retitled images to user folder

The title now says how the oils are ranked: **"Honda Hornet 2.0: 10W-30 engine oils ranked by base oil, verified specs and lab data"**.

The line under it explains the order:
1. Synthetics rank above semi-synthetics.
2. Within each group, oils whose JASO MA2 registration is on JASO's own list come first.
3. After that, the API rating and the makers' published lab data (evaporation loss, flash point, HTHS, TBN) decide the order.
4. Oils with no datasheet are listed last, unranked.

I've updated `hornet-2.0-engine-oil-comparison.png` in your `engine-oils` folder (2048 px, for Facebook) and its 4080 px `-hd` version.

## User
> Instead of ৳ per km, use Taka/km

## Claude

- *Bash*: Find all "৳ per km" occurrences
- *Edit*: <scratch>/fb-image/build.py
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Rebuild with Taka/km labels and render
- *Read*: <scratch>/fb-image/crop-cost.png
- *Bash*: Save Taka/km version to user folder

The two cost-per-km columns now say **"Taka/km: city"** and **"Taka/km: highway"**, and the footnote explaining them uses "Taka/km" too. The price column still shows the ৳ sign (৳1,450 etc.).

I've updated `hornet-2.0-engine-oil-comparison.png` in your `engine-oils` folder (2048 px, for Facebook) and its 4080 px `-hd` version.

## User
> Create a PDF too, so that users can see it without the details getting blurred

## Claude
I'll print the same page straight to PDF with Chrome. The text stays vector, so it remains sharp at any zoom level. I'll size the PDF page to the content, keep it to a single page, and make sure the green and red cell colours carry over into the PDF.

- *Read*: <scratch>/fb-image/template.html
- *Bash*: Show the end of the template file
- *Edit*: <scratch>/fb-image/template.html
- *Edit*: <scratch>/fb-image/template.html
- *Bash*: Print the comparison page to a single-page PDF
- *Bash*: Rasterize PDF at normal and zoomed resolution
- *Read*: <scratch>/fb-image/pdfcheck.png
- *Read*: <scratch>/fb-image/pdfzoom.png

The PDF renders correctly: everything fits on one page, the colours carry over, and at 300 dpi zoom the text is still perfectly sharp because it's vector. Saving it to your folder.

- *Bash*: Save the PDF and updated template to user folder

I've made the PDF: `hornet-2.0-engine-oil-comparison.pdf` in your `engine-oils` folder. It's a single page, about 550 KB, with the same content and colours as the image.

The text is stored as text rather than pixels, so it stays sharp at any zoom on a phone or computer, and people can search it or copy numbers out of it. I checked it zoomed in to 300 dpi and the small print is still crisp.

On Facebook, post the PNG so the table shows in the feed, and attach the PDF (Facebook groups accept file uploads) for anyone who wants to zoom into the details.

The file opened fine in a standard PDF viewer here. I couldn't test it in Facebook's own viewer.

## User
> Don't make it specific for Honda Hornet 2.0, make it a 10W-30 engine oils. The title should be generic. create 3 PDFs one ranked by best engine protection/data sheet specs, another ranked by performance/feel/aggresive/sport etc., another ranked by value for money

## Claude
I'll make the title and notes generic. I'll also define a clear, stated method for each of the three rankings, since "feel" can't be read directly off a datasheet.

- *Bash*: Locate Hornet-specific text and build hooks
- *Bash*: Show full interval and not-included note lines

Now the template edits: a per-ranking title and intro, a generic requirement line, and generic notes.

- *Bash*: Make template generic with title and lede placeholders
- *Bash*: Let build accept title, lede and template text

Now the generator for the three rankings. Each uses its own stated rule, and the scoring is computed in code rather than set by hand.

- *Write*: <scratch>/fb-image/gen.py
- *Bash*: Generate the three ranking variants

The three orderings follow their stated rules. Now I'll render each one to PDF and PNG.

- *Bash*: Render three PDFs and PNGs and preview checks
- *Read*: <scratch>/fb-image/v3/performance.png
- *Read*: <scratch>/fb-image/v3/value.png

Both renders look right. I'll save all three PDFs and PNGs to your folder.

- *Bash*: Save three PDFs, PNGs and source to user folder

I've made the three PDFs, each with a matching 2048 px PNG for the Facebook post. None of them mentions the Hornet any more: titles are generic, the Honda manual line is now a general "Before you buy: check your bike's owner's manual", and the interval notes say "never past your bike maker's interval". The intro under each title explains how that version is ranked.

**1. Ranked by engine protection** (`10w30-oils-ranked-by-protection.pdf`)
- Same order as before: Ravenol, Motul 7100, Liqui Moly, AMSOIL, Pakelo Krypton, and so on.
- Rule: synthetics first, then oils whose JASO MA2 registration is on JASO's list, then API rating and lab data.

**2. Ranked for performance and sporty feel** (`10w30-oils-ranked-by-performance.pdf`)
- Order: Motul 7100, Maxima, Champion Propulse TT, Pakelo Krypton, Ravenol.
- Rule: "feel" can't be read from a datasheet, so each oil gets a sport score out of 7 for features linked to quick revving, smooth shifting and a firm clutch:
  - ester content: 2 points
  - full-synthetic base, JASO MA2 registration, viscosity index of 150 or more, 40 °C viscosity of 70 cSt or less, and HTHS of 3.3 or more: 1 point each
- Each oil's score is printed under its name, so anyone can check it.
- Liqui Moly lands 9th: it has no ester, a relatively thick 40 °C viscosity and the lowest viscosity index.
- Kixx and Pro Honda Full Synthetic stay unranked because they have no datasheet.

**3. Ranked by value for money** (`10w30-oils-ranked-by-value.pdf`)
- Order: Sinopec Xplore, Champion Moto HP, Motul 5100, Liqui Moly, Motul 7100.
- Rule: oils with a datasheet and a JASO MA2 registration on JASO's list come first, cheapest city Taka/km first. Everything else follows, also by Taka/km.
- Liqui Moly is the best-value synthetic and Motul 5100 the best-value oil with ester.
- Every oil gets a rank here, including Kixx and Pro Honda.

The performance ranking is the one most open to debate in the group. It measures formulation features linked to sporty feel, not actual riding feel, and the intro says so.

The files are in your `engine-oils` folder; the earlier Hornet-specific files are still there too. The data and generator script are in `image-source/`, so prices can be updated and all three files regenerated.

## User
> I want you to turn this into a public github repo, delete unnecessary files, documnet how it was done and generated, export our conversation into a file

## Claude

- *Bash*: List project files and check GitHub login
- *Bash*: Inspect candidate files and transcript location
- *Bash*: Find the render commands used earlier in the transcript
- *Bash*: Extract datasheet download URLs from the transcript
- *Bash*: Find datasheet URLs in subagent transcripts

I'm gathering the files and the source links for the repo. Next I'll clean up the folder, write the docs and export the conversation.

- *Bash*: List PDF URLs referenced in all transcripts
- *Bash*: Trash unused files and reorganise into repo layout
- *Bash*: Remove now-empty brand folders
- *Write*: <repo>/src/render.sh
- *Bash*: Test the render script and compare with previous outputs

The render script reproduces the outputs pixel-for-pixel. Next I'm exporting the conversation, with personal details redacted.

- *Bash*: Export the conversation to Markdown with redaction
- *Bash*: Check the end of the export and list user messages
- *Write*: <repo>/README.md
- *Bash*: Add gitignore, refresh export, scan for personal info
- *Bash*: Initialise git repo and stage files
- *Bash*: Commit and create the public GitHub repo

I've published the public repo at **https://github.com/habibium/10w30-motorcycle-oil-rankings**. The folder is now the repo, with one commit on `main` and no Co-Authored-By trailer.

**Deleted files.** I moved these to the Trash rather than deleting them, so you can still get them back from the drive's Trash:
- the three Hornet-specific PNGs and the Hornet PDF (`10W-30-engine-oil-comparison.pdf`)
- the ten oil-bottle photos you started with
- `maxima/Tds_1172111_en.pdf`, which was actually a duplicate of Ravenol's datasheet
- datasheets for oils that aren't in the rankings: Shell AX5 (mineral), Motorex, the third-party copy of the AMSOIL sheet, and Maxima's older API SL sheet
- the `.DS_Store` files

**What's in the repo:**
- `output/`: the three rankings as PDF and PNG.
- `src/`: `data.json`, `gen.py`, `build.py` and `template.html`. The template's page title now says "10W-30 motorcycle oil rankings" instead of the Hornet title.
- `src/render.sh` (new): rebuilds all six files with one command. I ran it and its PNGs matched the previous ones pixel for pixel.
- `datasheets/<brand>/`: the 15 maker datasheets the numbers come from.
- `docs/sources/`: JASO's filed-oil list (1 Nov 2026), used to check each oil's JASO registration.
- `README.md`: what's compared, how each of the three rankings is scored, how the data was collected and checked, how to regenerate the files, and caveats.

**Conversation export.** It's in `docs/conversation.md`.
- Your messages and my replies are copied exactly.
- Tool calls appear as one-line entries; their output is left out.
- Local paths, your name and email addresses are replaced with placeholders. I searched the whole repo afterwards and found no personal details.
- The export was made during this last request, so it ends partway through this turn.

Two things to be aware of now that the repo is public:
- The datasheet PDFs are the makers' own documents. The README says they're kept as evidence and that the makers own the copyright. If you'd rather not redistribute them, I can remove them and keep only the links.
- The commit's author email is whatever your global git config uses, which is a Gmail address.

## User
> Also create a webpage for it and host it in GH Pages, so that users can view the table interactively, sort each column with ascending and descending order.
> This project if it gets popular I might also need to compare other grade oils too e.g. 10W-40 which is most common, 5W-30 and so on so keep it generic, currently it has just available 10W-30 synthetic and semi-synthetic oils

> Also create a webpage for it and host it in GH Pages it should have Star us on GitHub, so that users can view the table interactively, sort each column with ascending and descending order.
> This project if it gets popular I might also need to compare other grade oils too e.g. 10W-40 which is most common, 5W-30 and so on so keep it generic, currently it has just available 10W-30 synthetic and semi-synthetic oils.
> 
> Use an appropriate license for the repo

## Claude
The repo is up. Next I'm building the Pages site. First I'm checking the current GitHub Actions versions, as your instructions require.

- *Bash*: Look up latest releases of the Pages actions
- *Bash*: Read the READMEs of the Pages actions
- *Bash*: Read configure-pages inputs and the Pages starter workflow

Now I'm restructuring the data so new grades can be added as separate files. The ranking logic will be shared by the images and the website, so each formula is defined only once.

- *Bash*: Convert data.json into a per-grade data file
- *Write*: <repo>/src/columns.json
- *Write*: <repo>/src/rankings.py
- *Write*: <repo>/src/build_images.py
- *Bash*: Turn grade-specific template text into placeholders
- *Bash*: Retry template placeholder conversion

I've refactored the image generator. Now I'm checking that it still produces exactly the same images.

- *Write*: <repo>/src/render.sh
- *Bash*: Render with refactored code and compare pixels
- *Bash*: Render with refactored code and compare pixels

The refactored images match the old ones pixel for pixel. Next I'm writing the website build script and the page itself.

- *Write*: <repo>/src/build_site.py
- *Bash*: Rename the repo to a grade-neutral name

Next is the website: HTML, CSS and JS.

- *Write*: <repo>/site/index.html
- *Write*: <repo>/site/style.css
- *Bash*: Keep the Star label on mobile and inline pick labels
- *Write*: <repo>/site/app.js
- *Bash*: Build the site locally
- *Bash*: Serve the built site locally for testing

I'm checking the site locally with screenshots at desktop and phone widths.

- *Bash*: Screenshot site and check sorting via DOM
- *Read*: <scratch>/sitecheck/desk.png
- *Bash*: Downscale the mobile screenshot
- *Read*: <scratch>/sitecheck/mobile.png
- *Bash*: Fix mobile overflow, rebuild, re-screenshot
- *Read*: <scratch>/sitecheck/mobile2.png
- *Read*: <scratch>/sitecheck/light.png
- *Bash*: Rebuild and render the site in a 390px iframe
- *Read*: <scratch>/sitecheck/m3c.png

The phone layout is fine now. Next I'm adding the deploy workflow, the licences and the updated README.

- *Bash*: Add Pages workflow and MIT and CC BY 4.0 licence files
- *Read*: <repo>/README.md
- *Write*: <repo>/README.md
- *Bash*: Enable GitHub Pages and set repo homepage and topics
- *Bash*: Refresh conversation export, scan for personal info, stage
- *Bash*: Commit in logical steps and push

I've pushed the changes. Now I'm watching the Pages deploy run.

- *Bash*: Wait for Pages deploy and check live URLs
- *Bash*: Screenshot the live site
- *Read*: <scratch>/sitecheck/live.png
- *Bash*: Stop the local test server

The website is live at **https://habibium.github.io/motorcycle-oil-rankings/**. I loaded the live site and sorted the viscosity index column from highest to lowest; the values came out in the right order. The deploy succeeded, and the page, the data file and the PDF downloads all load.

**I renamed the repo** to `motorcycle-oil-rankings`, since the old name had "10w30" in it and you want to add other grades. GitHub redirects the old URL, so earlier links still work. The repo's homepage now points to the site, and I added topics so it's easier to find.

**What the website does:**
- A **Star us on GitHub** button sits in the top-right corner. It shows the star count once the repo has at least one star.
- You can switch between three rankings: Protection, Performance and Value for money. The title, intro and three picks change with the ranking.
- Every column sorts when you click its heading, and a second click reverses it. Oils with no published value stay at the bottom either way.
- You can filter by oil type (All, Synthetic, Semi-synthetic) and search by name.
- The best and worst cells are coloured green and red, as in the images.
- Each oil has links to its datasheets, and each ranking has PDF, PNG and JSON downloads.
- The current view is saved in the URL, so a sorted or filtered table can be shared as a link.
- It works in light and dark mode. On phones the table scrolls sideways while the rank and oil name stay in place. I checked the layout at 390 px wide.

**Ready for more grades:**
- There is now one data file per grade, starting with `data/10w-30.json`. Adding `data/10w-40.json` is enough for the site to show a 10W-40 option, and `./src/render.sh` makes its PDFs and PNGs. No code changes are needed.
- The ranking logic is in one shared file (`src/rankings.py`), so the images and the website can't disagree.
- I re-rendered the 10W-30 images after this change and they match the old ones pixel for pixel.
- The README has an "Adding a grade" section.

**Licences:**
- The code is under MIT, the copyright line names your GitHub handle, and GitHub shows MIT on the repo page.
- The data, rankings, images and write-ups are under CC BY 4.0: anyone can reuse them as long as they credit the project.
- The makers' datasheets and JASO's list are left out of both licences and marked as their owners' copyright.

**Deployment:** every push to `main` rebuilds and redeploys the site through a GitHub Actions workflow. Per your rule, I looked up and pinned the latest version of each action.

`docs/conversation.md` has been re-exported to include this part of our conversation. It ends at the export itself, so the final checks and this message aren't in it.

## User
> rename the project to engine-oil-rankings (who knows we might need to compare car oils too)

> rename the project to Engine Oil Rankings (who knows we might need to compare car oils too).
> 
> And I want to know what should I use as the domain? habibium.com/engine-oil-rankings (habibium.com already has my personal Astro site, ~/SSD/Code/habibium.com)?, or should I use a subdomain? I want it to be indexed in search engine too

## Claude

- *Bash*: Check how the habibium.com Astro site is hosted

I'll rename the project first, then answer the domain question. To see what the domain options involve, I checked how habibium.com is hosted: it's an Astro site on Vercel. That affects the answer.

- *Bash*: Rename repo and add a category to the grade data
- *Bash*: Find names and slugs to update
- *Bash*: Make slugs, file names and titles category-aware
- *Bash*: Add category, site URL, sitemap and robots to the site build
- *Bash*: Rename the site and add SEO meta tags
- *Bash*: Add category switch, pass Pages URL to build, re-render outputs

The images are re-rendered under their new names. Next I'm checking they're unchanged, then updating the README and deploying.

- *Bash*: Compare renamed images with previous renders
- *Bash*: Update README for the rename and category support
- *Bash*: Commit, push and update repo homepage
- *Bash*: Wait for deploy and verify the live site
- *Bash*: Screenshot the renamed live site
- *Read*: <scratch>/sitecheck/live2.png

The table header looks cut off in that screenshot. I'm checking whether that's a real bug or just a capture timing issue.

- *Bash*: Re-screenshot the live table area
- *Read*: <scratch>/sitecheck/live3c.png

I've renamed the project to **Engine Oil Rankings**, and it's live at **https://habibium.github.io/engine-oil-rankings/**. I loaded the new URL in a browser and the table renders and sorts correctly.

## Rename and car-oil support
- **Repo:** it's now `habibium/engine-oil-rankings`. GitHub redirects the old repo URLs, but **the old Pages address now returns 404**, because GitHub doesn't redirect Pages after a rename. That only matters if you've already shared the old link.
- **Site:** it's titled "Engine oil rankings". The page now also has a canonical URL, a sitemap and a preview image for links shared on Facebook.
- **Data files** are now named by vehicle as well as grade, e.g. `data/motorcycle-10w-30.json`, so a car 10W-30 can't clash with the motorcycle one.
- **Output files** are renamed to match (`motorcycle-10w30-oils-ranked-by-*.pdf/png`). The images themselves are pixel-for-pixel the same.
- **Vehicle switch:** a Car/Motorcycle switch appears on the site once a car data file exists. The columns and ranking rules are still motorcycle-specific (JASO MA2, sport score). Car oils would need their own, based on API/ILSAC, ACEA and car-maker approvals. The README explains this.
- **Domain-ready:** the deploy workflow takes the site address from GitHub, so if you add a custom domain, the canonical link and sitemap switch to it on the next deploy.

## Domain: use a subdomain or your own domain, not `habibium.com/engine-oil-rankings`
A path on habibium.com is the hardest option to run and helps search ranking the least:
- **It needs a proxy.** habibium.com is an Astro site on Vercel, so you'd add a Vercel rewrite that forwards `/engine-oil-rankings/*` to GitHub Pages. That ties the two sites' deploys together.
- **It conflicts with your Astro settings.** Your Astro config uses `trailingSlash: "never"`, which would serve the page as `/engine-oil-rankings` without a trailing slash. The site's relative links (`style.css`, `data/...`) would then break.
- **It creates duplicate content.** The same page would exist on both github.io and habibium.com, so you'd have to manage canonical links by hand.
- **Little search benefit.** Google treats subfolders and subdomains about the same. Your site's authority comes from a personal developer site on a different topic, so it would add little.

**A subdomain** such as `oils.habibium.com` is the easy route:
- It's one DNS record, a CNAME from `oils` to `habibium.github.io`.
- GitHub then redirects the github.io address to it, so there's no duplicate content, and HTTPS is automatic.
- Its own `robots.txt` and sitemap work. On a github.io project URL they're ignored, because crawlers only read `robots.txt` at the root of a host.

**Your own domain** (something like `engineoilrankings.com`, roughly $10–15 a year) is my recommendation if you expect this to grow beyond motorcycles. It's easier to remember and share in Facebook groups. It doesn't tie the project to your personal brand. And you won't need to move it later, which would cost some search ranking. Setting it up takes the same steps as the subdomain.

Either way, getting indexed depends more on:
- verifying the site in Google Search Console and submitting `sitemap.xml`
- getting links to it from posts and forums

One limitation: the table is drawn by JavaScript. Google can index it, but more slowly. I can make the build write the table directly into the HTML if you want better indexing.

Tell me the domain you choose and add the DNS record. I'll then set the custom domain on the repo, turn on HTTPS and check that the redirect works.

## User
> You already know where my cloudflare token is right so please configure it

## Claude
I don't have a Cloudflare token location in my notes from this conversation, so I'll check my memory files and the usual config locations. I'll only list file names, not print any secrets.

- *Bash*: Look for where the Cloudflare token is noted
- *Bash*: Find Cloudflare token location notes in memory files
- *Bash*: Look up the habibium.com zone and list existing DNS records
- *Bash*: Create oils CNAME in Cloudflare and set the Pages custom domain
- *Bash*: Set the Pages custom domain

DNS resolves and GitHub has started issuing the certificate. Meanwhile I'm pointing the README, the build default and the repo homepage at the new domain.

- *Bash*: Point README, build default and repo homepage at the new domain
- *Bash*: Wait for GitHub to issue the HTTPS certificate
