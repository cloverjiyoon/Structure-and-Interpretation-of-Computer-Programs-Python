test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> place0 = Place('place_0')
          >>> print(place0.exit)
          None
          >>> print(place0.entrance)
          None
          >>> place1 = Place('place_1', place0)
          >>> place1.exit is place0
          True
          >>> place0.entrance is place1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
