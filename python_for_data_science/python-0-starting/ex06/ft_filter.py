def ft_filter(function, iterable):
    """Filter entry using provided function."""
    return [x for x in iterable if function(x)]
