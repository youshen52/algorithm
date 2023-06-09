import heapq


def beam_search(initial_state, generate_candidates, evaluate_candidates, beam_width):
    """
    Performs beam search to find the optimal sequence given a set of possible candidates at each step.

    Args:
        initial_state: The initial state of the search.
        generate_candidates: A function that generates a list of candidate sequences given a state.
        evaluate_candidates: A function that evaluates and assigns a score to each candidate sequence.
        beam_width: The number of top candidates to keep at each step.

    Returns:
        The optimal sequence found by the beam search algorithm.
    """
    # Initialize the beam with the initial state
    beam = [(0, [initial_state])]

    # Perform beam search
    while True:
        new_beam = []
        # Generate and evaluate candidates for each sequence in the current beam
        for score, sequence in beam:
            # Generate candidates for the current sequence
            candidates = generate_candidates(sequence[-1])

            # Evaluate and score each candidate
            for candidate in candidates:
                candidate_sequence = sequence + [candidate]
                candidate_score = evaluate_candidates(candidate_sequence)
                new_beam.append((score + candidate_score, candidate_sequence))

        # Keep only the top-k candidates
        beam = heapq.nlargest(beam_width, new_beam, key=lambda x: x[0])

        # Check if the best sequence reaches the end state
        if evaluate_candidates(beam[0][1]) == 0:
            return beam[0][1]
