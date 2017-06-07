test = {
  'name': 'survey',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (survey)
          parenthesis
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
