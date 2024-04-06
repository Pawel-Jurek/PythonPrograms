import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    linked_sites = corpus.get(page)
    if linked_sites:
        result = {}
        additional_probability = 1 - damping_factor
        for site in corpus.keys():
            if site in linked_sites:
                result[site] = round(damping_factor / len(linked_sites) + additional_probability / len(corpus.keys()),4)
            else:
                result[site] = round(additional_probability / len(corpus.keys()), 4)
    else:
        result[site] = round(1 / len(corpus.keys()), 4)
    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visited_pages = {}
    for key in corpus.keys():
        visited_pages[key] = 0
    current_page = list(corpus.keys())[random.randint(0, len(corpus.keys())-1)]
    visited_pages[current_page] +=1

    for i in range(1,n,1):
        probability = transition_model(corpus, current_page, damping_factor)
        pages = []
        cdf_values = []

        for key, value in probability.items():
            if len(pages) == 0:
                pages.append(key)
                cdf_values.append(value)
            else:
                pages.append(key)
                cdf_values.append(value + cdf_values[-1])
        random_value = random.random()
        for j, cdf_value in enumerate(cdf_values):
            if cdf_value >= random_value:
                current_page = pages[j]
                break
        visited_pages[current_page] +=1

    for key in corpus.keys():
        visited_pages[key] /= n

    return visited_pages


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
