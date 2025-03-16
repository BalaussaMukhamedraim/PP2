# Play/Pause: Spacebar
# Stop: S key
# Next track: Right Arrow (→)
# Previous track: Left Arrow (←)
# Displays currently playing track in the terminal

import pygame
import os

# Initialize pygame
pygame.init()

# Set up the screen
WINDOW_SIZE = (400, 200)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Music Player")

# Folder with music files
MUSIC_FOLDER = "/Users/alia/Desktop/kbtu/PP2/lab_7/music"

# Get list of all .mp3 files in the folder
playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_track = 0  # Index of the currently playing track

# Load and play the first song
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))

# Function to play music
def play_music():
    print(f"Playing: {playlist[current_track]}")
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
    pygame.mixer.music.play()

# Start playing the first track
play_music()
playing = True  # Track if music is playing

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Play/Pause (Spacebar)
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():  # If music is playing
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True

            # Stop music (S key)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

            # Next Track (Right Arrow)
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                play_music()

            # Previous Track (Left Arrow)
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                play_music()

    # Update the screen
    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()