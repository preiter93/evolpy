import random
from copy import deepcopy
from .abstract_individuum import AbstractIndividuum


class Evolution(object):
    """
    Playing field of Evolution
    """

    def __init__(self, obj_individuum):
        if isinstance(obj_individuum, AbstractIndividuum):
            raise ValueError("Expect input of instance AbstractIndividuum")
        self.individuum = obj_individuum
        print("Input ok.")

    def optimize(
        self,
        population_size=200,
        max_generations=1000,
        crossover_rate=0.8,
        mutation_rate=0.1,
        max_fitness=None,
    ):
        """
        Skeletons of operations to perform the evolutionary algorithm.

        .. note::
        DO NOT override this function.
        """
        # Initiate population
        pop = [self.individuum.new_random() for _ in range(population_size)]
        fit = []
        for gen in range(max_generations):
            # Evaluate fitness
            fit = [ind.get_fitness() for ind in pop]

            # Callback
            self.callback(fit, gen)

            # Terminate
            if self.terminate_max_fitness(fit, max_fitness):
                print("Individuum reached maximum fitness!")
                return pop

            # Create next generation
            pop_child = []
            for i in range(0, self.get_number_of_recombinations(population_size)):
                # Select parents
                parents = self.selection_of_parents(pop, fit)
                # Recombination
                if random.random() < crossover_rate:
                    # Apply crossover function
                    childs = self.recombine(parents)
                else:
                    # Just take parents over to new generation
                    childs = [deepcopy(p) for p in parents]

                # Mutation
                for child in childs:
                    if random.random() < mutation_rate:
                        self.mutate(child)

                    # Store in new population
                    pop_child.append(child)

            # replace population by children
            pop = pop_child

        print("Reach max_generations limit!")
        return pop

    def callback(self, fit, gen):
        """
        Callback function.

        :fit: list of populations fitness
        :gen: int, number of generation
        """
        max_fit = max(fit)
        print("Max Fit:", max_fit, " in Gen:", gen)

    def terminate_max_fitness(self, fit, max_fitness):
        """
        Terminates if an individuum has reached the
        maximum fitness.
        The maximum fitness must be supplied to optimize()
        """
        return max(fit) >= max_fitness

    def selection_of_parents(self, population, fitness):
        """
        Selection of n (default = 2) individuals who take part in mating based on
        their fitness.

        There are many ways to select an individual for reproduction.
        The standard implementation is based on the roulette algorithm,
        which selects two individual with a certain probability based on
        its fitness value.

        .. note::
        You CAN override this function.
        """
        return [
            select_one_roulette(population, fitness),
            select_one_roulette(population, fitness),
        ]

    def recombine(self, parents):
        """
        Recombination of parents produces n (default = 2) offsprings.

        Again there are many ways to recombine individuals. The default
        applies simple recombination with one splitting point of
        the chromosomes.

        .. note::
        You CAN override this function.
        """
        if len(parents) != 2:
            raise ValueError(
                "Default implementation of recombination expects 2 parents."
            )
        # Get selected parents
        p1, p2 = parents[0], parents[1]
        # Extract their chromosomes
        ch1 = p1.get_chromosome()
        ch2 = p2.get_chromosome()
        # ch1 = self.get_chromosome_of_individuum(p1)
        # ch2 = self.get_chromosome_of_individuum(p2)
        # Recombine
        chs = chromosome_crossover_simple(ch1, ch2)
        return [self.individuum.new_from_chromosome(ch) for ch in chs]

    def mutate(self, individuum):
        """
        Mutate an individuum.

        Default:
        Replaces a gene at a random position with a new random gene.

        .. note::
        You CAN override this function.
        """
        chromosome = individuum.get_chromosome()
        num_genes = len(chromosome)
        pos = random.randint(0, num_genes - 1)
        chromosome[pos] = self.individuum.get_new_gene()

    def get_number_of_recombinations(self, population_size):
        """
        Return the number of recombinations/matings based on
        the population size.

        Default implementations generate two offsprings per recombination,
        hence this function returns population_size // 2.

                                        .. note::
        You CAN override this function.
        """
        return population_size // 2


def select_one_roulette(population, fitness):
    """
    Individuum with higher fitness is selected more likely.
    """
    if len(population) != len(fitness):
        raise ValueError("Size mismatch.")
    total_fitness = sum(fitness)
    pick = random.uniform(0, total_fitness)
    current = 0
    for fit, ind in zip(fitness, population):
        current += fit
        if current > pick:
            return ind


def chromosome_crossover_simple(p1, p2):
    """
    Recombine chromosome with another chromosome of the same type.
    (i) Picks a random position within the chromosome and
    (ii) produces two new offsprings from a crossover combination.
    .. note::
                    Homologous with 2 parents and 1 split point
    """
    num_genes = len(p1)
    if num_genes < 2:
        raise ValueError("Number of genes should be larger than two.")
    pt = random.randint(1, num_genes - 2)
    # perform crossover
    c1 = p1[:pt] + p2[pt:]
    c2 = p2[:pt] + p1[pt:]
    return [c1, c2]
