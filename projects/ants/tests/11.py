test = {
  'name': 'Problem 11',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing BodyguardAnt parameters
          >>> bodyguard = BodyguardAnt()
          >>> BodyguardAnt.food_cost
          4
          >>> bodyguard.armor
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing container attributes
          >>> bodyguard = BodyguardAnt()
          >>> print(bodyguard.ant)
          None
          >>> bodyguard.container
          True
          >>> test_ant = Ant()
          >>> test_ant.container
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing contain_ant
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard2 = BodyguardAnt()
          >>> test_ant = Ant()
          >>> test_ant2 = Ant()
          >>> bodyguard.can_contain(bodyguard2)
          False
          >>> bodyguard.can_contain(test_ant)
          True
          >>> test_ant.can_contain(bodyguard)
          False
          >>> bodyguard.contain_ant(test_ant)
          >>> bodyguard.ant is test_ant
          True
          >>> bodyguard.can_contain(test_ant2)
          False
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
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard.action(colony) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place bodyguard before thrower
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place thrower before bodyguard
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
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
