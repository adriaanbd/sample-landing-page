#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import pytest


@pytest.fixture(scope='module')
def html_soup(html_file="landing_page.html"):
    """Pass the bs4 html parsed file object to all tests."""
    with open(html_file) as html:
        soup = bs(html, 'html.parser')
        yield soup
        print("Closing file!")
    print("File closed!")


def test_title(html_soup):
    """Test title string."""
    assert "Landing Page" == html_soup.title.string


def test_header_requirements(html_soup):
    """Test header requirements from User Stories 1 to 4."""
    assert html_soup.header
    assert html_soup.header['id'] == "header"                           # US1
    assert html_soup.header.img                                         # US2A
    assert html_soup.header.img['id'] == 'header-img'                   # US2B
    assert html_soup.header.nav                                         # US3A
    assert html_soup.header.nav['id'] == 'nav-bar'                      # US3B
    nav_links = html_soup.find_all(attrs={"class": "nav-link"})
    assert nav_links                                                    # US4A
    assert 'class="nav-link"' in str(html_soup.find_all('nav')[0])      # US4B
    assert len(nav_links) >= 3


def test_form_requirements(html_soup):
    """Test form requirements from User Stories 7 to 12."""
    assert html_soup.form                                               # US7A
    assert html_soup.form['id'] == 'form'                               # US7B
    email_input = html_soup.form.find(attrs={'type': 'email'})
    assert email_input                                                  # US8
    assert "email" in email_input['placeholder']                        # US9
    assert html_soup.form.find(attrs={'id': 'email'})                   # US10
    submit_input = html_soup.form.find(attrs={'type': 'submit'})
    assert submit_input['id'] == 'submit'                               # US11
    assert "https://" in html_soup.form['action']                       # US12


def test_embedded_video(html_soup):
    assert html_soup.iframe['id'] == 'video'                            # US6


def test_voluntary_failure():
    """Raise Error if tests are still pending.
    TODO: US5 - nav-link redirects to corresponding section
    US13 - navbar should always be on top
    US14 - at least one media query
    US15 - should utilize CSS Flexbox at least once"""
    raise AssertionError("Finish your tests!")
