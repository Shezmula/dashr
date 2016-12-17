# Dashr

## What is it?

Dashr is a python interface to the [Dasher.tv](https://dasher.tv) API.

## What is included?

This is a quick and dirty hack, so currently almost nothing :)

## Example

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import dashr

def main():
  # Create a dashr instance
  d = dashr.Dashr('<YOUR_API_KEY>')

  # List all screens
  print(d.screens.list())

  # Get details for screen '123'
  print(d.screens.details(123))

  # Update the 'timezone' of the 'home-screen.current-time' suqare
  print(d.squares.update('home-screen.current-time', 'timezone': 'Europe/Berlin'))

  # Get the details of the 'home-screen.current-time' suqare
  print(d.squares.details('home-screen.current-time'))

  return 0

if __name__ == '__main__':
    sys.exit(main())
```
