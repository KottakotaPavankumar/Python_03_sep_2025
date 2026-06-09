# --- Import libraries ---
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
from tensorflow.keras.utils import to_categorical
from music21 import note, chord, stream

# --- Step 1: Generate mock note data (works even without MIDI files) ---
# For demonstration, we simulate extracted notes instead of parsing .mid files
notes = ['C4', 'E4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5'] * 50  # fake notes

# --- Step 2: Prepare training data ---
sequence_length = 20
pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

# Map note names to integers
note_to_int = dict((note_name, number) for number, note_name in enumerate(pitchnames))

network_input = []
network_output = []

# Create sequences of given length and their following note as output
for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]
    network_input.append([note_to_int[n] for n in seq_in])
    network_output.append(note_to_int[seq_out])

n_patterns = len(network_input)

# Reshape input for LSTM and normalize
network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
network_input = network_input / float(n_vocab)

# One-hot encode output labels
network_output = to_categorical(network_output, num_classes=n_vocab)

# --- Step 3: Build LSTM model ---
model = Sequential()
model.add(LSTM(128, input_shape=(sequence_length, 1), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(128))
model.add(Dense(128))
model.add(Dropout(0.3))
model.add(Dense(n_vocab))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

# --- Step 4: Train the model ---
# Small training just for demo purposes
model.fit(network_input, network_output, epochs=2, batch_size=64, verbose=1)

# --- Step 5: Generate a short sequence ---
start = np.random.randint(0, len(network_input) - 1)
pattern = network_input[start].reshape(1, sequence_length, 1)
generated_notes = []

for _ in range(10):
    prediction = model.predict(pattern, verbose=0)
    index = np.argmax(prediction)
    result = pitchnames[index]
    generated_notes.append(result)

    next_input = np.array([[[note_to_int[result] / float(n_vocab)]]])
    pattern = np.concatenate((pattern[:, 1:, :], next_input), axis=1)

# --- Step 6: Convert generated notes to MIDI ---
output_notes = []
for note_pattern in generated_notes:
    n = note.Note(note_pattern)
    n.offset = len(output_notes)
    output_notes.append(n)

midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')

print("\n--- Music generation completed successfully! ---")
print("Sample generated note sequence:", generated_notes)
print("Saved as: generated_music.mid")
