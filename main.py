import random
from evolpy.abstract_individuum import AbstractIndividuum
from evolpy.evolution import Evolution

NUM_GENES = 20
WANTED_CHROMOSOME = [1] * NUM_GENES


class MyIndividuum(AbstractIndividuum):
    @staticmethod
    def get_new_gene() -> int:
        """
        Return a random gene from all possible genes
        """
        return random.randint(0, 26)

    @staticmethod
    def get_number_of_genes() -> int:
        """
        Return the number of genes in the chromosome
        """
        return NUM_GENES

    def get_fitness(self) -> int:
        """
        Evaluate the fitness function, which measures the quality of the individual.
        """
        fitness = self.num_genes
        # Subtract one point if genes deviate
        for item1, item2 in zip(self.chromosome, WANTED_CHROMOSOME):
            if item1 != item2:
                fitness -= 1
        return fitness


pop = Evolution(MyIndividuum).optimize(max_fitness=NUM_GENES)
fit = [ind.get_fitness() for ind in pop]
max_index = fit.index(max(fit))
best_individuum = pop[max_index]
print(best_individuum.chromosome)
