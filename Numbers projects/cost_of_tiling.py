def get_positive_float(prompt):
    """Prompt user for a positive float. Keep asking until valid."""
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value <= 0:
                print("Value must be greater than zero. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_area(w, h, shape_type):
    area = w * h
    print(f'Area of {shape_type}: {area:.2f} sq.m')
    return area


def num_of_tiles_required(floor_area, tile_area):
    # Ceiling division to account for partial tiles
    return -(-floor_area // tile_area)


def calculate_tile_cost():
    print("\n=== Tile Cost Calculator ===")

    # Get validated inputs
    floor_width = get_positive_float('Enter floor width in meters: ')
    floor_height = get_positive_float('Enter floor height in meters: ')
    tile_width = get_positive_float('Enter tile width in meters: ')
    tile_height = get_positive_float('Enter tile height in meters: ')
    cost_per_tile = get_positive_float('Enter cost of 1 tile in Rupees: ')

    # Calculate areas
    floor_area = calculate_area(floor_width, floor_height, 'floor')
    tile_area = calculate_area(tile_width, tile_height, 'tile')

    # Calculate number of tiles and total cost
    num_tiles = num_of_tiles_required(floor_area, tile_area)
    total_cost = num_tiles * cost_per_tile

    print(f"\nYou will need approximately {num_tiles:.0f} tiles to cover the floor.")
    print(f"Total Cost of Tiles: ₹{total_cost:.2f}")
    print("=============================")


# Run
calculate_tile_cost()
