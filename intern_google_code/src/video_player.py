"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._all_videos = self._video_library.get_all_videos()    
        self._current_video = None
        self._is_paused = False
        self._playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        
        video_format = []
        for i in self._all_videos:
            list_tags = []
            for t in i.tags:
                list_tags.append(t)
            list_tags
            tag_str = " "
            video_format.append(f"{i.title} ({i.video_id}) [{tag_str.join(list_tags)}]")
        video_format.sort()
        for line in video_format:
            print(line)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global video_obj
        video_obj = self._video_library.get_video(video_id)
        if video_obj == None:
            print('Cannot play video: Video does not exist')
        
        else:
            if self._current_video == None:
                self._current_video = video_obj.title
                print(f"Playing video: {self._current_video}")
                
            elif self._current_video != None:
                print(f"Stopping video: {self._current_video}")
                self._current_video = video_obj.title
                print(f"Playing video: {self._current_video}")
                self._is_paused = False
            else:
                pass


    def stop_video(self):
        """Stops the current video."""
        if self._current_video == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._current_video}")
            self._current_video = None


    def play_random_video(self):
        """Plays a random video from the video library."""

        random_choice = random.choice(self._all_videos)
        self.play_video(random_choice.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self._current_video == None:
            print("Cannot pause video: No video is currently playing")
        elif self._is_paused == True:
            print(f"Video already paused: {self._current_video}")
        elif self._is_paused == False:
            print(f"Pausing video: {self._current_video}")
            self._is_paused = True
        else:
            pass

    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video == None:
            print("Cannot continue video: No video is currently playing")
        elif self._is_paused == False:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self._current_video}")
            self._is_paused = False

    def show_playing(self):
        """Displays video currently playing."""
        
        if self._current_video == None:
            print("No video is currently playing")
        else:
            list_tags = []
            for tag in video_obj.tags:
                list_tags.append(tag)
                list_tags
                tag_str = " "
                video_details = f"{video_obj.title} ({video_obj.video_id}) [{tag_str.join(list_tags)}]"
            if self._is_paused == False:
                print(f"Currently playing: {video_details}")
            else:
                print(f"Currently playing: {video_details} - PAUSED")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlist:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist[playlist_name.lower()] = []  ## saving a lowered version of the name casued problems
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in self._playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        
        if playlist_name.lower() in self._playlist:
            
            if video_id in self._playlist[playlist_name.lower()]:
                print(f"Cannot add video to {playlist_name}: Video already added")
            
            elif self._video_library.get_video(video_id) == None:
                print(f"Connot add video to {playlist_name}: Video does not exist")
            
            else:
                self._playlist[playlist_name.lower()].append(video_id)
                video_title = self._video_library.get_video(video_id).title
                print(f"Added video to {playlist_name}: {video_title}")
        else:
            pass
            


    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlist == {}:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for key in self._playlist:
                print(key)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
