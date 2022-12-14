class QualifierBag(dict):
    """Dictionary with dot notation."""

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key: str):
        """Safely return a value from the dictionary using dot notation."""

        if key in self:
            return self[key]

        return None
