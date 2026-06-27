#!/usr/bin/env python3
"""VerboseList."""


class VerboseList(list):
    """List class."""

    def append(self, item):
        """Append method."""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, items):
        """Extend method."""
        count = len(items)
        print(f"Extended the list with [{count}] items.")
        super().extend(items)

    def remove(self, item):
        """Remove method."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop method."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
