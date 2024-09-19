from parallelbar import progress_map
from parallelbar.tools import cpu_bench


# https://dubovikmaster.github.io/parallelbar/#usage
def main():
    tasks = range(10000)
    progress_map(cpu_bench, tasks)


if __name__ == "__main__":
    main()
