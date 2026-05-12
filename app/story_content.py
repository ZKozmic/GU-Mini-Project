"""Copy deck for the Streamlit story.

The main app should mostly draw things. Text lives here so the page does not
turn into one long scroll of triple-quoted strings.
"""

PAGE_TITLE = 'The Price of Adulthood'

TITLE = 'The Price of Adulthood: Can young Americans still afford the basic ingredients of life?'

OPENING_SENTENCE = ('The project will examine if, instead of asking if the country has grown wealthier over time, '
 'Americans are able to afford the necessities of becoming grown-ups as defined by the standard of '
 'living set forth in our culture.')

HERO = {'eyebrow': 'A descriptive data story',
 'subtitle': 'Can young Americans still afford the basic ingredients of life?',
 'question_label': 'Research question',
 'question': 'Since 1960, has the cost of entering independent adult life in the United States '
             'risen faster than typical income?',
 'does_label': 'What this project does',
 'does': 'It compares income and wages with the costs most closely tied to adult stability: '
         'housing, healthcare, education, childcare, and family formation.',
 'does_not_label': 'What this project does not do',
 'does_not': 'It does not claim that economic pressure directly caused later marriage, lower '
             'fertility, or political polarization. The project shows long-term patterns and '
             'pressure points, not a single grand cause.'}

NAV_ITEMS = [('overview', 'Overview'),
 ('wage-baseline', 'Wage Baseline'),
 ('housing-gate', 'Housing Gate'),
 ('medical-prices', 'Medical Prices'),
 ('education-childcare', 'Education & Childcare'),
 ('delayed-adulthood', 'Delayed Adulthood'),
 ('methods', 'Methods'),
 ('data-sources', 'Data & Sources'),
 ('limitations', 'Limitations'),
 ('references', 'References')]

NAV_NOTE = 'A single-page data story with five main charts and no dashboard filters.'

DISPLAY = {'heading': '## Display',
 'day_mode': 'Day mode',
 'day_help': 'Switch between light and dark page and chart colors.',
 'caution_label': 'Caution',
 'missing_data_hint': 'Run `python src/download_data.py` and `python src/build_yearly_dataset.py` '
                      'before opening the app.'}

AXIS = {'year': 'Year', 'ratio': 'Ratio', 'years': 'Years'}

SERIES = {'income': 'Real median family income index (1960=100)',
 'wage': 'Real hourly earnings index (1964=100)',
 'home_ratio': 'Home price / family income',
 'home_years': 'Home price in full-time work years',
 'medical': 'Medical care CPI index (1960=100)',
 'medical_wage': 'Medical CPI / hourly wage index (1964=100)',
 'education': 'Tuition, school fees, and childcare CPI index (1978=100)',
 'education_wage': 'Education/childcare CPI / hourly wage index (1978=100)',
 'men': 'Men',
 'women': 'Women'}

OVERVIEW = {'title': 'Overview',
 'kicker': 'Overview',
 'body': '\n'
         'The project will examine if, instead of asking if the country has grown wealthier over '
         'time, Americans are able to afford the necessities of becoming grown-ups as defined by '
         'the standard of living set forth in our culture. The typical American is said to often '
         'look back over time and reminisce about the "good old days" from the past when things '
         'were simpler; you could just go out and work; you would acquire a home (rent or own), '
         'have kids, be able to see a doctor when needed, and eventually reach the middle class.\n'
         '\n'
         'A strong memory, but it is not true. Not everyone had as good an experience in the past, '
         'and nostalgia can make the past seem hazy and safe. This project takes a different '
         'approach to the question of whether the old days of entering adulthood were "perfect." '
         'Instead, the project looks at whether we have seen a fundamental change in the cost of '
         'transitioning to adult life.\n'
         '\n'
         'The date of 1960 does not represent a utopia, but is clearly working from an earlier '
         'time period that can be used as a critical, historical reference point. The late 1950s '
         'were near the end of the post-World War II economic expansion, as the Baby Boom '
         'Generation came of age within an era shaped by post-war suburbia, competitive tensions '
         'across the Cold War, and one shared vocabulary reflecting the abundance and affluence of '
         'the middle-class. The Marshall Plan helped facilitate the reconstruction of Western '
         'Europe and significantly established U.S. presence early in the Cold War. By 1960 the '
         'American dream of being part of a flourishing middle-class also could be interpreted as '
         'synonymous with the economic potential of its people; nonetheless, economic potential '
         'amongst individuals varies greatly.\n'
         '\n'
         'The future of the American dream is uncertain. Online discussions about American life '
         'often center around serious problems, such as healthcare, student loans, wages, '
         'groceries, gas, poor work-life balance, long commutes, and the sense of being able to '
         'afford a house or raise a family. Reddit & Discord discussions are not representative of '
         'survey data; however, they do provide a frame of reference for how people talk about the '
         'actual costs associated with becoming independent adults.\n'
         '\n'
         "This project's aim is to quantify the everyday experience. It does this by asking "
         "questions like: How long does a house take to purchase compared to a person's salary? Do "
         "the prices of housing, healthcare, and education align with someone's salary? Are people "
         'reaching major life events (like marriage) consistently later in life than they did '
         'years ago? Where does a comparison to "the good old days" exist, if at all?\n'}

