test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_name(soda)
          'Soda'
          >>> restaurant_location(soda)
          [127.0, 0.1]
          >>> restaurant_categories(soda)
          ['Restaurants', 'Breakfast & Brunch']
          >>> restaurant_price(soda)
          1
          >>> restaurant_ratings(soda)
          [4.5, 4]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
