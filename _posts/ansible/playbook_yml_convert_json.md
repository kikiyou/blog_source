# playbook的yml格式转换成json

``` python
import yml
playbook = yaml.load(file(playbook).read())

playbook.yml

- pattern: '*'
  tasks:
  - do:
    - update apache
    - command
    - [/usr/bin/yum, update, apache]
    onchange:
    - do:
      - restart apache
      - command
      - [/sbin/service, apache, restart]
    - do:
      - run bin false
      - command
      - [/bin/false]

-----
[
  {
    "pattern": "*",
    "tasks": [
      {
        "do": [
          "update apache",
          "command",
          [
            "/usr/bin/yum",
            "update",
            "apache"
          ]
        ],
        "onchange": [
          {
            "do": [
              "restart apache",
              "command",
              [
                "/sbin/service",
                "apache",
                "restart"
              ]
            ]
          },
          {
            "do": [
              "run bin false",
              "command",
              [
                "/bin/false"
              ]
            ]
          }
        ]
      }
    ]
  }
]
```