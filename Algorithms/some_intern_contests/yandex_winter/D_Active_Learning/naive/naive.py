import sys

def main():
    # Read the first line to get N, k, m
    first_line = input().strip()
    N, k, m = map(int, first_line.split())

    # Read the feature descriptions for each object
    features = []
    for _ in range(N):
        line = input().strip()
        features.append(list(map(float, line.split())))

    # Initialize predictions (for simplicity, start with zeros)
    predictions = [0.0] * N

    for iteration in range(m):
        # Output the current predictions
        print(' '.join(map(str, predictions)))
        sys.stdout.flush()

        if iteration < m - 1:
            # Read the derivatives from the service
            derivatives_line = input().strip()
            derivatives = list(map(float, derivatives_line.split()))

            # Update predictions based on derivatives
            # This is a simple gradient descent step
            learning_rate = 0.1
            for i in range(N):
                predictions[i] -= learning_rate * derivatives[i]

if __name__ == "__main__":
    main()