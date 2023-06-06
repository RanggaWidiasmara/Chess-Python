import pygame

# Inisialisasi pygame
pygame.init()

# Ukuran layar awal game
width, height = 400, 400
square_size = 50  # Ukuran kotak - kotak di papan catur
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catur kel 16")

# Warna kotak
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Menggambar papan catur
def draw_board():
    for row in range(8):
        for col in range(8):
            x = col * square_size
            y = row * square_size
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

# Fungsi untuk menggambar kotak bidak catur
def draw_piece(x, y, image):
    piece_size = 50  # Ukuran kotak bidak catur
    piece_image = pygame.transform.scale(image, (piece_size, piece_size))
    screen.blit(piece_image, (x, y))

# Class bidak catur
class Piece:
    def __init__(self, color, image, position):
        self.color = color
        self.image = image
        self.position = position

# Class papan catur
class Board:
    def __init__(self):
        self.pieces = []
        self.load_pieces()

    # Load posisi awal bidak
    def load_pieces(self):
        # Bidak putih
        self.pieces.append(Piece('white', pygame.image.load('F:/Kuliah/Semester4/AI/white_pawn.png'), (100, 100)))
        # Bidak hitam
        self.pieces.append(Piece('black', pygame.image.load('black_pawn.png'), (250, 250)))

    # Menggambar bidak
    def draw_pieces(self):
        for piece in self.pieces:
            # Menggambar bidak sesuai posisi dan warna
            draw_piece(piece.position[0], piece.position[1], piece.image)

# Fungsi untuk periksa posisi bidak yang saling menimpa
def adjacent(position1, position2):
    return abs(position1[0] - position2[0]) == square_size and abs(position1[1] - position2[1]) == square_size

# Fungsi untuk mekanika permainan catur
def play_game():
    # Inisialisasi variabel dan objek
    global screen
    board = Board()
    game_over = False
    selected_piece = None

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Klik kiri mouse
                    # Mendapatkan posisi klik mouse
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_square = (mouse_pos[0] // square_size, mouse_pos[1] // square_size)

                    if selected_piece is not None:
                        # Memperbarui posisi bidak yang diklik
                        for piece in board.pieces:
                            if piece != selected_piece and piece.position == selected_piece.position:
                                if piece.color != selected_piece.color:
                                    # Menghilangkan bidak lawan jika tertimpa
                                    board.pieces.remove(selected_piece)
                                break

                        selected_piece.position = (clicked_square[0] * square_size, clicked_square[1] * square_size)
                        selected_piece = None

                    if selected_piece is None:
                        # Cek apakah ada bidak di kotak yang diklik
                        for piece in board.pieces:
                            if piece.position == (clicked_square[0] * square_size, clicked_square[1] * square_size):
                                selected_piece = piece
                    
        screen.fill(WHITE)

        draw_board()
        board.draw_pieces()
        pygame.display.update()

    pygame.quit()

play_game()