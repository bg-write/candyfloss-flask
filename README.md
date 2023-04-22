<a name="top"></a>

# Candyfloss

Now you don't need Twitter to keep up with the music world.

[![GitHub issues](https://img.shields.io/github/issues/bg-write/candyfloss-flask?style=flat-square)](https://github.com/bg-write/candyfloss-flask/issues)

![Candyfloss home page](./static/candyfloss-home-page-full.png)

## Table of Contents

I. [Introduction](#intro)

- Overview of Candyfloss
- Why Use Candyfloss?
- Project Goals & Intended Audience

II. [Getting Started](#getting-started)

- System Requirements
- Installing Dependencies
- Running the Code
- Running Tests

III. [Usage](#usage)

- Overview of Features
- Using Candyfloss

IV. [Architecture](#architecture)

- Overall Architecture
- How Was Candyfloss Built?
- Style Guide
- Tech Stack & Tools

V. [API Reference](#api)

- Overview of Candyfloss's API
- API Endpoints & Parameters
- Examples of API Usage

VI. [Giving Thanks](#legal)

- Next Steps
- How Can You Contribute?
- Closing Credits
- Cited Sources
- Candyfloss Outlets
- Outlets To Add

VII. [Glossary](#glossary)

- TBD

![image]()

## I. Introduction <a name="intro"></a>

[Return to top](#top)

### Overview of Candyfloss

**Candyfloss** is like Hacker News but for music.

Candyfloss is a digital daily newspaper curating the best music news and longform writing. Now you don't need Twitter to keep up with the music world. Candyfloss's styling is inspired by the print covers of the London Review of Books and has a strict cut-off point to fight endless scrolling. Candyfloss displays the 50 most recent links from several outlets and refreshes every hour.

To use Candyfloss:

1. Open the Candyfloss URL: <https://www.candyfloss.app/>.
2. Click a link.
3. Enjoy!

### Why Use Candyfloss?

**The problem**: I don't want to rely on social media for music news. However, social media is an easy way to keep track of new content from my favorite writers and outlets on various types of media: websites, newsletters, video channels, and more. Is there a way to see all these various links without the baggage of social media?

**The solution**: I created a simple RSS reader web app to share with colleagues.

### Project Goals & Intended Audience

Candyfloss aims to replace Twitter as your source for music news. Additional news outlets and improvements to the code's web scraping are pending.

An ideal user of Candyfloss is a fellow music journalist or music fan who wants to discover some of the best music writing today without being on social media.

![image]()

## II. Getting Started <a name="getting-started"></a>

[Return to top](#top)

The deployed app: <https://www.candyfloss.app/>

### System Requirements

I wanted to build Candyfloss in Python because it's one of my favorite languages; I love its balance of power and simplicity. I also wanted to learn Beautiful Soup, a neat Python library for parsing structured data.

I deployed Candyfloss as a Flask app via PythonAnywhere, which allows me to host the app on a separate domain and keep track of basic analytics with an affordable paid account.

### Installing Dependencies

TBD

### Running the Code

To run Candyfloss locally:

1. Open your IDE of choice.
2. Open a terminal window.
3. Enter and run this command: `flask --debug run`.
4. Open the development server URL that's provided in the terminal output.
5. You should now see Candyfloss.

### Running Tests

Pytest is testing `app.py` and each file found in the `feeds` folder. More feed and database testing to come. To run pytests for Candyfloss:

1. Open a new terminal window.
2. Enter and run the command `pytest -v`.

![image]()

## III. Usage <a name="usage"></a>

[Return to top](#top)

### Overview of Features

TBD.

### Using Candyfloss

TBD.

![image]()

## IV. Architecture <a name="architecture"></a>

[Return to top](#top)

### Overall Architecture

The most important folders and files to know:

- `feeds`: Holds the web scraping for each publication
- `static`: Holds my used images and `styles.css`
- `templates`: The HTML you see on the browser
- `tests`: Where I test `app.py` and `feeds` using pytest
- `app.py`: where I combine the feeds into one clean and organized feed, then rendered to `templates`

### How Candyfloss Works?

Below is the workflow I follow whenever I'm adding new outlets to Candyfloss.

#### 1) Find and Test the RSS URLs

I first find a working RSS feed for a publication. If a website doesn't promote its own RSS, I can usually find it by typing "/rss" or "/feed" at the end of a URL, or use Google's "RSS Subscription Extension" Chrome plugin.

To publications that make their RSS feeds easy to find: Thank you!

#### 2) Create a Publication's Feed

Each file in the `feeds` folder is where I use Beautiful Soup, requests, and lxml to call and clean up the RSS for each publication.

**"Get" the soup**: make my GET request using requests, Beautiful Soup, and lxml (for genuine web scraping when RSS is not available):

```python
def get_soup():
    html_text = requests.get(
        'RSS URL', timeout=10).text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()
```

**"Cook" the soup**: pinpoint the repeating element holding the content that I wish to pull from:

```python
def cook_soup():  # each article is in an <item/>
    return soup.find_all('item')


articles = cook_soup()
```

**"Deliver" the soup**: use a for loop to append the info I need into my empty lists, which I then combine into a new dict, which looks like:

```python
PUBLICATION = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]
```

> REFACTORING NOTES: Since deploying this app, I've refactored these steps to include an "Outlet" class to better abstract the structure and abilities of a publication. `p4k.py` displays how this process began. `p4k_class.py` shows how this process has evolved. Future work will include ways to take more advantage of class methods to simplify repeating logic. It also can be challenging when information is missing, mostly from publications not crediting their authors, or isn't formatted like most RSS feeds. The most common examples of the latter involves time and dates, which I clean up and standardize using Python's `datetime` functionality.

#### 3) Combine the Feeds into THE Feed

In `app.py`, I import all the publication feeds, combine them into one feed, and then use a sorting function to order this new feed by each link's date, and slice away any publication links after a set number (which for now is 50). This cleaned-up feed is then rendered into my main app route, along with the current date at any given time.

```python
# combining our feeds
link_dicts = pub1 + pub2 + pub3 + etc

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to return a specific set number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]
```

### Style Guide

Candyfloss's styling is inspired by the print covers of the London Review of Books and models Google's Python style guide with a few variations.

#### CSS

Candyfloss's CSS is all done in `styles.css`. Media queries are currently set for break points at 992px (most iPads and Surface Pros), 600px (most iPhones and Samsung Galaxies), and 360px (for the Galaxy Fold). Color CSS variables are defined as:

```CSS
--black: #0d0d0d;
--white: #ffffff;
--gold: #ffd900;
--blue: #0026ff;
```

#### The Code Itself

Candyfloss follows [Google's Python style guide](https://google.github.io/styleguide/pyguide.html) as closely as possible. This involves:

- Using `pylint` for automated code linting
- Using `yapf` for auto-formatting
- Including Google's settings file for Vim and `pylintrc`

#### Accessibility

The deployed Candyfloss app received an overall pass on mobile and desktop Lighthouse reports. Areas of improvement include addressing the performance on mobile due to speeds of first contentful paint, time to interactive, and total blocking time.

Desktop:

- Performance: 100
- Accessibility: 100
- Best Practice: 92
- SEO: 90

Mobile:

- Performance: 84
- Accessibility: 100
- Best Practice: 92
- SEO: 92

### Tech Stack & Tools

In order to work with Candyfloss locally, download the most updated versions of the following (unless version number is noted):

- [Python](https://www.python.org/) (3.8.6)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [lxml](https://lxml.de/)
- [pytest](https://docs.pytest.org/en/7.2.x/)
- [pylint](https://pylint.org/)
- [yapf](https://pypi.org/project/yapf/)
- [SQLite](https://www.sqlite.org/index.html)
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- Google's "[RSS Subscription Extension](https://chrome.google.com/webstore/detail/rss-subscription-extensio/nlbjncdgjeocebhnmkbbbdekmmmcbfjd)" Chrome plugin
- [Icons8](https://icons8.com/) (for the current corn favicon)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

More requirements can be found in `requirements.txt`

![image]()

## V. API Reference <a name="api"></a>

[Return to top](#top)

### Overview of Candyfloss's API

To view the API for Candyfloss's entire feed:

1. Follow the previous "To run Candyfloss" steps.
2. Find and click the end of the local server URL.
3. Type in "/api" to the end of the URL.
4. Press enter.
5. You'll now see the API.

To view the API for a specific publication:

1. Follow the previous "To view the API for Candyfloss's entire feed" steps.
2. At the end of the URL, type in "/PUBLICATION-NAME" (i.e. "/api/Pitchfork").
3. Press enter.
4. You'll now see the API for your specific publication.

> For now, case does matter. For example, you need to write "Pitchfork" as a proper noun. Please go to the "The Ever-Evolving List of Outlets Featured On Candyfloss" section of this README to see what publications are currently available to view on this API and how to spell them.

Candyfloss uses an SQLite database currently holding the outlets and RSS links being scraped.

To view this list of scraped outlets:

1. at the end of your local server URL, add "/db".

Future refactoring will make this database more dynamic and directly pull from all the feeds being imported ino `app.py`, and make it visible on the deployed app. I chose SQLite for its ease to use with Python but plan to upgrade the database in future refactoring.

### API Endpoints & Parameters

TBD.

### Examples of API Usage

TBD.

![image]()

## VI. Giving Thanks <a name="legal"></a>

[Return to top](#top)

### Next Steps

Candyfloss is always being updated. Future actions to take include:

- Flesh out documentation to DITA standards
- Update SQLite database to PostgreSQL
- Update `pytest` to now account for object and database refactoring and more closely follow Google's Python style guide
- Utilize class methods to further abstract some of my repeating logic when building and cleaning up feeds
- Refactor older feed files to incorporate my new class structures
- Add more publications!
- Are there too many links on the UI?
- Flesh out the app's overall metadata
- Add a search field on the UI
- Expand upon the current 404 page
- Any way to utilize relative data analysis or machine learning?

### How Can You Contribute?

Any way you can! I'm especially looking for help to flesh out my Python automated testing, and suggestions on new outlets I should add to Candyfloss.

### Closing Credits

A special shout-out to Nish Tahir for giving thoughtful feedback on an early version of this app, and James Bennington for his helpful guidance on how to document my code.

### Cited Sources

[Pallets's intro to Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) is a recommended starting point for anyone wanting to explore Flask. [Waweru Mwaura](https://circleci.com/blog/testing-flask-framework-with-pytest/) has a great blog post on the basics of using pytest with Flask. I also want to thank [Magnitopic](https://www.youtube.com/@Magnitopic) for their helpful [YouTube video](https://www.youtube.com/watch?v=AZMQVI6Ss64) on how to deploy a Flask app to PythonAnywhere. [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application), [CodingCasually](https://www.youtube.com/watch?v=tPxUSWTvZAs), and [ProfessorPitch](https://www.youtube.com/watch?v=YLOZpYAYPLQ) were all helpful with the initial local connection to SQLite.

### Candyfloss Outlets

Candyfloss pulls from the following outlets:

- OPE! (my own music blog)
- Pitchfork (album reviews)
- Stereogum (new music)
- Aquarium Drunkard (latest posts)
- The Ringer (music section)
- Fluxblog (substack)
- Music Journalism Insider (substack)
- Penny Fractions (ghost)
- Chicago Reader (Gossip Wolf column)
- Uproxx (music section)
- Abundant Living (ghost)
- Billboard (Chart Beat column)
- No Bells (latest posts)
- The Quietus (reviews)
- Loud And Quiet (reviews)
- No Depression (reviews)
- So It Goes (substack)
- Reply Alt (substack)
- Wire (In Writing column)
- Passion of the Weiss (latest posts)
- New York Times (music section)
- The Guardian (music section)
- NME (music features)
- VAN (classical music features)
- The Alternative (new music)

### Outlets To Add

The outlets I want to next add to Candyfloss:

- Bandcamp
- Creem
- Eight-Bit Theory
- Four Columns
- GQ
- SPIN
- Vulture
- Last Donut of the Night
- BBC
- Mix Mag
- Slate
- Atlantic
- Aeon
- OkayPlayer
- Music Business Worldwide
- Texas Monthly
- John's Music Blog
- 4Columns
- New Yorker
- NPR
- ... and more!

![image]()

## VII. Glossary <a name="glossary"></a>

[Return to top](#top)

### TBD

TBD.

---

© 2023 Brady Gerber. All Rights Reserved.

[Return to top](#top)
