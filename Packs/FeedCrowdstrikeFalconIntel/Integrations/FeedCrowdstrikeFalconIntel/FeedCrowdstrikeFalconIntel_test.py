import pytest
from FeedCrowdstrikeFalconIntel import Client

@pytest.mark.parametrize(
    "params, actors_filter, expected",
    [
        ({}, '', '/intel/combined/actors/v1'),
        ({}, 'blabla', '/intel/combined/actors/v1blabla'),
        ('last_modified_date%3A%3E{relevant_time}', 'blabla',
         '/intel/combined/actors/v1blabla%2Blast_modified_date%3A%3E{relevant_time}'),
        ('last_modified_date%3A%3E{relevant_time}', '',
         '/intel/combined/actors/v1?filter=last_modified_date%3A%3E{relevant_time}')
    ]
)
def test_build_url_suffix(params, actors_filter, expected):
    res = Client.build_url_suffix(Client, params, actors_filter)
    assert res == expected


list_data_cs = {
    "meta": {
        "query_time": 0.0188748,
        "pagination": {
            "offset": 0,
            "limit": 100,
            "total": 2
        },
        "powered_by": "msa-api",
        "trace_id": "b9494030-7054-46dc-9787-fa426ff96c2b"
    },
    "resources": [
        {
            "id": 1,
            "name": "A",
            "slug": "a",
            "url": "https://demisto.com",
            "short_description": "hello",
            "created_date": 1487960014,
            "last_modified_date": 1595568692,
            "first_activity_date": 1462060800,
            "last_activity_date": 1580860800,
            "active": False,
            "capability": {
                "id": 1,
                "slug": "hi",
                "value": "hi"
            },
            "known_as": "aaa",
            "motivations": [
                {
                    "id": 1,
                    "slug": "food",
                    "value": "food"
                }
            ],
            "notify_users": False,
            "origins": [
                {
                    "id": 1,
                    "slug": "apartment",
                    "value": "apartment"
                }
            ],
            "region": {
                "id": 1,
                "slug": "hostel",
                "value": "hostel"
            },
            "target_countries": [
                {
                    "id": 1,
                    "slug": "hotel",
                    "value": "hotel"
                },
            ],
            "target_industries": [
                {
                    "id": 1,
                    "slug": "stores",
                    "value": "stores"
                },
            ]
        },
        {
            "id": 2,
            "name": "B",
            "slug": "b",
            "url": "https://demisto.com",
            "short_description": "hello world",
            "created_date": 1589572143,
            "last_modified_date": 1595627719,
            "first_activity_date": 1483228800,
            "last_activity_date": 1593993600,
            "active": False,
            "capability": {
                "id": 2,
                "slug": "hi",
                "value": "hi"
            },
            "known_as": "bbb",
            "motivations": [
                {
                    "id": 2,
                    "slug": "sports",
                    "value": "sports"
                }
            ],
            "notify_users": False,
            "origins": [
                {
                    "id": 2,
                    "slug": "house",
                    "value": "house"
                }
            ],
            "region": {
                "id": 2,
                "slug": "home",
                "value": "home"
            },
            "target_countries": [
                {
                    "id": 2,
                    "slug": "bus_stations",
                    "value": "bus_stations"
                },
            ],
            "target_industries": [
                {
                    "id": 2,
                    "slug": "supermarkets",
                    "value": "supermarkets"
                },
            ]
        }
    ],
    "errors": []
}

