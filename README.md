# Experimental PokemonGo-Bot Plugin Enhancements

Test new features in existing plugins.

## PokemonOptimizer

Allow for custom filters (just one so far!).

```
{
    "type": "PGO-plugins.PokemonOptimizer",
    "config": {
        "keep": [{
                "filter": "above",
                "params": {
                    "minimum": [165],
                    "pokemon": ["Weedle", "Staryu"]
                },
                "evolve": false,
                "sort": ["cp"]
            }
        ]
    }
}
```

The above example will keep any named `pokemon` which is above *165 CP*.
