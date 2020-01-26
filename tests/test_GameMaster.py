from collections import Counter
from game.game_manager import GameMaster
from unittest import TestCase

import os


class TestGameManager(TestCase):
    def test_tile_usage(self):
        """
        The game master calls all other pieces, so we'll just run a game to its conclusion and do a few basic checks to
        ensure that the correct tiles are being doled out, the game terminates and is scored properly.
        """
        gm = GameMaster(ai_count=2)
        gm.play_game()

        # TODO: Finish tests of completed games.