CHARTS = {'wage': {'anchor': 'wage-baseline',
          'kicker': '01 Wage Baseline',
          'section_title': '1. The wage baseline: did ordinary income actually grow?',
          'section_body': '\n'
                          'To determine whether life has become more expensive, we first need to '
                          'establish a baseline. There are many ways in which America has become '
                          'wealthier. Wages have gone up, output has increased, and consumer '
                          'demand has grown. The ability to live as an adult is not based on the '
                          'Gross Domestic Product (GDP). It is based on how much you earn at '
                          'work.\n'
                          '\n'
                          'In this section, we will compare real median household income to real '
                          'hourly earnings for production and non-supervisory workers to '
                          'demonstrate what ordinary families and workers had access to before we '
                          'look at the huge costs associated with living as an adult. '
                          '<a class="citation-link" href="#ref-1">[1]</a>\n',
          'chart_title': 'Chart 1. Income and wage indices over time',
          'y_title': 'Index',
          'hook': 'The income baseline sets the size of the paycheck before costs enter.',
          'tip': 'Look for whether income and wages move together.',
          'caption': 'We are also going to show how the long-term trends of real median household '
                     'income have changed through different time periods against the long-term '
                     'trends of real hourly wages to illustrate what was available to households '
                     'before we look at the intended costs associated with housing, health care '
                     'and education.',
          'caution': "Warning! Real Median Household Income does not equal an individual's "
                     'personal income. Real Median Household Income is being used as a general '
                     'household measure, not to measure exactly what a 25-year-old would earn.',
          'wage_note': 'Wage series starts in 1964'},
 'housing': {'anchor': 'housing-gate',
             'kicker': '02 Housing Gate',
             'section_title': '2. The housing gate: the first door got heavier',
             'section_body': '\n'
                             'Housing is the first adult milestone that many people face in their '
                             'lives. Leaving home to rent, buy a house, live closer to work, start '
                             'a family, and add to an existing family are mostly based on whether '
                             'they can afford the cost of housing.\n'
                             '\n'
                             'The old bargain seems to be fraying as the value of housing is now '
                             'much greater than it was in the past. Owning a home is not just '
                             'about being able to afford a good place to live; it is also about '
                             'having a stable home to live in, access to good schools for '
                             'children, maintaining a stable work-life balance, and providing your '
                             'family with a way to build a future together. If housing prices are '
                             'significantly increasing faster than wages, then the meaning of '
                             'adult transition from one life stage to another changes from what '
                             'people hoped it would be a rite of passage to an entry fee.\n',
             'chart_title': 'Chart 2. Housing burden: home price relative to income and work years',
             'subtitles': ('Median new home price relative to median family income',
                           'Median new home price in full-time work years'),
             'hook': 'The first door to adulthood is often a lease or a mortgage.',
             'tip': 'Notice how housing becomes less about price alone and more about years of '
                    'work.',
             'caption': 'This chart shows how the median price for a newly constructed home '
                        'compares with family median yearly incomes and number of years of '
                        'full-time employment at an average hourly wage over time. '
                        '<a class="citation-link" href="#ref-2">[2]</a>',
             'caution': 'Important Note: The data represents median-priced new homes sold, not all '
                        'homes sold, and typically do not equate to all local markets. Reading '
                        'this chart should only be interpreted as a national indicator for the '
                        'increasing rigor of housing demand, not necessarily as an accurate '
                        'reflection of the amount of money a first-time homebuyer must pay.'},
 'medical': {'anchor': 'medical-prices',
             'kicker': '03 Medical Prices',
             'section_title': '3. The medical bill: a cost that follows you around',
             'section_body': '\n'
                             "Healthcare stands apart from many other costs as there's no "
                             'alternative way to obtain healthcare other than through purchasing '
                             'or accessing services. If you want to buy a home, you can wait until '
                             'you have more money; if you want to buy a car, you can pick one that '
                             'fits your budget; if you want to eat at home, you can choose that '
                             'option. However, if you become ill, you cannot wait to "afford it '
                             'better".\n'
                             '\n'
                             'The importance of medical costs is that they create a constant '
                             'background stress level by changing the amount of risk being taken. '
                             'Even if someone is insured, medical expenses can dictate how they '
                             'make decisions about their employment, how much they save, whether '
                             'or not they take on debt or start a family, and whether they worry '
                             'about one unfortunate event destroying everything they have worked '
                             "for. So, in adulthood, health is physical and it's also financial.\n",
             'chart_title': 'Chart 3. Medical care prices compared with wages',
             'y_title': 'Index',
             'hook': 'Some costs can be delayed. Illness usually cannot.',
             'tip': 'Look for the gap between medical prices and the wage comparison line.',
             'caption': 'This chart tracks the medical care price index and compares medical price '
                        'growth with hourly wage growth.',
             'caution': 'Caution. Medical CPI is a price index. It is not the same as '
                        'out-of-pocket medical spending, insurance premiums, deductibles, or '
                        'medical debt. It shows price pressure, not a complete household '
                        'healthcare bill.'},
 'education': {'anchor': 'education-childcare',
               'kicker': '04 Education & Childcare',
               'section_title': '4. The education and childcare gap: the price of getting ahead, '
                                'and the price of having children',
               'section_body': '\n'
                               'The two stages of early adulthood are education and child-rearing '
                               'which represent two extremes; education is thought to support '
                               'upward movement through the economy, whereas child-rearing is '
                               'designed to allow parents to have both family and gainful '
                               'employment. The two are related in that they both represent a '
                               'means for an individual to create a future.\n'
                               '\n'
                               'However, if either education or child-rearing costs grow at a '
                               'higher pace than wage growth, then individuals will be stuck in '
                               'the trap created by the promise of upward mobility by either '
                               'education or child-rearing. For example, a degree obtained may '
                               'result in an accumulation of debt. Alternatively, having a child '
                               'may result in an additional sizeable expense that impacts ones '
                               'working, marriage, and reproductive decisions; therefore, this '
                               'will result in individuals that have "different choices" simply '
                               'due to a difference in the available choices for them.\n',
               'chart_title': 'Chart 4. Education, school fees, and childcare prices',
               'y_title': 'Index',
               'hook': 'Getting ahead and raising children became more expensive promises.',
               'tip': 'Notice that this series starts later, but its climb is steep.',
               'caption': 'This chart shows the price index for tuition, school fees, and '
                          'childcare, and compares it with wages where possible. '
                          '<a class="citation-link" href="#ref-3">[3]</a>',
               'caution': 'Caution. This series begins in 1978, so it cannot be used to compare '
                          'directly with 1960. It is included as a later-stage pressure that '
                          'became increasingly important in the post-1970s affordability story.',
               'series_note': 'Series starts in 1978'},
 'marriage': {'anchor': 'delayed-adulthood',
              'kicker': '05 Delayed Adulthood',
              'section_title': '5. Delayed adulthood: when life milestones move later',
              'section_body': '\n'
                              'Financial considerations alone do not dictate when someone will '
                              'marry, have kids, or continue living with their parents; they are '
                              'impacted by many cultural and social factors as well as the way '
                              'each generation has increasingly achieved greater personal freedom '
                              'than its predecessors.\n'
                              '\n'
                              'Economic factors, however, will continue to determine how and when '
                              'people become adults as longer waits for things like life, but rent '
                              'is high, there aren’t many places to live, healthcare is dangerous, '
                              'and education is costly, thus settling down becomes less of an '
                              'indication of growing up and instead becomes a business decision.\n'
                              '\n'
                              'This section shows relationship between the length of time until '
                              'someone gets married on average among men and women but isn’t '
                              'intended as an explanation for why people waited longer to marry; '
                              'rather it demonstrates that very visible evidence of adulthood '
                              'became increasingly evident while concurrently a number of '
                              'reasonably significant cost-related lifetime markers also became '
                              'increasing difficult for many younger generations to afford.\n',
              'chart_title': 'Chart 5. Median age at first marriage by gender',
              'y_title': 'Median age',
              'hook': 'Life milestones moved later, but this chart does not prove why.',
              'tip': 'Look for the later timing without reading the chart as proof of causation.',
              'caption': 'This chart shows how the median age at first marriage changed over time '
                         'for men and women. '
                         '<a class="citation-link" href="#ref-4">[4]</a>',
              'caution': 'Caution. Marriage age is not a direct measure of affordability. It '
                         'reflects culture, law, gender roles, education, work, religion, and '
                         'personal freedom as well as money. This chart should be read as an '
                         'outcome that changed alongside affordability pressures, not as proof of '
                         'causation.'}}

