test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing Long/ShortThrower parameters
          >>> ShortThrower.food_cost
          2
          >>> LongThrower.food_cost
          2
          >>> short_t = ShortThrower()
          >>> long_t = LongThrower()
          >>> short_t.armor
          1
          >>> long_t.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test LongThrower Hit
          >>> ant = LongThrower()
          >>> in_range = Bee(2)
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places["tunnel_0_5"].add_insect(in_range)
          >>> ant.action(colony)
          >>> in_range.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test ShortThrower hit
          >>> ant = ShortThrower()
          >>> in_range = Bee(2)
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places["tunnel_0_3"].add_insect(in_range)
          >>> ant.action(colony)
          >>> in_range.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing ShortThrower miss
          >>> ant = ShortThrower()
          >>> out_of_range = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(ant)
          >>> colony.places["tunnel_0_4"].add_insect(out_of_range)
          >>> ant.action(colony)
          >>> out_of_range.armor
          2
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing LongThrower Inheritance from ThrowerAnt
          >>> def new_action(self, colony):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> old_thrower_action = ThrowerAnt.action
          >>> old_throw_at = ThrowerAnt.throw_at
          
          >>> ThrowerAnt.action = new_action
          >>> test_long = LongThrower()
          >>> passed = 0
          >>> try:
          ...     test_long.action(colony)
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_long = LongThrower()
          >>> try:
          ...     test_long.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
          2
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
      'teardown': r"""
      >>> ThrowerAnt.action = old_thrower_action
      >>> ThrowerAnt.throw_at = old_throw_at
      """,
      'type': 'doctest'
    }
  ]
}
