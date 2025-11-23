from collections import deque
import sys

try:
    from colorama import Fore, Back, Style, init
    COLORAMA_AVAILABLE = True
    init(autoreset=True)
except ImportError:
    COLORAMA_AVAILABLE = False

COLOR_MAP = {
    0: (Fore.WHITE, Back.BLACK) if COLORAMA_AVAILABLE else ("", ""),
    1: (Fore.BLACK, Back.RED) if COLORAMA_AVAILABLE else ("", ""),
    2: (Fore.BLACK, Back.CYAN) if COLORAMA_AVAILABLE else ("", ""),
    3: (Fore.BLACK, Back.GREEN) if COLORAMA_AVAILABLE else ("", ""),
    4: (Fore.BLACK, Back.YELLOW) if COLORAMA_AVAILABLE else ("", ""),
    5: (Fore.WHITE, Back.MAGENTA) if COLORAMA_AVAILABLE else ("", ""),
    6: (Fore.BLACK, Back.LIGHTBLUE_EX) if COLORAMA_AVAILABLE else ("", ""),
    7: (Fore.BLACK, Back.LIGHTGREEN_EX) if COLORAMA_AVAILABLE else ("", ""),
    8: (Fore.BLACK, Back.LIGHTYELLOW_EX) if COLORAMA_AVAILABLE else ("", ""),
}


def flood_fill(grid, x, y, color):
    if not grid or len(grid) == 0:
        return
    
    n = len(grid)
    m = len(grid[0])
    
    if not (0 <= x < n and 0 <= y < m):
        return
    
    if grid[x][y] != 0:
        return

    queue = deque()
    queue.append((x, y))
    grid[x][y] = color

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = color
                queue.append((nx, ny))


def find_next_free_cell(grid):
    if not grid or len(grid) == 0:
        return None
    
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                return i, j
    return None


def fill_all_regions(grid):
    color = 2
    start = find_next_free_cell(grid)

    while start is not None:
        flood_fill(grid, start[0], start[1], color)
        color += 1
        start = find_next_free_cell(grid)

    return grid


def print_grid(grid, colored=False):
    if not grid or len(grid) == 0:
        print("(grid vazio)")
        return
    
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()


def print_grid_colored(grid):
    if not grid or len(grid) == 0:
        print("(grid vazio)")
        return
    
    if not COLORAMA_AVAILABLE:
        print_grid(grid, colored=False)
        return
    
    for row in grid:
        for cell in row:
            color_idx = cell % len(COLOR_MAP)
            fg, bg = COLOR_MAP.get(color_idx, (Fore.WHITE, Back.BLACK))
            print(f"{fg}{bg} {cell} {Style.RESET_ALL}", end="")
        print()
    print()


def read_grid_from_stdin():
    try:
        n = int(input("Digite o número de linhas: "))
        m = int(input("Digite o número de colunas: "))
        
        if n <= 0 or m <= 0:
            raise ValueError("Número de linhas e colunas deve ser > 0")
        
        print("Digite o grid (cada linha separada por Enter, valores separados por espaço):")
        grid = []
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != m:
                raise ValueError(f"Linha {i}: esperado {m} colunas, recebido {len(row)}")
            grid.append(row)
        
        return n, m, grid
    
    except ValueError as e:
        print(f"Erro na entrada: {e}")
        sys.exit(1)


def read_grid_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        if len(lines) < 2:
            raise ValueError("Arquivo deve conter pelo menos 2 linhas")
        
        n, m = map(int, lines[0].split())
        
        if n <= 0 or m <= 0:
            raise ValueError("n e m devem ser > 0")
        
        if len(lines) < n + 1:
            raise ValueError(f"Arquivo deve conter {n} linhas de grid, mas tem apenas {len(lines) - 1}")
        
        grid = []
        for i in range(n):
            row = list(map(int, lines[i + 1].split()))
            if len(row) != m:
                raise ValueError(f"Linha {i}: esperado {m} colunas, recebido {len(row)}")
            grid.append(row)
        
        return n, m, grid
    
    except FileNotFoundError:
        print(f"Erro: arquivo '{filename}' não encontrado.")
        sys.exit(1)
    except ValueError as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        n, m, grid = read_grid_from_file(filename)
        use_color = "-c" in sys.argv or "--color" in sys.argv
    else:
        n, m, grid = read_grid_from_stdin()
        use_color = False

    print("\n" + "="*40)
    print("Grid ANTES do preenchimento:")
    print("="*40)
    print_grid(grid)

    final_grid = fill_all_regions(grid)

    print("="*40)
    print("Grid DEPOIS do preenchimento:")
    print("="*40)
    
    if use_color and COLORAMA_AVAILABLE:
        print("(Visualização Colorida - Ponto Extra)")
        print_grid_colored(final_grid)
    else:
        print_grid(final_grid)
    
    regions_count = len(set(val for row in final_grid for val in row if val >= 2))
    print(f"Regiões preenchidas: {regions_count}")


if __name__ == "__main__":
    main()
