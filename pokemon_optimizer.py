"""
Building on the work of others...
"""
from pokemongo_bot.cell_workers import PokemonOptimizer as _PokemonOptimizer


class PokemonOptimizer(_PokemonOptimizer):

    def filter_above(self, family, criteria):
        """
        Filter out values below the minimum and keep the rest.
        The `minimum` value has to match the `sort` criteria
        """
        params = criteria.get('params', {})
        limit = tuple(params.get('minimum', [0]))

        sorted_family = self.get_sorted_family(family, criteria)

        return [p for p in sorted_family if self.get_rank(p, criteria) > limit]

    def get_family_optimized(self, family_id, family):

        evolve_best = []
        keep_best = []

        for criteria in self.config_keep:
            try:
                filter_func = getattr(self, 'filter_{}'.format(criteria['filter']))
            except Exception as e:
                filter_func = self.get_top_rank

            if criteria.get("evolve", True):
                evolve_best += filter_func(family, criteria)
            else:
                keep_best += filter_func(family, criteria)

        evolve_best = self.unique_pokemons(evolve_best)
        keep_best = self.unique_pokemons(keep_best)

        return self.get_evolution_plan(family_id, family, evolve_best, keep_best)
