# https://pyseek.com/2023/07/creating-a-music-player-in-python-using-vlc-and-tkinter/
# dependency1: pip install pygame
# dependency2: pip install python-vlc

#Step 1: Import the necessary libraries
import os
import vlc
import tkinter as tk
from tkinter import filedialog

#Step 2: Create the MusicPlayer class
class MusicPlayer:
	def __init__(self, window):
		self.window = window
		self.window.title("Music Player")
		self.window.geometry("500x340")
	
		# Create the playlist
		self.playlist = tk.Listbox(self.window, width=50)
		self.playlist.pack(pady=10)
		
		# Create the controls frame
		controls_frame = tk.Frame(self.window)
		controls_frame.pack()
		
		# Create the play button
		self.play_button = tk.Button(controls_frame, text="Play", command=self.play)
		self.play_button.grid(row=0, column=0, padx=10)
		
		# Create the pause button
		self.pause_button= tk.Button(controls_frame, text="Pause", command=self.pause)
		self.pause_button.grid(row=0, column=1, padx=10)
			
		# Create the stop button
		self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop)
		self.stop_button.grid(row=0, column=2, padx=10)
		
		# Create the add button
		self.add_button = tk.Button(controls_frame, text="Add", command=self.add_to_playlist)
		self.add_button.grid(row=1, column=0, pady=10)
		
		# Create the remove button
		self.remove_button = tk.Button(controls_frame,text="Remove", command=self.remove_song)
		self.remove_button.grid(row=1, column=1, pady=10)
		
		# Create the vlc player instance
		self.player = vlc.Instance()
		self.media_player = self.player.media_player_new()
		
		# Set the end event
		the_event = vlc.EventType.MediaPlayerEndReached
		self.media_player.event_manager().event_attach(the_event, self.next_song)
	
# Step 3: Implement the player controls
	def play(self):
		selected_song = self.playlist.get(tk.ACTIVE)
		media = self.player.media_new(selected_song)
		self.media_player.set_media(media)
		self.media_player.play()
        
	def pause(self):
		self.media_player.pause()

	def stop(self):
		self.media_player.stop()

	def next_song(self, event):
		next_index = (self.playlist.curselection()[0] + 1) % self.playlist.size()
		self.playlist.selection_clear(0, tk.END)
		self.playlist.activate(next_index)
		self.playlist.selection_set(next_index)
		self.play()

	def add_to_playlist(self):
		file_path = filedialog.askopenfilename(defaultextension=".mp3",
		filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])
        
		if file_path:
			self.playlist.insert(tk.END, file_path)

	def remove_song(self):
		selected_index = self.playlist.curselection()[0]
		self.playlist.delete(selected_index)

# Step 4: Initialize the music player 
if __name__ == "__main__":
	window = tk.Tk()
	music_player = MusicPlayer(window)
	window.mainloop()
	

		
