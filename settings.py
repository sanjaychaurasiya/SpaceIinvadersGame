class Settings:
    """A class to store all the settings for the game."""

    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (245, 245, 245)

        # Ship settings.
        self.ship_limit = 2

        # Bullets settings
        self.bullet_width = 7
        self.bullet_height = 25
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 8

        # How quickly the game speed up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increases.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1
        self.bullet_speed = 0.7
        self.alien_speed = 0.2

        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