BACKGROUND_EXPANDERS = [{'title': 'Why mention Reddit or Discord if they are not formal data?',
  'body': '\n'
          'Online discussions are not representative evidence. Reddit and Discord overrepresent '
          'people who are online, vocal, frustrated, or unusually motivated to talk about their '
          'lives.\n'
          '\n'
          'They are included only as framing. They show the language people use when they talk '
          'about quality of life: rent, wages, student debt, medical bills, groceries, gas, '
          'work-life balance, loneliness, and whether the future still feels reachable. This '
          'project uses those conversations as a starting mood, then tests the larger pattern with '
          'official economic data.\n'},
 {'title': 'Was 1960 actually a "good old days" benchmark?',
  'body': '\n'
          'No. The year 1960 is a useful benchmark, not a claim that the past was universally '
          'better. Many young adults had different household arrangements then, but racial '
          'exclusion, gender inequality, unequal access to credit, and limited rights shaped who '
          'could actually enjoy the middle-class bargain.\n'
          '\n'
          'This project treats 1960 as a historically loaded baseline: a moment when the promise '
          "of middle-class adulthood was unusually central to America's self-image, not as a "
          'paradise to return to.\n'}]

METHODS = {'anchor': 'methods',
 'title': 'Methods: how the project measures affordability',
 'body': '\n'
         'This project uses official long-run data from FRED, BLS-linked CPI series, Census '
         'tables, and related public sources. Monthly, quarterly, and annual series are converted '
         'into annual values. Monthly and quarterly data are averaged by calendar year.\n'
         '\n'
         'The project uses three types of measures:\n'
         '\n'
         'Real dollars: nominal dollar values are adjusted with the all-items CPI so that values '
         'can be compared in 2024 dollars.\n'
         'Index values: each series is set to 100 in its first valid comparison year.\n'
         'Affordability ratios: costs are compared with income or wages, such as home price '
         'relative to family income or home price measured in full-time work years.\n'
         "If a variable hasn't been reported for a given year as of 1960, then an early date for "
         'that variable will not be generated by this project; instead, the project will begin the '
         'series at the earliest record available for that variable, and this will be clearly '
         'labelled. No interpolation of the historical years will be accomplished. The chart is '
         'not intended to indicate causes, but only the general historical patterns of the '
         'long-term data.\n',
 'optional_caption': 'Some optional processed background variables are available in the '
                     'optional_yearly.csv file, but these were not the primary datasets used for '
                     'developing the first draft of the web charts.'}

