test = {
  'name': 'Problem 13',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing QueenAnt parameters
          >>> ants.QueenAnt.food_cost
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # QueenAnt Placement
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[1].add_insect(back_ant)
          >>> tunnel[7].add_insect(front_ant)
          >>> tunnel[4].add_insect(impostor)
          >>> impostor.action(colony)
          >>> impostor.armor            # Impostors must die!
          0
          >>> tunnel[4].ant is None
          True
          >>> back_ant.damage           # Ants should not be buffed
          1
          >>> front_ant.damage
          1
          >>> tunnel[4].add_insect(queen)
          >>> queen.action(colony)
          >>> queen.armor               # Long live the Queen!
          1
          >>> back_ant.damage           # Ants behind queen should be buffed
          2
          >>> front_ant.damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # QueenAnt Removal
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> place = colony.places['tunnel_0_2']
          >>> place.add_insect(impostor)
          >>> place.remove_insect(impostor)
          >>> place.ant is None         # Impostors can be removed
          True
          >>> place.add_insect(queen)
          >>> place.remove_insect(queen)
          >>> place.ant is queen        # True queen cannot be removed
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> hive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, hive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      >>> ants.bees_win = lambda: None
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing game over
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[4].add_insect(queen)
          >>> tunnel[6].add_insect(impostor)
          >>> bee = ants.Bee(3)
          >>> tunnel[6].add_insect(bee)     # Bee in place with impostor
          >>> bee.action(colony)            # Game should not end
          
          >>> bee.move_to(tunnel[4])        # Bee moved to place with true queen
          >>> bee.action(colony)            # Game should end
          BeesWinException
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if queen will not crash with no one to buff
          >>> queen = ants.QueenAnt()
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(colony)
          >>> bee.armor # Queen should still hit the bee
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> hive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, hive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
