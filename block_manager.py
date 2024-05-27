from block import Block

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BLOCK_COLI_DIST = 12
BLOCKS_PER_ROW = 13
INITIAL_X_POS = -275
INITIAL_Y_POS = 350
X_KERN = 45
Y_KERN = 20

# blocks = []
# for i in range(13):
#     new_block = Block('red')
#     new_block.setposition(-275 + (i * 45), 350)
#     blocks.append(new_block)

class BlockManager:
    def __init__(self, scoreboard):
        self.blocks = []
        self.scoreboard = scoreboard

    def create_blocks(self):
        for i in range(len(COLORS)):
            for j in range(BLOCKS_PER_ROW):
                new_block = Block(COLORS[i])
                new_block.set_position(x_cord=INITIAL_X_POS + (j * X_KERN),
                                       y_cord=INITIAL_Y_POS - (i * Y_KERN))
                self.blocks.append(new_block)

    def check_collision(self, ball) -> bool:
        # Check if ball hit blocks
        for block in self.blocks:
            if block.distance(ball) < BLOCK_COLI_DIST:
                self.scoreboard.increment_score(block.get_color())
                block.clear()
                block.ht()
                self.blocks.remove(block)
                del block
                return True

        return False
