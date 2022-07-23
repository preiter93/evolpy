import random
from evolpy.default_individuums import IndividuumWithListChromosome
from evolpy.evolution import Evolution


def text_to_num(text):
    """
    Return unicode sequence of a text.
    """
    return [ord(x) for x in text]


def num_to_text(num):
    """
    Return text from unicode sequence
    """
    return "".join(f"{chr(x)}" for x in num)


TEXT = (
    "He was an old man who fished alone in a skiff in the Gulf Stream "
    "and he had gone eighty-four days now without taking a fish."
)
NUM_GENES = len(TEXT)
TEXT_UNICODE = text_to_num(TEXT)


class Monkeys(IndividuumWithListChromosome):
    """
    A Monkey aspiring to be Hemingway

    Be CAREFUL, this could take some time.
    """

    @staticmethod
    def pick_random_gene() -> int:
        """
        Return a random gene from all possible genes
        """
        min_value = min(TEXT_UNICODE)
        max_value = max(TEXT_UNICODE)
        return random.randint(min_value, max_value)

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
        for item1, item2 in zip(self.chromosome, TEXT_UNICODE):
            if item1 != item2:
                fitness -= 1
        return fitness


def callback_monkeys(pop, fit, gen):
    """
    Callback function.

    :pop: list of population
    :fit: list of populations fitness
    :gen: int, number of generation
    """
    max_fit = max(fit)
    max_index = fit.index(max_fit)
    text = num_to_text(pop[max_index].chromosome)
    print("\nMax Fit:", max_fit, "/", NUM_GENES, "in Gen:", gen, "\n ", text)


# Run EA
pop = Evolution(Monkeys).optimize(
    population_size=2000,
    max_generations=2000,
    crossover_rate=0.1,
    preservation_rate=0.1,
    mutation_rate=0.1,
    max_fitness=NUM_GENES,
    callback=callback_monkeys,
)

# Postprocess
fit = [ind.get_fitness() for ind in pop]
max_index = fit.index(max(fit))
best_individuum = pop[max_index]
print("\nBest Monkey:\n ", num_to_text(best_individuum.chromosome))
