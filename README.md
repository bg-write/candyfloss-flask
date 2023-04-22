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

- Installing Dependencies
- Running the Code
- Running Tests

III. [Architecture](#architecture)

- Overall Architecture
- How Candyfloss Works

IV. [Style Guide](#style)

- CSS
- The Code Itself
- Accessibility

V. [API Reference](#api)

- Overview of Candyfloss's API
- API for a Specific Publication
- Database API

VI. [Giving Thanks](#legal)

- Next Steps
- How Can You Contribute?
- Closing Credits
- Cited Sources
- Candyfloss Outlets
- Outlets to Add

VII. [Glossary](#glossary)

- Flask
- Virtual Environment
- Dependencies
- Pip
- SQLite
- API (Application Programming Interface)
- JSON (JavaScript Object Notation)

![image](https://doodleipsum.com/700?bg=6392D9&i=f701b63cfe38e57fa0408c238af32027)

## I. Introduction <a name="intro"></a>

[Return to top](#top)

### Overview of Candyfloss

**Candyfloss** is a digital daily newspaper curating the best music news and essays. Now you don't need Twitter to keep up with the music world. Candyfloss has a strict cut-off point to fight endless scrolling. It displays the 50 most recent links from several outlets and refreshes every hour.

To use Candyfloss:

1. Open Candyfloss: <https://www.candyfloss.app/>.
2. Click a link.
3. Enjoy!

### Why Use Candyfloss?

**The problem**: I don't want to rely on social media for music news.

**The solution**: I created a simple RSS reader web app to share with colleagues.

### Project Goals & Intended Audience

Candyfloss aims to replace Twitter as your source for music news. Additional news outlets and improvements to the code's web scraping are pending.

An ideal user is a fellow music journalist or music fan who wants to discover some of the best music writing today without being on social media.

![image](https://doodleipsum.com/700?bg=6392D9&i=9a88ce13e0be8a087884187b642fcedb)

## II. Getting Started <a name="getting-started"></a>

[Return to top](#top)

The deployed app: <https://www.candyfloss.app/>

### Installing Dependencies <a name="install"></a>

In order to work with Candyfloss locally, download the most updated versions of the following tools and libraries (unless a specific version is noted):

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

More requirements can be found in `requirements.txt`.

### Running the Code

To run Candyfloss locally:

1. Open your IDE of choice.
2. Open a terminal window.
3. Enter and run this command: `flask --debug run`.
4. Open the development server URL provided in the terminal output.
5. You should now see Candyfloss!

### Running Tests

Pytest is testing `app.py` and each file found in the `feeds` folder. More feed and database testing to come. To run pytests for Candyfloss:

1. Open a new terminal window.
2. Enter and run the command `pytest -v`.

![image](https://doodleipsum.com/700?bg=6392D9&i=be149914c1ca3abd4d013b3b7bb43666)

## III. Architecture <a name="architecture"></a>

[Return to top](#top)

### Overall Architecture

The most important folders and files to know:

- `feeds`: Holds the web scraping for each publication
- `static`: Holds images and `styles.css`
- `templates`: The HTML you see on the browser
- `tests`: Where I test `app.py` and `feeds` using pytest
- `app.py`: where I combine the feeds into one clean and organized feed which is then rendered to `templates`

### How Candyfloss Works

Below is the workflow for adding new outlets:

#### Find and Test the RSS URLs

I first find a working RSS feed for a publication. If a website doesn't promote its own RSS, I can find it most of the time by typing "`/rss`" or "`/feed`" at the end of a URL, or I use Google's "RSS Subscription Extension" Chrome plugin.

> To publications that make their RSS feeds easy to find: Thank you!

#### Create a Publication's Feed

Each file in the `feeds` folder is where I use Beautiful Soup, requests, and lxml to call and clean up the RSS for each publication. This is done in three parts:

**"Get" the soup**: make my GET request using requests, Beautiful Soup, and lxml (for when RSS isn't available):

```python
def get_soup():
    html_text = requests.get(
        'RSS URL', timeout=10).text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()
```

**"Cook" the soup**: pinpoint the repeating element holding the content I want:

```python
def cook_soup():  # each article is in an <item/>
    return soup.find_all('item')


articles = cook_soup()
```

**"Deliver" the soup**: use a `for` loop to append the info I need into my empty lists, which I then combine into a new dictionary that looks like this:

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

> REFACTORING NOTES: Since first deploying this app, I've refactored these steps to include an "Outlet" class to better abstract the structure and abilities of a publication. `p4k.py` displays how this process began. `p4k_class.py` shows how this process has evolved. Future work will include ways to take more advantage of class methods to simplify repeating logic.
>
> It can also be challenging when information is missing, mostly from publications not crediting their authors or isn't formatted like most RSS feeds. The most common examples of the latter involves time and dates, which I clean up and standardize using Python's `datetime` functionality.

#### Combine the Feeds into THE Feed

In `app.py`, I import all the publication feeds, combine them into one feed, and then use a sorting function to order this new feed by each link's date, and slice away any publication links after a set number (which for now is 50). This cleaned-up feed is then rendered into my main app route, along with the current date at any given time.

```python
# combining our feeds
link_dicts = pub1 + pub2 + pub3 + etc

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to return a specific set number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]
```

![image](https://doodleipsum.com/700?bg=6392D9&i=74992813671e428c3a0dc015673e1899)

## IV. Style Guide <a name="style"></a>

[Return to top](#top)

Candyfloss's styling is inspired by the print covers of the 'London Review of Books' and models Google's Python style guide with a few variations.

### CSS

Candyfloss's CSS is all done in `styles.css`. Media queries are currently set for the following break points:

- **992px**: most iPads and Surface Pros
- **600px**: most iPhones and Samsung Galaxies
- **360px**: for the Galaxy Fold

Color CSS variables are defined as:

```CSS
--black: #0d0d0d;
--white: #ffffff;
--gold: #ffd900;
--blue: #0026ff;
```

### The Code Itself

Candyfloss follows [Google's Python style guide](https://google.github.io/styleguide/pyguide.html) as closely as possible. This involves:

- Using `pylint` for automated code linting
- Using `yapf` for auto-formatting
- Including Google's settings file for Vim and `pylintrc`

### Accessibility

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

![image](https://doodleipsum.com/700?bg=6392D9&i=1d13152959d2ca9022a70d05a6b1cbc2)

## V. API Reference <a name="api"></a>

[Return to top](#top)

### Overview of Candyfloss's API

To view the API for Candyfloss's entire feed:

1. Compete the steps found in [Installing Dependencies](#install).
2. Find and click the end of the local server URL.
3. Type in "`/api`" to the end of the URL.
4. Press enter.
5. You'll now see the API!

### API for a Specific Publication

To view the API for a specific publication:

1. Follow the previous "Overview of Candyfloss's API" steps.
2. At the end of the URL, type in "`/PUBLICATION-NAME`" (i.e. "`/api/Pitchfork`").
3. Press enter.
4. You'll now see the API for your specific publication.

> For now, the spelling case does matter. For example, you need to write "Pitchfork" as a proper noun. Please go to the "[Candyfloss Outlets](#outlets)" section of this README to see what publications are currently available to view on this API and how to spell them.

### Database API

Candyfloss uses an SQLite database currently holding the outlets and RSS links being scraped.

To view this list of scraped outlets:

1. At the end of your local server URL, add "`/db`".

> Future refactoring will make this database more dynamic and directly pull from all the feeds being imported ino `app.py`, and make it visible on the deployed app.

![image](https://doodleipsum.com/700?bg=6392D9&i=47f0be30daaa2b2662e7cf09d7a21413)

## VI. Giving Thanks <a name="legal"></a>

[Return to top](#top)

### Next Steps

I'm continuing to make updates to Candyfloss when I can. Future actions to take include:

- Updating SQLite database to PostgreSQL
- Updating `pytest` to now account for object and database refactoring and more closely follow Google's Python style guide
- Utilizing class methods to further abstract some of my repeating logic when building and cleaning up feeds
- Refactoring older feed files to incorporate my new class structures
- Adding more publications
- Fleshing out the app's overall metadata
- Adding a search field on the UI
- Expanding upon the current 404 page
- Utilizing relative data analysis or machine learning

### How Can You Contribute?

Any way you can! I'm looking for help to flesh out my pytest automated testing, and suggestions on new outlets I should add to Candyfloss.

### Closing Credits

A special shout-out to Nish Tahir for giving thoughtful feedback on an early version of this app, and James Bennington for his guidance on how to document my code.

### Cited Sources

Candyfloss would not be possible without the following:

- [Pallets's intro to Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) is a recommended starting point for anyone wanting to explore Flask.
- [Waweru Mwaura](https://circleci.com/blog/testing-flask-framework-with-pytest/) has a great blog post on the basics of using pytest with Flask.
- I also want to thank [Magnitopic](https://www.youtube.com/@Magnitopic) for their helpful [YouTube video](https://www.youtube.com/watch?v=AZMQVI6Ss64) on how to deploy a Flask app to PythonAnywhere.
- [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application), [CodingCasually](https://www.youtube.com/watch?v=tPxUSWTvZAs), and [ProfessorPitch](https://www.youtube.com/watch?v=YLOZpYAYPLQ) were all helpful with the initial local connection to SQLite.
- Doodles by [Doodle Ipsum](https://doodleipsum.com/).

### Candyfloss Outlets <a name="outlets"></a>

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

The outlets I want to add when I have time:

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

![image](https://doodleipsum.com/700?bg=6392D9&i=1d13152959d2ca9022a70d05a6b1cbc2)

## VII. Glossary <a name="glossary"></a>

[Return to top](#top)

### Python

A high-level, interpreted programming language that is widely used in web development, scientific computing, data analysis, artificial intelligence, and more.

### Beautiful Soup

A Python library used for web scraping purposes to extract the data from HTML and XML files. It provides a set of simple methods to navigate and search the parse tree created from the HTML/XML source.

### Requests

A Python library used for making HTTP requests. It provides a simple and elegant way to send HTTP/1.1 requests using Python. It supports HTTP/2, SSL/TLS, and authentication.

### lxml

A Python library used for processing XML and HTML documents. It provides a simple and powerful API to parse, validate, and manipulate XML and HTML documents.

### Pytest

A Python testing framework used to write and run unit tests and a popular alternative to Python's built-in unit test module.

### Pylint

A Python library used for analyzing Python source code for errors and enforcing coding standards. It provides a set of rules and guidelines to help improve the quality and maintainability of Python code.

### yapf

A Python library used for formatting Python code according to a consistent style. It provides a simple and configurable way to automatically format Python code.

### Flask

A micro web framework written in Python. It is classified as a micro-framework because it does not require particular tools or libraries.

### PythonAnywhere

A cloud-based Python development and hosting platform. It provides a web-based Python development environment, a Python web hosting service, and a set of tools and features to help developers build and deploy Python applications easily.

### Virtual Environment

A tool that helps to keep dependencies required by different projects separate by creating isolated Python environments for them.

### Dependencies

External packages or libraries that are required by a Python application to run properly.

### Pip

The package installer for Python. You can use pip to install Python packages from the Python Package Index and other indexes.

### SQLite

A software library that provides a relational database management system.

### API (Application Programming Interface)

A set of protocols, routines, and tools used for building software applications. It specifies how software components should interact and makes it easier to develop software by providing pre-built components that can be used to build larger applications.

### JSON (JavaScript Object Notation)

A lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is a text format that is completely language-independent.

---

© 2023 Brady Gerber. All Rights Reserved.

[Return to top](#top)
