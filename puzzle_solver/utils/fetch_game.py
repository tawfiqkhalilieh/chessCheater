from constants import pieces
from puzzle_solver.utils.square_data import square_data
import chess
from selenium.webdriver.common.by import By

# I did it this way because I'm a big noob
async def fetch_game(driver, board):
    board = chess.Board(fen='8/8/8/8/8/8/8/8 w - - 0 1', chess960=True)

    try:
        # a1 square
        a1_class = driver.find_elements(By.CLASS_NAME, 'square-11')[-1].get_attribute('class')
        if "piece" in a1_class:
            a1_data = square_data(a1_class.split(), 'square-11')
            board.set_piece_at(chess.A1, chess.Piece(pieces[a1_data[1]], chess.WHITE if a1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a2 square
        a2_class = driver.find_elements(By.CLASS_NAME, 'square-12')[-1].get_attribute('class')
        if "piece" in a2_class:
            a2_data = square_data(a2_class.split(), 'square-12')
            board.set_piece_at(chess.A2, chess.Piece(pieces[a2_data[1]], chess.WHITE if a2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a3 square
        a3_class = driver.find_elements(By.CLASS_NAME, 'square-13')[-1].get_attribute('class')
        if "piece" in a3_class:
            a3_data = square_data(a3_class.split(), 'square-13')
            board.set_piece_at(chess.A3, chess.Piece(pieces[a3_data[1]], chess.WHITE if a3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a4 square
        a4_class = driver.find_elements(By.CLASS_NAME, 'square-14')[-1].get_attribute('class')
        if "piece" in a4_class:
            a4_data = square_data(a4_class.split(), 'square-14')
            board.set_piece_at(chess.A4, chess.Piece(pieces[a4_data[1]], chess.WHITE if a4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a5 square
        a5_class = driver.find_elements(By.CLASS_NAME, 'square-15')[-1].get_attribute('class')
        if "piece" in a5_class:
            a5_data = square_data(a5_class.split(), 'square-15')
            board.set_piece_at(chess.A5, chess.Piece(pieces[a5_data[1]], chess.WHITE if a5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a6 square
        a6_class = driver.find_elements(By.CLASS_NAME, 'square-16')[-1].get_attribute('class')
        if "piece" in a6_class:
            a6_data = square_data(a6_class.split(), 'square-16')
            board.set_piece_at(chess.A6, chess.Piece(pieces[a6_data[1]], chess.WHITE if a6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a7 square
        a7_class = driver.find_elements(By.CLASS_NAME, 'square-17')[-1].get_attribute('class')
        if "piece" in a7_class:
            a7_data = square_data(a7_class.split(), 'square-17')
            board.set_piece_at(chess.A7, chess.Piece(pieces[a7_data[1]], chess.WHITE if a7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # a8 square
        a8_class = driver.find_elements(By.CLASS_NAME, 'square-18')[-1].get_attribute('class')
        if "piece" in a8_class:
            a8_data = square_data(a8_class.split(), 'square-18')
            board.set_piece_at(chess.A8, chess.Piece(pieces[a8_data[1]], chess.WHITE if a8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b1 square
        b1_class = driver.find_elements(By.CLASS_NAME, 'square-21')[-1].get_attribute('class')
        if "piece" in b1_class:
            b1_data = square_data(b1_class.split(), 'square-21')
            board.set_piece_at(chess.B1, chess.Piece(pieces[b1_data[1]], chess.WHITE if b1_data[0] == 'w' else chess.BLACK))
    except:
        pass


    try:
        # b2 square
        b2_class = driver.find_elements(By.CLASS_NAME, 'square-22')[-1].get_attribute('class')
        if "piece" in b2_class:
            b2_data = square_data(b2_class.split(), 'square-22')
            board.set_piece_at(chess.B2, chess.Piece(pieces[b2_data[1]], chess.WHITE if b2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b3 square
        b3_class = driver.find_elements(By.CLASS_NAME, 'square-23')[-1].get_attribute('class')
        if "piece" in b3_class:
            b3_data = square_data(b3_class.split(), 'square-23')
            board.set_piece_at(chess.B3, chess.Piece(pieces[b3_data[1]], chess.WHITE if b3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b4 square
        b4_class = driver.find_elements(By.CLASS_NAME, 'square-24')[-1].get_attribute('class')
        if "piece" in b4_class:
            b4_data = square_data(b4_class.split(), 'square-24')
            board.set_piece_at(chess.B4, chess.Piece(pieces[b4_data[1]], chess.WHITE if b4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b5 square
        b5_class = driver.find_elements(By.CLASS_NAME, 'square-25')[-1].get_attribute('class')
        if "piece" in b5_class:
            b5_data = square_data(b5_class.split(), 'square-25')
            board.set_piece_at(chess.B5, chess.Piece(pieces[b5_data[1]], chess.WHITE if b5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b6 square
        b6_class = driver.find_elements(By.CLASS_NAME, 'square-26')[-1].get_attribute('class')
        if "piece" in b6_class:
            b6_data = square_data(b6_class.split(), 'square-26')
            board.set_piece_at(chess.B6, chess.Piece(pieces[b6_data[1]], chess.WHITE if b6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b7 square
        b7_class = driver.find_elements(By.CLASS_NAME, 'square-27')[-1].get_attribute('class')
        if "piece" in b7_class:
            b7_data = square_data(b7_class.split(), 'square-27')
            board.set_piece_at(chess.B7, chess.Piece(pieces[b7_data[1]], chess.WHITE if b7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # b8 square
        b8_class = driver.find_elements(By.CLASS_NAME, 'square-28')[-1].get_attribute('class')
        if "piece" in b8_class:
            b8_data = square_data(b8_class.split(), 'square-28')
            board.set_piece_at(chess.B8, chess.Piece(pieces[b8_data[1]], chess.WHITE if b8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c1 square
        c1_class = driver.find_elements(By.CLASS_NAME, 'square-31')[-1].get_attribute('class')
        if "piece" in c1_class:
            c1_data = square_data(c1_class.split(), 'square-31')
            board.set_piece_at(chess.C1, chess.Piece(pieces[c1_data[1]], chess.WHITE if c1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c2 square
        c2_class = driver.find_elements(By.CLASS_NAME, 'square-32')[-1].get_attribute('class')
        if "piece" in c2_class:
            c2_data = square_data(c2_class.split(), 'square-32')
            board.set_piece_at(chess.C2, chess.Piece(pieces[c2_data[1]], chess.WHITE if c2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c3 square
        c3_class = driver.find_elements(By.CLASS_NAME, 'square-33')[-1].get_attribute('class')
        if "piece" in c3_class:
            c3_data = square_data(c3_class.split(), 'square-33')
            board.set_piece_at(chess.C3, chess.Piece(pieces[c3_data[1]], chess.WHITE if c3_data[0] == 'w' else chess.BLACK))
        
    except:
        pass

    try:
        # c4 square
        c4_class = driver.find_elements(By.CLASS_NAME, 'square-34')[-1].get_attribute('class')
        if "piece" in c1_class:
            c4_data = square_data(c4_class.split(), 'square-34')
            board.set_piece_at(chess.C4, chess.Piece(pieces[c4_data[1]], chess.WHITE if c4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c5 square
        c5_class = driver.find_elements(By.CLASS_NAME, 'square-35')[-1].get_attribute('class')
        if "piece" in c5_class:
            c5_data = square_data(c5_class.split(), 'square-35')
            board.set_piece_at(chess.C5, chess.Piece(pieces[c5_data[1]], chess.WHITE if c5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c6 square
        c6_class = driver.find_elements(By.CLASS_NAME, 'square-36')[-1].get_attribute('class')
        if "piece" in c6_class:
            c6_data = square_data(c6_class.split(), 'square-36')
            board.set_piece_at(chess.C6, chess.Piece(pieces[c6_data[1]], chess.WHITE if c6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c7 square
        c7_class = driver.find_elements(By.CLASS_NAME, 'square-37')[-1].get_attribute('class')
        if "piece" in c7_class:
            c7_data = square_data(c7_class.split(), 'square-37')
            board.set_piece_at(chess.C7, chess.Piece(pieces[c7_data[1]], chess.WHITE if c7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # c8 square
        c8_class = driver.find_elements(By.CLASS_NAME, 'square-38')[-1].get_attribute('class')
        if "piece" in c8_class:
            c8_data = square_data(c8_class.split(), 'square-38')
            board.set_piece_at(chess.C8, chess.Piece(pieces[c8_data[1]], chess.WHITE if c8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d1 square
        d1_class = driver.find_elements(By.CLASS_NAME, 'square-41')[-1].get_attribute('class')
        if "piece" in d1_class:
            d1_data = square_data(d1_class.split(), 'square-41')
            board.set_piece_at(chess.D1, chess.Piece(pieces[d1_data[1]], chess.WHITE if d1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d2 square
        d2_class = driver.find_elements(By.CLASS_NAME, 'square-42')[-1].get_attribute('class')
        if "piece" in d2_class:
            d2_data = square_data(d2_class.split(), 'square-42')
            board.set_piece_at(chess.D2, chess.Piece(pieces[d2_data[1]], chess.WHITE if d2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d3 square
        d3_class = driver.find_elements(By.CLASS_NAME, 'square-43')[-1].get_attribute('class')
        if "piece" in d3_class:
            d3_data = square_data(d3_class.split(), 'square-43')
            board.set_piece_at(chess.D3, chess.Piece(pieces[d3_data[1]], chess.WHITE if d3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d4 square
        d4_class = driver.find_elements(By.CLASS_NAME, 'square-44')[-1].get_attribute('class')
        if "piece" in d4_class:
            d4_data = square_data(d4_class.split(), 'square-44')
            board.set_piece_at(chess.D4, chess.Piece(pieces[d4_data[1]], chess.WHITE if d4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d5 square
        d5_class = driver.find_elements(By.CLASS_NAME, 'square-45')[-1].get_attribute('class')
        if "piece" in d5_class:
            d5_data = square_data(d5_class.split(), 'square-45')
            board.set_piece_at(chess.D5, chess.Piece(pieces[d5_data[1]], chess.WHITE if d5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d6 square
        d6_class = driver.find_elements(By.CLASS_NAME, 'square-46')[-1].get_attribute('class')
        if "piece" in d6_class:
            d6_data = square_data(d6_class.split(), 'square-46')
            board.set_piece_at(chess.D6, chess.Piece(pieces[d6_data[1]], chess.WHITE if d6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d7 square
        d7_class = driver.find_elements(By.CLASS_NAME, 'square-47')[-1].get_attribute('class')
        if "piece" in d7_class:
            d7_data = square_data(d7_class.split(), 'square-47')
            board.set_piece_at(chess.D7, chess.Piece(pieces[d7_data[1]], chess.WHITE if d7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # d8 square
        d8_class = driver.find_elements(By.CLASS_NAME, 'square-48')[-1].get_attribute('class')
        if "piece" in d8_class:
            d8_data = square_data(d8_class.split(), 'square-48')
            board.set_piece_at(chess.D8, chess.Piece(pieces[d8_data[1]], chess.WHITE if d8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # e1 square
        e1_class = driver.find_elements(By.CLASS_NAME, 'square-51')[-1].get_attribute('class')
        if "piece" in e1_class:
            e1_data = square_data(e1_class.split(), 'square-51')
            board.set_piece_at(chess.E1, chess.Piece(pieces[e1_data[1]], chess.WHITE if e1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e2 square
    try:
        e2_class = driver.find_elements(By.CLASS_NAME, 'square-52')[-1].get_attribute('class')
        if "piece" in e2_class:
            e2_data = square_data(e2_class.split(), 'square-52')
            board.set_piece_at(chess.E2, chess.Piece(pieces[e2_data[1]], chess.WHITE if e2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e3 square
    try:
        e3_class = driver.find_elements(By.CLASS_NAME, 'square-53')[-1].get_attribute('class')
        if "piece" in e3_class:
            e3_data = square_data(e3_class.split(), 'square-53')
            board.set_piece_at(chess.E3, chess.Piece(pieces[e3_data[1]], chess.WHITE if e3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e4 square
    try:
        e4_class = driver.find_elements(By.CLASS_NAME, 'square-54')[-1].get_attribute('class')
        if "piece" in e4_class:
            e4_data = square_data(e4_class.split(), 'square-54')
            board.set_piece_at(chess.E4, chess.Piece(pieces[e4_data[1]], chess.WHITE if e4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e5 square
    try:
        e5_class = driver.find_elements(By.CLASS_NAME, 'square-55')[-1].get_attribute('class')
        if "piece" in e5_class:
            e5_data = square_data(e5_class.split(), 'square-55')
            board.set_piece_at(chess.E5, chess.Piece(pieces[e5_data[1]], chess.WHITE if e5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e6 square
    try:
        e6_class = driver.find_elements(By.CLASS_NAME, 'square-56')[-1].get_attribute('class')
        if "piece" in e6_class:
            e6_data = square_data(e6_class.split(), 'square-56')
            board.set_piece_at(chess.E6, chess.Piece(pieces[e6_data[1]], chess.WHITE if e6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e7 square
    try:
        e7_class = driver.find_elements(By.CLASS_NAME, 'square-57')[-1].get_attribute('class')
        if "piece" in e7_class:
            e7_data = square_data(e7_class.split(), 'square-57')
            board.set_piece_at(chess.E7, chess.Piece(pieces[e7_data[1]], chess.WHITE if e7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # e8 square
    try:
        e8_class = driver.find_elements(By.CLASS_NAME, 'square-58')[-1].get_attribute('class')
        if "piece" in e8_class:
            e8_data = square_data(e8_class.split(), 'square-58')
            board.set_piece_at(chess.E8, chess.Piece(pieces[e8_data[1]], chess.WHITE if e8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f1 square
    try:
        f1_class = driver.find_elements(By.CLASS_NAME, 'square-61')[-1].get_attribute('class')
        if "piece" in f1_class:
            f1_data = square_data(f1_class.split(), 'square-61')
            board.set_piece_at(chess.F1, chess.Piece(pieces[f1_data[1]], chess.WHITE if f1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f2 square
    try:
        f2_class = driver.find_elements(By.CLASS_NAME, 'square-62')[-1].get_attribute('class')
        if "piece" in f2_class:
            f2_data = square_data(f2_class.split(), 'square-62')
            board.set_piece_at(chess.F2, chess.Piece(pieces[f2_data[1]], chess.WHITE if f2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f3 square
    try:
        f3_class = driver.find_elements(By.CLASS_NAME, 'square-63')[-1].get_attribute('class')
        if "piece" in f3_class:
            f3_data = square_data(f3_class.split(), 'square-63')
            board.set_piece_at(chess.F3, chess.Piece(pieces[f3_data[1]], chess.WHITE if f3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f4 square
    try:
        f4_class = driver.find_elements(By.CLASS_NAME, 'square-64')[-1].get_attribute('class')
        if "piece" in f4_class:
            f4_data = square_data(f4_class.split(), 'square-64')
            board.set_piece_at(chess.F4, chess.Piece(pieces[f4_data[1]], chess.WHITE if f4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f5 square
    try:
        f5_class = driver.find_elements(By.CLASS_NAME, 'square-65')[-1].get_attribute('class')
        if "piece" in f5_class:
            f5_data = square_data(f5_class.split(), 'square-65')
            board.set_piece_at(chess.F5, chess.Piece(pieces[f5_data[1]], chess.WHITE if f5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f6 square
    try:
        f6_class = driver.find_elements(By.CLASS_NAME, 'square-66')[-1].get_attribute('class')
        if "piece" in f6_class:
            f6_data = square_data(f6_class.split(), 'square-66')
            board.set_piece_at(chess.F6, chess.Piece(pieces[f6_data[1]], chess.WHITE if f6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # f7 square
    try:
        f7_class = driver.find_elements(By.CLASS_NAME, 'square-67')[-1].get_attribute('class')
        if "piece" in f7_class:
            f7_data = square_data(f7_class.split(), 'square-67')
            board.set_piece_at(chess.F7, chess.Piece(pieces[f7_data[1]], chess.WHITE if f7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # f8 square
        f8_class = driver.find_elements(By.CLASS_NAME, 'square-68')[-1].get_attribute('class')
        if "piece" in f8_class:
            f8_data = square_data(f8_class.split(), 'square-68')
            board.set_piece_at(chess.F8, chess.Piece(pieces[f8_data[1]], chess.WHITE if f8_data[0] == 'w' else chess.BLACK))
    except:
        pass


    # g1 square
    try:
        g1_class = driver.find_elements(By.CLASS_NAME, 'square-71')[-1].get_attribute('class')
        if "piece" in g1_class:
            g1_data = square_data(g1_class.split(), 'square-71')
            board.set_piece_at(chess.G1, chess.Piece(pieces[g1_data[1]], chess.WHITE if g1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g2 square
    try:
        g2_class = driver.find_elements(By.CLASS_NAME, 'square-72')[-1].get_attribute('class')
        if "piece" in g2_class:
            g2_data = square_data(g2_class.split(), 'square-72')
            board.set_piece_at(chess.G2, chess.Piece(pieces[g2_data[1]], chess.WHITE if g2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g3 square
    try:
        g3_class = driver.find_elements(By.CLASS_NAME, 'square-73')[-1].get_attribute('class')
        if "piece" in g3_class:
            g3_data = square_data(g3_class.split(), 'square-73')
            board.set_piece_at(chess.G3, chess.Piece(pieces[g3_data[1]], chess.WHITE if g3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g4 square
    try:
        g4_class = driver.find_elements(By.CLASS_NAME, 'square-74')[-1].get_attribute('class')
        if "piece" in g4_class:
            g4_data = square_data(g4_class.split(), 'square-74')
            board.set_piece_at(chess.G4, chess.Piece(pieces[g4_data[1]], chess.WHITE if g4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g5 square
    try:
        g5_class = driver.find_elements(By.CLASS_NAME, 'square-75')[-1].get_attribute('class')
        if "piece" in g5_class:
            g5_data = square_data(g5_class.split(), 'square-75')
            board.set_piece_at(chess.G5, chess.Piece(pieces[g5_data[1]], chess.WHITE if g5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g6 square
    try:
        g6_class = driver.find_elements(By.CLASS_NAME, 'square-76')[-1].get_attribute('class')
        if "piece" in g6_class:
            g6_data = square_data(g6_class.split(), 'square-76')
            board.set_piece_at(chess.G6, chess.Piece(pieces[g6_data[1]], chess.WHITE if g6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g7 square
    try:
        g7_class = driver.find_elements(By.CLASS_NAME, 'square-77')[-1].get_attribute('class')
        if "piece" in g7_class:
            g7_data = square_data(g7_class.split(), 'square-77')
            board.set_piece_at(chess.G7, chess.Piece(pieces[g7_data[1]], chess.WHITE if g7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # g7 square
    try:
        g8_class = driver.find_elements(By.CLASS_NAME, 'square-78')[-1].get_attribute('class')
        if "piece" in g8_class:
            g7_data = square_data(g8_class.split(), 'square-78')
            board.set_piece_at(chess.G8, chess.Piece(pieces[g7_data[1]], chess.WHITE if g7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # h1 square
        h1_class = driver.find_elements(By.CLASS_NAME, 'square-81')[-1].get_attribute('class')
        if "piece" in h1_class:
            h1_data = square_data(h1_class.split(), 'square-81')
            board.set_piece_at(chess.H1, chess.Piece(pieces[h1_data[1]], chess.WHITE if h1_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h2 square
    try:
        h2_class = driver.find_elements(By.CLASS_NAME, 'square-82')[-1].get_attribute('class')
        if "piece" in h2_class:
            h2_data = square_data(h2_class.split(), 'square-82')
            board.set_piece_at(chess.H2, chess.Piece(pieces[h2_data[1]], chess.WHITE if h2_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h3 square
    try:
        h3_class = driver.find_elements(By.CLASS_NAME, 'square-83')[-1].get_attribute('class')
        if "piece" in h3_class:
            h3_data = square_data(h3_class.split(), 'square-83')
            board.set_piece_at(chess.H3, chess.Piece(pieces[h3_data[1]], chess.WHITE if h3_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h4 square
    try:
        h4_class = driver.find_elements(By.CLASS_NAME, 'square-84')[-1].get_attribute('class')
        if "piece" in h4_class:
            h4_data = square_data(h4_class.split(), 'square-84')
            board.set_piece_at(chess.H4, chess.Piece(pieces[h4_data[1]], chess.WHITE if h4_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h5 square
    try:
        h5_class = driver.find_elements(By.CLASS_NAME, 'square-85')[-1].get_attribute('class')
        if "piece" in h5_class:
            h5_data = square_data(h5_class.split(), 'square-85')
            board.set_piece_at(chess.H5, chess.Piece(pieces[h5_data[1]], chess.WHITE if h5_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h6 square
    try:
        h6_class = driver.find_elements(By.CLASS_NAME, 'square-86')[-1].get_attribute('class')
        if "piece" in h6_class:
            h6_data = square_data(h6_class.split(), 'square-86')
            board.set_piece_at(chess.H6, chess.Piece(pieces[h6_data[1]], chess.WHITE if h6_data[0] == 'w' else chess.BLACK))
    except:
        pass

    # h7 square
    try:
        h7_class = driver.find_elements(By.CLASS_NAME, 'square-87')[-1].get_attribute('class')
        if "piece" in h7_class:
            h7_data = square_data(h7_class.split(), 'square-87')
            board.set_piece_at(chess.H7, chess.Piece(pieces[h7_data[1]], chess.WHITE if h7_data[0] == 'w' else chess.BLACK))
    except:
        pass

    try:
        # h8 square
        h8_class = driver.find_elements(By.CLASS_NAME, 'square-88')[-1].get_attribute('class')
        if "piece" in h8_class:
            h8_data = square_data(h8_class.split(), 'square-88')
            board.set_piece_at(chess.H8, chess.Piece(pieces[h8_data[1]], chess.WHITE if h8_data[0] == 'w' else chess.BLACK))
    except:
        pass

    return board