DATA_SOURCES = {'anchor': 'data-sources',
 'title': 'Data & Sources',
 'intro': 'The main charts use the processed annual dataset in data/processed/main_yearly.csv. The '
          'raw source files are downloaded or documented through docs/source_manifest.csv.',
 'chips': [('FRED', False),
           ('BLS-linked CPI', False),
           ('Census', False),
           ('Pew/context', False),
           ('Online discussion framing (not formal data)', True)],
 'boxes': [{'title': 'FRED and BLS-linked series used in the main charts',
            'items': ['CPIAUCSL: Consumer Price Index for All Urban Consumers, used for inflation '
                      'adjustment.',
                      'MEFAINUSA672N: Real median family income, used as the household income '
                      'anchor.',
                      'AHETPI: Average hourly earnings of production and nonsupervisory employees, '
                      'used as the wage anchor.',
                      'MSPUS: Median sales price of houses sold in the United States, used for the '
                      'national home-price signal.',
                      'CPIMEDSL: Medical care CPI, used for healthcare price pressure.',
                      'CUSR0000SEEB: Tuition, school fees, and childcare CPI, used for education '
                      'and childcare price pressure.']},
           {'title': 'Census and context sources',
            'items': ['Census MS-2: Median age at first marriage by sex, used for the fifth main '
                      'chart.',
                      'Census AD-1: Living arrangements of young adults. It is documented and '
                      'processed, but not used as a main chart because the extracted series needs '
                      'further validation.',
                      'Pew/context sources: Used only to frame the historical discussion of young '
                      'adults\' living arrangements and the "good old days" question.',
                      'Reddit/Discord: Used only as informal framing for public language around '
                      'affordability. They are not treated as representative data.']}]}

