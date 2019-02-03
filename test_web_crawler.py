import pytest

from web_crawler import (
    get_urls,
    get_titles_and_links,
    site_map
)


def test_get_urls():
    url = "https://halome.nu/"
    expected_result = {
        'https://halome.nu/wars',
        'https://halome.nu/odst',
        'https://halome.nu/',
        'https://halome.nu/h2',
        'https://halome.nu/reach',
        'https://halome.nu/h3',
        'https://halome.nu/h4',
        'https://halome.nu/h5',
        'https://halome.nu/mythic'
    }
    assert get_urls(url, set(), url) == expected_result



def test_get_titles_and_links():
    url = "https://halome.nu/"
    expected_result = {
        'https://halome.nu/reach': {
            'title': 'Halo Reach Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
                }
            },
        'https://halome.nu/odst':  {
            'title': 'Halo ODST Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/wars': {
            'title': 'Halo Wars Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/': {
            'title': 'Halo 1 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h3': {
            'title': 'Halo 3 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h4': {
            'title': 'Halo 4 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/mythic': {
            'title': 'Halo 3: Mythic Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h5': {
            'title': 'Halo 5 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h2': {
            'title': 'Halo 2 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        }
    }
    set_of_urls = get_urls(url, set(), url)
    assert get_titles_and_links(set_of_urls, url) == expected_result

def test_site_map():
    url = "https://halome.nu/"
    expected_result = {
        'https://halome.nu/reach': {
            'title': 'Halo Reach Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/odst': {
            'title': 'Halo ODST Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/wars': {
            'title': 'Halo Wars Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/': {
            'title': 'Halo 1 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h3': {
            'title': 'Halo 3 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h4': {
            'title': 'Halo 4 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/mythic': {
            'title': 'Halo 3: Mythic Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h5': {
            'title': 'Halo 5 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        },
        'https://halome.nu/h2': {
            'title': 'Halo 2 Main Menu',
            'links': {
                'https://halome.nu/reach',
                'https://halome.nu/odst',
                'https://halome.nu/wars',
                'https://halome.nu/changelog.txt',
                'https://halome.nu/',
                'https://halome.nu/h3',
                'https://halome.nu/h4',
                'https://halome.nu/mythic',
                'https://halome.nu/h5',
                'https://halome.nu/h2'
            }
        }
    }
    assert site_map(url) == expected_result













