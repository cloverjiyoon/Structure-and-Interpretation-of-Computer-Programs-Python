test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'random_or_none, defined in ant.py',
          'choices': [
            'random_or_none, defined in ant.py',
            'random.random(), defined in the "random" module',
            'getitem, defined in the "operators" module'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What function selects a random bee from a list of bees, or
          None, if an empty list is passed in?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> place = colony.places['tunnel_0_0']
          >>> near_bee = Bee(2)
          >>> far_bee = Bee(2)
          >>> colony.places["tunnel_0_3"].add_insect(near_bee)
          >>> colony.places["tunnel_0_6"].add_insect(far_bee)
          >>> hive = colony.hive
          >>> thrower.nearest_bee(hive) is far_bee
          False
          >>> thrower.nearest_bee(hive) is near_bee
          True
          >>> thrower.action(colony)    # Attack!
          >>> near_bee.armor            # Should do 1 damage
          1
          >>> thrower.place is place    # Don't change self.place!
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