LIMITATIONS = {'anchor': 'limitations',
 'title': 'Limitations',
 'body': '\n'
         "- Median family income is not the same as a young adult's personal income.\n"
         '- New home prices are not all homes and do not represent every local market.\n'
         '- CPI series are price indices, not household bills, insurance premiums, deductibles, '
         'rent checks, or debt balances.\n'
         '- The education and childcare series begins in 1978, so it cannot be compared directly '
         'with a 1960 baseline.\n'
         '- Marriage age does not prove that affordability caused delayed adulthood.\n'
         '- Living-with-parents data from Census AD-1 needs further validation before becoming a '
         'main chart.\n'
         '- This version does not include political polarization analysis.\n'}

CONCLUSION = {'title': 'Conclusion: adulthood did not disappear, but its price changed',
 'body': '\n'
         'The story is not that America simply became poor. That would be too easy, and also '
         'wrong. The story is that the basic ingredients of adult stability did not move '
         'together.\n'
         '\n'
         'Income rose. But housing, healthcare, and education-related prices created different '
         'kinds of pressure. Some costs became larger gates. Others became risks that followed '
         'people around. At the same time, visible adult milestones, such as first marriage, moved '
         'later.\n'
         '\n'
         'Everyone did not have equal access to the middle-class bargain however; data gives the '
         'impression that even concept of this middle-class bargain has become different based '
         'upon economic conditions, especially for young adults. Furthermore, being an adult today '
         'has become not only a stage of life, but also something you need to plan out, delay '
         'plans, negotiate for, downsize due to budget restraints and prepare for economic '
         'constraints.\n'}

REFERENCES = {
    'anchor': 'references',
    'title': 'References',
    'items': [
        'Federal Reserve Bank of St. Louis. Real Median Family Income in the United States (MEFAINUSA672N). FRED Economic Data.',
        'Federal Reserve Bank of St. Louis. Median Sales Price of Houses Sold for the United States (MSPUS). FRED Economic Data.',
        'U.S. Bureau of Labor Statistics via FRED. Consumer Price Index for All Urban Consumers: Tuition, Other School Fees, and Childcare in U.S. City Average (CUSR0000SEEB).',
        'U.S. Census Bureau. Historical Marital Status Tables, Table MS-2: Estimated Median Age at First Marriage, by Sex: 1890 to Present.',
        'LLM usage statement: ChatGPT was used for small code debugging, formatting support, syntax clarification, and checklist organization. The final analysis, design choices, and written conclusions were reviewed and controlled by the author.'
    ]
}
