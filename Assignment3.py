from collections import deque

# 1. Initialize
# We use deque for the queue because it's efficient for adding/removing from both ends.
application_inbox = deque()
# A standard list works perfectly as a stack (LIFO) in Python.
processed_history = []

# 2. Ingest Data
messy_startups = ["  TechCorp  ", "bio-gen", "  Cloud_Scale ", "SOLAR-pulse  "]

for name in messy_startups:
    # Clean the string: remove whitespace and convert to lowercase
    cleaned_name = name.strip().lower()
    application_inbox.append(cleaned_name)

# 3. Process (FIFO - First-In, First-Out)
while application_inbox:
    # popleft() removes the item that was added first
    current_app = application_inbox.popleft()
    print(f"Approving: {current_app}")
    
    # Push to history stack
    processed_history.append(current_app)

# 4. Undo (LIFO - Last-In, First-Out)
# Simulating a mistake by popping the most recent item added to history
if processed_history:
    last_processed = processed_history.pop()
    print(f"Reverting approval for: {last_processed}")