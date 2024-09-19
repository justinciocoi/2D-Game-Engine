class Animation:
    def __init__(self, frames, frame_duration):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame_index = 0
        self.time_accumulated = 0
        self.playing = True

    def update(self, delta_time):
        if not self.playing:
            return
        self.time_accumulated += delta_time
        if self.time_accumulated >= self.frame_duration:
            self.time_accumulated = 0
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                self.playing = False  # Animation ends here

    def is_playing(self):
        return self.playing

    def reset(self):
        self.current_frame_index = 0
        self.playing = True