expected_list = [
    {
        "type": "Threat Actor",
        "value": "A",
        "rawJSON": {
                    'type': 'Threat Actor',
                    'value': "A",
                    'service': 'List Actors Feed',
                    "id": 1,
                    "name": "A",
                    "slug": "a",
                    "url": "https://demisto.com",
                    "short_description": "hello",
                    "created_date": 1487960014,
                    "last_modified_date": 1595568692,
                    "first_activity_date": 1462060800,
                    "last_activity_date": 1580860800,
                    "active": False,
                    "capability": {
                        "id": 1,
                        "slug": "hi",
                        "value": "hi"
                    },
                    "known_as": "aaa",
                    "motivations": [
                        {
                            "id": 1,
                            "slug": "food",
                            "value": "food"
                        }
                    ],
                    "notify_users": False,
                    "origins": [
                        {
                            "id": 1,
                            "slug": "apartment",
                            "value": "apartment"
                        }
                    ],
                    "region": {
                        "id": 1,
                        "slug": "hostel",
                        "value": "hostel"
                    },
                    "target_countries": [
                        {
                            "id": 1,
                            "slug": "hotel",
                            "value": "hotel"
                        },
                    ],
                    "target_industries": [
                        {
                            "id": 1,
                            "slug": "stores",
                            "value": "stores"
                        },
                    ]
                    },
        'fields': {'tags': {}, 'actor': "A", 'region': {"id": 1, "slug": "hostel", "value": "hostel"},
                   'actor_capability': {"id": 1, "slug": "hi", "value": "hi"}, 'geo_country': [
                   {"id": 1, "slug": "apartment", "value": "apartment"}],
                   'description': "hello", 'alias': "aaa",
                   'creation_date': 1487960014, 'actor_motivation': [{"id": 1, "slug": "food", "value": "food"}],
                   'updated_date': 1595568692,
                   'actor_target_country': [{"id": 1, "slug": "hotel", "value": "hotel"}],
                   'actor_target_industry': [{"id": 1, "slug": "stores", "value": "stores"}]}
    },
    {
        "type": "Threat Actor",
        "value": "B",
        "rawJSON": {
                    'type': 'Threat Actor',
                    'value': "B",
                    'service': 'List Actors Feed',
                    "id": 2,
                    "name": "B",
                    "slug": "b",
                    "url": "https://demisto.com",
                    "short_description": "hello world",
                    "created_date": 1589572143,
                    "last_modified_date": 1595627719,
                    "first_activity_date": 1483228800,
                    "last_activity_date": 1593993600,
                    "active": False,
                    "capability": {
                        "id": 2,
                        "slug": "hi",
                        "value": "hi"
                    },
                    "known_as": "bbb",
                    "motivations": [
                        {
                            "id": 2,
                            "slug": "sports",
                            "value": "sports"
                        }
                    ],
                    "notify_users": False,
                    "origins": [
                        {
                            "id": 2,
                            "slug": "house",
                            "value": "house"
                        }
                    ],
                    "region": {
                        "id": 2,
                        "slug": "home",
                        "value": "home"
                    },
                    "target_countries": [
                        {
                            "id": 2,
                            "slug": "bus_stations",
                            "value": "bus_stations"
                        },
                    ],
                    "target_industries": [
                        {
                            "id": 2,
                            "slug": "supermarkets",
                            "value": "supermarkets"
                        },
                    ]
                    },
        'fields': {'tags': {}, 'actor': "B", 'region': {"id": 2, "slug": "home", "value": "home"},
                   'actor_capability': {"id": 2, "slug": "hi", "value": "hi"}, 'geo_country':
                   [{"id": 2, "slug": "house", "value": "house"}],
                   'description': "hello world", 'alias': "bbb",
                   'creation_date': 1589572143, 'actor_motivation': [{"id": 2, "slug": "sports", "value": "sports"}],
                   'updated_date': 1595627719,
                   'actor_target_country': [{"id": 2, "slug": "bus_stations", "value": "bus_stations"}],
                   'actor_target_industry': [{"id": 2, "slug": "supermarkets", "value": "supermarkets"}]}
    }
]


@pytest.mark.parametrize(
    "response, expected",
    [
        (list_data_cs, expected_list),
    ]
)
def test_create_indicators_from_response(response, expected):
    res = Client.create_indicators_from_response(Client, list_data_cs, {})
    assert res == expected_list



